# SIMD Parallelism 

Modern x86 CPUs support __single instruction multiple data__ instructions that operate on special registers of holding 128, 256, or even 512 bits of data in one clock cycle. The specific support is different for manufactures (for example, AMD does not support `avx512`). The supported instruction sets can be found by 

```sh
cat /proc/cpuinfo | grep flags
```

To find whether the current CPU support the instruction set

```cpp
#include <iostream>
using namespace std;

int main() {
    // advanced vector extensions
    cout << __builtin_cpu_supports("avx") << endl; 
    cout << __builtin_cpu_supports("avx2") << endl; 
    cout << __builtin_cpu_supports("avx512f") << endl;
    return 0;
}
```

To use these instructions, we need to tell the compiler to enable the instruction extensions. Also, include `<immintrin.h>` to use vector intrinsic. For example,

```cpp
#pragma GCC target("avx2")
#pragma GCC optimize("O3")

#include <immintrin.h>
```

or compile the code with `gcc` with `O3` flag and provide the CPU architecture as `-march cpu-type` ( [List of CPU options](https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html))

## Registers and types
SIMD extensions supports special sets of registers 

- `SSE` supports 16 `128-bit` registers named `xmm0` through `xmm15`. 
- `AVX` supports 16 `256-bit` registers named `ymm0` through `ymm15`.
- `AVX512` supports 16 `512-bit` registers named `zmm0` through `zmm15`.

For C/C++, `imminstin.h` supports special vector types for data in these registers as

```cpp
__m{size}{dtype}
// For example

// 128-bit can do 4 floats or 2 doubles or 4 integers at the same time
__m128  // 128-bit single precision floats

// 256-bit = 8 floats, 4 doubles, 8 integers
__m256d // 256-bit double precision floats

// 512-bit = 16 floats, 8 doubles, 16 integers
__m512i // 512-bit integers
```

For `gcc`, we can also define your own vector types and then use most C/C++ math operations with them. 

```cpp
typedef int   v8si __attribute__ (( vector_size(32) ));
//     dtype  name                   size in bytes
```
## SIMD Intrinsics
__Intrinsics__ are C-style functions that do something with these vector data types, usually by simply calling the associated assembly instruction.

In general, the naming convention is `_mm{size}_{action}_{dtype}`.

### Moving data

To move data between SIMD registers and memory, the actions are `load, loadu, store, storeu`. The `u` stands for unaligned. `load` and `store` work correctly when read/write fits into a single cache line. In other words, the data in the memory should be aligned to 32 bytes for `_m256` instructions. 

Note that unaligned version will be slower. 

For loading constants to the registers, use 

```cpp
// Initializes 256-bit vector with float64 values.
extern __m256d _mm256_set_pd(double, double, double, double);
// Initializes 256-bit vector in reversed order.
extern __m256d _mm256_setr_pd(double, double, double, double);
// Initializes 256-bit vector filled with one scalar
extern __m256d _mm256_set1_pd(double);
```

## Performance considerations

Note that there are only 16 SIMD registers, and intrinsic simply maps the variables to the registers. When implementing a microkernel, we should fully use 16 registers and, at the same time, make sure there no register misses.

As an example, we can write a $4\times 4$ matrix multiplication microkernel for $C = C + A \cdot B$ where $A, B, C$ are stored in column-major as 

```cpp
// C[i, j] can be defined from macro as C + i + j * dim
// compute C[i:i + 4, j:j + 4]
void micro_kernel4x4(int i, int j, double *A, double *B, double *C)
{
    __m256d c00 = _mm256_loadu_pd(C[i, j    ]);
    __m256d c10 = _mm256_loadu_pd(C[i, j + 1]);
    __m256d c20 = _mm256_loadu_pd(C[i, j + 2]);
    __m256d c30 = _mm256_loadu_pd(C[i, j + 3]);

    __m256d a0, b0, b1, b2, b3;
    for (int k = 0; k < K; k++)
    {
        a0 = _mm256_load_pd(A[i, k]);
        b0 = _mm256_set1_pd(B[k, j    ]);
        b1 = _mm256_set1_pd(B[k, j + 1]);
        b2 = _mm256_set1_pd(B[k, j + 2]);
        b3 = _mm256_set1_pd(B[k, j + 3]);

        c00 = _mm256_fmadd_pd(a0, b0, c00);
        c10 = _mm256_fmadd_pd(a0, b1, c10);
        c20 = _mm256_fmadd_pd(a0, b2, c20);
        c30 = _mm256_fmadd_pd(a0, b3, c30);
    }
    _mm256_storeu_pd(C[i, j    ], c00);
    _mm256_storeu_pd(C[i, j + 1], c10);
    _mm256_storeu_pd(C[i, j + 2], c20);
    _mm256_storeu_pd(C[i, j + 3], c30);
}
```
