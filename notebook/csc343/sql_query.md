# SQL Query Syntax

## Basic Query 

Any query need SELECT FROM WHERE
```sql
SELECT column names
FROM Relation
WHERE condition;
```
With Multiple relationsA $\times $ B
```sql
From A, B
```



Temporarily renaming
```sql
SELECT e.name, d.name
FROM Employee e, department d
WHERE d.name = 'marketing' AND e.name = 'Horton';
```

Self joins requires renaming
```sql
SELECT e1.name, e2.name
FROM Employee e1, Employee e2
WHERE e1.salary < e2.salary;
```

\* in SELECT means all attributes of this relation
```sql
SELECT *
```

Rename attributes 
```sql
SELECT name AS new_name
```


Conditions allowed, note != is \<\> 
```sql
| = | <> | < | > | <= | >= |
AND | OR | NOT
```

Put tuples in order, add this as the final clause, default in ascending order, add DESC to force descending
```sql
ORDER BY <<attribute list>> ;
ORDER BY <<attribute list>> [DESC];
```
The attribute list can include expressions:
```sql
ORDER BY attribute_a + attribute_b;
```

Keywords and identifiers are not case-sensitive and white space are ignored


Expressions can be used in SELECT clauses,   
operands: attributes, constants
operators: arithmetic ops, string ops
```sql
SELECT, sid, grade+10 as adjusted
FROM Took;

SELECT dept|| cNum
From Course;
```

Expressions that are a constant
```sql
SELECT, dept, cNum, 'satisfies' AS breadthRequirement
FROM Course
WHERE breadth;

Pattern operators
```sql
<<attribute>> LIKE <<pattern>>
<<attribute>> NOT LIKE <<pattern>>
```
`%` any string   
`_` any string char
```sql
SELECT *
FROM Course
Where name LIKE '%Comp%';
```

## Aggregation

`SUM, AVG, COUNT, MIN, MAX` can be applied to a column in a `SELECT`

`COUNT(*)` counts the number of tuples 

`DISTINCT` inside the brackets can stop duplicates from contributing to the aggregation. 



`GROUP BY <attributes>` The tuples are grouped according to the values of those attributes and any aggregation give us a single value per group

If any aggregation is used, then each element of the SELECT list must be aggregated or an attribute on the GROUP BY list. 

`HAVING` decide which groups to keep. 
```sql
...
GROUP BY <<attributes>>
HAVING <<condition>>
```

Outside subqueries, HAVING may refer to attributes only if they are either aggregated or an attribute on the GROUP BY list. 

Order of execution of a query   
Writing query (execution order): 
```sql 
SELECT (5)
FROM (1)
WHERE (2)
GROUP BY (3)
HAVING (4)
ORDER BY (6)
```

## Set operations

A table can have duplicate tuples, unless it violate an integrity constraint. 

**Set operations with Bags**   
Using Multiset operations rather than set operations
```sql
(<subquery>)
UNION / INTERSECT / EXCEPT
(<subquery>)
```
brackets are mandatory

To force the result of a query to be a set, use `SELECT DISTINCT`

To force the set operations to be a bag, use `UNION/INTERSECT/EXCEPT ALL`



## Views

Use virtual views to temporarily refer to the result of a query

```sql
CREATE VIEW xxx AS
SELECT ...
FROM ...
WHERE ...
```

Break down a large query

## Joins

Joins allowed in `FROM`
```sql
R, S  == R CROSS JOIN 
R NATURAL JOIN
R JOIN S ON <CONDITION>
```

Inner join is not the best practice since a working query can be broken by adding a column to a schema.


### Outer Join
preserves dangling tuples by padding them with `NULL` in the other relation
```sql
R LEFT OUTER JOIN S
R RIGHT OUTER JOIN S
R FULL OUTER JOIN S
```

When use `LEFT, RIGHT, FULL` it will be outer join, if not added, then inner

## NULL
Used for indicating missing value or inapplicable attribute

Cant be checked by `IS NULL` and `IS NOT NULL`, e.x.
```sql
SELECT *
FROM Course
WHERE br IS NULL;
```

Also, if one or both operands to a comparison is `NULL`, the truth value will always be `UNKNOWN`

NULL can be imagined to have value 0.5, compared to TRUE = 1, FALSE = 0 when consider logical operations

Notice that `WHERE` will only pick rows with `TRUE`

## Subqueries
`FROM` clause, but you must name the result and parenthesized. Hence can refer to it in the outer query

```sql
SELECT ...
FROM A, 
   (SELECT *
    FROM Offering
    WHERE instructor='Horton') B
WHERE A.oid = B.oid;
```

`WHERE` clause if the subquery guaranteed to produce exactly one tuple. 

However, we can also use keywords `ANY/SOME` for existence, `ALL` for for all

```sql
x <<comparison>> ANY|ALL (<<subquery>>)
```

`IN, NOT IN, EXISTS` is some syntax sugar

```sql
x IN (<<subquery>>) === x = SOME (<<subquery>>)
x NOT IN (<<subquery>>) === x <> ALL (<<subquery>>)
EXISTS (<<subquery>>) \exists y\in (<<subquery>>)
```

