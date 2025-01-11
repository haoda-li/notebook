# Relational Model
## Relation
Based on the concept of a relation or table.  
A mathematical relation is a subset of a Cartesian product

- **Schema** definition of the structure of the relation, name and constraint
    - Notation Example: Team have name, home field, coach, then the schema is `Team(Name, Home Field, Coach)`
- **Instance** particular data in the relation
- **Conventional databases** stores the current version of the data, **temporal databases** record the history
- Terminology: relation = table, attribute = column, tuple = row, arity = number of attributes, cardinality = number of rows
- Relations are sets (no duplication, order does not matter), while most commercial DBMS uses multi-sets (bag) rather than sets

## Constraint
- Example: $\forall$ (`t1`, `t2`). `t1.name` $\neq$ `t2.name` or `t1.homefield` $\neq$ `t2.homefield`
- Solution: set {home, homefield} as a **superkey**
- **Superkey** a set of >=1 attributes whose combined values are unique
- Commonly, all database relations must have a defined super key, otherwise assign all attributes as the super key
- We want the minimal set of attributes as the superkey
- **Primary Key** if we choose one attribute to be the key, then in DBMS we can define it to the be primary key
- **Notation** $R[A]$ the set of all tuples from $R$, but with only the attributes in list $A$
 - $R$ relation
 - $A$ the list of attributes in R

## Reference
- **foreign key** refers to an attribute that is a key in another table.
 - a way to refer to a single tuple in another relation.
 - A foreign key may need to have several attributes
- Declare the foreign key constraints by $R_1[X]\subseteq R_2[Y]$
 - X, Y may be lists of the same arity
 - These $R_1[X]\subseteq R_2[Y]$ relationships are a kind of *referential integrity constraint* or *inclusion dependency*.
 - A foreign key must refer to a unique tuple, hence Y must be a key in $R_2$
 


 

 

## Designing a schema
 - Important goals: Represent the data well, avoid redundancy
