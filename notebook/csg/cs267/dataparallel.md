# Data Parallel Algorithms
Data parallel algorithms often apply to an array and the same operation is performed onto each (or each group) or elements at the same time. 

## Common operators

- __Unary operators__: $B = f(A)$ such as `square`. 
- __Binary operators__: $C = f(A, B)$ such as `add`.
- __Broadcast__: $C = f(a, B)$, such as `fill` (map a scalar to the array) or `saxpy` ($aX + Y$, scalar multiplication and add)
- __Memory operations__: array indexing include (stride) scatter/gather. Commonly seen in `numpy`. For example

    ```python
    A = B[::2] # copy with stride 2

    indices = [3, 0, 4, 2, 1]
    A = B[indices] # gather indexed values from one array
    A[indices] = B # scatter index values from one array
    ```

- __Masked operations__: A mask is an array of `true / false` or `0 / 1` and operations only performed when mask element is 1. 

    ```python
    mask = A % 2 == 1
    A[mask] += 1 # add 1 to all odd numbers in A 
    ```
- __Reduction__ accumulate an array to one value with any __associative__ op. Note that associativity is very important by allowing up to change operation orders (so that optimize and parallelize). Examples `sum(A), prod(A), dot(A, B)`.
  
- __Scan__ fill an array with partial reductions of any associative op. Examples `cumsum = scan(add)`
    - __Inclusive scan__ includes input $x_i$ for output $y_i$, __exclusive scan__ does not. 


## Ideal cost

Suppose that we have infinite number of processors, free control, and free communication. Then, the cost on the parallelism will be the depth of the spanned data dependency tree. 

- For unary and binary operations, the output only depends on corresponding elements, thus the cost is $O(1)$. 
- For broadcast, data get doubled at each time, thus the cost is $O(\log n)$. 
- For reduction, associativity allows up to do operation group-wise, thus the cost is $\Theta(\log_b n)$, where $b$ is the number of elements in a group, in general, the operations are binary, $b=2$. Note that this is also a lower bound.

### Matrix multiplications 

For a matrix multiplication $C = A \cdot B$, wlog. assume that the matrics are all $n\times n$. We note that for each entry 

$$c_{i,j} = \sum_{k=1}^N a_{i, k} b_{k, j} = \sum_{k=1}^N d_{i,j,k}$$

Which is 

1. A element-wise multiplication between $A_{i,:}$ and $B_{:, j}$. Costs $O(1)$ 
2. A reduction sum on $D_{i,j}$. Costs $O(\log n)$

Thus, the total cost is $\in O(\log n)$. 

### Scan via parallel prefix

A naïve parallel scanning can broadcast the $i$th value to an array of length $i$, and perform reduction on it to get the output for $i$th output. Then, the cost if $O(\log n)$, but the total work is $1+2+\cdots + n \in O(n^2)$. 

An idea was that we can divide 1 scan into two parts. Wlog assume that the operation is add. Observe that 

$$y_i = (\sum^{i-1} x_{j}) + x_i = (\sum^{i-2} x_{j}) + (x_{i-1} + x_i)$$ 

we have a recursive way to reduce the problem

1. Pairwise add two numbers so that even entries become $x_{i-1} + x_i$.
2. Compute scan on the even entries, so that even entries will have its scanned output
3. For each odd number, add its previous number, which is the even entry that has the correct scanned output.

```py title="recursive prefix"
def recursive_prefix_sum(arr):
    print(arr)
    n = len(arr)
    if n <= 2:
        if n == 2:
            arr[1] += arr[0]
        return
    arr[1::2] = arr[::2] + arr[1::2] if n % 2 == 0 else arr[:n-1:2] + arr[1::2]
    print(arr)
    recursive_prefix_sum(arr[1::2])
    arr[2::2] = arr[1:n-1:2] + arr[2::2] if n % 2 == 0 else arr[1::2] + arr[2::2]
    print(arr)

recursive_prefix_sum(np.arange(16))
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
# [ 0  1  2  5  4  9  6 13  8 17 10 21 12 25 14 29]
# [ 1  5  9 13 17 21 25 29]
# [ 1  6  9 22 17 38 25 54]
# [ 6 22 38 54]
# [ 6 28 38 92]
# [28 92]
# [  6  28  66 120]
# [  1   6  15  28  45  66  91 120]
# [  0   1   3   6  10  15  21  28  36  45  55  66  78  91 105 120]
```

## Non-trivial Scan applications 

Some applications that can benefit from `scan`

- n-bits Integer adding (scan for the carryover bits) in $O(\log n)$ time
- Inverting a $n\times n$ dense matrices / triangular matrices in $O(\log^2 n)$ time
- Evaluating expressions with $n$ tokens in $O(\log n)$ time
- Evaluating linear recurrences (e.x. Fibonacci series) of size $n$ in O(\log n)$ time
- Sparse matrix-vertex multiplication `SpMV` using segmented scan

### Stream Compression

Given a mask $m$ and array $A$, output $A[m]$ as a dense array. This is different from masked operation, where the operations happens in-place.

__Solution__ Compute cumulative sum on $m$, and then scatter values into result. 

```py title="stream compression"
# n:    8
# arr:  [3, 2, 4, 1, 5, 3, 3, 1]
# mask: [1, 0, 1, 1, 0, 0, 1, 1]
idx  = scan(mask, add)
# idx:  [1, 1, 2, 3, 3, 3, 4, 5]
result = empty(idx[n - 1]) # empty arr of size 5
result[idx[mask]] = arr[mask]
# result: [3, 4, 1, 3, 1]
```

Stream compression is the same as __remove elements satisfying a condition__. In this case, we let `mask = condition(arr)`. 

### Radix sort
Radix sort works for sorting array with fixed range, and its binary representation is ordered. For example, sorting an `int32` array. 

```c title="serial radix sort"
// Radix sort for 32 bit unsigned integer arr of size n
void radix_sort(uint32_t *arr, size_t n) {
    uint32_t bit = 1;
    uint32_t buffer[n];
    uint32_t temp[n];
    int start0, start1;
    for (int b = 0; b < 32; b++) {
        for (int i = 0; i < n; i++) {
            temp[i] = arr[i];
            buffer[i] = arr[i] & bit;
            if (buffer[i]) start1++;
        }
        for (int i = 0; i < n; i++) {
            if (buffer[i]) 
                arr[start1++] = temp[i];
            else 
                arr[start0++] = temp[i];
        }
        bit <<= 1;
    }

}
```

To parallelize, observe that we can mask all entries end with 1 from `buffer[i] = arr[i] & bit` and entries end with 0 from the complement. Then, the problem becomes a stream compression for 0-ending entries and a stream compression for 1-ending entries where the starting position is count of 0-ending entries (scalar add via broadcast). 

### Linked list length
For a linked list, finding the size of a linked list takes $O(n)$ time for serial algorithms. For parallel cases, we can see the problem as a reduction problem or a scan problem (if we want to assign the distance to `tail` for every node). 

In general, the algorithm works exactly the same as recursive prefix scan, but at the same time we prefix the pointers as well. 

### Fibonacci Series

Note that Fibonacci series is a linear occurrence problem $F_{n+1} = F_{n} + F_{n-1}$ and depends on previous two states. However, we can expand this by 

$$\begin{bmatrix}F_{n+1}\\F_n\end{bmatrix} = \begin{bmatrix}1&1\\1&0\end{bmatrix}\begin{bmatrix}F_{n}\\F_{n-1}\end{bmatrix}$$

so that it only depends on previous one state. 

Also, matmul is associative so that it go backs to a scan problem. 

### Adding n-bit integers
A serial n-bit bitwise add is implemented as 

```matlab
c[-1] = 0 % carryover c_in
for i = 0:n-1
    s[i] = (a[i] xor b[i]) xor c[i-1] % 1 or 3 one's
    c[i] = ((a[i] xor b[i]) and c[i-1]) or (a[i] and b[i]) % has carryover
```

Now, we see that `s[i]` and `c[i]` both depends on `c[i-1], a[i], b[i]`. We can first precompute things related to `a[i], b[i]` in $O(1)$ time. 

```matlab
s[i] = p[i] xor c[i-1] % p = a xor b for bit propagation
c[i] = (p[i] and c[i-1]) or g[i] % g = a and b for bit generation
```

Mathematically, we could represent $c$ as a boolean matmul

$$\begin{bmatrix}c_{i}\\1\end{bmatrix} = \begin{bmatrix}p_i&g_i\\0&1\end{bmatrix}\begin{bmatrix}c_{i-1}\\1\end{bmatrix}$$

### Inverting matrices
Wlog suppose that $T$ is $n\times n$ lower triangular matrix. Then, we can break $M$ into $\frac{n}{2}\times \frac{n}{2}$ matrices $T = \begin{bmatrix}A &\mathbf{0}\\C&B\end{bmatrix}$ where $A$ and $B$ are both lower triangular and $C$ is dense. In addition, we could prove the lemma

$$T^{-1} = \begin{bmatrix}A &\mathbf{0}\\C&B\end{bmatrix}^{-1} = \begin{bmatrix}A^{-1} &\mathbf{0}\\-B^{-1}CA^{-1}&B^{-1}\end{bmatrix}$$

_proof_. 

\begin{align*}
T^{-1}T &= 
\begin{bmatrix}A^{-1} &\mathbf{0}\\-B^{-1}CA^{-1}&B^{-1}\end{bmatrix}
\begin{bmatrix}A &\mathbf{0}\\C&B\end{bmatrix}\\
&= \begin{bmatrix}A^{-1}A + (-B^{-1}CA^{-1})\mathbf{0} &A^{-1}\mathbf{0} + \mathbf 0 B\\(-B^{-1}CA^{-1})A + B^{-1}C&(-B^{-1}CA^{-1})\mathbf 0 + B^{-1}B\end{bmatrix}\\
&= \begin{bmatrix}I&\mathbf0\\\mathbf0&I\end{bmatrix} \\
&= I
\end{align*}

Therefore, we can construct the recursive triangular inverting algorithm. 

```py title="inverse triangular matrix"
def tri_inv(T, n):
    if n == 1:
        return 1. / T
    A = T[:n//2, :n//2]
    C = T[n//2:, :n//2]
    B = T[n//2:, n//2:]
    Ainv = tri_inv(A, n//2) # Ainv, Binc in parallel
    Binv = tri_inv(B, n//2) 
    T[:n//2, :n//2] = Ainv
    T[n//2:, n//2:] = Binv
    T[n//2:, :n//2] = - Binv @ C @ Ainv # log(n) matmul
```

The total cost is $O(\log^2 n)$ by masters theorem
