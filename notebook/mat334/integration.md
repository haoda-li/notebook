# Complex Integration

## Path Integrations

First, consider some $f: [a,b]\rightarrow\mathbb C, f(t) := u(t) + iv(t)$. Assuming that $u,v$ are real-valued functions and integrable on their domain, then $f$ is integrable on $[a,b]$ as 

$$\int_a^b f(t)dt = \int_a^bu(t)dt + i\int_a^b v(t)dt$$

Note that with this definition, $f$ follows fundamental theorem of calculus.

Also, the basic rules for scaling by a constant real factor and summation still follows, namely  
For $f,g$ be complex functions and $\beta_0, \beta_1$ be real constant. 

$$\int_a^b \beta_0 f(t) + \beta_1 g(t)dt = \beta_0\int_a^b f(t)dt + \beta_1\int_a^b g(t)dt$$

## Curves
Let $c$ be some __parameterization__, $c:[a,b]\rightarrow \mathbb C$.  
Define a __curve__ $C = \{c(t): t\in [a,b]\}$ as the image of some __parameterization__ 
 - $C$ is __simple__ if there's no intersection $\forall t_1, t_2\in (a,b), t_1\neq t_2\implies c(t_1)\neq c(t_2)$. 
 - $C$ is __closed__ if $c(a) = c(b)$
 - $C$ is a __Jordan Curve__ if it is simple and closed
 - $C$ is __smooth__ if $c$ is differentiable on $[a,b]$ and $c'$ is continuous on $[a,b]$. 

__Theorem (Jordan Curve Theorem)__ Let $C\in\mathbb C$ be a Jordan curve. Then $\mathbb C-C$ consists of precisely 2 connected component, an interior component bounded by $C$ and an exterior component unbounded. 

A function $f$ is __continuous__ on $C$ if $f(z(t))$ is continuous, $f$ is __piecewise continuous__ if $[a,b]$ if $[a,b]$ can be broken up into a finite number of subintervals in which $f(z)$ is continuous on each interval. 

A __contour__ is a curve consisting of finite number of connected smooth curves, i.e. a union of smooth pieces.  
A __Jordan Contour__ is a closed simple contour. 

$A\subseteq \mathbb C$  is a __simply connected area__ if for any simple closed curve $C\subseteq A$, $C_{int}\subseteq A$ (intuitively, no holes within $A$). 

## Contour Integral
For a smooth contour $C$ parameterized by $c$ on $[a,b]$, the __contour integral__ is defined as 

$$\int_C f(z)dz = \int_a^b f(c(t))c'(t)dt$$

simply through substitution rule. 

### Invariance of Parameterization

__Theorem__ The integral is invariant of the parameterization of $C$ as long as orientation is preserved.   
_proof_. Consider two orientation preserved parameterizations $c_1:[a,b]\rightarrow \mathbb C, c_2:[c,d]\rightarrow \mathbb C$ of $C$.  assume that 
 - $c_1([a,b]) = c_2([c,d])$: their image is the same 
 - $c_1(a)=c_2(c), c_1(b) = c_2(d)$: their orientation is the same 

Note that the two conditions above will give that there exists an increasing differentiable function $h:[c,d]\rightarrow [a,b]$ s.t. $c_2 = c_1\circ h$ (won't prove).   
Therefore, we can check that 

\begin{align*}
\int_c^d f(c_2(t))c_2'(t) &= \int_c^d f(c_1(h(t)))c_1'(h(t))h'(t)dt\\
&= \int_a^b f(c_1(u))c_1'(u)du &u=h(t), du = h'(t)dt\\
\end{align*}

__Theorem__ If $C_1, C_2$ traces out the same curve but in opposite direction, then 

$$\int_{C_1}f(z)dz = -\int_{C_2}f(z)dz$$

_proof_. From the above theorem, we can pick any parameterizations that is convenient.  
Let $c_1, c_2: [0,1]\rightarrow\mathbb C$ be the parameterization of $C$, but in different orientations, i.e. $c_2(t) = c_1(1-t)$. so that 

\begin{align*}
\int_0^1f(c_2(t))c_2'(t)dt &= \int_{0}^1 f(c_1(1-t))c_1'(1-t)(-1)dt \\
&= \int_1^0f(c_1(u))c_1'(u)du &u=1-t, du=-tdt\\
&= -\int_0^1f(c_1(u))c_1'(u)du
\end{align*}

Note that we can fix an orientation for Jordan contours $C$ once for all, so that there's no ambiguity for the path integral defined on some curve. 

We fix the orientation as "counterclockwise", or more formally, as the curve is traversed, the interior is always on the left. With such convention, we write $\oint_C$ to specify such orientation. 

## FTC II on Complex
__Theorem (Fundamental Theorem of Calculus II)__ Let $f:R\rightarrow\mathbb C$ be continuous on $R$. If exists $F:R^0\rightarrow\mathbb C$ s.t. $F$ is analytic on $R$ and $f(z) = F'(z)$. Then, for a contour $C\subseteq R^0$ with endpoints $z_1,z_2$, then 

$$\int_C f(z)dz = F(z_2) - F(z_1)$$

_proof_. (Note that the proof is almost identical to the proof in real number calculus)

\begin{align*}
\int_C f(z)dz &= \int_C F'(z)dt\\
&= \int_a^b F'(c(t))c'(t)dt\\
&= \int_a^b \frac{dF}{dt}dt\\
&= F(z(b)) - F(z(a))
\end{align*}

### Corollary 1
If $C$ is a closed, then $\int_C f(z)dz = 0$ for all $f$ that satisfies the assumptions above. 

### Example
Evaluate $\int_C z^ndz$ over $C:\{e^{it}: t\in[0, 2\pi]\}$ counterclockwise. 

\begin{align*}
\int_C z^n dz = \int_0^{2\pi} (e^{it})^nie^{it} dt= i\int_0^{2\pi}e^{i(n+1)t}dt
\end{align*}

Note that when $n \neq -1$, we have

$$\int_0^{2\pi}e^{i(n+1)t}dt = \int_0^{2\pi} cos((n+1)t)dt + i\int_0^{2\pi}\sin((n+1)t)dt = 0$$

However, when $n = -1$, then 

$$i\int_0^{2\pi}e^{i(-1+1)t}dt = i\int_0^{2\pi}1 = 2\pi i\neq 0$$

Note that the anti-derivative of $z^{-1}$ is $\log z$ is not analytic unless we pick a branch of $\log z$. 

## ML inequality

__Theorem__ Let $C = c([a,b])$ be a contour, $f$ be a function continuous on $C$, $L$ be the arc-length of $C$ and $M> 0$ be the upper bound of $|f|$, formally $\forall t\in[a,b]. M\geq |f(c(t))|$.  Then, $|\int_C f(z)dz | \leq ML$. 

_proof_. Take some parameterizations of $C$

\begin{align*}
|\int_C f(z)dz| &= |\int_a^b f(c(t))c'(t)dt|\\
&\leq \int_a^b |f(c(t))||c'(t)| dt\\
&\leq \int_a^b M|c'(t)|dt\\
&= M\int_a^b|c'(t)|dt\\
&= ML
\end{align*}

### Example 1
Let $R > 1$, let $C$ be an arc of radius $R$ and of angle $\pi/3$. 

(a) Show that $|\int_C (z^3+1)^{-1}dz \leq \frac{\pi}3\frac{R}{R^3-1}$.  
Note that $L = \pi R/3$, with ML inequality, it's sufficient to show that $|(z^3+1)^{-1}| \leq \frac{1}{R^3-1}$ for all $z\in C$.  
By triangular inequality 

$$|z^3 + 1| \geq ||z^3| - |1|| = |R^3 - 1| = R^3 - 1$$ 

Therefore, $|(z^3 + 1)^{-1}| \leq (R^3-1)^{-1}$

### Example 2 
For $C_\epsilon$ be a circle of radius $\epsilon$ around the origin and $f$ be analytic insider $C\cup C_{int}$, show that 

$$\lim_{\epsilon \rightarrow 0} \oint_{C_{\epsilon}}z^a f(z)dz= \lim_{\epsilon\rightarrow} I_\epsilon = 0, \forall a > -1$$

_proof_. Note that $C\cup C_{int}$ is a compact set, since $f$ is continuous, the image of $f$ is bounded. Take $M > 0$ s.t. $\forall z \in C\cup C_{int}. M\geq |f(z)|$.  
Then, note that $\forall z \in C_{\epsilon}. |z^a| = \epsilon^a > 0$.  
By ML inequality, $|I_\epsilon| \leq \epsilon^{a+1}M$, define $b=a+1 > 0$, $|I_\epsilon| \leq \epsilon^{b}M$  
Let $\epsilon > 0$, take $\delta = (\frac{\epsilon}M)^{1/b}$ so that $I_\delta \leq \epsilon$

### Example 3
$I_R = \int_{C_R} \frac{e^{iz}}{z^2}dz$, $C_R = \{e^{it}: t\in[0, \pi]\}$. Show that $\lim_{R\rightarrow \infty}I_R = 0$. 

\begin{align*}
|\int_{C_R} \frac{e^{iz}}{z^2}dz| &= |\int_0^\pi \frac{\exp(iRe^{it})}{(Re^{it})^2}iRe^{it}dt|\\
&= |i||\int_0^\pi\frac{\exp(iRe^{it})}{Re^{it}}dt|\\
&\leq \int_0^\pi |R^{e^{it}}|^{-1} |\exp(iRe^{it})|dt\\
&= \int_0^\pi R^{-1}|e^{iR\cos t}e^{-R\sin t}|dt\\
&= R^{-1}\int_0^\pi e^{-R\sin t}dt
\end{align*}

Note that $e^{-R\sin t}=(e^{-\sin t})^{R} \leq 1$ for $0\leq t\leq \pi, R > 1$, so that 

$$|\int_{C_R} \frac{e^{iz}}{z^2}dz| \leq R^{-1}\int_0^\pi dt = \frac{\pi}{R}$$

Therefore, 

$$\lim_{R\rightarrow\infty}I_R = \lim_{R\rightarrow\infty}\frac{\pi}R = 0$$
