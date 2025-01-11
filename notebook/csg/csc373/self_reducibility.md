# Self Reducibility

## "Self-reducibility"

| Problem  |Devision   | Search  |Optimization |
| -------- | --------- | -------- | ------------- |
|SAT     | Given $\phi$, is it satisfiable | Given $\phi$, find values that makes $\phi$ true | - |
|Vertex Cover | Given $G,k$, is there a vertex cover of size $k$ | Given $G,k$, find a vertex cover of size $k$ | Given $G$, find a smallest vertex cover | 

**Turing Reducible** For problems $A,B$ (search, opt, decision) $A$ is Turing reducible to B IFF 
 - Assuming a constant time algorithm for $B$, then we can write a polynomial time algorithm for $A$. 

### Example: Clique Search
**Clique** Given $G$ undirected, $k\in\mathbb{Z}^+$ does $G$ contains a $k$-clique which $S\subseteq G, |S|=k$ with each possible edges between them.  
**Clique Search** Given $G$ undirected, $k\in\mathbb{Z}^+$, return a $k$-clique or null for non-existence. 

Claim: Clique-search Turing reducible to Clique  

Implicit assumption problem: solving decision problems require finding certificate. (Therefore, must treat the algorithm for B as a black box, no assumption allowed, other than it solves clique)

```python title="cs(G,k)"
if not cd(G,k):
    return Nil
for v in V:
    G = G - v if cd(G-v,k) 
return V
```
runs in $O(n T(n) + n(n+m))$ where $T(n)$ is the runtime of `cd` is poly time compare to $T(n)$. 

### Correctness
G in each iteration contains a k-clique (by `cd(G,k)`).  
For each vertex that is not in the k-clique, it will be removed. 

            

In general, to show self reducibility

1. Assume algorithm solves decision problem
2. Write algorithm for the search problem, making calls to $D$ as a black box. 
3. argue correctness and runtime.

Note this shows that search problem is Turing reducible to decision problem.

### Example: Hamiltonian Path search
given $G$, find a simple path that goes through every vertex. 

```python title="hs(G)"
if not hd(G):
    return Nil
for e in E:
    E = E - e if hd(G-e) 
return E
```


### Example: Vertex Cover

```python title="vcs(G,k)"
if not vcd(G,k):
  return Nil
C = []
for v in V and while k > 0:
  if vcd(G-v, k-1):
      C.append(v)
      G = G - v
      k -= 1
return c
```
runs in $O(nt(n)+n(M+n))$

### Correctness
$v$ belongs to a vertex cover of size $k$ IFF `vcd(G-v, k-1) == True`  
If C is a vertex cover of size $k$ and $v\in C$, then $C-\{v\}$ is a vertex vover of size $k-1$ in $G-v$.  
If `vcd(G-v, k-1) == True` then there is some vertex cover $C$ of size $k-1$ in $G-v$, then $C\cup\{v\}$ is a vertex cover of size $k$ since when we put $v$ back, all added edges are connected to $v$.  


## Optimization

### Example: Max clique  
find the largest clique in $G$.  

find the largest $k$ s.t. `cd(G,k) == True` (Using binary search, takes $O(\log n t(n))$). Then return `cs(G,k)`
