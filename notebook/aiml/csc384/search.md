# Search 

## Problem Setup

__State__ is a representation of a configuration of the problem domain.   

__State Space__ the set of all states. 

__Initial State__ the starting configuration

__Goal State__ Some configuration one want to achieve

__Action (State Space Transitions)__ A function from state to another state that is defined by allowed changes to move from one state to another

Then a __solution__ will a sequence of actions that transform the initial state to a goal state. 

### Search Graph

Assuming the search space is finite, we can define a Graph $G=(V,E)$ where $V$ is the states in the search space, with repetitions, and $(v_i,v_j)\in E$ if there's an action that transforms $v_i$ into $v_j$. 

A search tree reflects the behavior of an algorithm as it walks through a search problem. We consider the __solution depth__ $d$ and max branching factor $b$. 

Note that if we prune all circles in the graph, the search graph should be a tree rooted at the initial state, and branching out by possible actions. 

## Algorithm
An algorithm will take inputs as 
 - initial state
 - successor function $S(x)$: return the set of states that can be reached via one action from $x$. 
 - Goal Test $G(x)$ return true iff $x$ satisfies the goal condition.
 - action cost function $C(x,A,y)$ return the cost of the action $A(x)=y$, if unreachable, then return $\infty$
 
And output sequence of actions $(A_0, ...., A_n)$ that will transforms initial state into the goal. The solution might be optimal in cost, or in length, but generally does not have any guarantees. 

For a algorithm we need to consider: 
- completeness: will the search always find a solution if a solution exists
- optimality: will the search always find the optimal cost solution
- time complexity: often considered by the max number of nodes (paths) expanded
- space complexity: often considered by the max number of nodes (paths) stored

### Tree Search
To explore the state space, iteratively apply $S$ to states discovered so far, and $S(x)$ will give more states. We can at the same time, annotate their action and cost. For example, $S(x) = \{(y_1, a_1, [c_1]), ..., (y_k, a_k, [c_k])\}$. We can put states into a list called __Frontier (Open)__ and repeatedly pulling states from Open until a goal state is found. 

```python
def tree_search(s0, Succ, Goal):
    """
    s0: initial state
    Goal: Goal test
    Succ: successor function
    """
    Open = {s0}
    while not Open.is_empty():
        # the selection will be defined by different algorithm
        x = Open.pull()
        if Goal(x):
            return True
        Open = Open.union(Succ(x))
    return False
```

Note that the order of pulling from `Open` has a critical effect on the search, therefore, we need to define some order on `Open`
