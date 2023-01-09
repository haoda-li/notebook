# Single Processor Machines

## Program, Compiler, and Uni-processor model
We know that the processor executes machine codes (e.x. `Assembly`) and a compiler compiles a piece of code (say `C/C++/Fortan`) into machine code. 

|                      | Variables                                            | Operations                        | Control flow                  |
| -------------------- | ---------------------------------------------------- | --------------------------------- | ----------------------------- |
| program              | typed variables (int, float, pointer, array, struct) | arithmetic ops, logical ops, etc. | if, for, function calls       |
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


## Performance Model
Consider a simplified memory model, where we only have the cache (fast memory) and slow memory. All data are initially in slow memory, and the fast memory is empty. 

Let $m$ be the number of elements moved between fast and slow, $t_m$ be the time per memory save/load.   
Let $f$ be the number of arithmetic ops (flops), $t_f$ be the time per flop.  
Let $q = f/m$ be the average #flops per slow memory access.   
Assuming that $t_f << t_m$. 

The actual time taken is 

$$f \cdot t_f + m \cdot t_m = f \cdot t_f \cdot (1 + \frac{t_m}{t_f} \times \frac{1}{q})$$

$t_m/t_f$ is called the machine balance, which is hardware specific and constant (to us programmer).  
$q\geq t_m/t_f$ means that we can get at least half of peak speed ($f\cdot t_f$, or the time taken if all data in cache). 

## Matrix Multiplication
For the following examples, all matrices are $n\times n$, and vectors are $n\times 1$. Matrices and vectors are stored in contiguous row-major arrays (of arrays) of floats. Thus `A[i][j]` is the ith row, jth col. 

### Naive Matrix-Matrix Multiplication
Consider the following implementation for matrix-vector mult. `y += A * x`

```c
// assume cache size = cn, 3 < c << n
__load(x, n);
__load(y, n);
for (int i = 0; i < n; i++) {
    __load(A[i], n);
    for (int j = 0; i < n; j++) {
        y[i] += A[i][j] * x[j];
    }
}
__save(y, n);
```

$m = 3n + n^2, f = 2n^2, q \approx 2$

Similarly, consider matrix-matrix multiplication `C += A * B`. The most naive matrix-matrix multi. will be $n$ matrix-vector multiplication so that $m = 3n^2+n^3, f = 2n^3$. Then, we will still have $q\approx 2$. 

### Blocked (Tiled) Matrix Multiplication

Suppose that the cache is large enough to fit all 3 matrices. Then, we only need $3n^2$ loads and $n^2$ saves so that $m = 4n^2, f = 3n^3$. In this case, $q \in O(n)$. 

Thus, if we subdivide a matrices into smaller blocks, each of size $b\times b$ and load each block at a time, we can have $q\in O(b)$ performance. More specifically,

``` c title="blocked matrix multiplication"
// assume that n divides b for simplicity
// assume __block_load/save loads/saves the b * b sub-matrices 
// given the top-left corner
for (int i = 0; i < n; i += b) {
    for (int j = 0; j < n; j += b) {
        __block_load(C[i][j], b);
        for (int k = 0; k < n; k += b) {
            __block_load(A[i, k], b);
            __block_load(B[k, j], b);
            // assume this computes C += A*B given the top-left corner
            // and size of matrix
            matrix_matrix_multiplication(
                C[i][j], 
                A[i][k], 
                B[k][j],
                b
            )
        }
        __block_save(C[i][j], b);
    }
}
```

Each for loop will execute $N = n/b$ times so that 

$$
m = 2N^2b^2 + 2N^3b^2 = 2n^2 + 2n^3/b, q = f/m = \frac{2n^3}{2n^2 + 2n^3/b} \approx b
$$
