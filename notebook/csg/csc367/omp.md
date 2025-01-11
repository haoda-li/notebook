# OpenMP - Introduction of Parallelism 

PThreads are based on OS features. It has high overhead for thread creation. Also, it is quite low level, which means more and harder-found data race bugs. Also, deadlocks are usually easier. 

## Introduction
As almost all machines today are using multi-core CPU, we need simpler, "lighter" syntax way to write multithreading code.  An alternative is OpenMP. 

Using PThreads with 
```c++
#include <omp.h>
```
compile (using `gcc`) with 
```sh
gcc -fopenmp *.c 
```
### Basic directives
OpenMP uses "hints" or compiler "directives" as to what intended to parallelize
```c++
#pragma omp directivename [clause list]
```
### Library functions
Also, library functions included in `omp.h` for providing information about currently running program
```c++
/* used within parallel */
int omp_get_num_threads(); // return #threads running to the closest block
int omp_get_thread_num(); // get thread id
int omp_in_parallel(); // return non-zero if within a parallel region

/* used anywhere */
int omp_get_max_threads() // max #threads can be created;
int omp_get_num_procs(); // #processors available 
void omp_set_num_threads(int n); // set #threads for the next parallel section 
```

### Basic Example
```c++
int main() {
    omp_set_num_threads(8);
    #pragma omp parallel {
        omp_get_thread_num(); // 1 ... 8, no guarantees on order,
        omp_get_num_threads(); // 8;
    }
    omp_get_num_threads(); // 1
    return 0;
}
```

### Directive Clauses
```c++
// only parallel if expr holds
#pragma omp parallel if(expr) 

// #threads, overrides omp_set_num_threads or env variable OMP_NUM_THREADS
#pragma omp parallel num_threads(8)
```

### Nested parallelism
OpenMP supported arbitrarily deep nesting of `omp parallel`, whenever there are enough threads. However, `omp_get_num_threads, omp_get_thread_num` will only get number of threads within its group/parallel region. 
```c++
#pragma omp parallel num_threads(2) {
    omp_get_num_threads(); // 2
    #pragma omp parallel num_threads(2) {
        // there are 4 threads/cores running
        omp_get_num_threads(); // 2
    }
    omp_get_num_threads(); // 2
}
```
## Variable Semantics

### Data sharing / scope of variables
-`private`: each thread get a local copy
-`shared`: all threads share the same copy
-`firstprivate`: like private, but init to the value before the parallel directive
```c++
int main() {
    int A = 0, B = 1, C = 2, D = 3, E = 4;
    #pragma omp parallel private(A, B) shared(C) firstprivate(D) {
        printf("%d\n", A); // undeclared 
        B = 5;
        printf("%d\n", B); // 5

        printf("%d\n", C); // 2
        C = -2;
        printf("%d\n", C); // -2

        printf("%d\n", D); // 3
        D = -3;
        printf("%d\n", D); // -3

        printf("%d\n", E); // 4
        E = -4;
        printf("%d\n", E); // -4
    }
    printf("%d\n", A); // 0
    printf("%d\n", B); // 1
    printf("%d\n", C); // -2
    printf("%d\n", D); // 3
    printf("%d\n", E); // -4
```

### `default` State
use default clause to set default state
```c++
#pragma omp parallel default(shared | none)
```

`shared`: unless specified using private/firstprivate, all variables are shared
even variables init inside the parallel block
```c++
#pragma omp parallel default(shared)
```
`none`: must specify every variable used in parallel region otherwise compile error
```c++
#pragma omp parallel default(none)
```
no `default` clause: variable declared outside a parallel block is `shared` (with some exceptions like loop counters). inside is implicitly `private`.
```c++
#pragma omp parallel
```
## Reduction
Reduction refers to the operations where multiple local copies of a variable are combined into a single copy at the master when the parallel block ends. 

Syntax
```c++
#pragma omp parallel reduction(op: var)
```

For example, 
```c++
int s = 0;
#pragma omp parallel reduction(+: s) {
    s += 10;
}

/*  reduction can be considered as the following 
    but it guarantees no sync bugs and no contentions
*/
int s = 0; 
#pragma omp parallel {
    int s_local = s; // get a private copy
    s_local += 10; // do operations
    atomic_add(s, s_local); // atomic add as specified reduction ops
}
```
The supported op includes  `+, -, *, &, |, ^, &&, ||`

### Example: dot product
```c++
// compute the dot product of vec a * b
float dot(float *a, float *b, size_t n) {
    int s;
    #pragma omp parallel reduction(+: s) {
        int nthreads = omp_get_num_threads();
        int tid = omp_get_thread_num();
        int chunk = (n + nthreads - 1) / nthreads;

        for (int i = tid*chunk; i < tid*chunk + chunk && i < n; i++) {
            s += a[i] * b[i];
        }
    }
}
```
