# Greedy Algorithm

## Activity Schedule 
$A = \{a_1,...,a_n\}$ set of tasks, $|A|=n$, $a_i = (s_1,f_i), s_i=$ start time, $f_i=$ finish time. $S \subseteq A. S=$ set of tasks without overlap. Maximize $|S|$.  


### Implementation: Greedy based on finish time
```python linenums="1"
sort A by the finishing time
f = 0 # finishing time
S = []
for ai in A: 
    if f <= ai.s: # the start time of the ith activity
        S.append(si)
        f = ai.f
return S
```

### Correctness  (Thrm 16.1 CLRS)
Define $OPT\subseteq A$ be an optimal solution of the problem, in which $|OPT|$ is maximized and there is no overlapping in $OPT$. 
Define $S_k$ be the state of $S$ after the $k$th iteration of the for loop (4-7), $S_0$ be the state before entering the loop. 
__Claim__ $\exists OPT. \forall k\in\mathbb{N}.S_k\subseteq OPT\subseteq S_k\cup\{A_{k+1},...,A_n\}$. (loop invariant)  
_Proof_ prove by induction  
_Base case_ $S_0=\emptyset\subseteq OPT\subseteq \{A_1,...,A_n\}$  
_Inductive step_ Take $OPT$ be some optimal solution,assume the inductive hypothesis. Consider the two cases

 - $S_{i+1} = S_i$, a.k.a. $A_{k+1}$ overlaps with some activity in $S_{i}$. By induction hypothesis, $S_{i+1}\subseteq OPT\subseteq S_k \cup \{A_{k+1},..., A_n\}=S_{k+1}\cup \{A_{k+1},..., A_n\}$. Moreover, $A_{k+1}\not\in OPT$ because $A_{k+1}$ would overlap with some activity in $OPT$, hence $S_{i+1}\subseteq OPT\subseteq S_{k+1}\cup \{A_{k+1},..., A_n\} - \{A_{k+1}\} = S_{k+1}\cup \{A_{k+2},..., A_n\}$. 
 
- $S_{i+1} = S_{i}\cup \{A_{k+1}\}$.  
  If $A_{k+1}\in OPT$, then the claim is proven.  
  If $A_{k+1}\not\in OPT$, then consider $A_m\in OPT, m > i+1$ is the smallest index that is greater than $i+1$, then $A_m$ has greater finishing time than $A_{k+1}$, let $OPT' = OPT - {A_m} \cup \{A_{i+1}\}, |OPT'|=|OPT|$, $A_{k+1}$ will not overlap with any other activities in $OPT'$ since it will not overlap with any activities before $A_m$ by its starting time property, and it will not overlap with any activity after $A_m$ since it even finishes earlier than $A_m$, then $OPT'$ is a optimal solution, and $S_{k+1}\subseteq OPT'$ since $m > i+1, A_m\not\in S_{k+1}$, and $OPT' \subseteq S_{k+1}\cup\{A_{k+2},...,A_n\}$ since $A_{k+1}\in S_{k+1}$

### General strategy for proving Greedy correctness
every _partial solution_ generated can be _extended_ to an _optimal solution_  

Proof of sub-case 2.2 is called _exchange lemma_

## Minimal Spanning Tree
Let $G=(V,E)$ be a connected graph with weight function $w(e)\in\mathbb{N}. \forall e\in E$.  
A Spanning tree $S = (V,T)$ is an acyclic, connected subgraph (tree) of $G$. 
minimize $w(T)=\sum_{e\in T}w(e)$ 


### Implementation
 - _Prim's Algorithm_ Start with an arbitrary vertex $v$, let $C = \{v\}$ be the connected component. For each iteration, add the shortest edge attaches to $C$ and some $u\not\in C$, until $C = V$. 
 - _Kruskal's Algorithm_ Start with $T = \emptyset$, let $E'$ be $E$ sorted in non-increasing order of weight. Iterate over $E'$, if $e$ connects two different connected component (implement with disjoint set), adds to $T$. 

```python title="krustal_mst()" linenums="1"
sort E by non-increasing order
T = [] #empty disjoint set
for e in range(1,m):
    if e connects two disjoint sets:
        T.append(e) 
```
 - _Reverse remove Algorithm_ Starts with $T = E$, let $E'$ be $E$ sorted in non-decreasing order of weight, iterate over $E'$, remove $e$ from $T$ if the two vertices are still connected. 
 


### Correctness (Krustal's)
Define $T_i$ be the state of $T$ after the $i$th iteration of the for loop (line 3-5), $T_0=\emptyset$. Define $T^*$ be the optimal solution. 
**Claim** $\forall n\in\mathbb{N}. T_n\subseteq T^*\subseteq T_n\cup\{e_{n+1},...,e_{m}\}$  
*Proof* Let $n\in\mathbb{N}$. 
Suppose $n = 0$, $\emptyset\subseteq T^* \subseteq E$.  
Suppose $n > 0$, assume $P(n)$.  

 - Suppose $T_{n+1} = T_{n}$, then by the if condition (line 4), $e_{n+1}$ will create a cycle in $T_n$, hence $e_{n+1}\not\in T^*$. Therefore, $T_{n+1} = T_n \subseteq T^* \subseteq T_{n+1}\cup\{e_{n+2},...,e_m\}$
 - Suppose $T_{n+1} = T_{n}\cup\{e_{n+1}\}$  
  If $e_{n+1} \in T^*$, then proven  
  If $e_{n+1}\not\in T^*$, say $e_{n+1} = (u, v),u\in T_n, v\not\in T_n$, then consider some $e_i\in T^*$ with one endpoint being $v$, $e_i\not\in T_n$ since $T_n$ does not connect $v$. Then, $w(e_i)\geq w(e_{n+1})$ by the sorting property. Then consider $T^{**} = T^* - \{e_i\}\cup\{e_{k+1}\}, w(T^{**})\leq w(T^*)$. Also, $T^{**}$ is connected, acyclic by the MST property of $T^*$. Hence $T^{**}$ is a MST. $T_{n+1}\subseteq T^{**}\subseteq T^{**}\cup \{e_{n+2},...,e_m\}$. 

## Shortest Path
**Precondition** $G = (V,E)$ connected, with $w:E\rightarrow \mathbb{Z}^+$. $s,t\in V$  
**Postcondition** return $u\sim v$ with minimized $w(u\sim v) = \sum_{e\in u \sim v} w(e)$

### Implementations
- Brute force: worst case $O(c^n)$
- Special Case: $\forall e\in E. w(e) = 1\Rightarrow$ BFS $\in O(|E|)$
- Dijkstra's Algorithm
```python title="dijkstra(G, w, s, t)" linenums="1"
P = [] # list of edges of the shortest paths tree
Q = empty min-priority queue of vertices v, prioritize on v.d
for all v in V:
    v.parent = Nil
    v.d = Infinity
    Q.enqueue(v)
s.d = 0
Q.update()
while Q is not empty:
    v = Q.dequeue()
    P.append((v,v.parent))
    for (u,v) in all paths containing v:
        if u in Q and v.d + w(v,u) < u.d:
            u.parent = v
            u.d = v.d + w(u,v)
            Q.update()
P.remove((Nil, s))
return p
```
 - Similar to BFS, use a priority queue (prioritized by best distance so far) instead of an array
 - Similar to Prim's, but with different priorities

### Runtime
$O((m+n)\log n) = O(m \log n)$ since connected
Initialization takes (1-8) $O(n)$ time  
Consider the while loop (9-16), in each iteration, $v$ is dequeued from $Q$ and no nodes are enqueued, hence the while loop will execute $O(n)$ time.  
Consider the inner for loop, consider $G$ implemented as an adjacency list. Over all iterations, each edge generates at most one queue update and are examined at most twice. For each queue update, it takes $O(\log n)$ time. Therefore, the total is $O(m\log n)$
Since the graph is connected, the total time is $O(m \log n)$

### Properties
Define $\forall v\in V. \delta (s,v)=\min\{w(s\sim v)\mid s\sim v\text{ is a path in }G\}$  

**Lemma 1** $\forall v\in V$. in any iteration, $v.d\geq \delta(s,v)$.  
**Proof** by induction on the number of iteration, based on the algorithm, $u.d=\infty$ or weight of some particular path. 

**Lemma 2** (Triangular property) $\forall u,v,w\in V. \delta(u,v)\leq \delta(u,w)+\delta(w,v)$.  
**Proof** Otherwise $u\sim w\sim v$ is the shortest path. 

**Lemma 3** (sub-path property) Any sub-path of a shortest path is shortest.   
**Proof** prove by contradiction, a shorter sub-path will shorten the path. 





### Discussion
Show $P_k$ the value of $P$ after the $k$th iteration of the loop, can be extend to some optimal shortest path tree.
 - Core of inductive step: show that $\forall v\in P_k. v.d=\delta(s,v)$
 - Consider one iteration $P_{k+1}=P_k\cup\{v'.parent, v'\}$ which $v'$ is just being connected. Then it follows $v'.d=\delta(s,v')$.  
 By lemma 1, we only need to prove $u.d \leq \delta(s,v)$ by contradiction.  
 Assume $v.d>\delta(s,v)$. Consider $s\sim v\in P_{k+1}$, consider $(s\sim v)^*$ be the shortest path, let $(x,y)\in(s\sim v)^*$ be the first edge such that $x\in P_k, y\not\in P_k$.  
If $y\neq v$, then 
$y.d \leq x.d + w(x,y)\leq \delta(s,x)+w(x,y)<\delta(s,x)+w(x,y)+\delta(y,v)=\delta(s,v)<v.d$, contradict to $v.d$ is the min in $Q$ 
If $y=v,v.d\leq x.d+w(x,v)=\delta(s,v)<v.d$

### Correctness
Let $k\in\mathbb{N}. k < n$. Let $P(k)$ be such that "$\exists P^*$ be the optimal solution s.t. $P_k\subseteq P^*$ and $P^*-P_k$ contains only edges without both endpoints in $P_k$ and $\forall u\in P_k.\forall v\not\in P_k. u.d=\delta(s,u)\leq \delta(s,v)\leq v.d$".

Suppose $k = 0$, $P_0=\emptyset\subseteq P^*$.

Suppose $k > 0$, assume $P(k)$. consider $P_{k+1} = P_k \cup \{(u,v)\}, u\in P_k, v\not\in P_k$.
 - Suppose $(u,v)\in P^*$. Then $P_{k+1}\subseteq P^*$. Also $\delta(s,v)=\delta(s,u)+w(u,v)=\delta(s,v)$. By the priority of $Q$, $v.d$ is the smallest among vertices not connected by $P_k$, hence $\forall x\in P_{k+1}.\forall w\not\in P_{k+1}. x.d\leq \delta(s,x)\leq \delta(s,w)\leq w.d$.
 - Suppose $(u,v)\not\in P^*$. Then take $(s\sim v)^* \in P^*$, $(w,v)$ be the last edge in the path $(s\sim v)^*$.  
 I claim that $w\in P_k$.  
  - Let $(x,y)\in(s\sim v)^*$ be the first edge such that $x\in P_k, y\not\in P_k$. Then $y.d\le \delta(s,v) \leq v.d$ because $w((s,v)^*)=\delta(s,v)$ and $w(s\sim y) < w((s,v)^*)$ since $y$ is on the path. However this contradict with the fact that $v.d$ has the minimum priority. 
 - Therefore, $\delta(s,v) = w.d + w(w,v)$. Then, since $v.d$ is the shortest distance, $v.d \leq w.d + w(w,v) = \delta(s,v)$. By Lemma 1, $v.d = \delta(s,v)$  .
 Take $P^{**} = P^* - \{(w,v)\}\cup\{(u,v)\}$ is a shortest path tree and $\forall x\in P_k. \forall y\not\in P_k. x.d = \delta(s,x)\leq \delta(s,y) \leq y.d$
 
  

## Example Question 1

$D = \{1, 5, 10, 25\}. \forall n \in \mathbb{Z}^+$. Let $S$ be a multi-set of elements from $D$ such that $\sum_{s\in S} s = n$, minimize $|S|$  

### Implementation
```python title="sequence(n)" linenums="1"
S = []
while n > 0:
    if n >= 25:
        x = 25
    else if n >= 10:
        x = 10
    else if n >= 5:
        x = 5
    else:
        x = 1
S.append(x)
n -= x
return S
```

### Correctness Discussion
Let $S^* = \{s_1^*,...,s_j^*\}$ be the optimal sequence, let $S_i = \{s_1,...,s_k\}$ be the sequence of $S$ after $i$th iteration of the while loop. $S_0=\emptyset$.

Consider the case when $s_m \neq s^*_m$ for some $m$, then we will show that there are coins in $S^* - S_m$ and not the same value as $s_m$ that makes up to $s_m$, where it will use more coins. 

Notice that this algorithm does not work for a general $D = \{1, d_1,d_2,...,d_k\}$ where $D$ is strictly increasing. For example, $D=\{1,3,4\}. n = 6$. $S = \{4, 1, 1\}$ while $S^* = \{3, 3\}$

## Example Question 2

### Part (a)
_Prove $\forall G$ connected, $|E| \geq |V|$. if $e$ is the unique minimum cost edge, then $e$ must be in every MST of $G$._

*Proof*. Let $T$ be a MST of $G$ that does not contain $e=(u,v)$, Consider $u\sim v \in T$, then $e\cup u\sim v$ is a cycle, since $e$ has the unique minimum weight, take out any edge $w \in u\sim v$, $w(T-\{w|\cup\{e\})<w(T)$. By contradiction, claim is proven. 

### Part (b)
_Prove $\forall G$ connected, $|E| \geq |V|$. if $e$ is the unique maximum cost edge, then $e$ must not be in any MST of $G$. Or Disprove by counter-example._ 

*Proof*. I'll disprove this claim, take $G$ such that $G'=(V,E-\{e\})$ is disconnected, then $e$ is essential to make a spanning tree for $G$.
