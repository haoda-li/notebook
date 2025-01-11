# Introduction to Probability

## Frequentism vs. Bayesian

Frequentists' view point of probability
> The probability that some specific outcome of a process will be obtained can be interpreted
to mean the relative frequency with which that outcome would be obtained if the process were
repeated a large number of times under similar conditions.

Bayesian
> Each person has beliefs about random procedure which presumed to be different. It is inferential
point of view

The difference is that in frequentism, samples are coming from one unknown true distribution; in Bayesian, all unknowns must have probability structure. 

## Sample Spaces, Experiments, and Events

An __experiment__ is any process, real or hypothetical, in which the possible outcomes can be
identified ahead of time. 
The collection of all possible outcomes of an experiment is called the __sample space__
of the experiment which is often denoted by S.   
An __event__ is a well-defined subset of sample space. 

For example, an experiment can be "tossing a fair coin 3 time". Then, the sample space $S = \{TTT, TTH, THT, THH, HTT, HTH, HHT, HHH\}$ is the collection of all outcomes, and $E = \{THH, HTH, HHT\} \subseteq S$ is an event that two heads are tossed. 

## Probability

Probability is a function $P: \mathbb P(S)\rightarrow \mathbb R$ such that 

1. Non-negativity $\forall E\subseteq S. P(E)\geq 0$
2. $P(S) = 1$
3. Countable additivity $\forall E_1, E_2 \subseteq S. E_1\cap E_2 = \emptyset\Rightarrow P(\bigcup^\infty E_i) = \sum^\infty P(E_i)$. 

__Theorem 1__ $P(\emptyset) = 0$.   
_proof_. Let $E_1=\emptyset=E_2 = E_3 = ...$, so that they are disjoint. 

$$P(\emptyset) = P(\bigcup^\infty E_i) = \sum^\infty P(E_i) \geq P(E_1)+P(E_2) = 2P(\emptyset)$$

so that $P(\emptyset) \leq 0$, using non-negativity, $P(\emptyset) = 0$

__Theorem 2 (Finite additivity)__ For any disjoint events $E_1,...,E_n$, $P(\bigcup^n E_i) = \sum^n P(E_i)$  
_proof_. Define $E_i = \emptyset$ for $i>n$. Then by countable additivity.

__Theorem 3__ $\forall A\subseteq S. P(A^c) = 1-P(A)$  
_proof_. By finite additivity, $P(S) = P(A^c\cup A) = P(A^c)+P(A) = 1$. 

__Theorem 4__ $\forall A, B \subseteq S. A\subseteq B \Rightarrow P(A)\leq P(B)$.  
_proof_. By non-negativity and finite additivity. $P(B)=P(A+(B-A))=P(A)+P(B-A)\geq P(A)$. 

__Theorem 5__ $\forall A\subseteq S. 0\leq P(A)\leq 1$.  
_proof_. $A\subseteq S\Rightarrow P(A)\leq P(S) = 1$.

__Theorem 6__ $P(A-B)=P(A)-P(A\cap B)$.  
_proof_. $P(A) = P((A-B)\cup (A\cap B)) = P(A-B)+P(A\cap B)$.

__Theorem 7__ $P(A\cup B) = P(A) + P(B) - P(A\cap B)$. 
_proof_. $P(A\cup B) = P(A\cup B-A) = P(A) + P(B-A) = P(A)+P(B)-P(A\cap B)$

__Theorem 8 (sub-additivity)__ For $E_1,...,E_n$. $P(\bigcup^n E_i) \leq \sum^n P(E_i)$.  
_proof_. Define $A_1 = E_1, A_i = E_i - \cup^{i-1}_j E_j$ so that $\cup^n A_i = \cup^n E_i$ and $A_i$ are mutually disjoint. and $A_i\subset E_i$. Therefore, 

$$P(\bigcup^n E_i) = P(\bigcup^n A_i) = \sum^n P(A_i)\leq \sum^n P(E_i)$$

### Continuity of Probability
For a sequence of events $A_1, A_2,...$   
__Continuity from below__ If $A_1,A_2$ is increasing to $A$ ($A_1\subset A_2... , \bigcup A_i = A$) then $\lim_{n\rightarrow\infty}P(A_n) = P(A)$.  
_proof_. $A_j\subset A_{j+1}$ so that $A_j\cap A_{j+1} = A_j$. Therefore, define $C_{j+1} = A_{j+1}\cap A_j^c$ and $C_1 = A_1$ so that $C_j$ is the part of $A_{j+1}$ that is not in $A_j$ and $C_j$ are disjoint. Also, $C_j$ is increasing to $A$ by its construction. Therefore, we can prove by countable additivity. 

__Continuity from above__ If $A_1,A_2$ is decreasing to $A$ ($A_1\supset A_2... , \bigcap A_i = A$) then $\lim_{n\rightarrow\infty}P(A_n) = P(A)$.  
_proof_. Note that $A_1 - A_n$ is increasing to $A_1-A$. so that 

$$\lim_{n\rightarrow\infty} P(A_1-A_n) = P(A_1-A)$$

note that $P(A_1-A_n) = P(A_1)-P(A_n)$ since $A_n\subset A_1$, similarly $P(A_1-A) = P(A_1)-P(A)$

$$\lim_{n\rightarrow\infty} P(A_1)-P(A_n) = P(A_1)-P(A)\Rightarrow \lim_{n\rightarrow\infty} P(A_n) = P(A)$$

## Combinatorics
__Permutation__ When there are $n$ elements, the number of events pulling $k$ elements out of $n$ elements is called
a permutation of $n$ elements taken $k$ at a time and denoted by $nPk$.

$$nPk = \frac{n!}{(n-k)!}$$

__Combination__ The number of combinations of n elements taken k at a time is denoted by $nCk$ or $n\choose k$

$${n\choose k} = \frac{n!}{k!(n-k)!}$$

__Binomial coefficients__ 

$$(x+y)^n = \sum_{k=0}^n {n\choose k} x^k y^{n-k}$$

Note that the coefficient is determined by the number of combinations choosing
$k$ $x$-terms among $n$ $(x + y)$ terms.  
This result can be expanded to infinity as Newton's generalized binomial theorem.

__Multinomial Coefficients__ 

$$(x_1+...+x_k)^n = \sum {n\choose n_1,...,n_k} x_1^{n_1}\cdot...\cdot x_k^{n_k}$$

where the coefficient

$${n\choose n_1,...,n_k} = \frac{n!}{n_1!\cdot...\cdot n_k!}$$

### Inclusion Exclusion Formula

\begin{align*}
P(\bigcup^n A_i) = 
&\sum^n P(A_i) \\
&+(-1)\sum_{i<j} P(A_i\cap A_j) \\
&+ \sum_{i<j<k} P(A_i\cap A_j\cap A_k) \\
&+ \cdots \\
& + (-1)^{n-1}P(A_1\cap ... \cap A_n)
\end{align*}

_proof_ Using induction on the number of events $n$. 

## Conditional Probability
The __conditional probability__ of an event $A$ given $B$ is defined by $P(A\mid B) = \frac{P(A\cap B)}{P(B)}$, if $P(B) > 0$. 

### Independent Events
$A$ and $B$ are __independent__ if $P(A\cap B) = P(A)P(B)$.   
A collection of events $\{A_i\}$ are __(mutually) independent__ if $P(\bigcap A_i) = \prod P(A_i)$ for $A_i\neq \emptyset$,  
are pairwise independent if $\forall A_i\neq A_j$, $A_i, A_j$ are independent. 

__Theorem__ $A\perp B$ IFF $A\perp B^c$.   
_proof_. 

$\Rightarrow$

\begin{align*}
P(A\cap B^c) &= P(A-B) = P(A) - P(A\cap B) \\&= P(A)-P(A)P(B)=P(A)(1-P(B))=P(A)P(B^c)
\end{align*}

$\Leftarrow$

\begin{align*}
P(A\cap B) &= P(A)-P(A\cap B^c) = P(A) - P(A)P(B^c) \\&= P(A)(1-(1-P(B))) = P(A)P(B)
\end{align*}

$A$ and $B$ are __conditional independent__ given $C$ if 

$$P(A\cap B\mid C) = P(A\mid C)P(B\mid C)$$

### Bayes Theorem
__Theorem (Law of total probability)__ Let $B_1,...,B_k$ be a partition of the sample space $S$. For any event $A$ 

$$P(A) = \sum^k {P(B_i)}{P(A\mid B_i)}$$

_proof_. Note that 

$$A = A\cap S = A \cap \bigcup^k B_i = \bigcup^k A\cap B_i$$

are $A\cap B_i$ are disjoint since $B_i$'s are disjoint, so that finite additivity and conditional probability gives

$$P(A) = P(\bigcup^k A\cap B_i) = \sum^k P(A\cap B_i) = \sum^k {P(B_i)}{P(A\mid B_i)}$$

__Theorem (Bayes Theorem)__ $P(B\mid A) = \frac{P(A\mid B)P(B)}{P(A\mid B)P(B) + P(A\mid B^c)P(B^c)}$.  
_proof_. Direct from law of total probability.

Therefore, Bayes Theorem says that  
_Posterior probability can be expressed with respect to prior probabilities_
