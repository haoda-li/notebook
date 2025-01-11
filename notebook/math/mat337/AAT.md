# Arzela-Ascoli Theorem

### _Def'n_. Equicontinuous
A family of function $\mathcal F \subset C(K,\mathbb R^m)$ is equicontinuous at $a\in K$  

$$\forall f \in \mathcal F. \forall \epsilon > 0. \exists \delta > 0. \|x-a\|<\delta \Rightarrow \|f(x)-f(a)\|<\epsilon$$

Then $\mathcal F$ is equicontinuous on $K$ is $\mathcal F$ is equicontinuous $\forall a\in K$. 

### _Def'n_. Uniformly equicontinuous
$\mathcal F$ is uniformly equicontinuous if 

$$\forall \epsilon > 0. \exists \delta > 0. \forall f\in\mathcal F. \forall x,y\in K. \|x-y\|<\delta \Rightarrow \|f(x)-f(y)\|<\epsilon$$

### Theorem 1
$\mathcal G := \{g_n\}_{n\geq 1}\cup \{g\}$ where $g_n \in C(K,\mathbb R^m), g_n\rightarrow^{u.c.}g$, then $\mathcal G$ is equicontinuous.

_proof_. Let $a\in K, \epsilon > 0$,  
By completeness and uniform continuous, $g$ is also continuous,  
take $\delta' > 0$ s.t. $\forall x\in K. \|x-a\|<\delta' \Rightarrow \|g(x)-g(a)\|<\epsilon/3$.  
By uniform continuous, take $N\geq 0$ s.t. $\forall n\geq N. \|g_n-g\|_\infty <\epsilon/3$.  
Then, $\forall n\geq N. \forall x, \|x-a\|<\delta'$  
$\|g_n(x)-g_n(a)\| \leq \|g_n(x)-g(x)\| + \|g(x)-g(a)\| + \|g(a)-g_n(a)\| \leq 3(\epsilon/3)=\epsilon$

Then, for each $g_k \in \{g_1,g_2,...,g_N\}$, take $\delta_k$ by continuity of each $g_k$, 
take $\delta = \min\{\delta_1,..,\delta_k, \delta'\}$  

$$\forall f \in \mathcal F. \forall \epsilon > 0. \exists \delta > 0. \|x-a\|<\delta \Rightarrow \|f(x)-f(a)\|<\epsilon$$

### Example 1
$f_n(x)=x^n, x\in [0,1], \mathcal F = \{f_n\}_{n\geq 1}$ is not equicontinuous at 1.

_proof_. Take $\epsilon =1/2$, let $\delta > 0$, wlog, $\delta < 1$.  
Take $y = 1-\delta/2<1$, then $y^n \rightarrow 0$, hence we can take $N$ s.t. $\forall n\geq N, 1-y^n > 1/2$  
Therefore, $|1-y|=\delta/2 < \delta$ but $|f_n(1)-f_n(y)|= 1-y^n > 1/2$

### Lemma 1.   Compact Implies Equicontinuous
If $\mathcal F$ compact, then $\mathcal F$ equicontinuous on $K$.  

_proof_. Suppose $\mathcal F$ is not equicontinuous,   
take $a\in K, \epsilon > 0$ s.t. $\forall n\geq 1. \exists f_n\in\mathcal F. \exists x_n\in K$ s.t. $\|x_n-a\|<1/n$ but $\|f_n(x_n) - f_n(a)\| \geq \epsilon$, hence we construct sequences $\{x_n\}, \{f_n\}$  
Then, any subset of $\{f_n\}$ cannot be equicontinuous $(i)$  
However, since $\mathcal F$ is compact, take $\{f_{n_k}\}$ converges uniformly to some $f\in\mathcal F$, and $\{f_{n_k}\}\cup \{f\}$
is equicontinuous, this contradicts with $(i)$

### Lemma 2.  Equicontinuous implies uniformly equicontinuous

_proof_. Suppose $\mathcal F$ not u.e.c.  
Take $\epsilon > 0$ s.t. $\forall n\geq 1, \exists x_n,y_n \in K. \exists f_n\in \mathcal F. \|x_n-y_n\| < 1/n \land \|f_n(x_n)-f_n(y_n)\|\geq \epsilon$ hence we construct sequence $\{x_n\}, \{y_n\}, \{f_n\}$  
Since $K$ is compact, take $x_{n_k}\rightarrow a \in K$, then $y_{n_k} = x_{n_k}-(x_{n_k}-y_{n_k})\rightarrow a$

$\mathcal F$ is equicontinous at $a\in K\Rightarrow \exists \delta > 0, \|f_n(x)-f_n(a)\|\leq \epsilon/2$ for all $\|x-a\|<\delta, f\in\mathcal F$.  
Since $x_{n_k}\rightarrow a, y_{n_k}\rightarrow a, \exists M\in \mathbb N, \forall m \geq M. \|x_{n_m}-a\|<\delta\land \|y_{n_m}-a\|<\delta$  
Therefore, $\forall m\geq M$  

\begin{align*}
\|f_{n_m}(x_{n_m})- f_{n_m}(y_{n_m})\|&\leq \|f_{n_m}(x_{n_m})- f_{n_m}(a)\| + \|f_{n_m}(a)- f_{n_m}(y_{n_m})\|\\&< 2(\epsilon/2)\\&=\epsilon
\end{align*}

contradicts with assumption


### Def'n. Totally bouded
$S\subseteq K$ is an $\epsilon$-net of $K$ if $K\subseteq \cup_{a\in S}B_\epsilon(a)$  
$K$ is totally bounded if it has a finite $\epsilon$-net $\forall \epsilon > 0$

### Lemma 3. Bounded Implies Totally Bounded
If $K\subseteq \mathbb R^m$ bounded, then totally bounded. 

_proof_. Let $\epsilon > 0$, choose $N, N \leq \min\{\epsilon, \frac{1}{\sqrt m}\}$  
$K$ bounded, hence $\exists L > 0, \forall x = (x_1,...,x_m)\in K, |x_i|\leq L, \forall i$  
Let $F = \{\frac{k_i}{2N^2}\}_{k_i\in \mathbb Z}\subseteq [-L,L]$, then $F$ is a finite $\frac{1}{2N^2}$-net for $[-L,L]$.  
Let $A = \{x_1,...,x_m\}\subseteq \mathbb R^m$ s.t. $x_i \in F, \forall i$  
Let $\tilde A = \{a\in A: B_{\epsilon/2}(x)\cap K \neq \emptyset\}$. Then, for each $x\in \tilde A$, choose $x_a \in B_{\epsilon/2}(a)\cap K$.  
Take $x = (x_1,...,x_m)\in K$ for each $i = 1,...,m, \exists a_i \in F$ s.t. $|x_i-a_i|<\frac{1}{2N^2}$  
Then, $\|x-a\| = \sqrt{\sum |x_i-a_i|^2} < \sqrt{\frac{m}{4N^4}} = \sqrt M/2N^2 \leq N/2N^2 \leq (2N)^{-1} < \epsilon/2$  
Also, $B_{\epsilon/2}(a)\cap K\neq \emptyset, a\in \tilde A$, so that $x_a$ is defined.  
Then, $\|x-x_a\|\leq \|x-a\|+\|x-x_a\|< \epsilon/2+\epsilon/2 = \epsilon$

### Lemma 4
If $K$ bounded, then $K$ contains a sequence $\{x_i\}_{i\geq 1}$ dense in $K$. Moreover, $\forall \epsilon > 0. \exists N\in\mathbb N$ s.t. $\{x_i\}_{i\leq N}$ is an $\epsilon$-net for $K$. 

_proof_. For each $k\geq i$, let $B_k$ be a finite $k^{-1}$-net.  
Take $\{x_i\}$ be the sequence which lists the $B_k$ consecutively, i.e. $x_0,...,x_{N_0}\in B_0, x_{N_0+1}, ...,x_{N_1} \in B_1,..$  
Let $x\in K$, then $\forall k\geq 1. \exists n_k$ s.t. $x_{n_k}\in B_k$ and $\|x-x_{n_k}\|< k^{-1}$, hence dense.  
Also, given $\epsilon > 0$, choose $k > \epsilon^{-1}, \{x_i\}_{i\leq N_k}$ is a $\epsilon$-net. 

## _Thrm_. Arzela-Ascoli Theorem
$\mathcal F \subseteq C(K,\mathbb R^m)$ is compact IFF closed, bounded, euicontinuous

$\Rightarrow$ _proof._ Suppose not closed, then take $\{f_n\}\subseteq \mathcal F$ s.t. $f_n\rightarrow f\not\in \mathcal F$ contradicts with compactness.  
Suppose not bounded, take $\{f_n\}\subseteq \mathcal F$ that $\|f_n\|_\infty\rightarrow\infty$ contradicts  
and Lemma 1

$\Leftarrow$ _proof_. Fix $\{f_n\} \subseteq \mathcal F$, by the Lemma 4, $\exists \{x_i\}\subseteq K$ s.t. $\forall \epsilon > 0. \exists \{x_i\}_{i\leq N}$ is a $\epsilon$-net.  
WTF $\{f_{n_k}\} \subseteq \{f_n\}$ s.t. $f_{n_k}(x_i)\rightarrow^{k}L_i, \forall 1\leq i\leq N$.  
Let $A_0=\mathbb N$, since $\{f_n(x_1)\}_{n\in A_0}$ bounded, by Bolzano-Weierstrass Theorem, take the convergent subsequence, i.e. $A_1\subseteq A_0, \lim_{n\in A_1}f_n(x_1) =L_1$.  
Inductively take $\mathcal A = A_0\supseteq A_1\supseteq A_2\supseteq ...$ be a decreasing sequence, s.t. $\lim_{n\in A_i}f_n(x_i)=L_i$  
Then, for each $k\geq 1$, let $n_k$ be the $k$th element of $A_k$, i.e. 

\begin{matrix}
&A_1 &n_1 & & \\
&A_2 & & n_2 &\\
&A_3 & & &n_3 \\
&...
\end{matrix}

Since $A_n$ is decreasing, for each $i\geq 1$, there are at most $i-1$ elements are not in $A_i$.  
In particular, this implies $\lim_k f_{n_k}(x_i) = \lim_{n\in A_i} f_n(x_i) = L_i$  
Let $g_k = f_{n_k}$, let $\epsilon > 0$, since $\mathcal F$ is equicontinuous, i.e. uniform equicontinuous. Take $\delta > 0. \|x-y\|<\delta\Rightarrow\|f(x)-f(y)\|<\epsilon/3, \forall f \in \mathcal F$  
By definition of $\{x_i\}$, take $N\in\mathcal N, \{x_1,...,x_n\}$ is a $\delta$-net.  
Since $\lim_{k\rightarrow\infty} g_k(x_i)$ exists for all $i\geq 1$.  
$\exists M\in \mathbb N$ s.t. $\forall k,l\geq M. \forall 1\leq i\leq N\Rightarrow \|g_n(x_i)-g_l(x_i)\|<\epsilon/3$  
Since $\{x_1,...,x_N\}$ is a $\delta$-net, $\exists i, \|x_i-x\|<\delta$

$$\|g_k(x)-g_l(x)\|\leq \|g_k(x)-g_k(x_i)\| + \|g_k(x_i)-g_l(x_i)\| + \|g_l(x_i)-g_l(x)\|<\epsilon$$

Since $\{g_k\}$ is uniform Cauchy, and $C(K,\mathbb R^m)$ is complete, $g_k\rightarrow g\in C(K,\mathbb R^m)$  
Since $\mathcal F$ closed, $g\in\mathcal F$, therefore, compact. 

Note that we only used closed at the very end. Therefore, If $\{f_n\}\subseteq C([a,b])$ and is bounded and equicontinuous, then it has a convergent subsequence.
