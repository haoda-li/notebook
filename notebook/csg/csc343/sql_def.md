# SQL Definitions Syntax

## Build in data types
`CHAR(n)` fixed-length string of n char. Padd with blanks if necessary
`VARCHAR(n)` variable length string of up to n characters  
`TEXT` variable-length, unlimited (not SQL standard)  
`INT`  
`FLOAT`  
`BOOLEAN`  
`DATA; TIME; TIMESTAMP`

`'string'` must be surround by single quotes

### User-defined types
```sql
create domain Grade AS int
    default null
    check (value >= 0 and value <= 100);
    
create domain Campus as varchar(4)
    default 'StG'
    check (value in ('StG', 'UTM', 'UTSC'))
```

Constraints on a type are checked every time a value is assigned to an attribute of that type.

Fault value when no value has been specified.  
We can run a query and insert the resulting tuples into a relation even if the query does not give values for all the attributes in the relation if the types of the missing attributes have default values.

Table attributes can also have default values.

The difference
 - attribute default: for that one attribute in that one table
 - type default: for every attribute defined to be of that type

## Keys and Foreign Keys
### Primary Key
`PRIMARY KEY` for one or more attributes in a relation means
 - the attributes form a key
 - their values will never be null

Every table must have 0 or 1 primary key

example
```sql
create table T1 (
    ID integer primary key,
    name varchar(25)
);


-- only way for multi-attribute keys
create table Blah(
    ID integer,
    name varchar(25),
    primary key(ID)
);
```

### Unique Key
`unique` for one or more attributes 
- form a key
- value can be null (different from `primary key`)

Can declare more than one set of attributes to be `unique`

```sql
create table T1 (
    ID integer unique,
    name varchar(25)
);


-- only way for multi-attribute keys
create table Blah(
    ID integer,
    name varchar(25),
    unique (ID)
);
```

For uniqueness constraints, no two nulls are considered equal

- Set the attributes by unique, then you can't insert two `('A', 'B')`, but you can insert two `(null, 'B')`

### Foreign key
```sql
foreign key (sID) references Student
```

every value for sID in this table must actually occur in the Student table and sID must be `primary key` or `unique`

Can be declare with the attribute or as a separate table element.  
Can reference attributes that are not the primary key as long as they are unique; just name them

```sql
create table People (
    SIN int primary key,
    name text, 
    OHIP text unique
);

create table Volunteers (
    email text primary key,
    OHIPnum text references People(OHIP)
);
```

## Enforce foreign-key constraints


### "check" constraints
```sql
create domain Grade as smallint
    default null
    check (value >= 0 and value <= 100)
```

define on attribute, tuples of a relation, and across relations.

#### Attribute-based

- Defined with a single attributes. constrains its value in every tuple
- can only refer to that attribute
- can include a subquery

```sql
create table Student (
    sin int,
    program varchar(5) check (program in (select post from O)),
    firstName varchar(15) not null
);
```

checked only when insert a tuple, or update attribute value

`not null` is very commonly used

#### Tuple-based
- defined as a separate element of the table schema, so can refer to any attributes of the table
- The condition to be checked can be anything that could go in a `WHERE`, and can include a subquery

```sql
create table Student (
    sID int,
    age int, 
    year int,
    college varchar(4),
    
    check (year = age - 18),
    check college in (select name from Collges)
);
```

Only when a tuple is inserted, or it updated 

`check` only fails if it evaluates to `false`, (different from `where` which only evaluates to `true`)

Problem with `null`, the only way to prevent `null` is `not null`

name constraint
```sql
constraint XXX check (...);
constraint XXX foreign key (cNum, dept) references Course
```

### Assertions
`check` constraints apply to an attribute or table but they can't express constraints across tables  

`assertions` can express cross-table constraints
`create assertion (<name>) check (<predicate>);`

`assertions` are costly because they have to be checked upon every database update and each check can be expensive

### Triggers
cross-table constraints, as powerful as assertions, but can control the cost by having control over when they are applied

specify
- event: some type of database action 
```sql
after delete on Courses 
-- or
before update of grade on Took
```
- condition: bool-valued expression
```sql
when grade > 95
```

- action: any SQL statements
```sql
insert into Winners values (sID)
```



## Reaction Policies
`cascade` propagate the change to the referring table
`set null` set the referring attribute(s) to null

Suppose table R refers to table S  
We can define "fixes" that propagate changes backwards from S to R  
We cannot define fixes that propagate forward from R to S

Add your reaction policy where you specify the foreign key constraint

```sql
create table Took (
    ...
    foreign key (sID) references Student on delete cascade
    ...
);
```

You can react to ...
- `on delete`
- `on update`
- or both

Policy can specify 
- `restrict`: Don't allow deletion/update
- `cascade`: make the same deletion/update in the referring tuple
- `set null`: Set the corresponding value in the referring tuple to `null`

## Update Schema
- Alter: alter a domain or table

```sql
alter table Course
    add column numSections int;
   
alter table Course
    drop column breadth;
```

- Drop: remove a domain, table, or whole schema
```sql
drop table Course;
-- Course still exists, but no content in it
```

-Delete:
```sql
delete from Course
-- Course does not exist
```

## Schema

Schemas let you create different name spaces. For logical organization and for avoiding name clashes

A default schema `public` is available

To create additional schema:

```sql
CREATE SCHEMA University;
```

To refer to things inside a schema

```sql
CREATE SCHEMA University.Student (...);
SELECT * FROM University.student
```
