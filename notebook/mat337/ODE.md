# Fixed Point and ODE

## Discrete Dynamical Systems
__Discrete Dynamical Systems__ Let $X\subseteq (V,\|\cdot\|), T:X\rightarrow X$ continuous. $(X,T)$ is a discrete dynamical system  
__Forward orbit__ $\forall x\in X$, forward orbit of x is the sequence $O(x):=\{T^n_x\}_{n\geq 0}$, $T^n_x=T(T...T(x))$

__Fixed Point__ $x^*$ is   
__attractive fixed point (sink)__ if $\exists (a,b)\ni x^*$ s.t. $\forall x \in (a,b). T^N_x\rightarrow x^*$   
__repelling fixed point (source)__ if $\forall x\neq x^*$, $O(x)$ leaves $(a,b)$

__Contraction__ $X\subseteq (V,\|\cdot\|),T:X\rightarrow X$ is a contraction on $X$ if 

$$\exists c < 1. \forall x,y\in X. \|Tx-Ty\|\leq c\|x-y\|$$

i.e. $T$ is $c$-Lipschitz $c<1$

## Banach Contraction Principle
Let $X\subseteq (V,\|\cdot\|)$ be a closed subset of a complete normed vector space,  
IF $T:X\rightarrow X$ is a contraction on $X$  
THEN   
(i) $T$ has unique fixed point $x^*$  
(ii) $\forall x\in X. x^* = \lim_{n\rightarrow\infty} T^nx$  
(iii) $\|T^nx-x^*\|\leq c^n\|x-x^*\|\leq \frac{c^n}{1-c}\|x-Tx\|, c$ is the Lipschitz constant 

_proof_. Let $x_0\in X$, recursively define $x_{n+1} = Tx_n$, hence form a sequence $\{x_n\}$.  
Then, we can show that $\{x_n\}$ is Cauchy by observing

\begin{align*}
\|x_{n+m} - x_n\| &\leq \sum_0^{m-1}\|x_{n+i-1}-x_{n+i}\| &\text{triangle inequality} \\
&= \sum_{i=0}^{m-1} \|Tx_{n+i}-Tx_{n+i-1}\| \\
&\leq \sum_{i=0}^{m-1} c\|x_{n+i}-x_{n+i-1}\|&\text{by contraction}\\
&\leq \sum^{m-1}c^{n+i}\|x_1-x_0\| &\text{recursively repeat such process} \\
&<\sum^\infty c^{n+i}\|x_1-x_0\| \\
&= \frac{c^n\|x_1-x_0\|}{1-c}
\end{align*}

Since $c^n\rightarrow 0$, we can choose $N$ sufficiently large to have $\|x_{n+m}-x_n\|\rightarrow 0$  

_Existence_ By completeness of the normed space, Cauchy implies convergent to some $x^*\in V$, by $X$ closed, $x^*\in X$. By Lipshitz, hence continuous of $T$, $Tx^* = T(\lim x_n) = \lim Tx_n = x^*\Rightarrow x^*$ is the fixed point.  

_Uniqueness_ Suppose $y\in X$ is also fixed point, $\|x^*-y\| = \|Tx^* - Ty\| \leq c\|x^*-y\|\Rightarrow \|x^*-y\| = 0\Rightarrow x^*=y$

$$\|T^Nx-x^*\| = \|T^n x-T^nx^*\|\leq c^n\|x-x^*\|= c^n lim \|x-x_m\|\leq \frac{c^n}{1-c}\|Tx-x\|$$

## Solving ODE


__Example__ given the initial value problem $f'(x)=1+x-f(x), |x|\leq 1/2$ and $f(0)=1$

First convert to the integral problem  

$$f(x) = 1+ \int_0^x 1 + t - f(t)dt = 1+ x + \frac{x^2}{2} - \int_0^x f(t)dt, f\in C[-1/2,1/2]$$

Define $T$ on $C[-1/2,1/2]$ and $Tf = f$ and the solution of the integral equation is a fixed point of $T$
Then, to show $T$ is a contraction 

\begin{align*}
|Tf(x)-Tg(x) &= |\int_0^x f(t)-g(t)dt| \\
&\leq \big|\int_0^x |f(t)-g(t)|dt\big| &\text{tri. ineq.}\\
&\leq \int_0^x \|f-g\|dt \\
&=\|f-g\|_\infty \int_0^{|x|}dt\\
&\leq \frac{\|f-g\|_\infty}{2}
\end{align*}

Thus, by Banach Contraction Principle, choose $f_0 := 1\in C[-1/2,1/2]$, then 

\begin{align*}
f_1(x) &= Tf_0(x) = 1+x+\frac{x^2}{2} - \int_0^x dt = 1+\frac{x^2}{2} \\
f_2(x) &= Tf_1(x) = 1+x+\frac{x^2}{2} - \int_0^x 1+\frac{x^2}{2} dt = 1 + \frac{x^2}{2} - \frac{x^3}{6}\\
&...\\
f_n(x) &= \sum \frac{(-x)^{n+1}}{(n+1)!}
\end{align*}

Since $|x|\leq 1/2$, using M-test, this power series is uniform convergence, and note that $f_n(x):=e^{-x} + x$

### _Thrm_.  Existence of ODE
If $\Phi:[a,b]\times \mathbb R^n\rightarrow \mathbb R^n$ is Lipschitz on the second coordinate $y\in\mathbb R^n$.  
Then $\exists F_*\in C([a,b],\mathbb R^n)$ s.t. $F_*=TF_*=\Gamma + \int_a^x \Phi(t,F_*(t))dt$  

_proof_. (Picard iteration) 

Recursively define $F_0(x)=\Gamma, F_{k+1}(x)=TF_k = \Gamma + \int_a^x \Phi(t, F_k(t))dt$

Consider $F_{k+1}-F_k$, let $M = \|\Phi(t,\Gamma)\|_\infty$, by EVT, since $[a,b]$ compact, $M$ is the maximum.  
Then for any $x\in [a,b]$. $\|F_1(x) - F_0(x)\|  = \int_a^x \Phi(t,\Gamma)dt\leq M(x-a)$  

\begin{align*}
\|F_{k+1}(x) - F_k(x)\| &= \int_a^x \Phi(t, F_{k}(t))-\Phi(t, F_{k-1}(t))dt \\
&\leq L\int_a^x\|F_k - F_{k-1}\|_\infty dt &L \text{ is the Lipschitz constant} \\
&\leq L \int_a^x \frac{L^{k-1}M(x-a)^k}{k!} &\text{induction hypothesis}\\
&= L^k \frac{M(x-a)^{k+1}}{(k+1)!}
\end{align*}

Then, for $n\geq N$, for some large $N$

\begin{align*}
\|F_n - F_0\| &\leq \sum^{n-1} \|F_{k+1}-F_k\| \\
&\leq \sum^{n-1} \frac{L^k M(x-a)^{k+1}}{(k+1)!} \\
&\leq \frac{M}{L} \sum^\infty \frac{(L(x-a))^{k+1}}{(k+1)!}\\
&\leq \frac{M}{L} \sum^\infty \frac{(L(b-a))^{k+1}}{(k+1)!} < \infty
\end{align*}

Since the infinite sum is finite, the series is Cauchy. so that $F_n\rightarrow^{u.c.}F_*\in C([a,b], \mathbb R^n)$ by compactness and closeness. 

Therefore, $TF_* = T\lim F_n = \lim TF_n = F_*$ using continuity


__Uniqueness__ Suppose exists $G_*$, then 

\begin{align*}
TF_* - G_* &= TTF_* - TG_* &\text{by fixed point assumption} \\
&= T^kF_* - T^kG_* \\
&\leq \frac{(L(x-a))^{k+1}M}{(k+1)!L} \\
&\sim 0 &\text{Sterling's formula}
\end{align*}

### Example 
$f'(x)=f(x), f(0)=1, x\in [0,1]$

_proof_. Let $F_0(x)=1, F_1(x) = 1 + \int_0^x F_0(t)dt = 1 + \int_0^x dt = 1 + x$  
Assume $F_n(x) = \sum_0^k \frac{x^m}{m!}$, then 

$$F_{k+1}(x) = 1 + \int_0^x F_n(t)dt = 1 + \int_0^x \sum_0^k \frac{x^m}{m!} = \sum_0^{k+1}\frac{x^m}{m!}$$  

Therefore by induction, $F_*(x) = \lim_nF_n(x) = \sum^\infty x^m/m! = e^x$
