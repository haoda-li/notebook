# Optimization Approxiamation

Note: definition of NP-hardness based on worst-case analysis.  
Hence look for special characteristics o f"real life" inputs.  

- 2SAT $\in P$, 
- many graph problems are easier for restricted graph families 
     - max independent set on trees
     - planar graphs (graph without edge intersection)
     - degree-restricted 


NP-hard: no **exact efficient** solution for **all** inputs. 

## Approximation Algorithm


In general, for minimization problem.  
Let $opt(x):=$ best (minimum) value of any solution for input $x$.  
For any algorithm, let $A(x)$ be the value of the solution generated. $A(x)\geq opt(x)$.  
**Approximation ratio** for an minimization algorithm, $r(n)$ s.t. all inputs $x$ of size $n, A(x)\leq r(n)opt(x)$, for maximization algorithm, $r(n)A(x)\geq opt(x)$.  
By the definition, $r(n)\geq 1$

### Example: Min vertex cover
Idea 1: Pick vertices greedily by non-increasing degree. (pick one, remove edges connected to the removed vertex). $r(n)\in O(\log n)$.  
Idea2: repeatedly pick an edge $(u,v)$, remove $u,v$,$C=C\cup\{u,v\}$ and remove all edges attaches to them.  
Correctness: all edges are removed as they are covered and algo ends with no edge remaining
Runtime: $O(|E|^2)$  
**Claim** $r(n)=2$  
_proof_  
i. $r(n)\geq 2$: Consider a graph where each edge is matched with a pair of vertices. $2opt(G)=A(G)$  
ii. $r(n)\leq 2$: consider $C=$ `approx_cover(G)` for any $G$. For each pair of vertices in $C$, each pair are non-adjacent does not share any endpoint. Implies that $G$ contains at least $|C/2|$ edges that an disjoint from each other. Therefore, every vertex cover of $G$ must contain at least one endpoint from each edge in $C$. 
For all vertex cover $C', |C'|\geq |C|/2$


How to find $r(n)$ when $opt$ is unknown.  
For minimization problems, find a lower bound $L(x)\leq opt(x)$, find some other quantities, show that $A(x)\leq r(n)L(x)$

Idea3: 
- Given $G$, create a linear program:   
 - variables: $v_1,...,v_n$ for each vertex  
 - objective function: $\min{\sum V}$  
 - constraint: $\forall i,j. v_i + v_j \geq 1; \forall i. 0\leq v_i\leq 1$  
Notice that this is not the integer programming, we are allowed to give $v_i$ real number
- Solve over $\mathbb{R}$ so that $v_1^*,...,v_n^*$ is the output of linear programming
- output $C=\{v_i\in V\mid v_i^*\geq 0.5\}$

__Correctness__ For each pair of vertices, one of the vertices is greater than $0.5$ (otherwise they can't resolve the constraint $v_i + v_j \geq 1$). Hence the output is a vertex cover

__Runtime__ poly time since linear programming

__Approx. Ratio__  
$r(n)\geq 1.5$: Consider a triangle, the linear programming output $(1/2, 1/2, 1/2)$  
$r(n)\leq 2$: Consider min vertex cover $C'$, $v_1', ...,v_n'$ is the solution of the integer programming of vertex cover problem. Then $\sum v_i'=|C'|=opt(x)\geq \sum v_i^*$  
Note that for all vertex cover solutions, $v_i=\mathbb{I}(x^*\geq 1/2)$, then $\sum v_i \leq 2\sum x_1^*\leq 2\sum v_i'=2|C'|$




Generally, 
- VC=2 is the known best), some has non-constant 
- set-cover ($\lg n$). 
- Knapsack $1+\epsilon.$ run time in $O(n^3/\epsilon)$
- Traveling Salesman Problem (TSP): no finite ratio. 

## TSP
Input: $G=(V,E)$ undirected complete with $w(e)\in\mathbb{R}^+$, some edge has $\infty$ weight  
Output: tour: A Hamiltonian cycle with minimized total weight.

__Claim__ NP-hard to approximate TSP with any finite approx ratio.  
_proof_  Assume A solves TSP with approx ratio $C$.  
Consider input $G=(V,E)$ for the Ham. cycle problem, create input $G'=(V,E')$ for TSP, where $\forall e\in E. w(e)=1. \forall e\not\in E. w(e)=Cn + 1$.  
Rum A on this input, if $G$ contains a Ham. cycle, then the same cycle is the output for TSP, and has weight $n$. If $G$ has no Ham cycle, then every tour in $G'$ contains at least one edge with weight $Cn+1$, so all tours have total weight $> Cn+1 > Cn$  
The output has weight $\leq Cn$ (since it is an approximation) if $G$ has a Ham cycle and $>Cn$ if G does not have a Ham. cycle. Therefore, no polytime algo for Ham cycle IMPLIES no poly time approx. algo for TSP. 

### TSP with triangle inequality
```python title="approx_tsp(G, w)"
T = MST in G
# Eulerian tour: go through each edge in M twice, goes around M
tour = construct Eulerian tour of T
# pre-order traversal goes along the tour, 
# add each vertex that is not traversed before into the return set
return C:=pre-order_traversal(tour)
```
__Claim__ $\forall G$ follows the pre-condition. $r(n)\leq 2$  
_proof_ Let $C^*$ be the optimum tour. Since $T$ is a MST, it has the least total weight. $w(C^*)\geq w(T)$. Then, consider $C$ and `tour`. $C$ replaces some paths in `tour` with a shorter edge, this replacement is always shorter since the triangle inequality property. Therefore, $w(C)\leq w(tour)=2w(T)\leq 2w(C^*)$

Note that the lower bound on approx ratio is open - need examples of inputs where $w(C)=2w(C^*)$ or close to it. 

A similar idea, but starting from a perfect matching in $G$. yields to $r(n)\leq 1.5$

## KnapSack (0-1, natural number inputs)
__Algorithm__ use dynamic programming to find min weight required to achieve total value $v$. => $O(nV), V=\sum v_i$  
Instead of using exact values $v_1,...,v_n$, use scaled values $v_i=$multiple of $\epsilon^{-1}$. (e.x. $v_1=347,238,947, v_2=434,357,833\Rightarrow v_1=347,v_2=434$)
