# MCT and BWT

## Monotone Convergence Theorem

Monotone increasing and bounded above $\Rightarrow$ converges to supremum. 

### _Def'n._ Monotonic
A sequence $(a_n)$ is (strictly) monotone increasing if

$$a_n\leq a_{n+1}(a_n<a_{n+1}), \forall n\geq 1$$

### _Thrm 1._

$$\lim_{n\rightarrow\infty}a_n = \inf(a_n)$$

_proof_. We'd like to show that 

$$\forall \epsilon. \exists N. \forall n \geq N. |a_n - L| \leq \epsilon$$

Let $L=\inf(a_n)$. Let $\epsilon > 0$, take $a_N \in (a_n)$ s.t. $L-\epsilon < a_N$.  
Then $L-\epsilon < a_N \leq a_n \leq L$ for all $n\geq N. \Rightarrow \forall n\geq N. |a_n-L|<\epsilon$

### _Corollary 2._ 
Consider closed, non-empty nested intervals $I_n\supseteq I_{n+1}\supseteq I_{n+2}...$, then then $\cap^\infty_n I_n\neq \emptyset$

_proof._ Let $I_n=[a_n,b_n]$, then we have two monotone sequence $(a_n)$ is increasing, $(b_n)$ is decreasing. Then, $\forall k\geq 1. a_k \leq \lim_\infty a_n\leq \lim_\infty b_n \leq b_k$

Then, we can show $\Rightarrow [lim_\infty a_n, \lim_\infty b_n]=[\sup(a_n),\inf(b_n)]\subseteq \cap_{n\geq 1} I_n$

### Example 1
(D&D 2.6.B) Let $a_1 = 0, a_{n+1}=\sqrt{5 + a_n}$, find whether it's convergent and if convergent what's the limit. 

__Monotone__  

\begin{align*}
a_2 &= \sqrt 5 > 0 = a_1\\
a_{n+1} &= \sqrt{5 + a_n} > \sqrt{5 + a_{n-1}}=a_n
\end{align*}

__Bounded above__   
$a^2_{n+1} =5 + a_n < 5 + a_{n+1}$. Let $x = a_{n+1}\Rightarrow x^2 < 5 + x\Rightarrow x^2 -x -5 < 0$.  
$x\in [\frac{1-\sqrt{21}}{2}, \frac{1+\sqrt{21}}{2}]\Rightarrow a_{n+1}=x$ is bounded above.  

In fact, $L = \lim\sqrt{5 + a_{n-1}}=\sqrt{5+L} \Rightarrow L^2 = L - 5$. solve and take $L > 0$ since monotone increasing, then $L=\frac{1+\sqrt{21}}{2}$

### Example 2 
(D&D 2.6.I) Let $(a_n)$ be bounded, define $\lim\sup a_n = b_n = \sup\{a_k: k\geq n\}$ for $n\geq 1$. Prove that $(b_n)$ converges. 

__Monotone__ $b_n\leq b_{n+1}$  
since $b_n = \max(a_n, \sup\{a_k: k\geq n+1\})=\max(a_n,b_{n+1})\geq b_{n+1}$

__Bounded below__ $\forall n \geq 1. a_n\geq M, b_n = \sup(a_k:k\geq n )\geq M$

$$\exists L<\infty.  \lim b_n = \lim_{n\rightarrow\infty}\sup_{k\geq n} a_nL$$

__Remark__ $L_u = \lim\sup a_k \geq \lim\inf a_k = L_l$, if $L_u = L_l = L\Rightarrow \lim a_k = L$


## Bolzano-Weierstrass Theorem 
Every bounded sequence of real numbers has a convergent subsequence

### _Def'n_ Subsequence
A subsequence of $(a_n)$ is a sequence $(a_{n_k})$ where $n_1<n_2<...$

_proof._ Let $(a_n)\subseteq [-M, M]$.  
Construct the subsequence by 
- picking $I_1\subset [-M,M]$ that contains infinitely many $a_n$ s.t. $|I_1|\leq M/2$
- ...
- picking $I_n\subset I_{n-1}$ that contains infinitely many $a_n$ s.t. $|I_n| \leq |I_{n-1}|/2 \leq M/2^n$. 

By Nested interval lemma, $\cap_{n\geq 1}I_n \neq\emptyset$, take $L\in \cap I_n$. 

Pick $a_n\in I_n, \forall n \geq 1$ Since $L\in I_n\Rightarrow |a_n - L|\leq |I_n|<M/2^n$. 

Then $\forall \epsilon > 0$, take $N_\epsilon$ s.t. $\epsilon > M/2^{N_\epsilon} > |a_{N_\epsilon} - L|$  
but $|a_n - L | \leq |I_n|\leq |I_{N_\epsilon}| / 2^{n-N_\epsilon}, \forall n\geq N_\epsilon$

$$\epsilon > M / 2^{N_\epsilon} > |a_n - L|. \forall n\geq N_\epsilon\Rightarrow \lim{a_n} = L$$
