# NP-complete

## Definitions

**Theorem** $\forall D_1, D_2. D_1\rightarrow_p D_2, D_2\in P \Rightarrow D_1\in P$. (also for $NP$ and $coNP$) 

*Proof* $f$ can compute $D_1$'s input in polynomial time, solving $D_2$ by $A(i)$, solving $D_1$ by $A(f(i))$ is in polynomial time. 

**Corollary** $D_1\rightarrow_p D_2, D_1\not\in P\Rightarrow D_2\not\in P$

### NP-Complete
A decision problem $D$ is NP-complete IFF $D\in NP\land D\in NP hard$

### NP-hard
$D$ is NP-hard IFF $\forall D'\in NP, D'\rightarrow_p D$

**Theorem** If $D$ is $NP-complete$ then $D\in P$ IFF $P=NP$

**Corollary** (If $P\neq NP$, then $D$ is NP-complete) implies $D\not\in P$. 

### SAT 
Input: propositional formula $\phi$  
Output: is there a setting to variables $\phi$ that makes it true

### CNF-SAT
Input: a conjunctive normal propositional formula $\phi'=C_1\land ...\land C_m$ where each clause $C_i$ is a disjunction $l_{i,1}\lor ...\lor l_{i,k}$ where each literal $l_{i,j}$ is a variable or variable negation  
Output: is there a setting to variables $\phi$ that makes it true

### Cook-Levin Theorem
SAT is NP-complete  
brief explanation  
- $SAT\in NP$ (given a certificate (values for all variables), you can evaluate the formula in poly-time, if output True for some $c$ IFF $\phi\in SAT$)  
- $SAT\in NPhard$ for any $D\in NP$, show $D\rightarrow_p SAT$ in poly time.  
intuition: $D\in NP\Rightarrow \exists verifier$, for any $x$, turn the verifier algorithm into a circuit, then into $\phi_x$ (turns out to be polynomial). Then $x\in D$ IFF $\phi_x$ is satisfiable.

Note: original proof actually construct $\phi_x$ in CNF, then CNF-SAT is NP-hard, then SAT is NP-hard. 

## Show a problem is NP-hard
Note that reduction is transitive  

Given a problem $D$
- Find $D'$ known to be NP-hard
- Show $D'\rightarrow_p D$ (then $\forall D''\in NP, D''\rightarrow_p D'\rightarrow_p D$)

**Corollary** SAT, CND-SAT, 3SAT (all clause have exactly 3 literals) are all NP-complete.


### Example: subset sum
Show the problem (SS) is NP-complete  
Input $S=\{x_1,...,x_n\}. x_i\in \mathbb{Z}^+, t\in\mathbb{Z}^+$  
Output is there $S'\subseteq S, \sum_{x\in S'}x=t$.
1. SS $\in$ NP given certificate $c\subseteq S$ (checking c is a subset, addition)
2. WTS 3SAT$\rightarrow_p$ SS.  
Want: algorithm runs in polytime that  
input: $\psi$ is a propositional formula in 3SAT  
output: $S = \{y_1,...,y_k\},t$ s.t. $\psi$ is satisfiable iff $\exists S'\subseteq S, \sum_{S'}y_i = t$.  

Let $\cdot$ denote concatenation.  
Construct function $g$ such that for each variable and each clause

$$g(a,b) = \mathbb{I}((a=x_i \land b=x_i)\lor(a=x_i\land b=\bar{x_i})\lor(a=x_i\land b= C_j\land x_i \in C_j)\lor(a=\bar{x_i}\land b= C_j\land x_i \in C_j))$$


Then let $k\leq 2n$
$y_k = g(x_1,x_{\lceil k/2\rceil})\cdot ...\cdot g(x_n,x_{\lceil k/2\rceil})\cdot g(C_1,x_{\lceil k/2\rceil})\cdot...\cdot g(C_m,x_{\lceil k/2\rceil})$ if $k$ is odd

$y_k = g(x_1,\bar{x}_{\lceil k/2\rceil})\cdot ...\cdot g(x_n,\bar{x}_{\lceil k/2\rceil})\cdot g(C_1,\bar{x}_{\lceil k/2\rceil})\cdot ...\cdot g(C_m,\bar{x}_{\lceil k/2\rceil})$ is $k$ is $k$ is even

Then let $2n+1 \leq k\leq 2(m+n)$  
$y_k = 100...000$ if $k$ is odd and $1$ is located at $\lfloor 2(m+n)-k\rfloor + 1$'s position.  
$y_k = 200...000$ if $k$ is even and $2$ is located at $\lfloor 2(m+n)-k\rfloor + 1$'s position.  
Let $t = 1\cdot ...\cdot 1\cdot 4\cdot ...\cdot 4$ where there are $n$ 1's and $m$ 4's. 



## Argument of Correctness
Suppose $\psi$ is satisfiable, then there is some setting of variables such that every clause contains at least one True literal.   
Then start with $S'=$ the set where every $y$ corresponding to a true literal. Then, $\sum S' = 11..1\{1,2,3\}...\{1,2,3\}$ where there are $n$ 1's and $m$ $\{1,2,3\}$'s. Then, we can add from the number that corresponds to clauses to obtain $t$.  

Suppose $S$ contains some subset $S', \sum S'=t=11...144...4$, then
1. None of the digits can adds to next digit  
2. $S'$ must contain exactly one of the numbers corresponding to each $\{x_i,\bar{x_i}\}$ for all $i\in\{1,2,...,n\}$. 

Set variables to make the literals corresponding to $S'$ true. Then for the last $m$ digits of $t$, since numbers in the second half of $S$ adds up to at most three in each digit, there has to be some number corresponding to $\{x_i,\bar{x_i}\}$ in $S'$ must have a 1 in that digit. So each clause of $\psi$ contains at least one true literal.



### Example: Vertex Cover 
Input $G=(V,E), k\in\mathbb{Z}^+$. Output $G$ contains a vertex cover $C$ of size $k$ where $C\subseteq V$ s.t. $\forall e\in E$. have at least one endpoint in $C$. 

Claim. $3SAT\rightarrow_p VC$  
Example $(x_i + \bar{x_2} + \bar{x_4})(x_2+\bar{x_3}+x_1)(\bar{x_3}+x_4+\bar{x_2})$, label each literal by its position, where the $i$th clause is $(a_i,b_i,c_i)$.

Construct $G$ where each clause forms a triangle, for each variable makes $x_1-\bar{x_1}$, then add edges for each label to its corresponding variable. Construct $k=n+2m$

Suppose $\psi$ is satisfiable, then  $C_1 =$all true literals and $C_2 =$ two labels from each triangle where the one left out is connected to $C_1$, $C=C_1\cup C_2$. 

Suppose $C$ is a vertex cover of size $n+2m$. Then, for each triangle, at least 2 labels must be picked, otherwise can't cover the triangle, at least 1 variable must be picked, otherwise can't cover the edge between the variable and its negation. Set all picked variables being true, to cover edge between variables and labels, each must contain one literal in $C$. then in each triangle, at least one label is true, hence all clause evaluate true and $\psi$ is true. 

## Show decision problem is NP-complete
1. describe verifier that input $x$ and certificate $c$, verify in polytime as function of size(x) and show $x\in D$ IFF $\exists c$ output True.
2. Identify some $D'\in NPhard$, show $D'\rightarrow_p D$ the reduction algorithm takes arbitrary input $x$ for $D'$, generate input $y_x$ for $D$ s.t. $x\in D'\Rightarrow y_x \in D'$ and $x\not\in D'\rightarrow y_x\not\in D$ (usually contrapositive by $y_x\in D\Rightarrow x\in D'$)  
Notice that algorithm only gets $x$, not $c$ and backward argument starts from $y_x$
