# Inner Product Space and Fourier Series

## Inner Products Spaces

An inner product $\langle \cdot, \cdot\rangle :V\rightarrow \mathbb R$ is a function that satisfies 

- __positive definite__ $\langle x,x\rangle > 0$ and $\langle x,x\rangle =0$ IFF $x\equiv0$
- __symmetry__ $\langle x,y\rangle =\langle y,x\rangle$
- __bilinear__ $\langle ax+cy,z\rangle =a\langle x,z\rangle +c\langle y,z\rangle$

### Example 1
On $\mathbb R^n, x\cdot y = \sum_1^n x_i y_i$  

- $x\cdot x =\sum^n x_i^2 \geq 0$
- $x\cdot y = \sum x_i y_i = \sum y_i x_i = y\cdot x$
- $(ax+cy)\cdot z = \sum (ax_i + cy_i) z_i = a\sum x_i z_i + c\sum y_i z_i = ax\cdot z + cy\cdot z$ 

### Example 2
Let $A_{n\times n}$ be a positive definite symmetric matrix, i.e. all its eigenvalues are strictly positive. Then $\langle x\cdot y\rangle _A = x A y^T$ is an inner product on $\mathbb R^n$

Note that such $A$ can be diagonalized into $A=PDP^T$

 - $\langle x,x\rangle _A = xAx^T = xPDPx^T = vDv^T = \sum v_k^2 \lambda_k \rangle 0$ (since $A$ is definite, $\lambda_k \rangle 0$)  
 - $\langle x,x\rangle =0$ IFF $\sum v_k^2 \lambda_k = 0\Rightarrow v_k = 0 \Rightarrow xP = 0$, since $P$ is orthogonal, $x=0$

## _Thrm 1_. Cauchy Schwarz inequality 
For $x,y\in (V,\langle ,\rangle ), |\langle x,y\rangle |\leq \langle x,x\rangle ^2\langle y,y\rangle ^2$  

_proof_. By positive definite, for $t\in\mathbb R$, $\langle x-ty, x-ty\rangle  \geq 0$.  
Take $t = \frac{\langle x,y\rangle }{y,y}$,  

\begin{align*}
\langle x,x\rangle  - 2t |\langle x,y\rangle | + t^2 \langle y,y\rangle &= \langle x,x\rangle  - 2\frac{\langle x,y\rangle ^2}{\langle y,y\rangle} + \frac{\langle x,y\rangle ^2}{\langle y,y\rangle }\\
=&\langle x,x\rangle  - \frac{\langle x,y\rangle ^2}{\langle x,y\rangle } \geq 0\\
\implies &\langle x,y\rangle ^2 \leq \langle x,x\rangle \langle y,y\rangle\\
\end{align*}



### Example 3 
Over $C[a,b]$, $\langle f,g\rangle _{L^2} = \int_a^b f g dx$

 - $\langle f,f\rangle _{L^2} = \int_a^b f^2 dx \geq 0$  
 - $\langle f,f\rangle _{L^2}=0$ IFF $\int_a^b |f|^2 dx = 0$ IFF $f(x)=0$ because $f$ is continuous.


  Assume $f(x_0) >  0$, then by continuity, take $I_\delta(x_0):=[x_0-\delta, x_0+\delta], \forall x\in I_\delta(x_0). f(x) >  \epsilon > 0$ so that $\int_a^b |f|^2 dx >  \int_{I_\delta(x_0)} |f(x)|^2 dx >  \epsilon^2$ contradicts with $\langle f,f\rangle _{L^2}=0$ (other details to be filled)
 
 
 By Cauchy Schwartz inequality, 

\begin{align*}
  &\int fg\leq \sqrt{\int f^2}\sqrt{\int g^2}\\
\implies &\langle f,g\rangle _{L^2} \leq \|f\|_{L^2}\|g\|_{L^2}\\
\implies &f\in L^2([a,b])\\
\implies &f\in L^1([a,b])\\
\end{align*}
 
 Therefore, every inner product gives rise to a norm $\|x\|_v := \sqrt{\langle x,x\rangle }$

## _Def'n_. Hilbert space
a complete inner product space is called Hilbert space

__Completeness over inner product space__ A inner product space is complete if every Cauchy sequence $x_n$ has a limit in the space. i.e.  

$$\|x_n - x\|_V^2 = \langle x_n - x, x_n - x\rangle \rightarrow 0$$

$$L^2([a,b]):= \{f:[a,b]\rightarrow \mathbb R: \int_a^b |f|^2 \langle  \infty\}$$

__Remark__ The space $S:=(C[a,b], \|\cdot\|_{L^2})$ is not complete, but $L^2([a,b])$ is the completion of $S$. which means taking any Cauchy sequence, then it has a limit in $L^2$. In another words, continuous functions can approximate any square integrable function in $L^2$-norm.

## _Thrm 2_. Monotone Convergence Theorem
Take nonnegative $f_n(x)\geq 0$, if  $f_1(x)\leq f_2(x) \leq \cdots$  then point-wise limit $f_n(x)\rightarrow f(x)$ i.e. $|f_n(x)-f(x)|\rightarrow 0$

__Corollary__ By MCT, $\lim \int f_n = \int \lim f_n = \int f$

## _Thrm 3_. Dominated/Integral Convergence Theorem
If $\{h_n\}$ satisfy 

 - $|h_n(x)|\leq B(x)$, which $B$ is an integrable function
 - $h_n(x)\rightarrow^{\text{point-wise}} h(x)$
 
Then, $\lim \int f_n = \int \lim f_n = \int f$

## _Thrm 4._ Completeness
The space $(L^2, \|\cdot\|_{L^2})$ is complete

_proof_. Take Cauchy sequence $f_n \in L^2([a,b])$. By Cauchy, take subsequence $f_{n,k}$ s.t. $\|f_{n,k} - f_{n,k+1}\| \leq 2^{-k}$.  
Let $f(x):=f_{n,1}(x) + \sum (f_{n, k+1} - f_{n,k}(x))$. WTS $f\in L^2 (i)$, $f_{n,k}\rightarrow^{L^2} f (ii)$.  
Define $g:= |f_n,1| + \sum|f_{n,k+1}- f_{n,k}|$, $S_M(g) = |f_n,1| + \sum^M|f_{n,k+1}- f_{n,k}|$, then $f\leq g, S_M(f) \leq S_M(g)$  
Apply MCT to $\{S_M(g)\}, 0\leq |f_{n,1}| \leq |f_{n,2}-f_{n,1}|\leq ..., S_1(g) \leq S_2(g) \leq S_3(g)$  
Then, WTS $S_M(g)\rightarrow g(x)$, which suffices to show that the sequence $g$ converges, a.k.a. $g\in L^2$  

\begin{align*}
\|S_M(g)\|_{L^2} &\leq \|f_{n,1}\|_{}L^2 + \sum^M \|f_{n,k+1} - f_{n,k}\| \\
&\leq \|f_{n,1}\| + \sum^M 2^{-k} &\text{tri. ineq.}\\
&<\infty
\end{align*}

Thus we have that 

\begin{align*}
\int |g^2| dx &= \int \lim_{M\rightarrow \infty} |S_M(g)^2|dx\\
&=\lim_{n\rightarrow\infty} \int |S_M(g)|^2 dx &\text{MCT}\\
&\leq \lim_{M\rightarrow \infty} \|f_{n,1}\| + \sum^M 2^{-k} \leq \|f_{n,1}\| + 2 \\
&< \infty
\end{align*}

We have Cauchy seuqnce $f_n \in L^2$, WTS $\|f_n -f\|_{L^2}\rightarrow 0$  

(i) Since $|f|\leq g$ and $g\in L^2, \int |f|^2 \leq \int |g|^2 < \infty\implies f\in L^2$  

(ii) $\|f_n - f\|_{L^2}^2 = \int |f_n - f|^2 dx\rightarrow 0$.

Let $h_k:=|f_{n,k}- f|^2$, then  

$$h_k \leq |S_k(g)| + |g| \leq 2|g|\in L^2$$

so that $f_{n,k}\rightarrow^{\text{p.w.}} f$ since $g\in L^2$ so $\lim_{k\rightarrow \infty} f_{n,k}(x)=f(x)$ exists  
BY DCT, $\lim_{k\rightarrow \infty} \int |h_k|^2 = \int \lim_{k\rightarrow \infty} |h_k|^2 =0$,  

Therefore, $f_{n,k}\rightarrow^{L^2}f$

Then, expansion $f_{n,k}$ to $f_n$. i.e. $f_n \rightarrow^{L^2} f$.  
By Cauchy sequence of $f_n$, if the sub-sequence converges to some limit, so that the whole sequence will do so. 

## Fourier Series

### _Def'n._ Orthogonal
Given $x,y\ in (V,\langle\cdot, \cdot\rangle)$, x,y are orthogonal if $\langle x,y\rangle  = 0$  
### Example
$x\circ y = \cos(\theta) |x||y|$, so when $\theta = \pi /2, x\circ y = 0$

### _Def'n._ Orthogonal set
A collection of $\{e_k\}$ is called orthonormal if $\langle e_k,e_m\rangle  = \mathbb I(k=m)$

### _Thrm 4_. 
Every Hilbert space has orthonormal basis, i.e. $\forall x\in H. x = \sum^\infty \langle x,e_k\rangle  e_k$

### Example
Take $e_k = (0,...,0,1,0)$ where $1$ is at $k$th position, $\{e_k\}$ is orthonormal set. 

_proof_. $e_k \cdot e_m = \sum^n (e_k)_i (e_m)_i = 1\mathbb I(k=m)$

### Example
$\{1, \sqrt2\cos(n\theta), \sqrt2\sin(n\theta)\}$ is orthogonal for $(C([-\pi, \pi]), \|\cdot\|_{L^2})$

_proof_. We have the followings hold

\begin{align*}
&\frac{\sqrt2}{\pi}\int_{-\pi}^\pi \cos(n\theta)\cos(k\theta) = 1\mathbb I(n=k)\\
&\frac{\sqrt2}{\pi}\int_{-\pi}^\pi \sin(n\theta)\sin(k\theta) = 1\mathbb I(n=k)\\
&\frac{\sqrt2}{\pi}\int_{-\pi}^\pi \sin(n\theta)\cos(k\theta) = 0
\end{align*}

### _Def'n_. Fourier Series
For function $f\in L^2([a,b])$, the Fourier series is defined to be 

$$f(x):= a_0 + \sum a_n \frac{\cos(n\pi x)}{L} + b_n \frac{\sin(n\pi x)}{L}$$

where

$$a_n = \langle f, \frac{\cos(n\pi x)}{L})\rangle _{L^2}, b_n = \langle f, \frac{\sin(n\pi x)}{L}\rangle _{L^2}$$

### _Thrm_. Carleson Hunt Theorem
If $f\in L^2([-L,L])$, then $f$ equals its Fourier series _almost everywhere_.  
_almost everywhere_ outside a measure zero set

