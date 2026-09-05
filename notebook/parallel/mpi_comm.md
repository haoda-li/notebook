# MPI Communications
There are two flavors of communication

- Point-to-point operations: one processor send, another receive
- Collective operations: all processors participate in communications. With some common patterns. 

## Point-Point Communication
A processor communicates with another with sending and receiving messages. 

### `MPI_Send, MPI_Recv` Basic messaging

```c++
// send a message to the dest process
int MPI_Send(
    void *buf, // pointer to the message to be sent
    int count, // count of message
    MPI_Datatype datatype, // datatype of message
    int dest, // destination process
    int tag, // tag to distinguish it from other messages
    MPI_Comm comm
);
// receive a message from the source process
// and save the status
int MPI_Recv(
    void *buf, // pointer to the receiving buffer
    int count, // count of message 
    MPI_Datatype datatype, // datatype of message
    int source,  // source process
    int tag, // tag to distinguish it from other messages
    MPI_Comm comm, 
    MPI_Status *status
);

// the status struct
typedef struct MPI_Status {
    int MPI_SOURCE; // source of the received message
    int MPI_TAG; // tag of the received message
    int MPI_ERROR; // a potential error code
};
// to retrive the length of received message
int MPI_Get_count(MPI_Status *status, MPI_Datatype datatype, int *count);
```

#### Message Blocking
`MPI_Recv` is blocking, which means it will wait to return until message is received and put into `buf`. 

`MPI_Send` is not necessarily blocking, depends on the implementation, it 

- either blocks until the message is received, 
- or put the msg into another buffer and returns without waiting. 

`buf`, in both send and receive, are safe to reuse after the function returns. 

#### Deadlock

__WARNING__ Due to the unspecified behavior of `MPI_Send`, it can be either blocking or non-blocking. Consider the circular chain (each process send to the next one, and receive from previous one) example
```c++
// rank is the current process id
// np is the number of processes
MPI_Send(a,20, MPI_INT, (rank+1)%np, 1, MPI_COMM_WORLD);
MPI_Recv(b,20, MPI_INT, (rank-1+np)%np, 1, MPI_COMM_WORLD, &status);
```
If the implementation is blocking, then it will cause a deadlock, as all processes waiting for the blocked send to receive. 

Solution
```c++
if (rank % 2) {
    MPI_Send(a,20, MPI_INT, (rank+1)%np, 1, MPI_COMM_WORLD);
    MPI_Recv(b,20, MPI_INT, (rank-1+np)%np, 1, MPI_COMM_WORLD, &status);
}
else {
    MPI_Recv(b,20, MPI_INT, (rank-1+np)%np, 1, MPI_COMM_WORLD, &status);
    MPI_Send(a,20, MPI_INT, (rank+1)%np, 1, MPI_COMM_WORLD);
}
```

### `MPI_Sendrecv` Send/recv simultaneously
The deadlock problem is a common pattern, while handling such deadlocks is time consuming and annoying. Thus, a more elegant solution is to use `MPI_Sendrecv`.

Its API is self-explanatory 
```c++
int MPI_Sendrecv(
    void *sendbuf, int sendcount, MPI_Datatype sendtype, int dest, int sendtag,
    void *recvbuf, int recvcount, MPI_Datatype recvtype, int source, int recvtag,
    MPI_Comm comm, 
    MPI_Status *status
);

// circular chain
MPI_Sendrecv(
    a, 20, MPI_INT, (rank+1)%np, 1,
    b, 20, MPI_INT, (rank-1+np)%np, 1,
    MPI_COMM_WORLD, &status
);
```
Note that in this case, `send` and `recv` may happen simultaneously (depends on implementation). Therefore, `sendbuf, recvbuf` must be different. 

Another API is to use single buffer so that received message replaces sent message in the same buffer. In this case, the send and recv message must be the same size and type.
```c++
int MPI_Sendrecv_replace(
    void *buf, int count, MPI_Datatype datatype, 
    int dest, int sendtag,
    int source, int recvtag,
    MPI_Comm comm, MPI_Status *status
);
```

### `MPI_Isend, MPI_Irecv`, Non-blocking send/receive
Non-blocking send and recv will immediately return. 

__WARNING__ it unsafe to reuse after the function returns. The copying to communication buffer may not be finished as function returns.

```c++
// API, almost the same as send and recv
int MPI_Isend(
    const void *buf, int count, MPI_Datatype datatype, int dest, int tag,
    MPI_Comm comm, 
    MPI_Request *request
);
int MPI_Irecv(
    void *buf, int count, MPI_Datatype datatype, int source, int tag, 
    MPI_Comm comm, 
    MPI_Request * request
);
```

The `MPI_Request` will record the process status, and it is used with `MPI_Test` and `MPI_Wait` to determine whether the communication has finished. 

```c++
/* test whether finish
   if finished then return non-zero, and set flag to non-zero, 
   and deallocate request, set to MPI_REQUEST_NULL,
   and set approriate status as blocking send/recv
   if not finished then return zero
*/
int MPI_Test(MPI_Request *request, int *flag, MPI_Status *status);

/* block until request finishes, 
   and deallocate request, set to MPI_REQUEST_NULL
   and set approriate status as blocking send/recv
*/
int MPI_Wait(MPI_Request *request, MPI_Status *status)
```

## Collective Operations

Collective operations are common computing patterns where all processes communicate. 

All collective operations __have implicit barrier__ that blocks till finish. 

### `MPI_Barrier`
As all other barrier, blocks until __ALL__ processes is here. 

__WARNING__ barrier must be  set in all processes. Barrier, as OpenMP, is implemented on a count base. It releases all processes when counts to `n_processes`.

```c++
int MPI_Barrier(MPI_Comm comm);

/* Deadlock example
if (rank % 2) {
    ...
    MPI_Barrier(MPI_Comm comm);
}
*/
```

### `MPI_Bcast` Broadcast
Broadcasts a message from the process with rank root to all other processes
```c++
int MPI_Bcast(
    void *buffer, int count, MPI_Datatype datatype, int root, 
    MPI_Comm comm
);
```
For example, root process will generate the data (with some randomness) and broadcast to all processes so that all processes get the same data.
```c++
int data[100];
int root = 0, rank;
MPI_Comm_rank(MPI_COMM_WORLD, &rank);

// root process generate data
if (rank == root) random_init(data);

/* 
    "-" can be 0 or any garbage in the memory
    P0: 1 4 3 5 2 4 ... 3
    P1: - - - - - - ... -
    P1: - - - - - - ... -
    P1: - - - - - - ... -
*/
MPI_Bcast(data, 100, MPI_INT, root, MPI_COMM_WORLD);
/* 
    P0: 1 4 3 5 2 4 ... 3
    P1: 1 4 3 5 2 4 ... 3
    P2: 1 4 3 5 2 4 ... 3
    P3: 1 4 3 5 2 4 ... 3
*/
```

Broadcast is more efficient then let the root send `np-1` messages out, since it is optimized to send message in a hierarchical way (eg. `root -> 2 processes -> 4 processes -> ... -> all processes`). 

### `MPI_Reduce` Reduction
Reduces values on all processes to a single value, stored in the `root` process.  

Or `Allreduce`, stored (broadcast) in all processes.

Note that it is an element-wise reduction so that send buffer and recv buffer must be of the same count and dtype. 

```c++
int MPI_Reduce(
    const void *sendbuf, void *recvbuf, 
    int count, MPI_Datatype datatype,
    MPI_Op op, 
    int root, 
    MPI_Comm comm
);

int MPI_Allreduce(
    const void *sendbuf, void *recvbuf, 
    int count, MPI_Datatype datatype, 
    MPI_Op op, 
    MPI_Comm comm
);

/* MPI_Op is the reduction operation */
// max min argmax argmin
MPI_MAX, MPI_MIN, MPI_MINLOC, MPI_MAXLOC
// sum product
MPI_SUM, MPI_PROD
// logical and or xor
MPI_LAND, MPI_LOR, MPI_LXOR
// bitwise and or xor
MPI_BAND, MPI_BOR, MPI_BXOR
// or user defined op
```
Intuitive example of reduction with sum
```c
int data[6], sum[6];
init_darandom_init(data);ta
/* data:
    P0: 1 3 2 5 2 4
    P1: 4 5 2 6 2 5
    P2: 2 5 3 6 1 4
    P3: 5 6 1 0 6 2
*/

MPI_Reduce(data, sum, 6,  MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
/* sum:
    P0: 12 19  8 17 11 15
    P1:  -  -  -  -  -  -
    P2:  -  -  -  -  -  -
    P3:  -  -  -  -  -  -
*/
MPI_Allreduce(data, sum, 6,  MPI_INT, MPI_SUM, MPI_COMM_WORLD);
/* sum:
    P0: 12 19  8 17 11 15
    P1: 12 19  8 17 11 15
    P2: 12 19  8 17 11 15
    P3: 12 19  8 17 11 15
*/
```

### `MPI_Scatter, MPI_Gather`

Scatters a buffer to all processes, 
`Scatterv` version can specify different number of elements to be scattered
```c++
int MPI_Scatter(
    const void *sendbuf, int sendcount, MPI_Datatype sendtype,
    void *recvbuf, int recvcount, MPI_Datatype recvtype, 
    int root,
    MPI_Comm comm
);

int MPI_Scatterv(
    const void *sendbuf, 
    // array of length n_process, 
    // specifying the number of elements to send to each processor
    const int *sendcounts, 
    // array of length n_process, 
    // specifying the displacement (relative to sendbuf)
    const int *displs,
    MPI_Datatype sendtype,
    void *recvbuf, int recvcount, MPI_Datatype recvtype,
    int root, 
    MPI_Comm comm
);
```
Gathers together values from a group of processes.  
`Gatherv` version can specify different number of elements to be gathered.  
`Allgather, Allgatherv` is similar to all reduce, where the gather results are broadcasted to all processes.
```c++
int MPI_Gather(
    const void *sendbuf, int sendcount, MPI_Datatype sendtype,
    // recv args only apply to the root process, 
    // can be invalid for other processes
    void *recvbuf, int recvcount, MPI_Datatype recvtype, 
    int root, 
    MPI_Comm comm
);

int MPI_Gatherv(
    const void *sendbuf, int sendcount, MPI_Datatype sendtype,
    // recv args only apply to the root process, 
    // can be invalid for other processes
    void *recvbuf, 
    const int *recvcounts, 
    const int *displs,
    MPI_Datatype recvtype, 
    int root, 
    MPI_Comm comm
);

int MPI_Allather(
    const void *sendbuf, int sendcount, MPI_Datatype sendtype,
    void *recvbuf, int recvcount, MPI_Datatype recvtype,
    MPI_Comm comm
);

int MPI_Allgatherv(
    const void *sendbuf, int sendcount, MPI_Datatype sendtype,
    void *recvbuf, 
    const int *recvcounts, 
    const int *displs,
    MPI_Datatype recvtype, 
    MPI_Comm comm
);
```

The self-explanatory example

```c++
int a[8], b[4];
if (rank == root) init_data(a);

/* a
    P0: 1 2 3 4 5 6 7 8
    P1: - - - - - - - -
    P2: - - - - - - - -
    P3: - - - - - - - -
*/
MPI_Scatter(a, 2, MPI_INT, b, 2, MPI_INI, root, MPI_COMM_WORLD);
/* b
    P0: 1 2 - -
    P1: 3 4 - -
    P2: 5 6 - -
    P3: 7 8 - -
*/

(*b) *= -1;
/* b
    P0: -1 2 - -
    P1: -3 4 - -
    P2: -5 6 - -
    P3: -7 8 - -
*/
MPI_Gather(b, 2, MPI_INT, a, 2, MPI_INT, root, MPI_COMM_WORLD);
/* a
    P0: -1  2 -3  4 -5  6 -7  8
    P1:  -  -  -  -  -  -  -  -
    P2:  -  -  -  -  -  -  -  -
    P3:  -  -  -  -  -  -  -  -
*/
MPI_Allather(b, 2, MPI_INT, a, 2, MPI_INT, MPI_COMM_WORLD);
/* a
    P0: -1  2 -3  4 -5  6 -7  8
    P1: -1  2 -3  4 -5  6 -7  8
    P2: -1  2 -3  4 -5  6 -7  8
    P3: -1  2 -3  4 -5  6 -7  8
*/
```

### `MPI_Alltoall`
Sends data from all to all processes (better explained with example).

If `sendcount, recvcount` are both `1`, then it can be understood as a transpose. 
```c
int MPI_Alltoall(
    const void *sendbuf, int sendcount, MPI_Datatype sendtype,
    void *recvbuf, int recvcount, MPI_Datatype recvtype,
    MPI_Comm comm
);

// example
int a[8], b[8];
if (rank == root) init_data(a);
/* a
    P0:  0  1  2  3  4  5  6  7
    P1: 10 11 12 13 14 15 16 17
    P2: 20 21 22 23 24 25 26 27
    P3: 30 31 32 33 34 35 36 37
*/
MPI_Alltoall(a, 2, MPI_INT, b, 2, MPI_INT, MPI_COMM_WORLD);
/* b
    P0:  0  1 10 11 20 21 30 31
    P1:  2  3 12 13 22 23 32 33
    P2:  4  5 14 15 24 25 34 35
    P3:  6  7 16 17 26 27 36 37
*/
```