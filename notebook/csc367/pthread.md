# Shared Memory Model with PThread
## Shared Memory Model
A parallel programming model is the languages/libraries that abstract a machine system (with multiple cores/processors/servers). 

It helps us to identify controls (how to start parallelism, the ordering of operations), data (private vs. shared, what kind of interactions), synchronization (when to communicate, atomic ops).

Shared memory model is the most common model for personal computers, where each program is a collection of threads of control, and can be created mid-execution. 

For shared memory model, each worker is a thread. Each threads has a set of private variables and all together a set of shared variables. Communications are implicitly done by reading/writing the shard variables. 

## POSIX Threads (PThreads)
Using PThreads with 

```c++
#include <pthread.h>
```
compile (using `gcc`) with 
```sh
gcc -lpthread *.c 
```

### Fork

`pthread_create` starts a new thread in the calling processing, return `0` on success, error code on error. 
```c
int pthread_create(
    pthread_t *thread,
    const pthread_attr_t *attr,
    void *(*func)(void *),
    void *arg
);
```
`pthread_join` waits for the `thread` to terminate. return `0` on success, error code on error. 
```c
int pthread_join(
    pthread_t thread, 
    void **retval
);
```

A simple code example (this is a toy example and poorly performed)
```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// the program fills the arr with 1's

void* fill_one(void *data) {
    int *arr = (int *) data;
    *arr = 1;
}

int main() {

    // the shared variable
    int arr[5] = {0};

    pthread_t threads[5];
    int i;
    for (i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, fill_one, &(arr[i]));
    }
    for (i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    for (i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
}
```
## Mutex
Because the code does not run sequentially, we don't know when a thread switches to another. 
```c

// the program aims to make a into 1

void* make_true(void *data) {
    int *a = (int *) data;
    if (*a == 0) (*a)++;
}

int main() {
    int a = 0;
    pthread_t threads[20];
    int i;
    for (i = 0; i < 20; i++) {
        pthread_create(&threads[i], NULL, make_true, &a);
    }
    for (i = 0; i < 20; i++) {
        pthread_join(threads[i], NULL);
    }
    printf("%d", a);
}
// output can be any number from 1 to 20
```

### Mutual Exclusion 
A __race condition__ happens when 2 or more threads manipulate a shared resource. The segment of code accessing the shared resources is the __critical section__. 

__Mutual exclusion__ means that only one thread can enter the critical section, and others must wait _BEFORE_ entry, and another thread enters CS when the thread leaves. 

### Mutex API
```c
pthread_mutex_t lock;

// init a mutex
int pthread_mutex_init(
    pthread_mutex_t *mutex,
    const pthread_mutexattr_t *attr
);
// lock the mutex, if already locked, then blocked until obtain the lock
int pthread_mutex_lock(pthread_mutex_t *mutex); 
// lock the mutex, if already locked, then return EBUSY
int pthread_mutex_trylock(pthread_mutex_t *mutex);
// unlock the mutex
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

Then, we can make a correct example 

```c
// need a struct to pass lock and data into the func
typedef struct {
    int num;
    pthread_mutex_t lock;
} int_thread;

void* make_true(void *data) {
    int_thread *a = (int_thread *) data;
    pthread_mutex_lock(a->lock);
    if (a->num == 0) a->num ++;
    pthread_mutex_unlock(a->lock);
}

int main() {
    // allocate and init the lock
    pthread_mutex_t lock;
	pthread_mutex_init(&lock, NULL);

    int_thread a = {0, lock};
    
    pthread_t threads[20];
    int i;
    for (i = 0; i < 20; i++) {
        pthread_create(&threads[i], NULL, make_true, &a);
    }
    for (i = 0; i < 20; i++) {
        pthread_join(threads[i], NULL);
    }
    printf("%d", a);
}
// output 1
```

Note that the mutex lock is not unique in your program. You can have several locks for higher degree of concurrency and have more fine-grained controls (with the risk of more sync bugs).

### Correctness and Deadlock

Note that mutex does not solve sync issues automatically. It's just a "lock".

__Deadlock__ is another typical bug introduced by the lock, deadlock happens when a thread never releases a lock. 

A typical (but does not happen often) example 
```c
pthread_mutex_lock(lock);
/*...*/
if (cond) return false;
/*...*/
pthread_mutex_unlock(lock);
return true;
```

Deadlock happens mostly when we have multiple locks, a typical example

```c
// thread 1
pthread_mutex_lock(A);
/*...*/
pthread_mutex_lock(B);
/*...*/
pthread_mutex_unlock(A);
/*...*/
pthread_mutex_unlock(B);


// thread 2
pthread_mutex_lock(B);
/*...*/
pthread_mutex_lock(A);
/*...*/
pthread_mutex_unlock(B);
/*...*/
pthread_mutex_unlock(A);
```

Simplest way to avoid is to __enforce same ordering of locks in every piece of code__. 

### Overhead
Note that the waiting causes lock contention. Even without waiting, mutex acquiring has overhead. 

Solution: localize computations are much as possible, make fewer global updates. 
For reducing lock overhead on smaller operations, we can also use `atomic` operations. 

## Barriers
Another way to do synchronization is to use barrier. It works similar to `pthread_join`  in the master thread, which waits for all forked threads to finish.  
Threads that reach the barrier stop until other `n-1` threads (`n` often defined as #threads)  have reached it as well. 

### Barrier API
```c
// init the barrier, with the number of threads to wait
int pthread_barrier_init(
    pthread_barrier_t *barrier,
    const pthread_barrierattr_t *attr,
    unsigned int count
);

// wait till all threads reach this point
int pthread_barrier_wait(pthread_barrier_t *barrier);
// destroy the barrier data
int pthread_barrier_destroy(pthread_barrier_t *barrier);

// Common usage
pthread_barrier_t barrier;
pthread_barrier_init(&barrier, NULL, num_threads);
```