# Sigularities and Residue Theorem

## Singularity
$z_0$ is an __isolated singularity__ of $f$ if $f(z)$ is not differentiable or is undefined at $z_0$, but $f(z)$ is analytic on $A_{0, r_0}(z_0)$ for some $r_0 > 0$ 
### Classes of Singularities

Suppose $f$ has a isolated singularity at $z_0$, and its Larent expansion is $f(z) = \sum_{-\infty}^{\infty} c_n (z-z_0)^n$ on $A_{0, r_0}(z_0)$ for some $r_0 > 0$, then 
 - $z_0$ is a __removable singularity__ if $c_n = 0$ for all $n < 0$. 
 - $z_0$ is a __pole of order__ $N$ if $c_{-N}\neq 0$ abd $c_n = 0$ for all $n < -N$.
 - $z_0$ is a __essential singularity__ if $c_n\neq 0$ for all $n < 0$.

Another definition 
 - $z_0$ is a __removable singularity__ if $\exists s, 0 < s < r$ s.t. $f(z)$ is bounded on $A_{0, s}(z_0)$, i.e. $\lim_{z\rightarrow z_0} f(z)$ exist. 
 - $z_0$ is a __pole of order__ $N$ if $\exists s, 0 < s < r$ s.t. $(z-z_0)^N f(z)$ is bounded on $A_{0, s}(z_0)$, i.e. $\lim_{z\rightarrow z_0} (z-z_0)^N f(z)$ exist but $\lim_{z\rightarrow z_0} (z-z_0)^{N-1} f(z)$ DNE. 
 - $z_0$ is a __essential singularity__ if $\forall N, \forall s, 0 < s < r$ $(z-z_0)^N f(z)$ is unbounded, or $\lim_{z\rightarrow z_0} (z-z_0)^N f(z)$ DNE.

The two definitions are equivalent

### Claim 1
Let $f(z)$ have a removable singularity at $z_0$, and analytic on $A_{0, r}(z_0)$ for some $r > 0$. Then, $\exists g(z)$ analytic on $B_r(z_0)$ and $f=g$ on $A_{0,r}(z_0)$.

_proof_. Note that for removable sinularity, we have the Laurent series $f(z) = \sum_{n=0}^\infty c_n(z-z_0)^n$ since for $\forall m \leq  -1, c_m = 0$ on the anulus.  
Then, simply write as the power series on the ball. 

### Example 1
consider $\frac{\sin z}{z}$ on $A_{0,r}(0)$. its Laurent series is given by 

$$\frac{\sin z}{z} = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!}\frac{z^{2n+1}}{z} = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!}z^{2n}$$

Therefore, take $z=0$, we have the series equals to $1$. we can write $g(z) = \begin{cases}\sin z / z &z\neq 0\\ 1&z=0\end{cases}$

## Residue

Note that using Cauchy Theorem we can do contour deformation to solve singularity in $C_{int}$, and each integral around singularity can be related to CIF. Therefore, we can unify them together. 

For $f$ analytic, for some singularity $z_0$ on $f$ s.t. $f$ is analytic on $A_{o,r}(z_0)$ for $r>0$. The __residue__ is defined as 

$$Res(f, z_0) = c_{-1} = \frac{1}{2\pi i} \oint_{C}\frac{f(w)}{(w - z_0)^{-1+1} }dw = \frac{1}{2\pi i} \oint_{C_s}f(w)dw$$

for some circle $C_s$ of radius $0 < s < r$ centered at $z_0$. Note that $c_{-1}$ is the coefficient of Larent series expansion on $A_{0,r}(z_0)$. 

### Theorem 1. Residue Theorem
Let $D$ e a domain, Let $C\subset D$ be a Jordon contour,  let the set of singularities $Z = \{z_1,..., z_N\} \subset C_{int}, f(z)$ analytic on $D - Z$. Then, 

$$\oint_C f(z)dz = 2\pi i \sum_{k=1}^N Res(f, z_k)$$

_proof_. First, by contour deformation, we only need to show that 

$$\int_{C_k} f(z)dz = 2\pi i Res(f, z_k)$$

where $C_k \subset A_{0, r_k}(z_k)$ s.t. $f$ is analytic on each anulus. From the definition of residue above, 

$$2\pi i Res(f, z_k) = 2\pi i \frac{1}{2\pi i} \oint_{C_k} f(w)dw = \oint_{C_k} f(z)dz$$

### Claim 2

$f(z)$ has a pole of order 1 at $z_0$ IFF $Res(f, z_0) = \lim_{z\rightarrow z_0} (z-z_0)f(z)$

_proof_. $f$ has pole of order 1 IFF the Larent series starts from $-1$, so that

$$(z-z_0)f(z) = \sum_{n=0}^{\infty} c_{n-1} (z-z_0)^n$$

Therefore, consider the limit $\lim_{z\rightarrow z_0} (z-z_0)f(z)$, if the limit exists, all terms with $(z-z_0)$ must approach $0$ as $z\rightarrow z_0$, the only term left can be the 0th term, i.e. $c_{-1}$ 

### Claim 3
For $z_0$ is a pole of order $k$ singularity, or a removable singularity, or an analytic point, (i.e. $z_0$ has at most order $k$)take any $M\geq k$, we have 

$$Res(f, z_0) = \frac{1}{(m-1)!} \lim_{z\rightarrow z_0} \frac{d^{M-1}}{dz^{M-1}} (z-z_0)^M f(z)$$

_proof_. 

\begin{align*}
(z-z_0)^M f(z) &= \sum_{n=0}^\infty c_{n-M} (z-z_0)^n\\
\frac{d^{M-1}}{dz^{m-1}}(z-z_0)^M f(z) &= \sum_{n=M-1}^\infty (\prod_{k=0}^{M-2} (n-k))c_{n-M} (z-z_0)^{n-M-1}
\end{align*}

Therefore, the coefficient at $(z-z_0)^0$ is when $n = M-1$

$$(\prod_{k=0}^{M-2} (M-1 - k))c_{-1} = (M-1)! c_{-1}$$

## Residue At Infinity

If $f(z)$ analytic on $A_{s,\infty}(0)$ for some $s>0$, define the __residue at inifinity__ as

$$Res(f,\infty) = \lim_{R\rightarrow\infty} \frac{1}{2\pi i} \oint_{C_R} f(z)dz$$

Note that this definition makes sense because on $A_{s,\infty}(0)$, consider Laurent series expansion $f(z) = \sum_{-\infty}^\infty c_nz^n$ we have 

\begin{align*}
\lim_{R\rightarrow\infty} \frac{1}{2\pi i} \oint_{C_R} f(z)dz &= \frac{1}{2\pi i}\lim_{R\rightarrow\infty}  \oint_{C_R} \sum_{n=-\infty}^\infty c_n z^ndz\\
&\rightarrow^{u.c} \frac{1}{2\pi i}\lim_{R\rightarrow\infty} \sum_{n=-\infty}^\infty \oint_{C_R}  c_n z^ndz\\
&= \frac{1}{2\pi i} \oint_{C_R} c_{-1}z^{-1}dz&\text{CT}\\
&= c_{-1}
\end{align*}

### Claim 1
If $f$ has finitely many singularities $z_1,...,z_n \in \mathbb C$, then 

$$Res(f,\infty) = \sum_{k=1}^n Res(f, z_k)$$

_proof_. 

\begin{align*}
Res(f,\infty) &= \lim_{R\rightarrow\infty} \frac{1}{2\pi i} \oint_{C_R} f(z)dz\\
&= \sum_{k=1}^n Res(f, z_k) &\text{Residue Thrm}
\end{align*}

### Claim 2
$Res(f,\infty) = -Res(\frac{1}{z^2} f(\frac{1}{z}), 0)$

_proof_. By our definition

\begin{align*}
Res(f,\infty) &= \lim_{R\rightarrow\infty} \frac{1}{2\pi i} \oint_{C_R} f(z)dz\\
&= \lim_{R\rightarrow\infty} \frac{1}{2\pi i} \oint_{C_{R^{-1}}} f(u^{-1})(-u^{-2})du &z=u^{-1}, dz=-u^{-2}du\\
&= \lim_{\epsilon\rightarrow0} -\frac{1}{2\pi i} \oint_{C_{\epsilon}} \frac{1}{u^2}f(\frac{1}{u})du\\
&= -Res(\frac{1}{z^2} f(\frac{1}{z}), 0)
\end{align*}

### Claim 3
For $p, q$ polynomials, if some $C$ large enough circle to contain all the roots of polynomial $q(z)$ and $deg(q)\geq deg(p) + 2$, then 

$$\oint_C \frac{p(z)}{q(z)} dz = 0$$

_proof_. Consider 
$\lim_{z\rightarrow\infty} z\frac{p(z)}{q(z)}, deg(zp(z)) = deg(p(z)) + 2\leq deg(q)$ so that the limit exists and $\lim_{z\rightarrow\infty} z\frac{p(z)}{q(z)} = 0$. Therefore,

$$Res(p/q,\infty) = \frac{1}{2\pi i}\oint_C \frac{p(z)}{q(z)} dz = 0$$

## Winding Number
For closed curve $C$, define for the winding number of $C$ at $z_0$ (not on $C$) as 

$$w(C, z_0) = \frac{1}{2\pi i}\int_C \frac{1}{z-z_0} dz$$ 

Graphically, winding number is the number of circles of $C$ oriented c.c.w. around $z_0$. 

__Theorem__ For curves $C$ that does not go across $0$, any parameterization $c(t)$ of $C$ can be decomposed into 

$$c(t) = r(t)e^{i\theta(t)}$$

__Theorem__ $w(C, 0) = \frac{\theta(b) - \theta(a)}{2\pi i}$

### Generalized Residue Theorem
Let $D$ be a simply connected domain, $\mathbf z = \{z_1,...,z_n\} \in D$ be singularities. $C \subset D - \mathbf z$ be a closed curve and $f$ is analytic on $D-\mathbf z$. Then, 

$$\int_C f(z)dz = 2\pi i \sum_{i=1}^n w(C, z_k) Res(f, z_k)$$
