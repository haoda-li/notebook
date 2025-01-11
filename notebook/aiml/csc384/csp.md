# CSP Backtracking

## Feature Vectors

Define a feature vector of a state as 
- a set of n variables (features)
- each variable has a domain of different values
- A state is specified by an assignment of a value for each variable
- A partial state is specified by an assignment of a value to some of the variables

For example, for sudoku, we have 81 variables $a_{11},..,a_{99}$, each variable belongs to the domain $\{1,..,9\}$. Then, a state of the puzzle can be represented by specified value in each cell. A partial state is where some (not all) cells filled in.

## CSP Problem Setup
Compare to search problem, we don't care about the sequence of actions, we only need to find a setting of variables that satisfies all of the constraints. 

Define a constraint satisfaction problem as
 - a set of variables $V = \{v_1,.., v_n\}$
 - a finite domain of possible values for each variable $D(v_i)$ s.t. $v_i \in D(v_i)$
 - a set of constraints $C_1,...,C_m: \mathcal P(V)\rightarrow \{0, 1\}$, which give an assignment of variables, return whether it satisfies the constraint. Note that most constraint will only check for a particular set of variables, called its scope. 
 
We want to find the __solution__ as an assignment to all of the variables, s.t. $C_1,...,C_m$ will all return True. A CSP is unsatisfiable if no solution exists. 

```python

class Variable:
    def __init__(self, 
                 name: str, 
                 domain: List,
                 value
                 ):
        # current assigned value
        # variable is unassigned IFF value is None
        self.value = value 
        # a string specifying the variable's name
        self.name = name
        # a set of values in variable's domain
        self.domain = domain
    
    def domainSize(self):
        return len(self.domain)
    
    def isAssigned(self):
        return self.value is None
    
class Constraint:
    def __init__(self, 
                 name: str, 
                 scope: List[Variable]):
        # a string specifying the constraint's name
        self.name = name
        # s list of variables in the constraint’s scope
        self.scope = scope
        
    def arity(self):
        return len(self.scope)
    
    def num_unassigned(self):
        """ Returns number of variables in 
        constraint’s scope that are not assigned
        """
        return sum([v.isAssigned for v in self.scope])
        
    def check(self):
        """ return True if currently assigned values 
        to the variables in the scope satisfy the constraint.
        Or num_unassigned > 0
        """
        return self.num_unassigned > 0
```

### Sudoku Example
 - Variables $v_{11}, ..., v_{99}$  
 - domain $D(v_{ij}) = \{1,...,9\}$ if $v_{ij}$ is not filled, otherwise $k$ if $v_{ij}$ is filled with $k$. 
 - constraints (27 constraints):
     - $\text{all-diff}(v_{11}, ..., v_{19}), \text{all-diff}(v_{21}, ..., v_{29}), ..., \text{all-diff}(v_{91}, ..., v_{99})$: row constraint
     - $\text{all-diff}(v_{11}, ..., v_{91}), \text{all-diff}(v_{12}, ..., v_{92}), ..., \text{all-diff}(v_{19}, ..., v_{99})$: column constraint
     - $\text{all-diff}(v_{11}, ..., v_{33}), \text{all-diff}(v_{41}, ..., v_{43}), ..., \text{all-diff}(v_{77}, ..., v_{99})$: sub square constraint

## Backtracking Search

Because CSP does not require finding a path, and traditional search does not capture additional structure of CSP problem. Although CSP can be viewed as search, we need some specifications to frame the algorithm. 

Instead of paths, we will search through the space of partial assignments.  
Unlike search, order does not matter.  
If a constraint is violated during the process of building up a solution, we can immediately reject it.  
When backtracking finishes, we filled in all variables, and get a solution. 

We initialize all variables with `var.value = None` and put them into `unAssignedVars`, and run `backtracking` on the unassigned variables. 

```python
def backtracking(unAssignedVars):
    # base case: all assigned, and we output
    if unAssignedVars.empty():
        return [[(var.name, var.value) for var in variables]]
    # recursively assign vars 
    solns = []
    var = unAssignedVars.extract()
    for val in var.domain():
        var.value = val
        cnstrOK = True
        for cnstr in constrainsOf(var):
            # if one constraint fails with all of its vars assigned
            # then we stop
            if cnstr.numUnassigned == 0 and not cnstr.check():
                cnstrOK = False
                break
        # if no constraint is violated, we go to the next variable
        if cnstrOK:
            solns += backtracking(unAssignedVars)
    # undo assignment and restore var to unAssigned
    var.value = None
    unAssignedVars.insert(var)
    return solns

unAssignedVars = variables
backtracking(unAssignedVars)
```
