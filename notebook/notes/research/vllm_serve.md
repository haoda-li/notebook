# vLLM Serving Optimizations

Reference to vLLM's official docs:
- [Optimization & tuning](https://docs.vllm.ai/en/latest/configuration/optimization/) 
- [Architecture overview](https://docs.vllm.ai/en/latest/design/arch_overview/)

## Serving Processes

| Process | Count | Device | Job | Data |
|---|---|---|---| --- |
| **API server** | `A` (defaults to `DP`) | CPU only | HTTP, chat template, tokenize, multi-modal loading, detokenize, SSE streaming | Tokenizer, chat template rendering, image/audio decode |
| **EngineCore** | 1 per DP rank | CPU only | Scheduler busy loop, KV cache *manager*, request state | KV cache manager (KV cache block tables, block hashes, more on the PagedAttention), Waiting/running queues, per-request state machine, Grammar/FSM compilation for structured output | 
| **GPU worker** | `N` (number of devices) | CPU proc driving 1 GPU | Loads weights, builds input tensors, runs forward, samples | model weights, KV cache, activations, scratchpad buffers, computation graphs | 
| **DP coordinator** | 1, only if `DP > 1` | CPU only | Load balance across DP ranks, sync forward passes for MoE | Waiting/running queues, per-request state machine |

## User Sessions 

Consider a user session: user sends request of their questions to the vLLM server, gets an answer, and sends a new question (with the context of all previous communications). 

### Life of one request
1. HTTP hits the API server process. Chat template applied, tokenizer turns the request body into token IDs. 
2. Multimodal inputs fetched and preprocessed on CPU threads; the vision encoder itself runs later on GPU.
3. Request serialized over ZMQ to an EngineCore.
4. Scheduler hashes the prompt's blocks, looks them up in the prefix-cache table. Hits are reused by pointer. Misses get fresh blocks from the free pool.
5. Request admitted into a batch subject to `max_num_seqs` and the `max_num_batched_tokens` budget; long prompts are split by chunked prefill so decodes of other requests aren't starved.
6. **(CPU -> GPU)** (block tables + token slices) → workers.
7. Worker builds input tensors, runs the forward (Embed token IDs into hidden embeddings, run decoders, lm_heads, and finally sampling).
8. **(GPU → CPU)** Output sampled IDs.
9. EngineCore appends the token, decides whether the request continues, and loops to step 5.
10. Token IDs stream back to the API server process, which incrementally detokenizes, checks stop conditions, and emits an SSE chunk.
11. On finish, blocks are returned to the free pool but kept content-addressable — an LRU cache, evicted only under pressure.

### What a "session" actually is
There is **no server-side session**. Each turn resends the whole conversation; vLLM re-tokenizes it and finds the prior turns' KV already cached at step 4. So multi-turn efficiency is entirely a prefix-cache hit-rate property.

### [Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/)

In coding tasks, a user wants structured outputs (for example want a JSON object or python script). Instead of injecting a prompt that "I want legit JSON", vLLM compiles your schema into an automaton, and at every decode step it builds a bitmask over the vocabulary and sets the logits of every token that would break the grammar to `-inf`. The model cannot emit a malformed token because that token has probability zero.

## Batching and Scheduling

Note that decode process is **memory bound**, the model need to load the full weight to only compute for a token's hidden vector of size `(1, hidden_dim)`. Therefore, it's naturally to parallelize multiple requests' decode at the same forward pass. 

As an example, roofline for Llama-3.1-8B in FP16 on an H100 (16 GB weights, 3.35 TB/s HBM):

| Batch size | Min time per step (weight streaming) | Tokens/step | Throughput |
|---|---|---|---|
| 1 | ~4.8 ms | 1 | ~210 tok/s |
| 32 | ~4.8 ms | 32 | ~6,700 tok/s |
| 128 | ~5–6 ms (GEMMs start to matter) | 128 | ~22,000 tok/s |

### Continuous Batching

If we naively batch the requests (static batching): gather `BS` requests, runs it to completion, then form the next one. The problem is that generation lengths vary wildly, and the ending time always depends on the longest generation. 

Example, four requests arrive together, output lengths 10 / 200 / 30 / 500:

```
static batching, 500 steps:

R1 |=====                                              |  10 tok, then 490 steps of dead slot
R2 |==========================                         | 200 tok, then 300 steps of dead slot
R3 |========                                           |  30 tok, then 470 steps of dead slot
R4 |===================================================| 500 tok
   ^ batch admitted                                    ^ batch retires, next one can start

useful work = (10+200+30+500) / (4 × 500) = 740/2000 = 37% slot utilization
```

**Continuous batching** (a.k.a. iteration-level scheduling) rebuilds the batch before every forward pass. A finished sequence is removed the step it emits its stop token; a waiting request joins the very next step. Slot utilization goes to ~100% as long as the waiting queue is non-empty. 

Continuous batching also requires a scheduler, before a waiting request joins the forward pass, its kv cache has to be present on the device. 

Note that continuous batching **requires paged attention**. Rows in the batch are at different, constantly changing lengths. With one contiguous KV buffer per sequence you'd have to allocate `max_model_len` for each.


## [Disaggregated Inference](https://docs.vllm.ai/en/latest/features/disagg_prefill/)

Prefill is compute-bound, decode is memory-bound, and the two phases want opposite hardware, parallelism, and batch configurations. Disaggregation runs them in separate instance pools and ships the prompt's KV cache across the network in between — trading a **transfer cost** for **independent tuning and independent scaling** of the two phases.

### The problem

| | Prefill | Decode |
|---|---|---|
| Saturates GPU at | batch size 1, if the prompt is long | large batch only |
| Latency metric | time to first token (TTFT) | tokens per second (TPS) |
| Wants | high TP (splits the compute, cuts latency) | low TP + more DP replicas, max KV space |
| Duration | one long burst, 10s–100s of ms | 1/100ms per pass |

Problems

- Sharding: one single server requires to have consistent sharding - otherwise we need to transfer weights whenever switch better prefill and decode. 
- Overhead for switch computation graph: the device need to load the compute graph, which can take ~10us. 
- Batching and scheduling: need to prefill all sequences within a batch before starting decode. Since prefill is compute bound, TTFT grows linearly with the number of batches. 


### KV Cache Transfer

Remind that prefill is the step to fill the KV cache (and output the first token), and decode is to use these cache to generate tokens. Therefore, we need to transfer the KV cache from the prefill server to the decode server. 

```
total sendrecv bytes = sequence length * 2 (K,V) × layers × kv_heads × head_dim × dtype_bytes
```

Plus a few bytes of metadata: the first sampled token (prefill produces it), request ID / transaction ID, and block layout info.

Some examples of bytes transferred

| Model | Bytes/token | 8K-token prompt |
|---|---|---|
| Llama-3.1-8B (32L, 8 KV heads, FP16) | 128 KiB | **1.0 GiB** |
| Llama-3.1-70B (80L, 8 KV heads, FP16) | 320 KiB | **2.5 GiB** |
| Llama-2-7B, no GQA (32 KV heads) | 512 KiB | 4.0 GiB |
| DeepSeek-V3 class, MLA | ~70 KiB | ~0.5 GiB |


We can further reduce the transfer latency by **Layer-wise pipelining**. Connectors stream per layer rather than waiting for the full prefill. Layer *i*'s KV is finished when layer *i*'s forward completes, so transfer overlaps the remaining layers' compute. 



### Overhead
- The KV transfer. Need enough server to server bandwidth (for example infiniband for NVIDIA).
- Minimum viable deployment is 2 instances.
- Possible idle devices if prefill/decode server ratio is mismatched. A 1P:3D deployment facing sudden prefill-heavy traffic has an idle decode pool and a queued prefiller. 
