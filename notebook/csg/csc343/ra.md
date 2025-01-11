# Relational Algebra



**Example schema** will be used for examples 

 - Relations: Movies(<u>mID</u>, title, director, year, length); Artists(<u>aID</u>, aName, nationality); Roles(<u>mID, aID, character</u>)
 - Foreign key constraints: Roles[mID]$\subseteq$ Movies[mID]; Roles[aID]$\subseteq$ Artists[aID]

## Relational algebra 
 - The value of any expression is a relation
 - Assumptions
    - Relations as sets (without duplicated rows)
    - Every cell has a value
 - Operands: tables
 - Operator  examples:
    - Choose only the rows wanted
    - Choose only the columns wanted
    - combine tables


## Operators

### Select Rows 
$\sigma_c(R)$: $R$ table, $c$ boolean expression

  - The result is a relation with the same schema but with only the tuples satisfy $c$
  - Select all British actors  $\sigma_{\text{nationality = 'British'}}(Actors)$ 
  - Select all movies from 1970s $\sigma_{1970\leq year\leq 1979}(Movies)$


### Project
$\Pi_c(R)$ slice vertically

- onto fewer attributes can remove key that makes duplicates possible, whenever duplicates happens, only one copy of each is kept  
- To perform multiple query together Example: find the names of all directors of movies from the 1970s $\pi_{director}(\sigma_{1970 <year<=1979}(Movies))$


### Cartesian Product
$R_1\times R_2$ map two relations to a new relation with every combination of a tuple from $R_1$ concatenated to a tuple from $R_2$

  - Resulted schema is every attribute from $R_1$ followed by $R_2$ in order
  - The resulted relation have $R_1.cardinality|\times R_2.cardinality$ tuples

### Natural join
$R_1\bowtie R_2$ take the Cartesian product and select rows with the same attribute and value  that are in both relation to ensure equality on attributes, then project to remove duplicate attributes

 - Natural join is commutative and associative

#### Theta Join
$R_1\bowtie_{c} R_2:= \sigma_c{R\times S}$

### Assignment
$R:= Expression$ or $R(A_1,...,A_n):=Expression$, the second way allows to rename all the attributes

 - $R$ must be temporary and not one of the relations in the schema, it should not be updated

### Rename
$\rho_{R_1}(R_2)$ or $\rho_{R_1(A_1,...,A_n)}(R_2)$ renames the relation. Note that $R_1:=\rho_{R_1(A_1,...,A_n)}(R_2)$ is equivalent to $R_1(A_1,...,A_n):=R_2$

### Division
$R/S:=$ the largest relation $Q$ s.t. $Q\times S\subseteq R$. the operation will return a relation will all the attributes in $R$ that's not in $S$ and all tuples in $R$ that match every tuple in $S$
