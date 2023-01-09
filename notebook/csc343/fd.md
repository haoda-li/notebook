# Functional Dependency
Let $R$ be a relation, $X,Y$ subset of attributes of $R$

**X determines Y** assets that if two tuples agree on all the attributes in set $X$, they much also agree on all the attributes in set $Y$.  
$X\rightarrow Y: \forall t_1,t_2. t_1[A]=t_2[A]\rightarrow t_1[B]=t_2[B]$

$A_1...A_n \rightarrow B_1...B_m: \forall t_1,t_2.t_1[A_1]=t_2[A_1]\land ...\land t_1[A_n]=t_2[A_n]\rightarrow t_1[B_1]=t_2[B_1]\land ...\land t_1[B_m]=t_2[B_m]$ 

We can't break the LHS and get multiple FDs, but we can break RHS.

**FD are closely related to keys**  
Suppose K is a set of attributes for relation R  
K is a superkey for R IFF K functionally determines all of R

**Inferring FDs**  Given a set of FDs we can often infer further FDs  
Example: $A\rightarrow B \land B\rightarrow C \Rightarrow A\rightarrow C$


## Methods for Inferring FDs
Proven an FD follows using the Closure Test  
- Assume your know the values of the LHS attributes, and figure out everything else that is determined
```py title="Attribute-closure(Y, S)"
""" Y: set of attributes
    S: set of FDs
"""
Y+ = Y
while more changes occur:
    if exists FD LHS->RHS in S s.t. LHS in Y+:
        Y+ += YHS
return Y+
```


Follow Algorithm
```py title="FD_follows(S, LHS->RHS)"
Y += Attribute-closure(LHS, S)
return RHS is in Y+
```

Projection algorithm
```py title="project(S, L)"
T = []
for each subset X of L:
    Compute X+
    for attribute A in X+:
        if A in L: 
            T += [X-> A]
return T
```
(Too expansive)

Minimal Basis: to minimize FDs
```py title="minimal_basis(S)"
split the RHS of each FD
for X->Y in FD where |X|>=2:
    remove any attribute from X that get an FD that follows from S
for f in FD:
    if S-{f} implies f:
        remove f from S
```

## FD on Database Design

### Decomposition
decompose $R(A_1,...,A_n)$ to two relations $R_1, R_2$ where
$R_1, R_2$ are projections of $R$ and $R_1\bowtie R_2=R$

**Boyce-Codd Normal Form** $\forall X\rightarrow Y\in R$ be nontrivial FD ($Y\not\subseteq X$) with $X$ being the superkey (equv $X^+$ contains all attributes). 

To find BCNF

```py title="BCNF_decompose(R, F)"
""" R: relation
    F: sets of FDs
"""
if X->Y in F violates BCNF:
    compute X+
    replace R by two relations:
        R1 = X+ 
        R2 = R-((X+)-X)
    project the FD's F onto R1 and R2
    BCNF_decompose(R1, F)
    BCNF_decompose(R2, F)
```
NOTE

If there are $\geq 1$ FD violates BCNF, there will probably be multiple results.

#### Speed-ups
Only need to check whether the LHS of each FD is a superkey using the closure test

When project FDs onto the new relation, check if the new relation violate BCNF because of this FD, abort the projection. 


### Properties of decomposition
We want:
1. No anomalies
2. Lossless join, which be able to
 - project the original relations onto the decomposed schema
 - then reconstruct the original by joining, we should get back exactly the original tuples
3. Dependency preserved

A lossy join may create new tuples 

BCNF guarantees 1 and 2, not 3.  
3NF guarantees 2 and 3, not 1. However, 3NF guarantees minimal bases

### Third Normal Form (3NF)
An attribute is **prime** if it is a member of any key

$X\rightarrow A$ violates 3NF IFF X is not a superkey and A is not prime

```py title="3NF_synthesis(F, L)"
""" F: set of FDs
    L: set of attributes
"""
    construct a minimal basis M for F
    for X->Y in M:
        define a new relation with schema union(X,Y)
        if no relation is a superkey for L:
            add a relation whose schema is some key
```    

**Example** R(A,B,C,D), $A\rightarrow B, A\rightarrow C$. 
- FD set is already a minimal basis
- R1(A,B), R2(A,C)
- No relation is a superkey for L: R3(A,D)


### Chase Test
When a new set of relations is not generated from BCNF or 3NF, to check lossless condition.
