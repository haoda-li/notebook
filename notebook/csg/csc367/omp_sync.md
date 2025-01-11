# OpenMP - Synchronizations and Performance Profiling

## Synchronization

### `barrier`
Wait for all threads spawned by closest enclosing `parallel`. 
```c++
#pragma omp barrier
```

Note that `for` and `sections` will set implicit barriers. 

### `single` and `master`
```c++
#pragma omp single [private | firstprivate | nowait] {
    /* ... */
}
```
Only one thread will execute the code block, and set a implicit barrier unless `nowait`

```c++
#pragma omp single [private | firstprivate]{
    /* ... */
}
```
Only the master thread executes the code block, no barrier will be set. 

### `critical` sections
`critical [(name)]` Set up a critical section (in `section`) where threads must serialize to avoid race conditions.

```c++
int data = 100;
#pragma omp parallel sections {
    #pragma omp section {
        #pragma omp critical(cs1) {
        data += 42;
    }
}
    #pragma omp section {
        #pragma omp critical(cs1) {
            data += 5;
        }
    }
}
printf("Data=%d\n", data); // 149
```

### `atomic` 
If the critical section is just an update to a single memory location, and it's a supported atomic operation
```c++
#pragma omp atomic [ read | write | update | capture ]
var op= expr

// for example
#pragma omp atomic update
sum_global += sum_local;
```

Such operations still have overhead (varying based on hardware support), but smaller than `critical`. 

### Explicit `lock`
The same way as of pthread `mutex`
```c++
void omp_init_lock(omp_lock_t *lock); // pthread_mutex_init
void omp_destroy_lock(omp_lock_t *lock);// pthread_mutex_destroy
void omp_set_lock(omp_lock_t *lock); // pthread_mutex_lock
void omp_unset_lock(omp_lock_t *lock); // pthread_mutex_unlock
int omp_test_lock(omp_lock_t *lock); // pthread_mutex_trylock

// nested locks
// can be locked multiple times by same thread
// unlocked only once it's been unset the same number of times
void omp_init_nest_lock(omp_lock_t *lock);
void omp_destroy_nest_lock(omp_lock_t *lock);
void omp_set_nest_lock(omp_lock_t *lock);
void omp_unset_nest_lock(omp_lock_t *lock);
int omp_test_nest_lock(omp_lock_t *lock);
```

## Performance Profiling
`omp` has its built-in timing functions
```c++
// returns elapsed wall clock time in seconds
double omp_get_wtime();

double start = omp_get_wtime();
#pragma omp parallel {
    /* ... */
}
double time = omp_get_wtime() - start;

// returns the number of seconds between two successive clock ticks
double omp_get_wtick();

omp_get_wtick();
#pragma omp parallel {
    /* ... */
}
double time = omp_get_wtick();
```

### False Sharing and Cache Coherence
Consider our shared memory system, note that each thread (physically the core) gets its own L1 cache (and probably L2 depends on arch), while share the L3 cache and memory. 

Note that the smallest unit for moving between the cache and the memory is the cache line, typically 64 bytes. It is larger than a `float` (4 Bytes) or `double` (8 Bytes). If two (or more) threads are modifying close data, the cache line is not coherent among all threads, and the hardware (processor) need time to sync them up, which is called __false sharing__. 

> When a system participant attempts to periodically access data that is not being altered by another party, but that data shares a cache block with data that is being altered, the caching protocol may force the first participant to reload the whole cache block despite a lack of logical necessity.

A typical example is that each thread is given some iterative work, and at each iteration we update them into a global array
```c++
double result[NUM_THREADS] = {0};

#pragma omp parallel {
    int tid =  omp_get_thread_num();
    /* ... */
    for (int i = 0; i < N; i++) {
        result[tid] += ...;
    }
}
```
Solution: if you know the cache line size of the machine, then pad the array to avoid false sharing. 
```c++
/* cache line size / sizeof(double) */
# define PAD 8 
double result[NUM_THREADS][0] = {0};

#pragma omp parallel {
    int tid =  omp_get_thread_num();
    /* ... */
    for (int i = 0; i < N; i++) {
        result[tid][0] += ...;
    }
}
```