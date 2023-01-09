# Uninformed search

The rule remains the same for any search problem being solved, and these strategies do not take into account any domain specific information about the particular search problem.

Note that in most of cases, we are dealing with exponential growing number of nodes and edges. And the states are often implicitly defined. We need to discover them through successor state functions and states must contain enough information to allow the successor function to perform its computation. 

## Breath-First Search (BFS)
`Open` is implemented as a `queue` (first-in-first-out). Therefore, we will always finish expanding nodes at depth $k$ before moving to $k+1$. 

- completeness: yes, it will traverse all of the states expanded from $s0$
- optimality: shorted-path, but not necessarily least cost
- time: $\sum_i^d b^i \in O(b^{d+1})$.
- space: $O(b^{d+1})$

## Depth-First Search (DFS)
`Open` is implemented as a `stack` (first-in-last-out)

- completeness: No if there's circles (will fall into an infinite loop). Yes if state space is finite and without circles
- optimality: No
- time: $O(b^m)$ where $m$ is the length of longest path
- space: $O(bm)$ Frontier only contains the current path along with the unexplored siblings of states
along current path.

## Iterative Deepening Search (IDS) and Depth Limited Search (DLS)
__DLS__ only add states into `Open` if the path from $s0$ to the state is less than or equal to the defined depth limit. `Open` will still be implemented as a `stack`. 

__IDS__ iterative increasing the depth limit and perform DLS, until a solution is found or DLS does not cutoff any paths (no state can be expanded further more). 

- completeness: yes, the same reason as finite state DFS
- optimality: shortest length (if there's a shorter path, we should have found it with the iteration of smaller depth limit) but not least cost (we can use cost limit instead of depth limit to achieve this, but it will be computationally expensive)
- time: $\sum_{i}^d (d+1-i)\cdot O(b^i)\in O(b^d)$
- space: $O(bd)$ since we drop the tree when one iteration of DLS ends

Although IDS looks more complex than BFS, note that the node expansion is exponential. The time complexity of IDS can sometimes be better than $BFS$ since it does not expand paths at the solution depth while BFS did. And space complexity for BFS is much worse than IDS. 

## Uniform-Cost Search (UCS)
`Open` is implemented as a `priority_queue` with priority being the cost. If the cost is the same, then it will perform BFS. 

- completeness: yes if the cost of each action in the expansion is positive, say $c \geq \epsilon > 0$
- optimality: optimal in cost
- time: $O(b^{\lfloor c^*/\epsilon\rfloor+1})$ $c^*$ be the optimal cost, $\epsilon$ be the cost bound for an action
- space: $O(b^{\lfloor c^*/\epsilon\rfloor+1})$ 

_proof of cost optimality_
1. if a path $p2$ is expanded after $p1$, then the cost $c(p1)\leq c(p2)$ as $p2$ will contains $p1$
2. the paths in the search space has strictly increasing cost

## Path checking and Cycle checking
Note that circles (the path of state transforms may return to a known state) is a big issue. 

__path checking__: Each time a path is added into `Open`, check if this path is a circle. If it is, then prune the path.  To check whether it is a cycle, we only need to check whether the last added node is already in the path.   
path checking is very  quick ($O(d)$), but cannot prune all cycles in the search tree. 

__cycle checking__: Check the last added node with all paths in the open. Only keep the path with least cost.   
cycle check is effective, but time and space costly. 
