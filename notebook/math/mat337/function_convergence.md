# Functions Convergence

## Convergence 

### _Def'n_. Pointwise convergence
Given $\{h_k\}\subset C(S,\mathbb R)$. We say that they converge pointwise if $\forall x\in S. h_k(x)\rightarrow h(x)$. 

$$\forall \epsilon > 0. \forall x \in S. \exists N > 0. \forall k \geq N. |f_k(x)-f(x)|<\epsilon$$

### _Def'n_. Convergence Uniformly
$f_k\rightarrow^{u.c.}f$ if $\|f_k - f\|_{\infty}\rightarrow 0$. 

$$\forall \epsilon > 0. \exists N > 0. \forall k\geq N. \sup_{x\in S}|f_k(x)-f(x)|\leq \epsilon$$

### Example
consider 
$f_k(x):=
    \begin{cases}
        k^2 x & 0\leq x\leq 1/k \\
       k^2 x (\frac{2}{k}-x) & 1/2 \leq x \leq 2/k \\
       0 &2/k \leq x \leq 1
    \end{cases}$  
    
__Claim__ $f_k \rightarrow^{p.w.} 0$  

_proof_. Let $x\in[0,1]$. take $N > 0$ s.t. $2/N \leq x$. Therefore, $\forall k \geq N, |f_k(x)-0|<\epsilon$

__Claim__ $f_k\not\rightarrow^{u.c.} 0$  

_proof_. $\sup_{x\in[0,1]}|f_k(x)-0|=k\rightarrow\infty$

__Claim__ $\lim_{k\rightarrow\infty}\int_0^1 f_k(x)dx \neq \int_0^1 \lim_{k\rightarrow\infty}f_k(x)dx$  

_proof_. $LHS=\lim_{k\rightarrow\infty}\int_0^{1/k} k^2 x dx + \int_{1/k}^{2/k} k^2(\frac{2}{k}-x)dx + 0 = \lim_{k\rightarrow\infty}1=1$  
$RHS = 0 \neq 1$

### Example
Let $f_n:[0,A]\rightarrow \mathbb R, f(x):= \frac{\sin(nx)}{n}\rightarrow^{u.c.}0$.  

_proof_. $\sup_{x\in[0,A]}|\frac{\sin(nx)}{x} - 0| \leq 1/n \rightarrow 0$


### _Thrm 1_. 
__Claim__ u.c. does not preserve derivatives  

_proof_. $f'(x)=\frac{n\cos(nx)}{n} = cos(nx)$ doesn't converge to any function. 

### _Thrm 2_. Dini's Theorem
If $f,f_n\in C([a,b]). (\forall n \geq 1. f_n \leq f_{n+1} \land f_n(x)\rightarrow f(x))\Rightarrow f_n\rightarrow^{u.c.} f$

_proof_. Since $f_n \leq f_{n+1}\land f_n \rightarrow f \Rightarrow g(x):=f(x)-f_n(x)\geq 0$ 

(i) By continuity at $x_0$, take $\delta_1 > 0, \forall y\in\mathbb R. |x_0 - y|\Rightarrow |g(x_0) - g(y)|\leq \epsilon/2$  

(ii) By $f_n(x_0)\rightarrow^{p.w.}f(x_0)$, take $N>0, \forall n > N. |f_n(x_0)-f(x_0)|\leq \epsilon/2$  

\begin{align*}
|g(y)| &= |f(y)-f_n(y)| \\
&\leq |f(x_0)-f_n(x_0)| + |g(x_0) - g(y)| \\
&\leq \epsilon /2 + \epsilon /2 = \epsilon. &\forall y\in (x_0-\delta, x_0 + \delta)
\end{align*}

Then, suppose that we don't have u.c.  
$\Rightarrow \sup_{x\in[a,b]}|g(x)|=\sup_{x\in[a,b]} |f(x)-f_n(x)|\geq d, d > 0$.  
$\|g\|_{\infty}>d\Rightarrow \forall n > 1. \exists x_n \in [a,b]. g_n(x_n)\geq d$  
By $\{x_n\}\in[a,b]$, with bolzano weierstrass theorem, $x_{n_k}\rightarrow x_0 \in [a,b]$.  
But we show for $\epsilon < d. \exists \delta > 0. |x_0 - y|<\delta\Rightarrow |g(y)|< \epsilon < d$.  
For $\delta, \exists N>0$ so that $\forall k\geq N.|x_{n_k}-x_0|\leq \delta$. Take $y = x_{n_k}\Rightarrow |g(x_{n_k})|<\epsilon < d$ causes contradiction

## Uniform convergence and completeness

### _Thrm 3_. 
If $f_k\in C([a,b]),f_k \rightarrow^{u.c.}f$, then $f\in C([a,b])$  

_proof_. Let $\epsilon > 0$, and $x_0\in [a,b]$.  
By uniform continuous, take $N_{\epsilon/3} > 0, \forall k > N_{\epsilon/3}. \sup_{x\in[a,b]}|f_k(k)-f(x)|\leq \epsilon/3$  
By continuity of $f_k$, take $\delta_{\epsilon/3} > 0, |x_0 - y|\leq \delta \Rightarrow |f_{N_{\epsilon/3} }(x_0) - f_{N_{\epsilon/3} }(y)|\leq \epsilon/3$  
Take $\delta = \delta_{\epsilon/3}$,  

\begin{align*}
|f(x_0) - f(y)| &\leq |f(x_0) - f_{N_{\epsilon/3} }(x_0)| &\text{by uniform continuous} \\
&\quad+ |f_{N_{\epsilon/3} }(x_0) - f_{N_{\epsilon/3} }(y)|&\text{by continuity}  \\
&\quad+ |f_{N_{\epsilon/3} }(y) - f(y)|&\text{by uniform continuous}  \\
&= \epsilon/3 + \epsilon/3 + \epsilon/3 = \epsilon
\end{align*}



### Example
$f_n(x) = (1 + \frac{x}{n})^n\rightarrow^{u.c.} e^x := \sum^\infty \frac{x^k}{k!}$ over any interval $[a,b]$

_proof_. 

\begin{align*}
\sup_{x\in [a,b]} |(1+\frac{x}{n})^n - e^x| &=\|\sum_{k=1}^n {n\choose k}\frac{x^k}{n^k} - \sum\frac{x^k}{k!}\|_\infty \\
&\leq |\sum^\infty \frac{x^k}{k!}| &{n\choose k}/n^k \leq \frac{n}{k!}\\
&\leq |\sum \frac{b^k}{k!}| &x\in [a,b]
\end{align*}
  
By big-oh, Take $N_\epsilon > 0, \forall n \geq N. \sum \frac{b^k}{k!} \leq \epsilon$

### _Thrm 4_. 
__Claim__ $\lim_{n\rightarrow\infty}\int_0^1 f_n(x)dx = \int_0^1 \lim_{n\rightarrow\infty}f_n(x)dx = \int_0^1 e^x dx = e-1$ 

_proof_. 

\begin{align*}
\int_0^1 (1 + \frac{x}{n})^n dx &= \big(\frac{ {n+x}^{n+1} }{(n+1)n^n}\big)\big|_0^1  \\
&= \frac{(n+1)^{n+1} }{(n+1)n^n} - \frac{n^{n+1} }{(n+1)n^n}\\ 
&= (1 + \frac{1}{n})^n - \frac{n}{n+1}\\ 
\lim_{n\rightarrow \infty} (1 + \frac{1}{n})^n - \frac{n}{n+1} &= e - 1\\
\end{align*}



### Example
Point-wise convergence does not imply uniform continuous  

_proof_. Take $f_n:[0,1]\rightarrow \mathbb{R} : = x^n$.  
$f_n(x_0) \rightarrow^{p.w.} \mathbb I (x_0 = 1)$  
But $\sup_{x\in[0,1]}|x_n - \mathbb I(x = 1)| = \sup_{x\in(0,1)}|x^n|$.  
Therefore, for $x_0 = 0.5^{1/n}, f_n(x_0) = 1/2 > 0$.  
You will lose u.c. when you arbitrarily close to 1. 

### Example

$\forall f,g\in C(K). K$ compact, if $f_n \rightarrow^{u.c.} f, g_n \rightarrow^{u.c.} g$, then $f_n g_n \rightarrow^{u.c.} f g$  

_proof_. Let $\epsilon > 0$, for all $x\in K$  

\begin{align*}
|f_n(x)g_n(x) - f(x)g(x)| &= |f_n(x)g_n(x) - g(x)f_n(x) + g(x)f_n(x) - f(x)g(x)| \\
&\leq |f_n(x)||g_n(x)-g(x)| + |g(x)||f_n(x)-f(x)| \\
&< B_1 |g_n(x)-g(x)| + B_2 |f_n(x)-f(x)|&\text{By EVT on $f_n, g_n$, since $K$ compact} \\
&\leq B_1 \|g_n - g\|_\infty + B_2 \|f_n-f\|_{\infty}&\text{By u.c. of $f,g$} \\
\text{take } N_1&\implies \forall n \geq N_1 . \|g_n-g\|_\infty \leq |\frac{\epsilon}{2B_1}|, N_2\\&\implies \forall n \geq N_2 . \|f_n-f\|_\infty \leq |\frac{\epsilon}{2B_2}| \\ 
&\leq \epsilon
\end{align*}


## Integral Convergence Theorem

If $f_n \in C([a,b])\land f_n \rightarrow^{u.c.}f$,  
then $\forall [c,d]\subseteq [a,b]. \lim_{n\rightarrow\infty}\int_c^d f_n(t)dt = \int_c^d \lim_{n\rightarrow\infty}f_n(t)dt$

_proof_. 

\begin{align*}
\Big|\int_c^d f_n(t) - f(t)dt\Big| &\leq \int_c^d |f_n(t)-f(t)|dt  \\
&\leq \int_c^d \sup_{s\in[a,b]}|f_n(s)-f(s)|dt \\
&= \sup_{s\in[a,b]} |f_n(s)-f(s)| \int_c^d d_t \\
&= \|f_n-f\|_\infty(d-c) \\
&\text{by u.c., take }\tilde\epsilon = \frac{\epsilon}{b-a} s.t. \exists N_{\tilde \epsilon} \geq 0. \forall n\geq N_{\tilde\epsilon}, \|f_n-f\|_\infty \leq \tilde\epsilon  \\
&\leq \frac{d-c}{a-b}\epsilon
\end{align*}

Note that if $[a,b]=[0,\infty)$, then the proof breaks down.  
because $\int_c^d dt$ can be arbitrarily large, so one fix is to have a density $\rho(x)$ so that $\int_c^d \rho(s)ds\leq B$

### _Thrm 5_. Leibriz's Rule (differentiation under the integral)
$\forall f(x,t), d_x f(x,t) \in C([a,b]\times[c,d])$. If $f(x) = \int_c^d f(x,t)dt$, then $\frac{dF}{dx} = \int_c^d d_x f(x,t)dt$  

_proof_. Fix $x_0\in[a,b]$,

$$F'(x_0) = \lim_{h\rightarrow 0}\frac{F(x_0 + h) - F(x_0)}{h}$$

Consider the RHS, 

\begin{align*}
\lim_{h\rightarrow 0}\frac{F(x_0 + h) - F(x_0)}{h} &= \frac{1}{h}\int_c^d f(x_0+h,t)-f(x_0, t)dt \\
\text{by MVT, take }\xi(t,h)\in [x_0, x_0+h], &\frac{F(x_0 + h) - F(x_0)}{h} = d_x f(\xi(t,h), t) \\
&= \int_c^d d_xf(\xi(t,h),t)dt
\end{align*}

WTS given $\epsilon$, can find $h$ small enough so that $|\int_c^d d_xf(\xi(t,h), t) - d_xf(x_0, t)dt|\leq \epsilon$  
Using continuity of $d_xf(x_0, t)$, take $\delta > 0. |x_0 - y|<\delta \Rightarrow |d_xf(y,t) - d_xf(x_0,t)|\leq \frac{\epsilon}{d-c}$  

Since $|\xi(t,h)-x_0|<h$, take $\delta < h$, then $|d_xf(\xi(t,h), t) - d_xf(x_0, t)|\leq \frac{\epsilon}{d-c}$,  

\begin{align*}
 |\int_c^d d_xf(\xi(t,h), t)-d_xf(x_0, t)dt| &\leq \int_c^d |d_xf(\xi(t,h), t)-d_xf(x_0, t)|dt \\
 &\leq \frac{\epsilon}{d-c}\int_c^d dt = \epsilon
\end{align*}

Therefore, $\epsilon>0, \exists h$ small enough so that 

$$|\frac{F(x_0 + h, t) - F(x_0)}{h} - \int_c^d d_xf(x_0,t)dt|\leq \epsilon$$

Therefore, 

$$F'(x_0)=\lim_{h\rightarrow 0} \frac{F(x_0+h)-F(x)}{h} = \int_c^d d_xf(x_0, t)dt$$
