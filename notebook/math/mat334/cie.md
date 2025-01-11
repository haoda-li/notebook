# Cauchy's Integral Formula

## Cauchy's Integral Formula

__Lemma__ For $z_0 \in \mathbb C, C_r$ be the circle of radius $r$. Then, $\oint_{C_r}\frac{1}{z-z_0}dz = 2\pi i$. 

_proof_. We parameterize the circle by $c(t) = re^{it} + z_0$

$$\oint_{C_r}\frac{1}{z-z_0}dz = \int_0^{2\pi}\frac{1}{re^{it}-z_0+z_0}rie^{it}dt =i \int_0^{2\pi}dt = 2\pi i$$

__Theorem__ Let $f:D\rightarrow\mathbb C$ analytic and $D$ simply connected. Then for any Jordon contour $C\subset D$. For $z\in C_{int}$, 

$$f(z) = \frac{1}{2\pi i}\oint_C \frac{f(w)}{w-z}dw$$

_proof_. Let $z\in D$, define $C_\delta$ be a circle of radius $\delta$ centered at $z$, we choose $\delta$ small enough so that $C_\delta \subset C_{int}$. Then, we deform the integral over $C$ to $C_\delta$.

\begin{align*}
\frac{1}{2\pi i}\oint_C \frac{f(w)}{w-z}dw &= \frac{1}{2\pi i}\oint_{C_\delta} \frac{f(w) -f(z)}{w-z} + \frac{f(z)}{w-z}dw\\
&= \frac{1}{2\pi i}\oint_{C_\delta} \frac{f(w) -f(z)}{w-z}dw + \frac{f(z)}{2\pi i}\oint_C\frac{1}{w-z}dw \\
&= \frac{1}{2\pi i}\oint_{C_\delta} \frac{f(w) -f(z)}{w-z}dw + f(z) &\text{lemma}
\end{align*}

Thus, we need to show that $\oint_{C_\delta} \frac{f(w) -f(z)}{w-z}dw  = 0$.  
Since $C_\delta \subset C\cup C_{int}$ and it is compact. We can bound $\frac{f(w) -f(z)}{w-z}$ on $C_\delta - \{z\}$, in addition, since $f$ is analytic, $\lim_{w\rightarrow z} \frac{f(w) -f(z)}{w-z} = f'(z)$. Therefore, 
$\frac{f(w) -f(z)}{w-z} \leq M$ for all $w\in C_\delta$. By ML inequality, 

$$|\frac{1}{2\pi i}\oint_{C_\delta} \frac{f(w) -f(z)}{w-z}dw| \leq |\frac1{2\pi}||(2\pi\delta)M| = \delta M$$

Note that we can pick $\delta$ arbitrarily small so that the supremum of the integral approaches 0. 


## Holomorphic from Analyticity

__Theorem (Analytic functions are infinitely complex-differentiable)__ If $f$ in analytic on $C\cup C_{int}$ for some Jordon contour $C$, then

$$f^{(k)}(z) = \frac{k!}{2\pi i} \oint_C \frac{f(w)}{(w-z)^{k+1}}dw$$

__proof__. First, consider $k = 1$, we have 

\begin{align*}
\frac{f(z+h) - f(z)}h &= \frac{1}{h2\pi i}\oint_C f(w)(\frac{1}{w-(z+h)} - \frac 1{w-z})dw\\
&= \frac{1}{2\pi i}\oint_C \frac{f(w)}{(w-(z+h))(w-z)}dw\\
&= \frac{1}{2\pi i}\oint_C \frac{f(w)}{(w-z)^2}dw + \frac{h}{2\pi i}\oint_C \frac{f(w)}{(w-z)^2(w-z-h)}dw
\end{align*}

Then, let $I = \oint_C \frac{f(w)}{(w-z)^2(w-z-h)}dw$, we need the $\lim_{h\rightarrow 0} \frac{h}{2\pi i}I = 0$. 

Similar to the CIF proof, note that $f(w)$ is bounded on $C$, and since $C$ can be taken arbitrarily small, $|I|$ is then bounded by $\frac M{(\delta + h)^2\delta} 2\pi\delta$ so that

$$\lim_{h\rightarrow 0} |\frac{h}{2\pi i}I| = \frac{|h|M}{(\delta + |h|)^2} = 0$$

Then, we can repeat this process in our inductive step and prove this statement. 

## Liouville's Theorem

__Theorem__ If $f:\mathbb C\rightarrow\mathbb C$ is entire (analytic on $\mathbb C$) and bounded, then $f$ is a constant. 

_proof_. First note that $f$ is analytic, take $R$ be the radius of circle $C$ around some $z$, and $M$ so that $|f(z)| < M$ for $z \in C$, using ML inequality and the theorem above, we can easily have

\begin{align*}
|f^{(k)}(z)| &= \frac{k!}{2\pi} |\oint_C \frac{f(w)}{(w-z)^{k+1}}dw| \\
&= \frac{k!}{2\pi} \frac{M}{R^{k+1}} 2\pi R\\
&= \frac{k!M}{R^n}
\end{align*}

Take $k=1$, we have

$$\forall R > 0, |f'(z)|\leq \frac{M}{R}$$

Take $R$ arbitrarily large, we have $|f'(z)| = 0$ so that for any point $z\in\mathbb C$

$$f(z) - f(0) = \int_0^z f'(z)dz = 0\implies f(z) = f(0)$$

### Fundamental Theorem of Algebra 

__Theorem__ Let $p(z)$ be some complex polynomials. Then $\exists z\in \mathbb C$ s.t. $p(z) = 0$. 

_proof_. Let $p(z):= \sum_{j=0}^n c_j z^j$ be some n-degree complex polynomial. Assume that $\forall z\in\mathbb C, p(z) \neq 0$. Then, $\frac{1}{p(z)}$ is entire and bounded. By Liouville's Theorem, it is a constant. This causes contradiction as $p$ must be in degree of $n$. 

## Maximum Principles

__Lemma__ If $f$ is analytic on some domain $D$, then $|f(z)|$ is unbounded unless $f(z)$ is a constant. 

_proof_. Let $z\in \mathbb D$, take some ball $B_{\delta}(z) \subset D$. Then, we can establish 

\begin{align*}
f(z)\frac{\delta^2}{2} &= \int_0^\delta f(z)\tau d\tau\\
&= \frac{1}{2\pi}\int_0^\pi \oint_{C_\tau}\frac{f(w)}{w-z}\tau dw d\tau\\
&= \frac1{2\pi}\int_0^\pi \oint_{C_\tau}f(w)dwd\tau &\forall w\in C_\tau.(w-z)=\tau \\
&= \frac1{2\pi}\iint_{B_{\delta}(z)}fdA
\end{align*}

Suppose $z$ is a maximum, then 

$$|f(z)|\frac{\delta^2}{2} = |\frac1{2\pi}\iint_{B_{\delta}(z)}fdA| \leq \frac{1}{2\pi}|f(z)|A = \frac{1}{2\pi}|f(z)|\pi\delta^2 = \frac{|f(z)|\delta^2}{2}$$

Implies that for all $z$, $f(z)$ is constant within its neighborhood, implies that $f$ is a constant. 

__Theorem__ If $f$ is analytic and bounded on region $D$ and $|f(z)|$ is continuous in the closure $\bar D$, then $|f(z)|$ must has its maximum on $\partial D$. 
Note that first, by extreme value theorem, a closed and bounded region must have a maximum, then by lemma. Any open region cannot have a maximum, hence the maximum must be on some closure. 
