# Heuristic Search 

Define a domain specific heuristic function $h(p)$ where input the path, and output the guess of the cost getting to a goal state from the final state of a path $p$. Note that $h$ is defined on state, instead of the whole path. Actually, we can define $h$ on state only. $h(s) = 0$ if `Goal(s) == True`

## Greedy Best-First Search
`Open` is implemented as a `priority_queue` with priority being the heuristic cost. 

If the heuristic perfectly predicts the actual cost from a state to the optimal goal, it will be the optimal and efficient. But in practice, it can be incomplete and very far from optimal.

Also, note that GBFS is incomplete if the heuristic is misleading, since it will only check for locally optimal path. 

## A* Search
`Open` is implemented as a `priority_queue` with priority as `f(p) = heuristic(p) + cost(p)`. Therefore, instead of performing locally optimal action, $f$ estimates the cost of the path from initial state to a goal state. 

### Completeness
Note that A* is complete as long as the branching factor is finite, the cost for every action is finite and lower bounded by some $\epsilon > 0$, and the heuristic value is finite for every path that can be extended to reach a goal state. 

The idea is that the misleading paths will keep increase as its cost is growing, and then we will go back the path that can be extended to reach a goal state. 

### Optimality
Let $h^*(p)$ be the cost of optimal path from $p$ to a goal node. A heuristic is __admissible__ if for all path, the heuristic underestimates the cost, $\forall p. h(p)\leq h^*(p)$.

If a heuristic is admissible and the cost if lower bounded by some positive number, then the search won't miss any promising paths.

__Theorem__ With an admissible heuristic, A\* will always finds an optimal cost solution, if solution exists, the branch factor is finite, and cost is finite and positively lower bounded. 

__Lemma 1__ A\* with an admissible heuristic never expands a path with f-value greater than
the cost of an optimal solution.  
_proof_. By induction, we can show that at every iteration a predix of the optimal path is on the Open, and all other expanded paths cannot have f-val greater than the optimal partial path by the priority. We will eventually expanding the partial optimal path while keeping the maximum f at each iteration smaller than the optimal cost. 

### Consistency
A __monotone__ heuristic is a heuristic that satisfies triangle inequality, i.e. the h-val of a path is always smaller or equal to the h-val of another path plus its the cost from transforming the final state.

__Theorem__ monotone heuristic is admissible. 

For every path. its h-val is always smaller than the cost of transform to some optimal path and go to the goal state. 

Also, monotone implies that f-val is monotonic growing for paths expanded and the paths expanded is always minimum cost.

### Space and Time
If $h=0$, then it's UCS, so the time and space bound is similar to UCS. But Even if we have a good heuristic, time and space will still be exponential. 

### Iterative Deepening A*
Similar to IDS, we set f-val limit instead of depth limit. At each iteration, set new limit as the smallest f-val of any path that exceeded the previous limit. 
