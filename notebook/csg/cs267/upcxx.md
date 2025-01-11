# UPC++ Introduction

[UPC++ User guide](https://upcxx.lbl.gov/docs/html/guide.html)

UPC++ is an asynchronous RMA/RPC library for distributed C++ applications. Compared to MPI, which the distribution happens on processors, UPC communicates by reading/writing memory using a partitioned global address space. 

The distributed computing model are great for structured/regular data, since we need to cache the remote data and synchronize after each timestep. However, MPI is hard to use for irregular data structures such as meshes, sparse matrices, hash tables; and irregular/asynchronous data movement/updates. 

## Remote Direct Memory Access (RDMA)

Recent advancement in hardware allows for RDMA and changes the communication pattern for distributed systems. 

Considering the communication model, MPI uses a two-sided message model, one proc send a data package to another, and the other one need to receive them in (possibly virtual) buffer and put them into correct locations. A shared-memory model often use one-sided communication, each thread does not check the memory address but send/put data directly into the address. 

The process model for UPC++ is similar to MPI in many ways, but focuses on one-sided communication model (no need to match sends to receives, no unexpected messages, no need to guarantee message ordering). The metadata is shared among processors rather than split between send and receiver. 

## Introduction
Compiling a UPC++ program, 

```bash
upcxx -g hello-world.cpp -o hello-world.exe
```

Launching the program with UPC++ context 

```bash
upcxx-run -n 4 ./hello-world.exe # -n num_procs
```

```cpp title="hello-world.cpp"
#include <iostream>
#include <upcxx/upcxx.hpp>
using namespace std;
using namespace upcxx;
int main() {
    init(); 
    cout << "process: "<< rank_me() << endl;
    cout << "number processes: "<< rank_n() << endl;
    finalize();
    return 0;
}
```

## Global Memory
Allocate global memory in shared segments, accessible by all processors. The actual data will exist on the calling process's shared segment. 

```cpp
// the data is on a global shared segment
new_<T>(...); // analogy to new , calls the class constructor and allocating memory
delete_(global_ptr<T>); // analogy to delete ptr

// Example: store the rank of the proc
global_ptr<int> gptr = new_<int>(rank_me());

new_array<T>(size); // allocating 1-d array
delete_array(gptr); // delete array

// Example: create an int array of size 10
global_ptr<int> gptr_arr = new_array<int>(10);
delete_array(gptr_arr); 

// allocate and deallocate without calling constructors
allocate<T>(size); // analogy to malloc
deallocate(gptr); // analogy to free
```

### Downcasting with `local`
If the shared memory is located to a local process, then can obtain a local address. 
```cpp
// a precondition of global_ptr<T>::local()
UPCXX_ASSERT(x_arr.is_local());   
int *local_ptr = x_arr.local();
local_ptr[i] = ... // work with local ptr
```

### Distributed Objects

Each process cannot automatically get global pointers defined by other processes, we need a space to get each other's global pointers (or values). UPC++ provides distributed objects. Each proc will have the same variable name, but different values. 

```cpp
// create a distributed variable with value
dist_object<T> var(T value);

// Example: get each other's value
dist_object<double> x(0);
*x = random(); // assign a random number to the dist as of a pointer
// get value from the next proc
double next_x = x.fetch((rank_me() + 1) % rank_n()).wait(); 
```
This is essentially for sharing global pointers
```cpp
dist_object<global_ptr<double>> x_global(new_array<double>(10));
// get local pointer
double *x = x_global->local();
// get pointer to the next proc
global_ptr<double> next_x = x_global.fetch((rank_me() + 1) % rank_n()).wait(); 
```

### Asynchronous communication (RMA)

The data communication in the shared segment is in general asynchronous. We need to initiate the operation and wait for its completion. 

```cpp
// remotely get data from the pointer
future<T> rget(global_ptr<T> gptr);
// remotely put the data value 
rput(T local_value, global_ptr<T> gptr);

// Example: rget
global_ptr<int> gptr; // assume that gptr points to some remote data
future<int> f1 = rget(gptr);
/* unrelated work, rget is non-blocking */
int t1 = f1.wait(); // wait for completion, blocking
```

## Synchronization

Barriers that is the same as of other libraries. 

```cpp
barrier(); // block until all other threads arrive

// barrier in the upcxx manner
future<> f = barrier_async(); // thread is ready for barrier
f.wait();
```

### Future
Similar to `promise` in javascript, future is the returning value of an async operation and holds the returning values plus a state. 

```cpp
future<T> f = ... // any async operation defined by UPC++
bool ready = f.ready(); // return true if finishes
f.wait(); // blocking until f is ready
```

### Callbacks
Similar to the callback chaining in javascript. `then` can be attached to a future, and invoked after the future is ready. Note that the return type of `then` is a `future`. 

```cpp
// remotely get numbers and add 1 to it
future<int> f1 = rget(gptr);
future<int> f2 = f1.then([](int x1) { return x1 + 1; });
int gptrp1 = f2.wait();

// chaining to simplify the syntax
int gptrp1 = rget(gptr).then([](int x) { return x + 1; }).wait();
```

### Conjoining futures
Conjoin multiple `future`s into one, and wait for all of them are ready. 

```cpp
future<T1, T2> when_all(future<T1> f1, future<T2> f2);

// add two numbers from two remote pointers and return the sum
int sum = when_all(rget(gptr1), rget(gptr2)).then([](int x1, int x2) { return x1 + x2; }).wait();
```



## Remote procedure calls (RPC)

An RPC enables the calling process to invoke a function at a remote process, using parameters sent to the remote process via the RPC. 

```cpp
future<RType> rpc(intrank_t rank, Func function, Arg arg1, Arg arg2, ...);

// Example: invoke a multiplication on rank r
future<int> fut_result = rpc(r, [](int a, int b) { return a * b; }, a, b);
// the execution is done on r, but the result is returned back to local rank
int result = fut_result.wait();

// Example: summing local on rank 0
int sum = 0; // global variable
rpc(0, [](int x) { sum += x;}, local).wait();
// now sum in rank 0 will have the sum of all local
```

## Atomics

Atomic operations use an "atomic domain" to specify the operations needed and the data type. 

```cpp
atomic_domain<Dtype> ad({ atomic_op1, atomic_op2, ... });

// Example: summing numbers

global_ptr<int> sum = ...; // global ptr points to sum
int local = ...; // local number to be added

// specify the supported ops and create the atomic domain
atomic_domain<int> ad({ atomic_op::load, atomic_op::fetch_add }); 
// perform the atomic add
ad.fetch_add(local, sum, memory_order_relaxed).wait();
``` 

## Collectives

Collectives are similar to other libraries, mainly broadcast and reduction

### Broadcast
```cpp
future<T> broadcast(T value, intrank_t sender);
future<> broadcast(T *buffer, size_t count, intrank_t sender);

// broacast rank number from rank 0 to all procs
// root_rank on all procs will be 0
int root_rank = broadcast(rank_me(), 0).wait();


int arr[10];
if (rank_me == 0) {
  for (int i = 0; i < 10; i++)
    arr[i] = i;
}
broadcast(arr, 10, 0).wait();
// all procs now will have arr = [0, 1, 2, ..., 9]
```

### Reduction
Reduction supports operations includes `op_fast_add, op_fast_mul, op_fast_min, op_fast_max, op_fast_bit_and, op_fast_bit_or, and op_fast_bit_xor`

```cpp
future<T> reduce_all(T value, BinaryOp op);
future<T> reduce_all(T* src, T* dest, size_t count, BinaryOp op);
future<T> reduce_one(T value, BinaryOp intrank_t receiver);
future<T> reduce_one(T* src, T* dest, size_t count, BinaryOp intrank_t receiver);

// summing all local across procs
int sum = reduce_all(local, op_fast_add).wait();

// elementwise summing arrays to root
int sum_buffer[4];

/* suppose that there are 4 procs with local_buffer
proc 0:  1  2  3  4
proc 1:  2  2  3  4
proc 2:  0  3  1  3
proc 3:  9  5  3  1
sum   : 12 12 10 12
*/
reduce_one(local_buffer, sum_buffer, 4, op_fast_add, 0);
// now sum_buffer on rank 0 will haev 12 12 10 12
```

## Example: Distributed Hash Table

```cpp
#include <map>
#include <upcxx/upcxx.hpp>

using namespace upcxx;
using namespace std;

class DistrMap {
private:
  // store the local unordered map in a distributed object to access from RPCs
  using dobj_map_t = dist_object<unordered_map<string, string>>;
  dobj_map_t local_map;
  // map the key to a target process
  int get_target_rank(const string &key) {
    return hash<string>{}(key) % rank_n();
  }
public:
  // initialize the local map
  DistrMap() : local_map({}) {}
  // insert a key-value pair into the hash table
  future<> insert(const string &key, const string &val) {
    // the RPC returns an empty future by default
    return rpc(
      get_target_rank(key),
      // lambda to insert the key-value pair
      [](dobj_map_t &lmap, const string &key, const string &val) {
        // insert into the local map at the target
        lmap->insert({key, val});
      },
      local_map, key, val
    );
  }
  // find a key and return associated value in a future
  future<string> find(const string &key) {
    return rpc(
      get_target_rank(key),
      // lambda to find the key in the local map
      [](dobj_map_t &lmap, const string &key) -> string {
        auto elem = lmap->find(key);
        if (elem == lmap->end()) return string(); // not found
        else return elem->second; // key found: return value
      }, 
      local_map, key
    );
  }
};
```