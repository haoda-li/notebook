# SQL Data Manipulation Syntax

## Insert
```sql
INSERT INTO <<table>> VALUES <<list of rows>>
INSERT INTO <<table>> (<<subquery>>)
```

If we name the attributes we are providing values for, the system will use `NULL` or a default for the rest

Create a table before insert

```sql
CREATE TABLE Invite (
    name TEXT,
    campus TEXT DEFAULT 'StG',
    email TEST,
    age INT
);

INSERT INTO Invite(name, email)(
   SELECT first, email
   FROM Student
   WHERE cgpa > 3.4
);
```

the query have values for name and email, campus gets the default value, age gets `NULL`

## Delete

```sql
-- delete tuples satisfying WHERE clause
DELETE FROM <<relation>>
WHERE <<condition>>;

-- delete all tuples
DELETE FROM <<relation>>

--   alternatively can use DROP, which destroy the table
DROP TABLE <<relation>>
```

**Example**
```sql
DELETE FROM Course
WHERE NOT EXISTS (
    SELECT *
    FROM Took JOIN Offering ON Took.oid = Offering.oid
    WHERE grade > 50 AND
    Offering.dept = Course.dept AND
    Offering.num = Course.num
);
```

## Update
```sql
UPDATE <<relation>>
SET <<list of attribute assignments>>
WHERE <<condition on tuples>>;
```

Updating one tuple
```sql
UPDATE Student
SET campus = 'UTM'
WHERE sid = 99999;
```
Update several tuple
```sql
UPDATE Took
SET grade = 50
WHERE grade >= 47 AND grade < 50;
```

## Manipulating Views
Generally, it is impossible to modify a virtual view. 

We don't often (most systems prohibit) translate updates on views into equivalent updates on base tables.

### Materialized Views
Problem: each time a base table changes, the materialized view may change. Since cannot afford to recompute the view with each change

Solution: periodic reconstruction of the materialized view, which is otherwise "out of date". 
