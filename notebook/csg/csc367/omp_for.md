
# OpenMP - For Loop, Sections, Tasks
## For Loops in Concurrent Tasks
From the dot product example, we see that we manually partition the `for` loop using thread number and thread id. 

Such partitioning can be done by 
```c++
/* pragma omp for must be immediately before the for loop
*/
#pragma omp parallel [clause list] {
    /* ... */
    #pragma omp for [clause list]
    for (init; test; update) {
        /* loop body */
    }
    /* ... */
}
```
### Restrictions on `for` loop
Therefore several restrictions on the for loop to be parallelized by `omp`
```c++
// for (init_expr, test_expr, update_expr)
for (int i = 0; i < n; i++) {
    /* body */
}
```
  
- `init_expr` must be integer type and must be an integer assignment
- `test_expr` must be a `<, >, <=, >=` expr
- `update_expr` must be integer increments
- `body` cannot have `break`

### For loop Clauses
The `clause list` includes

 - `private(var), firstprivate(var)` as parallel directive
 - `lastprivate(var)` only in `for, sections`, set variable to the thread that execute the last iteration or last section
 - `reduction(op: var)`  as parallel directive
 - `schedule(cls[, param])` specify how the for loop should be divided, more on `schedule` section
 - `nowait` only in `for, sections`, no barrier/sync after the for loop
 - `ordered` only in `for`, block of code that must be executed in sequential order
```c++
// https://stackoverflow.com/a/13230816
tid  List of     Timeline
     iterations
0    0,1,2       ==o==o==o
1    3,4,5       ==.......o==o==o
2    6,7,8       ==..............o==o==o
```

### Parallel For
We can combine `#pragma omp parallel` with `#pragma omp for` as 
```c++
#pragma omp parallel for [clause list]
```
where `clause list` is the union of `parallel` and `for`.  
Note that the scope clauses `private, default(none), default(shared)` will not impact the behavior of loop counter. 

### Loop counter and loop carried dependence
Note that `#pragma omp for` will make loop index private by default, and assign new values and conditions. Thus, for correctness, there should be no loop carried dependence in loop body. For example,

```c++
int j = 5;
for (int i = 0; i < n; i++) {
    // j is increment in each iteration
    j += 2;
    A[i] = b[j];
}

/* j is loop dependent, 
   adding omp for directly will be incorrect
*/
#pragma omp parallel for
for (int i = 0; i < n; i++) {
    // j is increment in each iteration
    int j = 5 + 2 * (i + 1);
    A[i] = b[j];
}
```

### `schedule`: Ways to assign iterations
The schedule clause is of the form `schedule(cls[, param])`

where `cls` is of `static, dynamic, guided, runtime`

#### Static `schedule(static, S)`
Split iterations into equal chunks of size `S`, assign to thread round-robin. If `S` is not specified, `S = N / nthreads` (uniform data partition model)
```c++
/* the following 2 are the same, each thread gets
T0: [0: 256]  T1: [256: 512]  T2: [512: 768]  T3: [768: 1024]
*/
#pragma omp parallel for schedule(static) num_threads(4)
for (int i = 0; i < 1024; i++)
#pragma omp parallel for schedule(static, 256) num_threads(4)
for (int i = 0; i < 1024; i++)

/* If chunk size is smaller 
T0: [0:128], [512:640]
T1: [128:256], [640:768]
T2: [256:384], [768:896]
T3: [384:512], [896:1024]
*/
#pragma omp parallel for schedule(static, 128) num_threads(4)
for (int i = 0; i < 1024; i++)
```
#### Dynamic `schedule(dynamic, S)`
Split iterations into equal chunks of size `S`, assign to thread when it is idle. If `S` is not specified, `S = 1`. (Work pool model)

Often has better load balance if the amount of work is uneven among iterations. However, it has more overhead due to dynamic nature. 

Also, tradeoffs between chunk size and dynamic scheduling overhead.  Larger chunk size may cause huge load imbalance (think of 20 chunks, 16 threads). 

#### Guided `schedule(guided, S)`
Dynamic scheduling, but instead of constant chunk size, it starts with a large chunk size and gets smaller as computation progresses, if loads gets imbalanced. 

`S` is the minimum size, if not specified, then `S = 1`. 

#### Runtime `schedule(runtime)`
Delay until runtime, by passing env variable `OMP_SHEDULE` to the program

#### Auto
If no schedule type is identified (either as clause or at runtime), the runtime system will choose the most appropriate schedule (depends on OS/hardware).

### `nowait` clause
Each `omp for` will have a implicit barrier, using `nowait` can cancel the wait behavior. 

## Sections and Tasks
In the for loop, each iteration of chunk of iterations have the same work. We can have similar kinds of parallelism with different tasks, using `sections`. 

### Sections
```c++
#pragma omp parallel {
    #pragma omp sections [clauses] {
        #pragma omp section {
            // task 1
        }
        #pragma omp section {
            // task 2
        }
        /* ... */
        #pragma omp section {
            // task n
        }
    }
}

// similar to for, it can be merged into
#pragma omp parallel sections [clauses]
```
`clauses list` includes `private, firstprivate, lastprivate, reduction, nowait`.  
`sections` behaves similar to `for`, it will have an implicit barrier (hence `nowait`). 

### Tasks
Another way is to use `task`, it is similar to `section`, but won't put barrier. For sync/barrier, we use `taskwait`. 
```c++
#pragma omp parallel {
    #pragma omp task [clauses] {
      // task 1
    }
    #pragma omp task [clauses] {
      // task 2
    }
    /* ... */
    #pragma omp task [clauses] {
      // task n
    }
}
```

Note that `omp task` generates a task whenever a thread encounters it, and the task can be executed immediate or deferred. A deferred task is not necessarily executed by the thread that creates it. And`taskwait` will wait for all `task` generated by the thread. 

With such properties, task are designed and mostly used for recursive decompositions. Where a single thread enters the function, generates new tasks when encounter the `omp task` clause, and then `taskwait` all generated `task` to be finished. 
```c++
// parallel recursive fibonacci implementation
int fib(int n) {
    int x, y;
    if (n < 2) return n;

    // x, y are local to the thread executing fib
    // but they have to be shared on recursive child tasks
    // further generated
    #pragma omp task shared(x)
    x = fib(n-1);
    #pragma omp task shared(y)
    y = fib(n-2);
    // wait for recursive calls and collect results
    #pragma omp taskwait

    return x + y;
}

int main() {
    int M = 5000;
    #pragma omp parallel {
        // single thread to enter the function call
        // other threads created by parallel will 
        // execute the tasks generated
        #pragma omp single
        fib(M);
    }
}
```