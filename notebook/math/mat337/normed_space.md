# Normed Space

## _Def'n_. Norm
Let $V$ be a vector space over $\mathbb{R}$, a norm $\|\cdot\|$ over $V$ is a function $V\rightarrow \mathbb{R}^+$ s.t. 

 - positive definite: $\|x\|\geq 0 \land \|x\| = 0 IFF x\equiv 0 \in V$  
 - homogeneous $\|ax\| = |a|\|x\|. \forall a\in \mathbb{R}$
 - triangular inequality $\|x+y\| = \|x\| + \|y\|$
 
### Example: Euclidean space over $\mathbb{R}^n$
$\|x\|_2 = \sqrt{\sum |x_k|^2}$ 
 - positive definite  
 $|x_k|^2 \geq 0 \Rightarrow \sqrt{\sum |x_k|^2} \geq 0$  
 $\|x\| = 0\Rightarrow x = 0$
 - homogeneous $\|ax\| = \sqrt{\sum |ax_k|^2} = \sqrt{|a|^2\sum |x_k|^2} = |a|\|x\|$
 - Tri-ineq  
 By Cauchy Swartz Inequality  
 $\|x+y\|^2 = \sum |x_k + y_k|^2 \leq \sum |x_k|^2 + |y_k|^2 = \sum |x_k|^2 + \sum|y_k|^2 = \|x\|^2 + \|y\|^2$

### Example: Some well-known norms
Some norms are  

- __p-norm__ $\|x\|_p:=(\sum |x_k|^p)^{p^{-1}}, p\geq 1$
- __Lp-norm__ $\|f\|_{L_p} := (\int_S f(x)^p dx)^{p^{-1}}, p\geq 1$ is a norm over $C:=$ the set of all continuous functions
- __sup-norm__ $\|f\|_\infty:= sup\{|f(x)|:x\in S\}$ is a norm over $C_b(S):=$ the set of all continuous bounded functions or over $C(S)$ if $S$ is compact. 

### Example: sup-norm  
__Claim__. sup-norm is a norm
_proof_.   

1. $|f(x)| \geq 0$, $f(x):= 0 \Rightarrow \|f\|_\infty = 0, \|f\|_\infty=0\Rightarrow |f(x)|\leq 0\Rightarrow f(x)=0$
2. $\|af\|_\infty = sup|af(S)| = |a|sup|f(S)|= |a|\|f\|_\infty$  
3. $\|f+g\|=sup(|f+g|) \leq sup(|f| + |g|) \leq sup|f| + sup|g| = \|f\| + \|g\|$

__$C^k(S):=$__ The set of all real number functions whose k-first derivative exists and continuous

Some norms are defined on $C^k$, such as $\|f\|':= \max\|f'\|_\infty; \|f\|_{C^k} = \sum \|f^{(n)}\|_\infty$

__Remark__ $C^\infty$ a.k.a. __smooth__ are normed space that obey completeness

## Topology of normed-spaces
### _Thrm 1._
The set $C:=\{f:[0,1]\rightarrow \mathbb{R}: f(0)=1\}$ is closed in $(C([0,1]), \|f\|_\infty:= sup_{x\in [0,1]}f(x))$.  

_proof_. Take a sequence $g_n \in C$ s.t. $\|g_n - g\| \rightarrow 0$. Then, consider 

\begin{align*}
|g(0) - 1| &\leq |g(0) - g_n(0)| + |g_n(0) -1|\\
&\leq |g(0)-g_n(0)| \leq \|g_n-g\|=0\\
&\Rightarrow g(0)\rightarrow 1\Rightarrow g(0) = 1\Rightarrow g\in C
\end{align*}

### _Thrm 2._
Let $A:=\{f\in [0,1]: f(x) > 0, \|f'\|_\infty < 2\}$ is open in $C^1([0,1])$ wrt $\|f\|_{\infty, C^1}:=\|f\|_\infty + \|f'\|_\infty$  

_proof_. Take any $g\in A$.  
Since $g(x) > 0$, by EVT on $[0,1]$, take $\delta_1$ s.t. $g(x)> \delta_1 > 0$.  
Since $g'(x) < 2$, by EVT on $[0,1]$, take $\delta_2$ s.t. $g'(x)< 2-\delta_2 < 2$.  
Take $\delta = \min(\delta_1, \delta_2)/ 2$.  

\begin{align*}
    \|h-g\|_\infty < \delta &\implies |h(x)-g(x)|< \delta \\
    &\implies h(x) > g(x)-\delta > \delta_1/2 > 0\\
    \|h'-g'\|_\infty < \delta &\implies |h'(x) - g'(x)| < \delta\\ 
    &\implies h'(x) < g'(x)+\delta < 2-\delta_2 + \delta_2/2 < 2
\end{align*}


### _Thrm 3._
$C_c(\mathbb{R}):=$ space of compactly supported function on reals, $C_c(\mathbb R), f\in C_c(\mathbb R)$ if $\exists M > 0$ s.t. $f(x)=0, \forall |x| > M$

__Claim__ $C_c(\mathbb R)$ is not complete wrt $\|f\|_\infty$

_proof_. WTF a Cauchy sequence $f_n \in C_c(\mathbb R)$ s.t. $f_m \rightarrow f\not\in C_c(\mathbb R)$.  
Take $f_n(x) = \frac{1-(x/n)^2}{1+x^2}\mathbb I (|x|\leq n)$ and we can show that $f_n$ is Cauchy wrt $\|\cdot\|_\infty$  

wlog, assume $n > m$,  
Consider 

$$\|f_n - f_m\| = \sup_{x\in [-n,n]} |\frac{1-(x/n)^2}{1+x^2} - f_m(x)|$$

Suppose that $x\in [-m,m]$,

$$\sup_{x\in [-n,n]} |\frac{1-(x/n)^2}{1+x^2} - \frac{1-(x/m)^2}{1+x^2}| = |\frac{x^2}{1+x^2}||n^{-2} - m^{-2}| \rightarrow |1||0|=0$$

Suppose that $x\in [-n, -m)\cup (m, n]$,

$$\sup_{x\in [-n,n]} |\frac{1-(x/n)^2}{1+x^2}|\leq |\frac{1}{1+x^2}|\leq |\frac{1}{1+m^2}|\rightarrow 0$$

Therefore, take $N = \epsilon^{1/2}$ we can prove Cauchy. 

However, $f_n(x)=\frac{1-(x/n)^2}{1+x^2}\rightarrow \frac{1}{1+x^2}\rightarrow 0$ is not compactly supported

Therefore, only compact in metric space $\rightarrow$ closed and bounded but not the converse. 
