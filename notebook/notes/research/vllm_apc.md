# Paged Attention & Automatic Prefix Caching

[vLLM doc: Paged Attention](https://docs.vllm.ai/en/latest/design/paged_attention/)  
[vLLM doc: Automatic Prefix Caching](https://docs.vllm.ai/en/latest/design/prefix_caching/)

## Pre-req: Scaled Dot-Product Attention

For a single attention head, given:

- Query vector `q` (from the current token being generated)
- Key matrix `K` (keys from all tokens in the context, shape `[seq_len, head_size]`)
- Value matrix `V` (values from all tokens in the context, shape `[seq_len, head_size]`)

The attention output is:

$$\text{Attention}(q, K, V) = \text{softmax}\left(\frac{q \cdot K^T + M}{\sqrt{d_k}}\right) \cdot V$$

where $d_k$ = `head_size` and $M$ is the causal mask.

The causal mask is a matrix where:

$$M_{ij} = \begin{cases} 0 & \text{if } j \leq i \quad \text{(attend to current and past)} \\ -\infty & \text{if } j > i \quad \text{(block future positions)} \end{cases}$$

Adding $-\infty$ before softmax makes those positions evaluate to $e^{-\infty} = 0$, effectively preventing any information flow from future tokens. For a sequence of length 4, the mask looks like:

```
     pos 0   pos 1   pos 2   pos 3
q0 [  0      -inf    -inf    -inf  ]
q1 [  0        0     -inf    -inf  ]
q2 [  0        0       0     -inf  ]
q3 [  0        0       0       0   ]
```

The key observation for caching: `K[i]` and `V[i]` at any layer depend on all tokens `0..i` (due to causal attention in prior layers), so they are fully determined by the prefix up to position `i`. This is why only prefix caching is valid.

## [Paged Attention](https://docs.vllm.ai/en/latest/design/paged_attention/)

Instead of allocating one contiguous KV cache per sequence, vLLM divides device memory into fixed-size **blocks** (like OS virtual memory pages). Each block stores KV data for a fixed number of tokens (`BLOCK_SIZE`, e.g., 16) for one attention head.


```
Flat KV Cache: [batch, num_kv_heads, context_size, head_size]
Block KV Cache: [num_blocks, num_kv_heads, block_size, head_size]
```

A **block table** maps each sequence's logical block indices to physical block numbers in device memory. This indirection enables:

- Non-contiguous memory allocation (no fragmentation)
- Sharing physical blocks across sequences (e.g., beam search, prefix caching)
- Dynamic growth without pre-allocating max-sequence-length memory

### Online Softmax

For a single query vector $q$ against keys $K$ and values $V$

$$o =  \frac{1}{\sum_{i=1}^{N} \exp(s_i-m)}\sum_{i=1}^{N} \exp(s_i - m)v_i, \quad s_i = \frac{q \cdot k_i}{\sqrt{d_k}}, m = \max(\mathbf s)$$

Partition the KV cache into $B$ blocks, we get

$$o = \frac{1}{\sum_{b=1}^B\sum_{i\in b} \exp(s_i-m)}\sum_{b=1}^B\sum_{i\in b} \exp(s_i - m)v_i$$


Consider $m_b$ to be the max score of the block, we keep track of nominator and denominator separatedly. 

Since $\exp(a-b) = \exp(a) / \exp(b)$

$$u_B = \frac{1}{\exp(m_B)}\sum_{b=1}^B\sum_{i\in b} \exp(s_i)v_i, \quad m_B= \max(m_1, ..., m_b)$$

Now say we add a new block $B+1$, we get 

$$u_{B+1} = \frac{\exp(m_B)}{\exp(m_{B+1})}u_B + \frac{1}{\exp(m_{B+1})}\sum_{i\in {B+1}} \exp(s_i)v_i$$

And we get similar 

$$l_{B+1} = \frac{\exp(m_B)}{\exp(m_{B+1})}l_B + \frac{1}{\exp(m_{B+1})}\sum_{i\in {B+1}} \exp(s_i)$$

Note that $m_{B+1} = \max(m_B, m_{b+1})$. Therefore, for each block accumulation, we only need to keep track of $m, u, l$, and rescale them in each iteration.  

### Why Paged Attention Is More Efficient

Since KV cache pages (blocks) can live at **arbitrary physical memory locations**, and the math above shows we only need per-block $(m_b, l_b, u_b)$ that combine via rescaling, the blocks don't need to be contiguous. Each page is processed independently, and the online softmax merges results — enabling virtual-memory-style KV cache management.

**Flat KV cache** must pre-allocate `max_seq_len * head_size` per sequence at request arrival, because the buffer is contiguous and can't grow. For a batch of sequences with varying lengths, this wastes memory on unused slots:

**Paged attention** allocates blocks on demand as the sequence grows. No pre-allocation, no wasted trailing space:


## [Automatic Prefix Caching (APC)](https://docs.vllm.ai/en/latest/design/prefix_caching/)

Many requests share common prefixes (system prompts, few-shot examples, shared document context). Without caching, vLLM recomputes the KV cache for these shared prefixes every time.


APC caches **full KV cache blocks** and identifies them by a content-based hash. When a new request arrives, vLLM checks if any prefix blocks already exist in cache before allocating new ones.


**What prefix caching skips**: Suppose positions 0–2 are a cached prefix and position 3 is new. The cached blocks already contain `K[0..2]` and `V[0..2]` at every layer. With prefix caching, we skip **all computation** for positions 0–2. The entire forward pass for those tokens is skipped. We only run the full transformer stack (attention + MLP, all layers) for position 3. When position 3 computes attention, it still reads `K[0..2]` and `V[0..2]` from the cached blocks — that data is already there in device memory.

### Block Identification

Each block is identified by its content (token IDs) and the identity of all preceding blocks — two blocks with identical tokens are only considered equivalent if their entire prefix history also matches.

Only **full blocks** (completely filled with `BLOCK_SIZE` tokens) are cached.

### Allocation Flow for a New Request

1. **`get_computed_blocks()`** — Hash the prompt tokens block-by-block. Look up each hash in the cache. Return the longest prefix of consecutive cache hits.

2. **`allocate_slots()`**:

    - "Touch" cached blocks: increment `ref_cnt`, remove from free queue (prevents eviction)
    - Allocate new blocks from the free queue head for the remaining tokens
    - Immediately cache any newly allocated block that becomes full

### Eviction Policy (LRU)

- All blocks are pre-allocated at startup as a fixed **block pool**.
- Unreferenced blocks sit in a **free queue** (doubly linked list, O(1) operations).
- When a block is needed, pop from the **head** (least recently used). If the head block is cached, evict it (remove hash mapping, clear metadata).
- When a request finishes, its blocks are added to the free queue **tail in reverse order** — the last block (most unique, least reusable) is evicted first.

### End-to-End Example (block_size=4)

```
Request A: "The cat sat on the mat and then"  (8 tokens = 2 full blocks)

Block 0: hash("The cat sat on")  → allocated, cached immediately
Block 1: hash(parent=Block0, "the mat and then") → allocated, cached immediately

Request B: "The cat sat on the rug"  (6 tokens)

Block 0: hash("The cat sat on") → CACHE HIT, reuse physical block
Block 1: hash(parent=Block0, "the rug__") → not full yet, allocate new block
```

Request B skips prefill computation for the first 4 tokens entirely.

