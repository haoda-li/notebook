# Extremum

### _Def'n_. Boundedness
__Bound__  A set $S\subset\mathbb{R}$ is  

- __bounded above__ $\exists M\in\mathbb{R}. \forall s \in S. s\leq M$.  
- __bounded below__ $\exists L\in\mathbb{R}. \forall s \in S. s\geq L$.

### _Def'n_. Extremum
__Supremum__ $\sup(S)\in\mathbb{R}$ is a upper bound and $\forall v. v\geq \sup(S)\land v$ is upper bound.  
__Infimum__ $\inf(S)\in\mathbb{R}$ is a lower bound and $\forall v. v\leq \inf(S)\land v$ is lower bound. 

__Proposition__ $u$ is a supremum of $S$ IFF $u$ is a upper bound and $\forall \epsilon > 0. \exists s_\epsilon \in S. u-\epsilon < s_\epsilon$

##  Least upper bound principle
$\forall S\neq \emptyset, S$ bounded above. $S$ has a supremum.  

_proof_.  Since bounded above, take $M\in\mathbb{R}$ where $\forall s \in S. M\geq s$.   
Pick $s'=s_0$,

$$s_1 \in S\Rightarrow M\geq s'\Rightarrow m_0 + 1 > s_0$$

Find lowest $a_0\in \{s_0, ..., m_0 + 1\}$ that is an upper bound for $S$.  

_Induction_ $y_n = \sum_0^n a_i / 10^i$ where $a_i=\min\{a \in \{0, 1, ..., 9\}\mid y_i \geq S\}$. Take $x_n \in S$ s.t. $a_0.a_1...a_n - 10^{-n}\leq x_n \leq y_n$

_WTS_ $L = a_0.a_1... = sup(S)$  

Upper bound property: start with any $s_0.s_1,... \in S$ either  
1. $\forall i. s_i = a_i\Rightarrow S = L$  
2. $\exists k$ be the first different digit and $s_k > a_k$
Construct $y_k^* = a_0.a_1...a_{k-1}s_k$. then $L < y_k^*\leq s_0.s_1$, while by the ordering this cannot happen. 

Subsequence Property: For each $\epsilon$, you can pick $n > 0$ s.t. $L-\epsilon \leq L - 10^{-n} \leq x_n \leq y_n < L$






### _Thrm 1._ Uniqueness of supremum

_proof_ Assume $\exists u,v$ be two supremums, $v < u$. Take $\epsilon = u -v, \forall \epsilon > 0. \exists s_\epsilon \in S \Rightarrow u - (u-v) < s_\epsilon \Rightarrow v < s_\epsilon$. 

### _Thrm 2_. 
For all bounded above set $A$ and $c\geq 0$. $\sup(cA) = c \sup(A)$  

_proof_. Let $M = \sup(A)$.  
Upper bound property: $\forall s. s\leq M \Rightarrow cs \leq cM$  
Subsequence property: Let $\epsilon \geq 0$, take $s_{\epsilon/c}$, then $cs_{\epsilon/c}\geq u - \epsilon$


