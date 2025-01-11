# Distributed Memory Model and MPI Introduction

## Distributed Memory Architecture

Commonly, a distributed memory system refers to a multiprocessor computer system in which each processor has its own private memory, and communicate messages through a __network__(interconnections). 

The __network__ refers to the the collection of processors and their communication interface . It can be seen as a graph where nodes are the processors and edges are the interconnections (for communication). The topology of such graph is a key factor of the network performance (latency, bandwidth, scalability). 

Compare to a shared memory model, distributed memory model can scale to much larger computations as we consider the hardware limit on shared memory. 

### Message Passing Model
Although distributed memory architecture supports different programs on each host, but the common usage (and the purpose of designing such distributed memory system), is to have all processes execute the same code, and communicate via messages, or Single Program Multiple Data (SPMD). 

The message passing model is primarily designed for distributed memory even though it can still apply to shared memory system 
- Nodes are connected with a network
- Partition the data across the nodes, computation in parallel
- If local data is needed on remote node, send it over the interconnect
- Computation is done collectively
- Can always add more and more nodes, bottleneck is not the number of cores or memory on a single node
- Scale out instead of scale up. Can increase the data size while increasing
processors

Programming philosophy is different from OpenMP/Pthreads
 - communication overhead is more significant, let the processes compute independently as much as possible (sometimes replicate data is better).
 - need to consider the message passing operations (since each process now have different data)
 - data partition based, since SPMD.

## MPI: Message Passing Protocol
The standard library for message passing. 

In the C/C++ files 
```c
#include <mpi.h>
```

Run the program 
```bash
mpirun -np 8 ./myapp arg1 arg2
```

However, since MPI is mostly used in large scale systems for scientific computations. There are other toolchains to compile, run, and manage them (commonly Slurm, command `srun`). 

### Basics

#### `MPI_init, MPI_finalize`
`MPI_init` the MPI environment, extract and remove MPI parts of the command line args

```c
// init the MPI env
// MPI_SUCCESS or err code
int MPI_init(int *argc, char ***argv);
```

`MPI_finalize` terminate the env, and no MPI calls are allowed afterwards.
```c
// terminate MPI environment
// MPI_SUCCESS or err code
int MPI_Finalize();
```

#### `MPI_Comm, MPI_COMM_WORLD`
`MPI_Comm` the struct (communicators) that store info. about __communication domains__ (set of processes that are allowed to communicate). By default, stored in `MPI_COMM_WORLD`

Communicator size and id of current process can be obtained
```c
int MPI_Comm_size(MPI_Comm comm, int *size);
int MPI_Comm_rank(MPI_Comm comm, int *rank);
```

#### `MPI_Wtime`
Get the elapsed time on the processor, in secs
```c
double MPI_Wtime();
```

#### Basic Example
```c
int main(int argc, char **argv) {
    // first thing to do, init MPI env, get #processes and id
    MPI_Init( &argc, &argv );
    double start, end;
    start = MPI_Wtime();
    int n_proc, rank;
    // use default communicator MPI_COMM_WORLD 
    MPI_Comm_size(MPI_COMM_WORLD, &n_proc);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    /* read your program args and run program in MPI world*/

    end = MPI_Wtime();
    printf("Elapsed time: %f\n", t2 - t1); 
    // last thing, terminate MPI env
    MPI_Finalize();
    return 0;
}
```

### Data types
data types are used to determine what kind of data is to communicate (so that we can use typed variables as buffer to send and receive them).

Basic data types equivalent to built-in C types, including
```c
MPI_CHAR, MPI_UNSIGNED_CHAR // 1
MPI_SHORT, MPI_UNSIGNED_SHORT // 2
MPI_INT, MPI_UNSIGNED // 4
MPI_LONG, MPI_UNSIGNED_LONG // 8
MPI_FLOAT // 4
MPI_DOUBLE // 8
```
In addition 
```c
MPI_BYTE // used like MPI_UNSIGNED_CHAR
MPI_PACKED // used with pack and unpack 
MPI_Datatype // used to define new data type
``` 

#### `MPI_Datatype`
The super class of all C equivalent data types, and it can be used to create new data type (for example sending `struct`). 

```c
MPI_Type_contiguous(int size, MPI_Datatype oldtype, MPI_Datatype *newtype);
MPI_Type_commit(MPI_Datatype *newtype);


// example
typedef struct {
  double x;
  double y;
  double z;
} vec3d;

MPI_Datatype MPI_VEC3D;

// define the MPI version of vec3d
// struct is just a contiguous memory
MPI_Type_contiguous(3, MPI_DOUBLE, &MPI_VEC3D);
// commit it so that it can be used in communications
MPI_Type_commit(&MPI_VEC3D);
```

#### Pack and Unpack
Pack/unpack several variables (with different data type) together for communication. 
```c
int MPI_Pack(
    const void *inbuf, // pointer to data to be packed
    int incount, // count of to be packed data
    MPI_Datatype datatype, // dtype of to be packed data
    void *outbuf, // pointer to the "pack" buffer
    int outsize, // size of the "pack" buffer in Bytes
    int *position, // current position in buffer, in bytes
    MPI_Comm comm 
);

int MPI_Unpack(
    const void *inbuf,
    int insize,
    int *position,
    void *outbuf,
    int outcount,
    MPI_Datatype datatype,
    MPI_Comm comm
);


// example
short c[50];
int i;
char buffer[110];
int position = 0;

MPI_Pack(c, 50, MPI_SHORT, buffer, 110, &position, MPI_COMM_WORLD);
MPI_Pack(i, 1, MPI_INT, buffer, 110, &position, MPI_COMM_WORLD);

// communication, more on later
MPI_Send(buffer, position, MPI_PACKED, 1, 0, MPI_COMM_WORLD);
MPI_Recv(buffer, 110, MPI_PACKED, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

MPI_Unpack(buffer, 110, &position, &i, 1, MPI_INT, MPI_COMM_WORLD);
MPI_Unpack(buffer, 110, &position, c, 50, MPI_SHORT, MPI_COMM_WORLD);
```
