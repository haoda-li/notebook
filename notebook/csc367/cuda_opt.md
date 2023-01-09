# CUDA Programming - Parallel Reduction

To parallelize a reduction, obviously we will do binary operations pair-wise in each time step, collect the results, and then reduce pair-wise until obtaining the final results. For a $N$ elements array, such reduction will take `lg(n)` time steps. 

Note that GPU can only synchronize block-wise, global synchronization can only be done implicitly when kernel finishes.

We will use the sum example

## Interleave Addressing
The basic idea is to 
1. load one element from global memory to shared memory
2. each thread reduce two elements and so on, until one thread left.
3. write the shared memory back to global memory.

```c++
__global__ void dot_product0(float *g_idata, float *g_odata) {
    // for dynamic sized shared memory
    extern __shared__ int sdata[];
    unsigned int tid = threadIdx.x;
	unsigned int i = blockIdx.x * blockDim.x + threadIdx.x;

    sdata[tid] = g_idata1[i];
    __syncthreads();
    
    for(unsigned int s = 1; s < blockDim.x; s*=2){
	    if (tid % (2*s) == 0)  sdata[tid] += sdata[tid + s];
		__syncthreads();
	}
	
	if (tid == 0) { g_odata[blockIdx.x] = sdata[0]; }
}

#define M (1024*1024)

int main() {
    /* all GPU arrays pointers are already allocated 
        d_idata: M array, alreay copied input data
        s: float, 1024
    */
    int block_num = M;
    while (block_num > 1) {
        dot_product0<<<block_num, 128, 128 * sizeof(float)>>>(d_idata, d_idata);
        block_num /= 128;
    }
    /* d_idata[0] is now the sum */
}
```

## Divergence Execution
Adjacent threads will run different if-branch, causing divergent execution. Although we don't have the else branch, the threads running the else branch, since within the same warp, are waiting for the then branch. Instead of scheduling new work. 

```c++
/* 
if (tid % (2*s) == 0)  sdata[tid] += sdata[tid + s]; 
*/

// Instead, we write
int idx = 2 * s * tid;
if (idx < blockDim.x) sdata[idx] += sdata[idx + s];
```
Thus, we are doing the same interleave addressing, but the adjacent threads are computing the same branch. For the latter half, they can be scheduled with new works.  

## Bank Conflict
Note that shared memory are managed in 4 Byte banks. Thus in each time step, the same bank (eg. `shmem[0], shmem[32], ...`) are accessed by different threads in the same warp, causing bank conflict. 

To avoid bank conflict, reverse fop loop and threadID-based indexing as 
```c++
/*
for(unsigned int s = 1; s < blockDim.x; s*=2){
     int idx = 2 * s * tid;
        if (idx < blockDim.x) sdata[idx] += sdata[idx + s];
   __syncthreads();
}
*/

// Instead, we write
for (unsigned int s = blockDim.x/2; s > 0; s >>= 1) { 
    if (tid < s) {  
        sdata[tid] += sdata[tid + s];
    }
    __syncthreads();
}
```

## Unroll First Iteration
Consider the kernel, note that half of the thread will only execute the read part and idle. Thus, we can unroll the first iteration of the for loop to reduce idle time. 

```c++
/*
sdata[tid] = g_idata1[i];
*/

// gridSize need to be halved since now each thread will read 2 elements
sdata[tid] = g_idata[i] + g_idata1[i+blockDim.x];
```
Note that we can even take steps further by unroll first few iterations, so that fewer threads get idled. 

```c++
/*
sdata[tid] = g_idata1[i];
*/

// blockSize can be provided using template
// gridSize need to be tuned since now each thread will read lg n elements
unsigned int gridSize = blockSize * 2 * gridDim.x;
sdata[tid] = 0;
while (i < n) {
    sdata[tid] += g_idata[i] + g_idata[i + blockSize];
    i += gridSize;
}
```
## Unroll the Warp
Using the property that _instructions are synced within a warp_. We can save more instructions and `__syncthreads()`. Now, we can end the loop at 32 for all threads, and only one warp will run the unrolled warp code. 
```c++
/*
for (unsigned int s = blockDim.x/2; s > 0; s >>= 1) { ... }
*/

for (unsigned int s = blockDim.x/2; s > 32; s >>= 1) { ... } 

if (tid < 32) {
    // volatile enforce warp sync execution
    // by preventing compiler optimzations on the shared mem
    volatile int* smem = sdata;
    smem[tid] += smem[tid + 32];
    smem[tid] += smem[tid + 16];
    smem[tid] += smem[tid + 8];
    smem[tid] += smem[tid + 4];
    smem[tid] += smem[tid + 2];
    smem[tid] += smem[tid + 1];
}
```

## Complete Unrolling using template
Note that we call the kernel with a given `blockSize`, and we know that each block can have a max of 1024 threads. Thus we know the block size at compile time. We can use C++ template to complete unroll the for loop, when we call the kernel, we can save the `for` loop test conditions and indexer. 

```c++
template <unsigned int blockSize>
__global__ void reduceSum(float *g_data1, float *g_odata)
{
    extern __shared__ int sdata[];
	
	unsigned int tid = threadIdx.x;
	unsigned int i = blockIdx.x * (blockDim.x*2) + threadIdx.x;

	unsigned int gridSize = blockSize * 2 * gridDim.x;
    sdata[tid] = 0;
    while (i < n) {
        sdata[tid] += g_idata[i] + g_idata[i + blockSize];
        i += gridSize;
    }
	__syncthreads();
	
	if (blockSize >= 512) { 
        if (tid < 256) sdata[tid] += sdata[tid + 256];
        __syncthreads();
    }
	if (blockSize >= 256) { 
        if (tid < 128) sdata[tid] += sdata[tid + 128]; 
        __syncthreads();
    }
	if (blockSize >= 128) {	
        if (tid < 64) sdata[tid] += sdata[tid + 64];
        __syncthreads();
    }
	
	if (tid < 32) {
		volatile int* smem = sdata;
		if (blockSize >= 64) smem[tid] += smem[tid + 32];
		if (blockSize >= 32) smem[tid] += smem[tid + 16];
		if (blockSize >= 16) smem[tid] += smem[tid + 8];
		if (blockSize >= 8) smem[tid] += smem[tid + 4];
		if (blockSize >= 4) smem[tid] += smem[tid + 2];
		if (blockSize >= 2) smem[tid] += smem[tid + 1];
	}
	
	if (tid == 0) { g_odata[blockIdx.x] = sdata[0]; }
}
```
