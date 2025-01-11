# Topology of real number space

## Def'n. Cauchy sequence 

$$\forall \epsilon > 0. \exists N >0 .\forall m,n \geq N. |a_m - a_n| \leq \epsilon$$

Any convergent sequence is Cauchy  
Every Cauchy sequence is bounded

#### Def'n. Metric space
a space X plus a notion of distance

#### Def'n. Completeness
a metric space $S$ is complete if Cauchy sequence in $S$ converges to some point in that space.

### Claim (D&D 2.8.5) 
every Cauchy sequence of reals converges. i.e. $\mathbb{R}$ is complete.  

_proof_. Let $(x_n)\in\mathbb{R}$ be Cauchy and $x_n\rightarrow L$. WTS $L\in\mathbb{R}$  

We'll use diagonalization argument: For fixed $x_n\in\mathbb{R}, \exists (r_{n,k})$ be rational Cauchy s.t. $\lim_{k\rightarrow\infty}r_{n,k}=x_n$. 
Let $a_n$ be s.t. $|a_n - x_n|\leq 1/n$ by choosing a candidate for each $n$. 

$$\implies |a_n-L|\leq |a_n-x_n| + |x_n-L|\leq 1/n + \epsilon_n \implies \lim_{n\rightarrow\infty} a_n = L \in\mathbb{R}$$

## _Thrm_. Mean Value Theorem

$$\exists \xi\in(x,y).|f(x)-f(y)| = |f'(\xi)||x-y| $$

### Example
$a_1 = 1, a_{n+1} = cos(a_n)$ show that $a_n\rightarrow L$.   
_proof._ WTS $(a_n)$ is Cauchy. Take some  $\xi\in(a_n,a_{n-1})$, then

\begin{align*}
|\cos(a_{n - 1})-\cos(a_n)|&\leq |\sin(\xi)||a_{n-1}-a_n|\\ 
\implies |a_n - a_{n+1}|&\leq r|a_{n-1}-a_n|\\
&\leq r^n|a_2 - a_1| 
\end{align*}

If $r < 1$, then $\lim|a_n - a_{n-1}|=0$

## Close and Open

__Limit point__ For a sequence $(x_n)\in\mathbb{R}$, its limit point $x\in\mathbb{R}$ satisfies $\lim_{n\rightarrow\infty}x_n = x$.  

__Closed__ if it contains all its limit points

__Example__ $\mathbb{R}^n$ is closed because $\mathbb{R}$ is complete 

__Claim__ Finite union of closed sets is closed  

__Open__ if $\forall x\in U.\exists r_{x,v}>0. B_r(x)\subseteq U$

$U$ open, $f$ continuous $\Rightarrow f^{-1}(U)$ is open

__Claim__ (D&D 4.3.8) $U$ open IFF $\mathbb{R}-U\rightarrow U^c$ is closed 


### Theorem
finite intersection of open sets is open.  

_proof_. $(\cap^M U_i)^{c^c} = (\cup^M U_i^c)^c$  
Since $U_i$ open, $U_i^c$ closed, $\cup^M U_i^c$ closed. 

## Compactness

__Compact Defn 1__ $C\subseteq\mathbb{R}$ is compact if all sequence $\{x_n\}\subseteq C$ has a converging subsequence $\{x_{n_k}\}\subseteq C$  
$\forall \{x_n\}\subseteq C. \exists \{x_{n_k}\}\subseteq \{x_n\}. x_{n_k}\rightarrow x\in C$

__Compact Defn 2__ A set $C$ is compact if every open cover of $C$ has a finite subcover that covers $C$. 

__Open cover__ A collection of open balls $\{U_a\}_{a\geq 1}$ is an open cover if $c\subseteq \cup^\infty U_a$

__Claim__  $[a,b]\subseteq \mathbb{R}$ is compact.  

_proof_. By Bolzano Weierstrass Theorem. every bounded sequence has a convergent subsequence. Since $[a,b]$ closed, such limit falls in $[a,b]$. 

__Continuous mapping theorem__ For continous $f, x_n\rightarrow x\Rightarrow f(x_n)\rightarrow f(x)$. 

__Corollary__ $f:U\rightarrow V$, if $C\subseteq U$ is compact, then $f(C)$ is also compact.  

## _Thrm_. Heine-Borel Theorem
$C\subseteq \mathbb{R}$ is compact IFF closed and bounded. 

__Claim 1__ compact $\Rightarrow$ bounded

_proof_. Suppose compact but not bounded. Then take $\{x_n\}\subset C$, wlop, $x_n\rightarrow \infty$. Then, we can take a monotone increasing subsequence $y_n$ of $x_n$. Then by compactness, take $y_{n_k}\rightarrow y\in C$. But a monotone divergent sequence cannot have convergent subsequence. 

__Claim 2__ compact $\Rightarrow$ closed  

_proof_. Let $\{x_n\}\subseteq C. x_n\rightarrow x$, WTS $x\in C$.  
By compactness, take $\{x_{n_k}\}\rightarrow L$. We can show that 
$|x-L| = |x - x_{n_k} + x_{n_k} - L| \leq |x - x_{n_k}| + |x_{n_k} - L| \rightarrow 0$

__Claim 3__ closed & bounded $\Rightarrow$ compact  

_proof_. Let $\{x_n\}\subseteq C$. Since bounded, by BWT, take $\{x_{n_k}\}$ where $x_{n_k}\rightarrow L\in\mathbb{R}$.  
Since $C$ closed, its limit point is in $C$. 

## _Thrm_. Extreme value theorem

If a function $f:K\rightarrow R$ is continous and $K$ is compact, then $f(K)$ is compact and $\exists a,b\in K. \forall k\in K. f(a)\leq f(k)\leq f(b)$

__Part1__ $f(K)$ compact  
_proof_. Let $(y_k)\subseteq f(K)$, take $(x_k)\subseteq K s.t. f(x_k)=y_k$. By compactness of $K$, take $(x_{k_n})\subseteq (x_k)$ and $x_k\rightarrow x\in K.$ Then by continuous mapping theorem, $f(x_{k_n})\rightarrow f(x)\in f(K)$

__Part2__ $f(K)$ has max and min  
_proof_. By compactness and least bound principle, take $M,m$ be the supremum and infimum of $f(X)$. WTS thats contained in $f(K)$.  
Construct a sequence $(d_n)\subset K$ s.t. $M-\frac{1}{n}\leq f(d_n)\leq M$ (since M is the supremum we can do such construction).  
Since $K$ is compact, by Bolz. Weis. Theorem, take $(d_{n_k})\subseteq (d_n), d_{n_k}\rightarrow d$ is convergent. 

Then by squeeze theorem, $M-\frac{1}{n}\leq f(d_{n_k})\leq M$ is squeezed by $M$, $\lim f(d_{n_k}) = f(\lim f(d_{n_k})) = M$. By compactness of $f(K), M\in f(K)$.

__Example__ $f$ continuous on $[a,b]\subseteq \mathbb{R}$ has no local extremum, then $f$ is monotone.  
__local maxmimum/minimum__ $x_0$ is local max/min if $\exists \epsilon > 0. \forall x\in [x_0-\epsilon, x_0+\epsilon], f(x)\leq | \geq f(x_0)$.



## Uniform Continuilty 
$f:S\rightarrow R$ is uniformly continuous if $\forall \epsilon > 0. \exists \delta > 0. \forall x,y. |x-y|\leq \delta \Rightarrow |f(x)-f(y)|<\epsilon$

__Sequential criterion__ A function $f:S\rightarrow R$ is not uniform continuous if $\exists (x_n), (y_n)\subseteq S$ s.t. $|x_n - y_n|\rightarrow 0$ but $\exists \epsilon_0 >0 s.t. |f(x_n)-f(y_n)|\geq \epsilon_0 > 0$

_proof_. negation of the uniform continuous definition 

__Example__ $f(x):=x^2$  
Let $x_n = n + n^{-1}, y_n = n$. Then $|x_n-y_n|= n^{-1}\rightarrow 0$, but $|(n+n^{-1})^2 - n^2| = |-2|+n^{-2}\rightarrow 2 > 0$

__$\alpha$-Holder__ $f:S\rightarrow R$ is a-Holder if $|f(x)-f(y)|\leq c |x-y|^\alpha, \alpha\in[0,1]. \forall x,y\in S$.  

__Example__ $f(x)=x^p, p\in(0,1)$ is call p-Holder and is uniform continuous.  

_proof_. Let $\epsilon > 0$, take $\delta = (\epsilon / c)^{a^{-1}} < 1$ because $\alpha \leq 1$  
$|f(x)-f(y)|\leq c|x-y|^\alpha \leq c\delta^\alpha =\epsilon$

When $\alpha = 1, i.e. |f(x)-f(y)|\leq c|x-y|$, they are called Lipschitz.

__Example__ Any differentiable functions are Lipschitz (bounded derivative)  

_proof_. by MVT, $|f(x)-f(y)| = |f'(c)||x-y|\leq B|x-y|$

## _Thrm_. Heine-Cantar Theorem 
if $K$ compact, and $f:K\rightarrow R$ is continuous, then $f$ is also uniform continuous.  

_proof_. Suppose $f$ is not uniform continuous  
Take $(x_n), (y_n)$ and for $\epsilon > 0$ s.t. $|x_n - y_n|\leq 1/n$ but $|f(x_n)-f(y_n)|\geq \epsilon > 0$. By $K$ compact, take $(x_{n_k})\rightarrow x\in K$。  
However, $|y_{n_k}-x|\leq |y_{n_k}-x_{n_k}| + |x_{n_k}-x| \leq n_k^{-1} + \epsilon_k \rightarrow 0$ i.e. $y_{n_k}\rightarrow x$  
$\forall n_k > N_{\epsilon_0/4}|f(x_n)-f(y_n)|\leq |f(x_n)-f(x)| + |f(x)-f(y)| \leq \epsilon_0/2$ causes contradiction

## _Thrm_. Intermediate value theorem
If $f:[a,b]\rightarrow \mathbb{R}$ is continuous and $z\in\mathbb{R}$ satisfy $f(a)\leq z\leq f(b)$, then $\exists c \in [a,b]$ s.t. $f(c)=z$. 

_proof_. Let $A = \{x\in[a,b]: f(x) < z\}$, then $A$ is upper bounded. Then, take $c = sup(A)$.

$\forall \epsilon_n = n^{-1}$, take $a_n \in A$ s.t. $c - n^{-1} \leq a_n \leq c$ and  $f(a_n)\leq z$ so $f(c) = \lim_{n\rightarrow \infty} f(a_n)\leq z$ (1).  
Explicitly assume $c < b$ (otherwise we've done), then take $\exists b_n$ s.t. $c < b_n \leq b, \lim_\infty b_n =c$.  
Since $z$ is upper bound for $A, b_n\not\in A, f(b_n)\leq z$ (2). 
By (1)(2) $f(c)=z$

## Connected 
__Disconnected__ $A\subseteq \mathbb{R}$ is disconnected $U,V$ open cover s.t. $A = U\sqcup V$  
__Connected__ $A$ is connected if $\forall U,V. A\neq U\sqcup V$  
__Path connected__ of $\forall a,b \in A. \exists \gamma:[0,1]\rightarrow A$ be a continuous path i.e. $\gamma(0)=a, \gamma(1)=b, \gamma([0,1])\subseteq A$  
