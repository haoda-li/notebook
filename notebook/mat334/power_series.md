# Power Series and Larent Series

## Series
For definitions of series, check [real analysis notes](../mat337/series.md).

## Power Series (Taylor Series)

Let $f(z) = \sum^\infty_{n=0} a_n(z-z_0)^n$ for all $z\in\mathbb C$, if the RHS converges, then we call such $f(z)$ a __power series__ centered at $z_0$. 

### Commonly used Power Series
The power series for complex is almost the same as for reals (same proof). 

$$S_n = \frac{1-c^{n+1}}{1-c} = \sum_{k=0}^n c^k, \forall |c| < 1.  S_\infty = \frac{1}{1-c} = \sum_{k=0}^\infty c^k$$

$$e^z = \sum_{k=0}^\infty  \frac{z^k}{k!}$$

$$\cos z = \frac{e^{iz} + e^{-iz}}{2} = \frac{1}{2}(\sum_{k=0}^\infty  \frac{i^kz^k}{k!} + \sum_{k=0}^\infty  \frac{(-i)^kz^k}{k!}) = \sum_{k=0}^\infty \frac{(-1)^kz^{2k}}{(2k)!}$$

$$\sin z = \sum_{k=0}^\infty \frac{(-1)^kz^{2k+1}}{(2k+1)!}$$

### Theorem 1
Let $f(z) = \sum^\infty a_n z^n$, if $f(z_1)$ converges absolutely for some $z_1\in \mathbb C$, then $f(z)$ converges on $B_{|z_1|}(0)$ and converges uniformly on $\overline{B_r(0)}$ for all $r \in (0, |z_1|)$.

_proof_. First note that $\lim_\infty |a_n z_1^n| = 0$ since the series converges absolutely at $z_1$. 
Let $r \in (0, z_1), z \in \overline{B_r(0)}$.   
take $N > 0$ s.t. $\forall n\geq N. |a_n z_1^n| < 1$. Therefore,

$$|a_nz^n| = |a_nz_1^n||\frac z{z_1}|^n < |\frac z{z_1}|^n \leq (\frac r{|z_1|})^n$$

Therefore, by M-test, $f(z)$ is uniformly convergent on $\overline{B_r(0)}$. 

### Example 1
$f(z) = \sum^\infty \frac{z^n}{n!}$ converges on $\mathbb C$ and is continuous.   

_proof_. Let $z\in\mathbb C$, take $r > |z|$, since $r\in\mathbb R$, we know that $f(r) = e^r$. Thus, by the above theorem, $f(z)$ converges for all $z\in\mathbb C$. In addition, we have uniform converges of $f(z)$ on any closed ball, hence it is also continuous. 

## Existence of Power Series Expansion
__Theorem__ If $f(z)$ is analytic on $B_r(z_0)$, then on $B_r(z_0)$ we have 

$$f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$

and the series is absolutely convergent and uniformly convergent on $\overline{B_\delta(z_0)}$ for all $\delta \in (0,r)$, also convergent on $B_r(z_0)$.

_proof_. Let $z\in B_r(0)$, let $\delta$ where $|z| < \delta < r_1 < r$. Take $C$ be the circle of radius $r_1$ centered at 0. Then 

\begin{align*}
f(z) &= \frac1{2\pi i}\oint_C\frac{f(w)}{w-z}dw &\text{CIF}\\
&=  \frac1{2\pi i}\oint_C\frac{f(w)}{w}\frac1{1-z/w}dw \\
&=  \frac1{2\pi i}\oint_C\frac{f(w)}w\sum^\infty (\frac zw)^ndw \\
&=  \frac1{2\pi i}\oint_C\sum^\infty \frac{f(w)}{w^{n+1}}z^ndw \\
&= \sum^\infty \frac1{2\pi i}\oint_C \frac{f(w)}{w^{n+1}}z^ndw\\
&=  \sum^\infty \frac{f^{(n)}(0)}{n!}z^n &\text{CIF}
\end{align*}

Therefore, we can use M-test to prove the claim. 

### Radius of Convergence

__Theorem (existence)__ Let $f(z) = \sum^\infty a_nz^n$, then $\exists R \in [0, \infty)$ s.t. $f(z)\rightarrow z\in B_r(0)$, does not converge for $z\in \mathbb C - \overline{B_R(0)}$ and converge uniformly on $\overline{B_r(0)}$ for all $r\in(0,R)$. 

And we have 
1. ratio test If $\lim_{n\rightarrow\infty} \frac{|a_{n+1}|}{|a_n|} = S, R = S^{-1}$
2. root test. If $\lim_\infty |a_n|^{1/n} = S, R = S^{-1}$
3. [Hadamard's Theorem](../mat337/series.md#thrm-5-hadamards-theorem). $S = \lim_\infty\sup |a_n|^{1/n} = S, R = S^{-1}$

__Lemma__ $\lim_\infty |a_n|^{1/n} = \lim_\infty\sup \big((n+1)|a_{n+1}|\big)^{1/n}$.   
_proof_. Part of [Hadamard's Theorem](../mat337/series.md#thrm-5-hadamards-theorem).

__Theorem__ Let $f(z) = \sum^\infty a_nz^n$ with radius of convergence $R>0$, then $f(z)$ is analytic on $B_R(0)$. 

_proof_. Let $g(z) = \sum^\infty (n+1)a_{n+1}z^n$, by lemma, $g$ also has radius of convergence $R$. 

Then, we need to show that there exists some anti-derivative of $g$ and g is continuous on $B_R(0)$, so we need to show that all Jordon contour $C \subset B_R(0)$, $\oint_C g(z)dz = 0$. Note that this holds since there is some $0 <\delta < R$ s.t. $C\subset \overline{B_\delta(0)}$ and g is uniformly convergent on $\overline{B_\delta(0)}$, and thus on $C$. Therefore, 

$$\oint_C g(z)dz= \oint_C \sum^\infty (n+1)a_{n+1} z^n dz = \sum^\infty \oint_C  (n+1)a_{n+1} z^n dz = \sum^\infty 0$$

Therefore, take $G$ be some anti-derivative s.t. 

\begin{align*}
G(z_1) &= \int_0^{z_1} g(z)dz \\
&= \int_0^{z_1} \sum^\infty_{n=0} (n+1)a_{n+1} z^n dz\\
&= \sum^\infty_{n=0}  \int_0^{z_1} (n+1)a_{n+1} z^n dz&\text{u.c. on} B_{|z_1|}(0)\\
&= \sum^\infty_{n=1}  \frac{na_n}{n}z_1^n\\
&= \sum^\infty_{n=1}  a_nz_1^n\\
&= f(z_1) - a_0
\end{align*}

Therefore, $f(z) = G(z) + a_0$ is analytic.

## Laurent Series

Define an __annulus__ $A_{r_1, r_2}(z_0) = \{z: r_1 < |z-z_0| < r_2\}$ and $A_{r_1, \infty} (z_0) = \{z : |z-z_0| > r_1\}$. 

__Theorem__ Let $f(z)$ be analytic on $A_{r_1,r_2}(0)$, then $\forall z \in A_{r_1,r_2}(0)$, 

$$f(z) = \sum_{n=-\infty}^{\infty}\bigg(\frac1{2\pi i}\oint_C \frac{f(w)}{w^{n+1}}dw\bigg) z^n$$

where $C \subset A_{r_1,r_2}(0)$ is a Jordon contour s.t. $0\in C_{int}$. Moreover, $f$ converges uniformly on $\overline{A_{s_1,s_2}(0)}$ for all $r_1<s_1<s_2<r_2$. 

_proof_. Let $z \in A_{r_1,r_2}(0)$, let $s_1, s_2, r_1', r_2'$ s.t. $r_1< r_1' < s_1 \leq |z| \leq s_2 < r_2' < r_2$. Then, CIF and CT gives 

$$f(z) = \frac1{2\pi i}\oint_{C_{r_2'}}\frac{f(w)}{w-z}dw - \frac1{2\pi i}\oint_{C_{r_1'}}\frac{f(w)}{w-z}dw  = I_2 - I_1$$

As from power series proof. 

$$I_2 =\sum_{n=0}^\infty\frac{1}{2\pi i}\oint_C \frac{f(w)}{w^{n+1}} dw z^n$$

And similarly, 

$$-I_1 =\frac1{2\pi i} \oint_C\frac{f(w)}{z}\frac1{1-w/z} dw = \sum_{n=-\infty}^{-1} \frac1{2\pi i}\oint_C \frac{f(w)}{w^{n+1}} dw z^n$$

### Lemma 1
If $f(z) = \sum_0^\infty a_n z^n$ and $g(z) = \sum_0^\infty b_nz^n$ on $B_r(0)$, then either $f=g$ or $\exists r > \delta > 0$ s.t. $f\neq g$ on $A_{0, \delta}(0)$. 

_proof_. If $f(0)\neq g(0)$, then by continuity, $\exists \delta > 0$ s.t. $f(z)\neq g(z)$ on $B_\delta(0)$. Now suppose that $f(0)= g(0)$ i.e. If $f\neq g$, then there must exist some $n$ s.t. $a_n \neq b_n$. Take $n_0$ be the least $n$ s.t. $a_{n_0}\neq b_{n_0}$. Therefore,

\begin{align*}
f(z) &= &\sum_{n=0}^{n_0-1} a_nz^n + &z^{n_0} \sum_{n=0}^\infty a_{n - n_0}z^n\\
 &= &p(z) + &z^{n_0}\tilde f(z)\\
g(z) &= &\sum_{n=0}^{n_0-1} a_nz^n + &z^{n_0} \sum_{n=0}^\infty b_{n - n_0}z^n\\
&= &p(z) + &z^{n_0}\tilde g(z)
\end{align*}

Notablly, $\tilde f(0) = a_{n_0} \neq b_{n_0} = \tilde g(0)$, so exists $\delta > 0$ s.t. $\tilde f\neq \tilde g$ on $B_\delta(0)$. Therefore, on $z^{n_0}\tilde f\neq z^{n_0}\tilde g$ on $A_{0, \delta}(0)$


### Theorem 2
Let $f,g$ be analytic on a domain $D$. Let $A\subset D$ s.t. $f(z) = g(z)$ for all $z\in A$. If $A$ has a limit point contained in $D$ then $f=g$ on $D$. 

_proof_. Let $z_0$ be a limit point of $A \subseteq D$. Write the functions as their power series expansion $f(z) = \sum_{n=0}^\infty a_n(z-z_0)^n$ and $g(z)=\sum_{n=0}^\infty b_n(z-z_0)^n$ on $B_r(z_0)\subset D$. We want to show $f=g$ on such $B_r(z_0)$. 

By the lemma above, 
 - Either $f=g$ on $B_r(z_0)$
 - Or exists $\delta > 0$ s.t. $f\neq g$ on $A_{0, \delta}(z_0)$. Take such $\delta$, however, $z_0$ is a limit point of $A$ so that this is a contradiction. 

Now, take $D'\subseteq A \subseteq D$ be the largest open set s.t. $f=g$. If $D'\neq D$, let $z_1 \in \partial D'\cap D$, since $z_1$ is a limit point, we can expand $D'$ with $B_r(z_1)$. $D'\cup B_r(z_1)$ is larger than $D'$ and $f=g$, hence contradiction. 
