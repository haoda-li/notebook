# Constraint Propagation

In backtracking search, we only detect constraints violations when all of its variables being assigned. Which may take much more. But if we can "look ahead" on yet unassigned variables, we can detect obvious failures and prune them early. 

## Forward Checking
When a variable is instantiated, we check all constrains that have only one uninstantiated variable (`cnstr.numUnassigned() == 1`)

For the uninstantiated variable, we check all of its possible values, prune those that violates the constraint.

During backtracking search, we will be making new variable assignments, and need to undo the pruning when we backtrack. Therefore, we need some more facilities 

```python
class VariableFC(Variable):
    
    def curDomain(self):
        """ return a list of variable's current values
        """
        pass
    
    def curDomainSize(self):
        return len(self.curDomain())
    
    def pruneValue(val, assignedVar, assignedVal):
        """ remove value from variable's curDomain. remember that 
        assignedVal assigned to assignedVar is the reason for this 
        pruning
        """ 
        pass
    
class ConstraintFC(Constraint):
    
    def unassignedVars(self):
        return [var for var in self.scope if var.value is None]
    
def restoreValues(var, val):
    """ return all values pruned because of the passed var-val assignment 
    to the current domain of their respective variable.
    """
    pass
```

```python
def forward_check(cnstr, assignedVar, assignedVal):
    var = cnstr.unAssignedVars()[0]
    # try whether the current value satisfy the constraint
    for val in var.curDomain():
        var.value = val
        # if not, remove from current domain
        if not cnstr.check():
            var.pruneValue(var, assignedVar, assignedVal)
    # reset var back after trying
    var.setValue(None)
    # if no value is possible to assign, meaning the 
    # assignedVar and assignedVal cannot be used
    if var.curDomainSize() == 0:
        return "DWO"
    return "OK"

def backtrack_fc(unAssignedVars):
    # base case: all assigned, and we output
    if unAssignedVars.empty():
        return [[(var.name, var.value) for var in variables]]
    # recursively assign vars 
    solns = []
    var = unAssignedVars.extract()
    for val in var.domain():
        var.value = val
        noDWO = True
        for cnstr in constrainsOf(var):
            # if this assignment will make another 
            # variable have no possible value assignment
            # then we stop
            if cnstr.numUnassigned == 1 and not forward_check(cnstr, var, val) == "DWO":
                noDWO = False
                break
        # if no constraint is violated, we go to the next variable
        if noDWO:
            solns += backtracking_fc(unAssignedVars)
        restoreValues(var, val)
    # undo assignment and restore var to unAssigned
    var.value = None
    unAssignedVars.insert(var)
    return solns
```

### Minimum Remaining Value Heuristic
With FC, we can always branch (extract from unassigned variables) on a variable with smallest current domain size. 

The idea is that if a variable has only one value left, then it is forced with the assignment, and we can go quicker in constraint propagation. 

## Generalized Arc Consistency
GAC check all constraints by ensures that all constraints satisfy a certain level of consistency w.r.t. the already assigned variables. 

A constraint $C(V_1, ..., V_n)$ is GAC w.r.t. $V_i$ IFF for all val of $V_i$, there exists values of $V_1,..,V_{i-1}, V_{i+1}, V_n$ s.t. $C$ is satisfied. 

$C$ is GAC IFF all of its variables are in GAC. 

And the CSP is GAC IFF all of its constraints are in GAC. 

Therefore, the idea for GAC is: If we find a value $d$ of variable $V_i$ that is not GAC, $d$ is said to be arc inconsistent and we can remove $d$ from $dom(V_i)$. 

__propagation__ we prune the domain of a variable to make a constraint GAC, but this may make another constraints no longer GAC, hence we need to re-prune that constraint again until all constraints are in GAC. 

### `hasSupport`

A var-val assignment is said to has a __support__ in constraint $C$ if exists some variable assignment s.t. the value assignments are all in variables current domains, respectively, and $C$ is satisfied. A constraint is GAC if all of its scope variables $V_i$, and every value in current domain of $V_i$, has a support. 

We will use an additional member method for `Constraint` to check for this. 

```python
def GAC_enforce(constraints, assignedVar, assignedVal):
    while not constraints.empty():
        cnstr = constraints.extract()
        for var in cnstr.scope():
            for val in var.curDomain():
                if not cnstr.hasSupport(var, val):
                    var.pruneValue(val, assignedVar, assignedVal)
                    if var.curDomainSize == 0:
                        return "DWO"
                for recheck in constrainsOf(var):
                    if recheck is not cnstr and not recheck in constraints:
                        constraints.insert(recheck)
    return "OK"

def backtrack_gac(unAssignedVars):
    # base case: all assigned, and we output
    if unAssignedVars.empty():
        return [[(var.name, var.value) for var in variables]]
    # recursively assign vars 
    solns = []
    var = unAssignedVars.extract()
    for val in var.domain():
        var.value = val
        noDWO = True
        if GAC_enforce(constrainsOf(var), var, val) == "DWO":
            noDWO = False
            break
        # if no constraint is violated, we go to the next variable
        if noDWO:
            solns += backtracking_gac(unAssignedVars)
        restoreValues(var, val)
    # undo assignment and restore var to unAssigned
    var.value = None
    unAssignedVars.insert(var)
    return solns
```
