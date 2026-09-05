# Network Flow

## Problem Definition
**network** $N=(V,E)$ is a directed, connected with:

 - **source** $s\in V$ no incoming edge
 - **sink** $t\in V$ no outgoing edge
 - **capacity** $c:E\rightarrow \mathbb{N}$


### Question
Assign **flow** $f(e)\in\mathbb{R}^{\geq 0}$ s.t. 
 - $\forall e\in E. 0\leq f(e)\leq c(e)$
 - $\forall v\in V-\{s,t\}, f^{in}(v)=f^{out}(v)$, where $f^{in}(v)=\sum_{(u,v)\in E}f(u,v), f^{out}(v)=\sum_{(u,v)\in E}f(v,u)$
 - Maximize flow in $N$: $|f|=f^{out}(s)=f^{in}(t)$

### Discussion
Start with any feasible solution (one that satisfies the basic constraints)

Make incremental improvements, until this is no longer possible

### Ford-Fulkerson Algorithm
start with any valid flow $f$, e.g. $f(e)=0$   
 while there is some augmenting path $P$ in $N$: augment $f$ along $P$
 
path $P=s\rightarrow v_1\sim v_k\rightarrow t$ is augmenting IFF $f(e)<c(e), \forall e\in P$

**First step**   
For every edge on $P$, define residual capacity of the edge $\Delta(u,v)=c(u,v)-f(u,v)$, define residual capacity of the path $\Delta(P)=\min\{\Delta(u,v)\mid (u,v)\in P\}$, then augmenting $f$ along $P$ simply add $\Delta(P)$ to $f(e)$ for each $e\in P$

After the augmentation, the graph will end up with non-maximum 

**Second step**  
Extend the notion of augmenting path. For each path, regardless direction.
- send flow on a "backward edge" to somewhere else. Call its residual capacity $\Delta(e)=f(e)$
- All other edges are "forward" remains unchanged. 
- To augment $f$, increase $f(e)$ for forward edges, decrease $f(e)$ for backward edges. 

### Residual Network
For network $N$, flow $f$, create a residual network $N'=(V,E')$. For each edge, change it to dual directions with weights $w(u,v)=\Delta(u,v)$ on the unchanged direction, $w(v,u)=f(u,v)$ on the reversed direction.

Therefore, augment path in $N$ is equivalent to augment path in $N'$

### Correctness of the strategy
**Cut** a partition of $V=\{V_s,V_t\},s\in V_s, t\in V_t$   
$\forall X=\{V_s,V_t\}$ cut.    
Define capacity $c(X)=\sum_{u\in V_s, v\in V_t\\(u,v)\in E} c(u,v)$, we say such path is forward in respect to $X$.   
Define flow $f(X)=\sum_{u\in V_s, v\in V_t\\(u,v)\in E} f(u,v)-\sum_{u\in V_t, v\in V_s\\(u,v)\in E} f(u,v)$

**Observations**
- $\forall N, f \text{ valid}, X. f(X)\leq c(X)$
- $\forall N,f,X. f(X)=|f|$

**Theorem** $\forall N, f \text{ valid}. |f|$ is maximized IFF $N$ has no augmenting path. 

**Proof** $\Rightarrow$ Suppose $N$ contains an augmenting path. then current $|f|$ is no maximized. Proven by contradiction. 

$\Leftarrow$ Assume $N$ does not contain an augmenting path, construct cut $X$ as: 

- start with $V_s=\{s\}, V_t=V-V_s$ 
- for any edge $(u,v), u\in V_s, v\in V_t, f(u,v)<c(u,v), V_t = V_t-\{v\}, V_s = V_s\cup \{v\}$
- for any $(u,v), u\in V_t, v\in V_s, f(u,v)>0, V_t=V_t - \{u\}, V_s=V_s\cup \{u\}$

repeat as long as possible. Equivalently, $V_s =$ all vertices reachable from $s$ in $N'$, $V_t=V-V_s$

Then, $t\not\in V_s$, $X=(V_s,V_t)$ is valid and $\forall (u,v)\in E, u\in V_s, v\in V_t. f(u,v)=c(u,v). \forall (u,v)\in E, u\in V_t, v\in V_s, f(u,v)=0$.

Therefore $|f|=f(X)=c(X)$

### Complexity
possible for runtime depend on the smallest capacity
$V=\{s,t,a,b\}, E=\{(s,a,10^{100}), (a,t,10^{100}), (a,b,1), (s,b,10^{100}, (b,c,10^{100})\}$
Consider the loop $s\rightarrow a\rightarrow b\rightarrow t,s\rightarrow a\leftarrow b\rightarrow t$

To improve
1. use BFS to find augmented paths: $O(|V||E|)$ augmentations required. Since BFS runs in $O(|E|)$ the total is $O(|V||E|^2)$
2. since we will rerun BFS sometimes, with each execution of BFS, use all augmented path found before running BFS again. Possible to improve to $O(|V|^2|E|)$
3. $O(n^3)$ possible using a different tech called preflow algorithms. 


## Reduction
In practice, solving problems through Network flow involves transforming the original problem into network flow. 

```
1  input 
        Describe how to create N_X
2. network N_X
        Use F-F algorithm ...
3. find max-flow f or min-cut X
        Describe how to construct a solution from the N_X result
4. construct solution to original problem
```
### Correctness
 - Argue that every solution to original problem corresponds to some valid flow/cut in $N_X$
 - Argue that every flow in $N_X$ (or every cut) corresponds to some solution for original problem


## Max bipartite matching Problem
Input: $G=(V_1,V_2, E)$ undirected, bipartite ($\forall (u,v)\in E. u\in V_1, v\in V_2$)

Output: a matching $M\subseteq E$ s.t. no two edges in $M$ shares endpoints. max $|M|$

### Solution
add $s$ to $V_1$, add all edges from $s$ to all vertices in $V_1$, make all edges in $E$ directed from $V_1$ to $V_2$. Add $t$ to $V_2$, add all edges from all vetices in $V_2$ to $t$. Then do network flow (integer). output $M=\{(u,v)\in E\mid f(u,v)=1\}$

### Correctness
for any matching $M$ in $G$, $\exists$ a corresponding flow $f(u,v)=\mathbb{I}$((u,v) matching),$f(s,u)=\mathbb{I}$(u matched), $f(v,t)=\mathbb{I}$(if v matched). Then, $\max|f|\geq $max matching size

for any valid flow $f$, $\exists M = \{(u,v)\in E\mid f(u,v)=1\}$ because of the capacity constraint, no edges in $M$ can share an endpoint. Then max matching size $\geq \max|f|$

## Max independent set for bipartite graphs
Input: $G=(V_1,V_2,E)$ bipartite 

Output: an independent set $S\subseteq V_1\cup V_2$ with no edge having both endpoints in $S$. max $|S|$.

### Solution
1. add $s$ to $V_1$, add all edges from $s$ to all vertices in $V_1$ and has capacity 1, make all edges in $E$ directed from $V_1$ to $V_2$ and have capacity $\infty$. Add $t$ to $V_2$, add all edges from all vetices in $V_2$ to $t$ have capacity 1.
2. Find cut $X$ in $N$ with min capacity (first, find max flow, then let $X=$connected component of $s$ in $N'$)
3. Let $X=(V_s,V_t)$, )Output $S=(V_1\cap V_s) \cup (V_2\cap V_t)$

### Correctness
- Given any independent set $S\subseteq V_1\cup V_2$, consider the cut $X=(V_s,V_t)$ where $V_s=\{s\}\cup (V_1\cap S)\cup(V_2-S)$. Then, $c(X)=\sum_{u\in V_1,u\not\in S} c(s,u) + \sum_{v\in V_2, v\not\in S}c(v,t) = |V_1-S|+|V_2-S|=|V_1\cup V_2|-|S|$. So min cut capacity $\geq |V_1|+|V_2|$ (max independent set size)

- For any cut $X=(V_s,V_t)$ with $c(X)<\infty$, then $S=(V_1\cap V_s)\cup(V_2\cap V_t)$ is an independent set since the cut has a finite capacity (else, there would be an edge with infinity capacity), then similarly $c(X)|=|V_1\cup V_2|-|S|$

Therefore, the cuts is equivalent to the independent set. Hence, the max independent set size $=|V_1+V_2|-\text{min cup capacity}$
