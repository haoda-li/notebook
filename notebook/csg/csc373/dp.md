# Dynamic Programming

## Activity Scheduling with Profits
- Input: $A =\{A_1,...,A_n\}$ where $A_i=(s_i,f_i,w_i)$ where $w_i\in\mathbb{N}$ is the profit
- Output: $S\subseteq A, S$ has no conflict and $w(S)=\sum_{A_i\in S} w_i$ is maximized

### Discussion
 - Note that Greedy won't work (finish time, profit, unit-profit)
 - Assume the activity are sorted by finish time. Consider $S^*$ optimal, consider $A_n$ which is the activity with the largest finishing time. 
  - If $A_n\in S^*$, then $S^*-A_n$ must be optimal for $A'=\{A_1,...,A_k\}$ where $k$ is the last activity that does not overlap with $A_n$, a.k.a. $\{A_{k+1},...,A_{n-1}\}$ each overlap with $A_n$
  - If $A_n\not\in S^*$, then $S^*$ is optimal for $A-\{A_n\}$
 - **Recursive substructure** when an optimal solution of a problem is made up of optimal solutions of the sub-problems.

### Recursive Implementation
`initialization(A)` compute $P = p[1],...,p[n]$ where $p[i]=$index of the last activity that does not overlap with $A_i$, note $p[i]\leq i-1$

```python title="solution(A)"
P = initialization(A)
return RecOpt(n, P)
```

```py title="RecOpt(n, P)"
if n = 0;
    return 0
return max(RecOpt(n-1), w_n + RecOpt(p[n]))
```
Note that the runtime has combinatorial explosion due to the repeated calls of `RecOpt(i)` for small `i` for exponentially many times. THe runtime is exponential only because it is recursive, To solve it
 - memorization: memorize the output of RecOpt(i) and record for later usage
 - Instead, compute values bottom-up
 
```python title="IterOpt(A)"
initialization(A)
OPT = []
OPT[0] = 0
for i in range(1, n):
    OPT[i] = max(OPT[i-1], w_i + OPT[p[i]])
return OPT # note that OPT is useful to get S
```


## Dynamic Programming
 - For optimization problems where global optimum is obtained from optimum to subproblems
 - The subproblems need to be simple Each subproblem can be characterized using a fixed number of indexes or other information
 - Subproblem overlap: smaller subproblems repeated in solutions to larger problems
 
### "Process"
0. Understand the recursive structure of the optimum solutions
1. Define a table (iterative data structure) to store the optimum value for all subproblems
2. Give a recurrence for the table values, with justification
3. Write iterative algorithm to compute the value bottom-up (solve the recurrence)
4. Use the table values to compute an actual solution

## Matrix Chain Multiplication
Input: $(d_0,...,d_n), d_i\in\mathbb{Z}^+$ representing matrix dimensions, since the inner dimension are same, we don't store it twice, a.k.a. $A_0=[d_0\times d_1], A_1 = [d_1\times d_2],..., A_{n-1}=[d_{n-1}\times d_n]$   
Output: fully parenthesized expression for $\prod_1^{n-1} A_i$ that minimize total #flips to computer the product

### Example 
$A_{1\times 10}, B_{10\times 10}, C_{10\times 100}$ are matrices. We can compute it by $A(BC)$ or $(AB)C$, note that multiplication are associative.
 - $A(BC)$: Consider $BC$, #flips = $10^2 \times 100$, then $A(BC)$ #flips = $1\times 10\times 100$. sum: $11,000$
 - $(AB)C$: $AB$: $1\times 10\times 10 = 100$, $(AB)C=1\times 10\times 100 = 1000$, sum: $1100$

### Discussion
- Brutal force # ways to parenthesize is called a Catalan number $\in\Omega(4^n)$
- Greedy ? consider input $(10, 1, 10, 100), (1, 10, 100, 1000)$, try greedy strategies and consider the counter example above. 


### "Process"
0. Recursive Structure: 
 - imagine OPT, the last product will be like $(A_1\times A_{k-1})\times (A_k\times A_{n-1})$, note the inner product won't influence the number of operations of this product, hence to minimize, the inner product need to be optimal. 
 - Subproblems will all have the form "find the best parenthesizing of $A_i\times ...\times A_j, i\leq j$". Then let $N[i,j]=$ min #flips required to multiple $A_i\times ...\times A_j, 0\leq i\leq j\leq n-1$
 - For $i<j$, for any one pair of parenthesis, the number of operations is $N[i,k-1] + N[k,j] + d_id_kd_{j+1}$ where $N(p,q)$ is the min number of operations taken for $A_p\times...\times A_q$. $N[i,j]=\min\{N[i,k-1] + N[k,j] + d_id_kd_{j+1}\mid i+1\leq k\leq j\}$
1. Table:
Consider the table with entry $N[i,j]$, the matrix is strictly upper triangular (since we can interchange $i,j$, the lower triangle is not needed), and the diagonal $N[i,i]$ is filled with $0$. 

2. Table Implementation

```python title="table"
N = empty (n-1)*(n-1) matrix
for i in range(m-1, 0, -1):
    N[i,i] = 0
    (B[i,i] = -1)
    for j in range(i+1, n-1):
        N[i,j] = Infinity
        (B[i,j] = -1)
    for k in range(i+1, j):
        if N[i,k-1] + N[k,j] + d_i*d_k*d_j < N[i,j]:
            N[i,j] = N[i,k-1] + N[k,j] + d_i*d_k*d_j
            (B[i,j] = k)
return N[0, n-1]
```

 - Reconstruct solution:
    - Use $B[i,j] =$ value of $k$ that makes $N[i,j] = N[i,k+1] + N[k,j] + d_i d_k d_{j+1}$ and add into the table
    - For parenthesis
  
```python title="paren(B,i,j)"
if i == j:
    print 'A_i'
else:
    print '(' + paren(B, i, B[i,j]-1) + '*' + paren(B,B[i,j], j) + ')'
```

## Shortest Paths - All-Pairs
- Input: directed $G=(V,E), w(v)\in \mathbb{Z}$, no cycle with negative weight.  
- Output: $\forall u,v \in V, \min\{w(u\sim v)\mid u\sim v\text{ is a path}\}$

### "Process"
#### 0. Recursive Structure
Consider a shortest $u\sim v$ path,let $k=$ max index of vertices on $u\sim v$ excluding $u,v$.  
Claim: both $u\sim k, k\sim v$ are shortest paths with all intermediate vertices $<k$  
Proof: by contradiction, if $P_1$ is a shorter path from $u$ to $k$, then $P_1 + k\sim v$ would be shorter than $u \sim v$, even if $P_1$ had vertices in common with $k\sim v$, say vertex $j$, then $P_1+ k \sim v$ contains a cycle, by assumption, the cycle must have weight $\geq 0$, then we have a better path by removing the cycle. 

#### 1. Table
$A[k,u,v]=$ min weight of all $u\sim v$ using only vertices from $1,...,k$ as intermediate for $u,v\in \{1,...,n\}. k\in\{0,...,n\}$

#### 2. Recurrence

```python title="recurrence relationship"
A[0,u,v]= { 
    0         if u = v, 
    w(u,v)    if u != v (u,v) in E,
    Infinity  if u != v, (u,v) not in E
}

for k > 0：
    A[k,u,v] = min(
        A[k-1,u,v], # don't use k
        A[k-1,u,k]+A[k-1,k,v] # use k
)
```

#### 3. Iterative (Floyd-Warshall)
```python title="DP construction"
for u in range(n):
    for v in range(n):
        if u == v: 
            A[0,u,v] = 0
            B[0,u,v] = -1 # not exist
        elif (u,v) in E:
            A[0,u,v] = w(u,v)
            B[0,u,v] = 0 # directly
        else:
            A[0,u,v] = Infinity
            B[0,u,v] = -1

for k in range(n):
    for u in range(n):
        for v in range(n):
            if A[k-1, u, k] + A[k-1, k, v] < A[k-1, u, v] 
                A[k, u, v] = A[k-1, u, k] + A[k-1, k, v] 
                B[k, u, v] = k
            else:
                A[k, u, v] = A[k-1, u, v]
                B[k, u, v] = B[k-1, u, v]
```

#### 4. Reconstruct the actual solution
Use $B[k, u, v]$ to track max vertex on any $u\sim v$ path that has total weight $A[k, u, b]$

```python title="reconstruction"
Path(u,v, B, n):
    find the intermediate index
    recursively find the weights
```

### Observation
In practice, runtime $\in \Theta(n^3)$, space $\in\Theta(n^3)$.  
To improve the space, notice that $\forall k, u, v. A[k, u, k] = A[k-1, u, k], A[k ,k, v] = A[k-1, k, v]$. Therefore, we don't need a 3-D array, we can keep updating on a 2-D array. We can simply get rid of all index $k$, then the body of the triple for loop becomes: 

```python
if A[u, k] + A[k, v] < A[u, v]:
    A[u, v] = A[u, k] + A[k, v] 
    B[u, v] = k
# omit the else since nothing changed
```
The space then is $O(n^2)$

## Transite Closure
$G$ directed, $\forall u,v\in V$ is there a path $u\sim v$?

### Discussion
Use adjacency matrix 
Example let $A =$

|   | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 0 | 0 |
| 3 | 1 | 1 | 1 | 0 |
| 4 | 0 | 0 | 0 | 1 |

Note: $\pi(u,v) = 1$, u is the row index, v is the column index, if $u\rightarrow v$

Notice that $A^2 =$

|   | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 2 |
| 2 | 2 | 1 | 0 | 1 |
| 3 | 3 | 2 | 1 | 1 |
| 4 | 0 | 0 | 0 | 1 |

Notice that 

$$A^2[2,4]=\sum_{i=1}^4 A[2,i]\times A[i,4]$$

Each term of the summation above represents one possible path of length $\leq 2$ between 2 and 4

### Trick 1 
switch $\times\rightarrow\land, +\rightarrow\lor$.  
Generally, $A^k[u,v] = \mathbb{I}$ there is some path of length $\leq k$ from $u$ to $v$, wanted $A^n$ using boolean ops. 

### Trick 2
square the resulted matrix for each matrix multiplication. $A^1, A^2, A^4, ..., A^{\lfloor \lg(n) \rfloor^2}$

### Recursive
```python title="pow(A, n)"
if n = 1: 
    return A
elif n is odd:
    return pow(A,floor(n,2))*pow(A,floor(n,2))* A
else:
    return pow(A,floor(n,2))*pow(A,floor(n,2))
```
Runtime $O(n^3\log n)$

### Trick 3 
divide and conquer algorithm for matrix product in $O(n^{\lg 7})$, then the runtime is $O(n^{\lg 7}\log n)\in O(n^3)$

## Example Question 1: KnapSack
Given $W\in\mathbb{Z}^+, I = \{(w_1, v_1),...,(w_n,v_n)\}$, $w_i,v_i\in\mathbb{Z}^+$. Maximize for set $S$ s.t. $\sum_{i\in S} w_i \leq W \land \sum_{i\in S} v_i$ maximized. 

### Recurrence
Let $v_k\in S$ having the maximum value, then $S-\{k\}$ must be the optimal set for $W-w_k$, otherwise will cause contradiction. 

### Table


$T(k, i) =$ maximum value of items with weight $i$ and item $1,...,k$. 


```python
for i in range(W):
    T[0, i] = 0
for i in range(W):
    for k in range(n):
        T[i, k] = max(T[i - 1, k], 
                      T[i, k - 1])
```

## Example Question 2
Input a list of strictly increasing positive integers $D=\{d_1,...,d_m\}$, a positive integer $A$. Output a count set $C$ of $D$ s.t. $\sum_C = A$, or Null if cannot solve

### Recurrence
The optimal set either

 - includes $d_m$, then $T(A, m) = T(A-d_m, m) \cup\{d_m\}$
 - not includes $d_m$, then $T(A, m) = T(A, m-1)$
 
The relation
 - $T(a, 0) = None$ since there's no coin
 - $T(0, m) = 0$ since there's no value
 - $T(a, m) = T(a, m-1)$ if $d[m]>a$
 - $T(a, m) = \min\{T(a, m -1), 1 + T(a-d[m], m)\})$
