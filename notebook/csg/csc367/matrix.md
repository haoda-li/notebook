# Single Processor Matrix Multiplications

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

Knowing the cache size $M$, we can then find calculate $b \leq \sqrt{M / 3}$. 

Also, in practice a memory hierarchy system has more than two levels of cache, and the algorithm is possible for further subdividing into smaller blocks according to cache levels.

### Recursive Matrix Multiplication
Another approach is to do blocking recursively, instead of using a fixed block size. 

```c title="Recursive matrix multiplication"
RMM(A, B, n) {
    // base case: when n is sufficiently small
    // for naive MM
    if (n == 1) {
        return A * B;
    }
    // recursive steps
    else {
        A00, A01, A10, A11 = subdivide(A);
        B00, B01, B10, B11 = subdivide(B);
        C00 = RMM(A00, B00, n/2) + RMM(A01, B10, n/2);
        C01 = RMM(A00, B01, n/2) + RMM(A01, B11, n/2);
        C10 = RMM(A11, B00, n/2) + RMM(A11, B10, n/2);
        C11 = RMM(A11, B01, n/2) + RMM(A11, B11, n/2);
        C = assemble(C00, C01, C10, C11);
        return C;
    }
}
```

arithmetic computational cost is 

$$T(n) = 8T(\frac n2) + 4(\frac{n}{2})^2$$

By master's theorem, we get $2n^3 - n^2 \in O(n^3)$

data movement cost is similar

$$T_m(n) = \begin{cases}8T_m(\frac n2) + 4\times 3(\frac{n}{2})^2&3n^2 > M\\3n^2\end{cases}$$

RMM has the same asymptotic bound as BMM, but does not need to know the cache sizes. However, because of the cost of function stack allocation, RMM is generally a bit smaller than BMM. 

## Data Layouts
Consider the existence of cache line, to maximize spatial locality, the data layout can be further optimized according to the algorithm. 

For BMM, instead of save the whole matrices in row-major or col-major. We can do blocked-row major/col-major. Therefore, each block will be in contiguous memory. 

For RMM, we can use Z-Morton order, i.e. the matrix is recursively subdivided into 4 blocks, until the matrix is sufficiently small. However, Z-Morton order can be very hard for matrix indexing. 


