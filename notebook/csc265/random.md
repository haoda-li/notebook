# Randomized QuickSort

## QuickSort

 Given a unsorted array $A$ `quicksort` sort the array by first choose a pivot $x$ from $A$, then partition the array into $A[0:q-1] \leq A[q] =  x \leq A[q+1:n]$ and then recursively sort the left partition and right partition. 

As a reference, the algorithm is provided below


```python
from random import shuffle, randint

def partition(A, l, r):
    global NUM_COMPS # for runtime demo
    x = A[r]
    i = l - 1
    for j in range(l, r):
        NUM_COMPS += 1 # for runtime demo
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        quicksort(A, l, q-1)
        quicksort(A, q + 1, r)
```

### Runtime Analysis

Assuming that we don't do early returning (otherwise we can check whether $A[l:r]$ is already sorted). As of a best case, the chosen pivot is always in the middle, then it takes $O(n\lg n)$ time. Also, in average, `quicksort` takes $\Theta(n\log n)$ time (proof omitted). 

However, if the pivot is chosen unwisely, the running time is quite bad. As an example, we choose the rightmost element of $A[l:r]$ as our pivot, if $A$ is already sorted (either ascending or descending), then all elements go to either $A[l:r-1]$ or $A[l+1:r]$, thus `quicksort` takes $\frac{n(n-1)}{2}\in O(n^2)$ comparisons. 


```python
N = 25
A = list(range(N))
NUM_COMPS = 0
quicksort(A, 0, N-1)
print("\nNumber of comparisons: ", NUM_COMPS)
#>> Number of comparisons:  300
```

```python
ncomps_sum = 0
for _ in range(100):
    NUM_COMPS = 0
    shuffle(A)
    quicksort(A, 0, N-1)
    ncomps_sum += NUM_COMPS
print("Average number of comparisons: ", ncomps_sum / 100)
#>> Average number of comparisons:  97.4
```

    
Note that whichever pivot strategy we choose, there is always a way to a construct worst case array. 

## Randomized Quicksort
Intuitively, to avoid running into the worst case scenario, we can randomly permute $A$ before entering `quicksort`, so that we are expecting an average case running time on the permuted array $A$. 

Alternatively, we know that the fixed choice of pivot causes the problem, so that we randomly pick pivot from $A[l:r]$. 

The two thought led to the two different implementations


```python
# implementation 1: permute A before quick sort
def rand_quicksort_permute(A, l, r):
    shuffle(A)
    quicksort(A, l, r)

# implementation 2: randomly pick pivot for each partition
def rand_partition(A, l, r):
    global NUM_COMPS # for runtime demo
    x = A[randint(l, r)]
    i = l - 1
    for j in range(l, r):
        NUM_COMPS += 1 # for runtime demo
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def rand_quicksort_partition(A, l, r):
    if l < r:
        q = rand_partition(A, l, r)
        quicksort(A, l, q-1)
        quicksort(A, q + 1, r)
```

### Worst Case Expected Runtime
Since we introduced randomness into our algorithm, the running time for the same input in different runs will be different. Thus, let $T_x$ be the running time of the algorithm given a fixed input $x$. Thus, thee expected running time is very intuitively defined as $E(T_x)$. 

As a refresher, worst case running time for an algorithm is $T(n):=\max\{T_x: |x| = n\}$, and the average running time for a algorithm with finite input space is $\bar T(n):=\frac{1}{|\mathcal X(n)|}\sum_{x\in \mathcal X(n)} T_x$ where $\mathcal X(n)$ is the set of all input of size $n$. For infinite sied input space, then it is defined as a weighted average $\bar T(n) = \sum_{x\in\mathcal X(n)}p_xT_{x}$ where $p_x$ is the probability of input $x$ be chosen, $\sum_{x\in\mathcal X(n)} p_x = 1$.

Thus, the __worst case expected running time__ is defined as 

$$E(T(n)) := \max\{E(T_x): |x| = n\}$$

For permutation based randomized quicksort, since we randomly permute the input, $E(T_x) = \bar T(n)$ for any input $x$ of size $n$. Thus, $E(T(n)) = \bar T(n) \in \Theta(n\log n)$. 

For pivot based randomized quicksort, the proof is similar to average case proof. The key idea is that after each `rand_partition(A, l, r)`, the expected number of elements in $A[l: q-1], A[q+1:r]$ is the same as the average number of elements after `partition(A, l, r)` over all $A$ of size $n$.


```python
shuffle(A)

ncomps_sum = 0
for _ in range(100):
    A_fixed = A.copy()
    NUM_COMPS = 0
    rand_quicksort_permute(A_fixed, 0, N-1)
    ncomps_sum += NUM_COMPS
print("Average number of comparisons for partition based: ", ncomps_sum / 100)
#>> Average number of comparisons for partition based:  96.51

ncomps_sum = 0
for _ in range(100):
    A_fixed = A.copy()
    NUM_COMPS = 0
    rand_quicksort_partition(A_fixed, 0, N-1)
    ncomps_sum += NUM_COMPS
print("Average number of comparisons for partition based: ", ncomps_sum / 100)

#>> Average number of comparisons for partition based:  96.75
```

   
    
