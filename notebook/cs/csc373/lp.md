# Linear Programming

## Intuitive Example
determine type of ridings difference  
**Input** platforms issues to emphasize. Market research gives following table of voters (lost/grand for each $1 spending)

| | urban       | sub | rural |
|---|-------------|-----|-------|
| roads       | -2  | 5     | 3  |
| gun control | 8   | 2     | -5 |
| farms       | 0   | 0     | 10 |
| government  | 10  | 0     | -2 |


**Goal** Achieve gains of at least 50k urban, 100 sub-urban, 25k rural while spending as little as possible, identify unknowns $x_1,x_2,x_3,x_4\in\mathbb{R^{\geq 0}}$ is the spend on roads, gun control, farms, and government in advertising (unit is 1k), respectively, where $x_1+x_2+x_3+x_4$ minimized. 
Formalized: 

$$\begin{bmatrix}
        -2 & 8 & 0 & 10 \\
        5 & 2 & 0 & 0 \\
        3 & -5 & 10 & -2 \\
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 1
\end{bmatrix} \begin{bmatrix}
        x_1 \\
        x_2 \\
        x_3 \\
        x_4
\end{bmatrix} \geq 
\begin{bmatrix}
        50 \\
        100 \\
        25 \\
        0 \\ 0 \\ 0 \\ 0
\end{bmatrix}$$

minimize $\sum_1^4 x_i$


## Problem Definition
a linear program consists of 
 - variables $\vec{X}\in\mathbb{R}^n$
 - objective function: min/maximization $\vec{c}\vec{X},\vec{c}\in\mathbb{R^n}$
 - constraint $\vec{a_j}\vec{X} \le | = |\ge b_j, \vec{a_j}\in\mathbb{R}^n, 1\leq j\leq m$. Note that the constraint are not strict (otherwise it cannot be solved as real number for open set). Matrix notation is used when all the constraints comparison relations are the same

Any inequality can be translated as cutting on an infinite plane. Each constraint eliminates one-half plane. 

**Feasible region** is the collection of values that satisfy every constraint.
 - $\emptyset$ - No solution 
 - unbounded - No extremum, no solution
 - bounded - either exactly one solution or infinitely many solutions

### Algorithm 
- Simplex algorithm worst-case exponential time (However, the edge case is very rare, commonly, it runs in polynomial with small constant)
- Interior point methods (worst-case polynomial but has large constant)

## Applications

### Network Flow Problem
 - variables: $x(u,v) = f(u,v).\forall (u,v)\in E$
 - objective function: maximize $\sum_{(s,v)\in E} x(s,v)$
 - constraint: $0\leq x(u,v)\leq c(u,v)\land \sum_{(u,v)\in E}x(u,v)=\sum_{(v,u)\in E} x(v,u). \forall u\in V-\{s,t\}$
 
 clearly, solutions to network flow problem corresponds to solutions to the linear program.   
 Note that the method does not guarantee integer-valued solution, even the actual solution is integer
 
### Shortest Path (with $w(e)\in\mathbb{Z}^+$)
 - variables: $\forall v\in V. d_v=\min\{w(s\sim v)\}$
 - objective function: $\max d_t$
 - constraints:  
  $d_v\geq 0. \forall v\in V$  
  $d_s=0$  
  $d_v\leq d_u+w(u,v) \land d_u\leq d_v+w(u,v) \forall (u,v)\in E$
  
### Vertex Cover
given $G=(V,E)$ undirected, want $S\subseteq V$ that $S$ covers all edges a.k.a. $\forall (u,v)\in E. u\in S\lor v\in S$, $|S|$ minimized
 - variables: $\mathbb{I}_v:=\mathbb{I}(v\in S). \forall v\in V.$
 - objective function: $\min\sum_{v\in V}\mathbb{I}_v$
 - constraint: $\mathbb{I}_u + \mathbb{I}_v \geq 1 \forall (u,v)\in E$  
 hidden constraint: since $\mathbb{I}_v$ is an indicator $\mathbb{I}_v\in\{0,1\}$, while in this case, this is not a linear program constraint. The program becomes an integer program.  
 **However, integer program is not in polynomial time!**

## Example Problem 1
"Duckwheat" is produced in Kansas and Mexico and consumed in New York    and California. Each month, Kansas produces 15 "shnupells" of duckwheat    and Mexico, 8, while New York consumes 10 shnupells and California, 13.    The monthly transportation costs per shnupell are 4 from Mexico to New York, 1 from Mexico to California, 2 from Kansas to New York, and 3 from Kansas to California.

### Variables
$x_1,x_2,x_3,x_4$ be the amount of Duckwheat from 

 - $x_1$ K to N
 - $x_2$ K to C
 - $x_3$ M to N
 - $x_4$ M to C  
 
### Objective
minimize $2x_1 + 3x_2 + 4x_3 + x_4$

### Constraint
 - $x_1 + x_2 = 15$
 - $x_3+x_4 = 8$
 - $x_1 + x_3 = 10$
 - $x_2+ x_4 = 13$
 - $x_1,x_2,x_3,x_4 \geq 0$
 
Then it equals to maximize

$$2x + 3(15-x)+4(10-x)+(x-2)=-4x+93$$

where $2\leq x\leq 10$, hence $x=2$

## Example Problem 2
Consider a set of mobile computing clients in a certain town who each need to be connected to one of several possible "base stations". We'll suppose there are $n$ clients, with the position of each client specified by its $(x,y)$ coordinates in the plane. There are also m base stations, each of whose position is specified by $(x,y)$ coordinates as well.  
We wish to connect each client to exactly one base station. Our choice of connections is constrained in the following ways. There is a "range parameter" r −− a client can only be connected to a base station that is    within distance r. There is also a "load parameter" L −− no more than L clients can be connected to any single base station.   
Show how to represent this problem as a linear program, and how to solve    it using linear programming algorithms. Justify carefully that your    solution is correct. Can you guarantee that your algorithm runs in    polytime?

### Variables
$I_{11},...,I_{nn}$ where $I_{ij}$ is the indicator that there is a connection between client $i$ and base station $j$.  
### Objective 
minimize $\sum_{i=1}^n\sum_{j=1}^n d_{ij}I_{ij}$ where $d_{ij}$ is the distance between client $i$ and base station $j$.  
### Constraint 
- $\forall i\in\{1,2,...,n\}. \sum_{j=1}^n I_{ij} = 1$
- $\forall i,j. d_{ij}I_{ij}\leq r_{ij}$
- $\forall j. \sum_{i=1}^n I_{ij}\leq L_j$

Since $I_{ij}$ is a indicator function, this is an integer problem

