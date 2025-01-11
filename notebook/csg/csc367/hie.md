# Single Processor Machines

## Program, Compiler, and Uni-processor model
We know that the processor executes machine codes (e.x. `Assembly`) and a compiler compiles a piece of code (say `C/C++/Fortan`) into machine code. 

|                      | Variables                                            | Operations                        | Control flow                  |
| -------------------- | ---------------------------------------------------- | --------------------------------- | ----------------------------- |
| program              | typed variables (`int, float, pointer, array, struct`) | arithmetic ops, logical ops, etc. | if, for, function calls       |
| Assembly (Processor) | move bytes between memory and register               | arithmetic instructions (ALU)     | jump/branch instructions (CU) |

Ideally, assuming control, save, load are free, arithmetic operations all have the same cost.

### Compiler Optimizations
Compiler optimizations aim to reduce number of instructions by
 
- Improve register reuse (fewer save/load instruction)
    + interchange nested loops
    + reorder instructions, ex. `e = a + b; f = e - 1` becomes `R1 = a + b; R1 = R1 - 1`
- Eliminate unnecessary control flows (fewer branch/jump)
    + unroll small loops 
    + fuse loops (merge nested loops into one)
    + eliminate dead code branch
- Strength reduction (turn expensive instruction into cheaper ones)
    + multiply by 2 becomes shift right

However, most optimizations are performed locally. They often give up optimizations on complex code to preserve correctness. 

## Memory Hierarchy
The memory system can contain multiple levels. For example, a personal computer system (Ryzen5-2700) should have 

| memory             | device                   | latency | size   | bandwidth  |
| ------------------ | ------------------------ | ------- | ------ | ---------- |
| register           | per-code                 | 0       | bytes  |            |
| L1 cache           | per-core                 | >1ns    | 768KB  | 1TB/sec    |
| L2 cache           | per-processor            | ~3ns    | 4MB    | 1TB/sec    |
| L3 cache (or SRAM) | per-CPU (or motherboard) | ~6ns    | 16MB   | ~500GB/sec |
| Main memory        | DDR4 RAM                 | ~20ns   | 8-64GB | ~25GB/sec  |
| Hard drive         | SSD                      | ~10ms   | 1TB    | ~5GB       |

### Caches Locality

A __cache line__ is the contiguous block that read/write in between memory and cache per instruction. It's typically a few memory addresses. 

Since cache has significantly smaller latency, we want to store previously accessed cache lines so that references to memory is reduced. A __cache hit__ if the data required by the processor is already in cache, otherwise a __cache miss__, which resulting a load from main memory. 

 - __Temporal locality__: reuse data already in cache
 - __Spatial locality__: Operate on data that are stored close in memory, so that the data can be brought into cache all together. 

## Single Processor Parallelism

### Single Instruction Multiple Data (SIMD)
__SIMD__ (single instruction, multiple data) can execute one arithmetic instruction (one clock cycle) on multiple scalars. 

For example `AVX-512` do arithmetic operations on 512 bits (aka 8 double precision / 16 single precision operations) at a time.  

Some restriction on SIMD includes: expose parallelism to the compiler (flags/pragma to the compiler), data needs to be contiguous in memory and cache aligned. 

### Memory Alignment and Strides
Note that cache line is loaded from memory to cache at one time, which means contiguous memory accesses cannot be done in parallel (otherwise very easy to cause data conflicts). However, non-contiguous memory access can be done in parallel. 

Memory alignment is a common technique, instead of writing data in contiguous blocks, align them on cache line boundaries. For example, if the cache line is 32 bytes, we can store data in 

```c
double x[]; // each double is 8 bytes
x[0], x[4], x[8] // stride for 32 / 8 = 4 doubles 
```

### Fused Multiply Add (FMA)
FMA refers to operations like $x = y + c \cdot z$, which is very common for matrix multiplication. With FMA support, such operation can be done as one instruction instead of two. Also, only one rounding is performed, hence rounding error won't accumulate and is smaller. 


## Roofline Model
[Roofline: an insightful visual performance model for multicore architectures](https://people.eecs.berkeley.edu/~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf)

The idea is that applications are measured by 

| factor | unit | level |
| --- | --- | --- |
| arithmetic performance | FLOPs/s | machine |
| memory bandwidth | bytes/s | machine |
| computational intensity | FLOPs/byte | application | 

Then, consider a task of $N$ FLOPs or arithmetic operations and $M$ bytes of data movement. Assuming a cold start (all data initially resides in DRAM) and each byte of data will be moved exactly once. Then we have that 

```
time = max(N / (Peak FLOPS per sec), M / Peak Bandwidth)
N / time = min(Peak FLOPS per sec, (N / M) * Peak Bandwidth)
```

Thus, we can get the roofline performance model, where x-axis is the FLOPs / data ratio (N/M) and y-axis is the speed FLOPs / sec. 