# Examples of Surfaces

## Level Surfaces

A surface can be given as a level surface as 

$$\{(x,y,z): f(x,y,z) = 0$$

where $f$ is smooth.

__Claim__ If $\Sigma$ is a level surface with smooth $f$ and $\forall p \in \Sigma. \nabla f\neq \vec 0$. Then $\Sigma$ is a regular surface. 

_proof_. Near each point $\mathbf p=(x_0, y_0, z_0)\in \Sigma, f(\mathbf p) = 0$, we want to show that $\Sigma$ is a graph of coordinate function of the other two coordinates.   
WLOG assuming that $\sigma$ is the map from XZ-plane. 

$$\sigma(x, z) := (x, \psi(x, z), z)$$

where $\psi(x_0, z_0) = y_0$. 

By implicit funciton theorem, consider $f$ near $\mathbf p$. 

\begin{align*}
f(\mathbf a) &= f(\mathbf p) + Df\vert_{\mathbf p} (\mathbf a-\mathbf p) + rem.\\
&= 0 + \begin{bmatrix}
\frac{\partial f}{\partial x}(x_0, y_0, z_0)\\
\frac{\partial f}{\partial y}(x_0, y_0, z_0)\\
\frac{\partial f}{\partial z}(x_0, y_0, z_0)\end{bmatrix}\begin{bmatrix}x-x_0\\y-y_0\\z-z_0\end{bmatrix} + rem.
\end{align*}

Note that $Df\vert_{\mathbf p}\neq 0$ so that the linear expansion is invertible. Therefore, we can apply implicit function theorem and confirm that the non-linear $f$ is also invertible. 

In this case, $Df|_{\mathbf p}$ is non-zero and is the normal vector of $\Sigma$. In this case, we also have that $\Sigma$ is orientable, since $N(p) = Df|_{\mathbf p}\neq 0$ and $f$ is smooth. 

### Examples of level surface

For level surface 

$$\Sigma = \{(x,y,z): x^2 + y^2 + z^4 = 1\}$$

we have that $Df = (2x, 2y, 4z^3)$ vanishes only when at $p=(0, 0, 0)$, while $p\not\in\Sigma$, hence it is smooth. 

Consider $a>b>0$ and 

$$\Sigma = \{(x,y,z): (x^2+y^2+z^2 + a^2 - b^2)^2 = (4a^2(x^2+y^2))\}$$

Let $f(x,y,z) = (x^2+y^2+z^2 + a^2 - b^2)^2 - (4a^2(x^2+y^2))$, then 

$$Df = \begin{pmatrix}
4x(x^2+y^2+z^2 - a^2 - b^2)\\
4y(x^2+y^2+z^2 - a^2 - b^2)\\
4z(x^2+y^2+z^2 + a^2 - b^2)
\end{pmatrix}$$

The only possible point where $Df=0$ is $p(0,0,0)\not\in\Sigma$, hence $\Sigma$ is smooth. 
Furthere more, consider 

$$\begin{pmatrix}
x\\y\\z
\end{pmatrix} = \begin{pmatrix}
(a+b\cos\theta)\cos\varphi\\
(a+b\cos\theta)\sin\varphi\\
b\sin\theta
\end{pmatrix}$$

Note that 

$$x^2+y^2 + z^2 = a^2+2ab\cos\theta + b^2\cos^2\theta + b^2\sin^2\theta = a^2 + 2ab\cos\theta + b^2$$

\begin{align*}
LHS &= (a^2 + 2ab\cos\theta + b^2 +a^2 - b^2)^2\\
&= (2a)^2(a + b\cos\theta)^2\\
&= 4a^2(x^2 + y^2)\\
&= RHS
\end{align*}

### Lagrange's Method of Undetermined Multipliers

Let $\Sigma = \{(x,y,z): f(x,y,z) = 0\}$ be smooth. 

__Claim 1__ $\nabla f$ is perpendicular to the tangent plane at every $p\in \Sigma$.

_proof_. Since $\Sigma$ is smooth. Let $p\in\Sigma$, let $\sigma: U\rightarrow V$ be some patch containing $p$. Then, we have that 

$$\frac{df}{du} = \frac{df}{dx}\frac{dx}{du}+\frac{df}{dy}\frac{dy}{du}+\frac{df}{dz}\frac{dz}{du} = \nabla f\cdot \sigma_u$$


$$\frac{df}{dv} = \frac{df}{dx}\frac{dx}{dv}+\frac{df}{dy}\frac{dy}{dv}+\frac{df}{dz}\frac{dz}{dv} = \nabla f\cdot \sigma_v$$

However, $\Sigma$ is defined on a level surface so that $\frac{df}{du} = \frac{df}{dv} = 0$. while $\nabla f\neq 0, D\sigma \neq 0$, hence $\nabla f\perp \sigma_v$. 

__Claim 2__. $\Sigma$ is orientable. 

_proof_. Note that $\nabla f$ is perpendicular to the tangent plane at all $p \in S$. Which means it is parallel to $\hat N$. Therefore, we can take $\hat N = \frac{\nabla f}{\|\nabla f\|}$, since $f$ is smooth and nowhere vanishing, $\hat N$ is well-defined and $\Sigma$ is therefore orientable. 

__Claim 3__. For some $F:\mathbb R^3\rightarrow \mathbb R$ is smooth, and $F$, with the restriction to $\Sigma$, has a local extremum at $p$, then $\nabla F = \lambda \nabla f$. 

_proof_. Let $\gamma$ be arbitrary smooth curve on $\Sigma$ passing through $p$, since $F$ has a local extremum on $\Sigma$, it is also a extremum on such path $\gamma$, therefore we have that 

$$\frac{dF}{dt} = \nabla f\cdot \frac{d\gamma}{dt} = 0$$

Therefore, $\nabla F\perp \gamma'$ is perpendicular to any curve on $\Sigma$ at $p$, implying that $\nabla F$ is perpendicular to $T_p\Sigma$. Therefore $\nabla F$ parallel to $\nabla f\implies \nabla f = \lambda \nabla F$

## Surface of  Revolution
A surface of revolution is the surface obtained by rotating a plane curve around a straight line in the plane. 

Consider the example where the curve resides in the XZ plane, defined as 

$$\gamma: (a, b)\rightarrow \mathbb R^3. \gamma(t)= (f(t), 0, g(t)), f(t) > 0$$

and the surface is obtained by rotating $\gamma$ about z-axis with rotation parameter $\theta$, the surface patch is then

$$\sigma(t, \theta) = (f(t)\cos\theta, f(t)\sin\theta, g(t))$$

Where $\sigma_1: U_1\rightarrow V_1\cap \Sigma$ with $\theta\in (0, 2\pi),  \sigma_2: U_2\rightarrow V_2\cap \Sigma$ with $\theta\in (-\pi, \pi)$

For example, the sphere without the north and south pole is a surface of revolution with $\gamma(t) = (\cos t, 0, \sin t), t\in (-\pi/2, \pi/2)$. Cylinder with $\gamma(t) = (R, 0, t), t\in\mathbb R$

Note that 

\begin{align*}
\partial_t\sigma &= (f'(t)\cos\theta, f'(t)\sin\theta, g'(t))\\
\partial_\theta\sigma &= (-f(t)\sin\theta, f(t)\cos\theta, 0)\\
N = \sigma_t\times \sigma_\theta &= (f(t)g'(t)\cos\theta, -f(t)g'(t)\sin\theta, f(t)f'(t))\\
\|N\| &= \sqrt{f^2(t)(g'(t))^2 + f^2(t)(f'(t))^2}\\
&= f(t)\sqrt{(f'(t)^2) + (g'(t)^2) }\\
&= f(t)\|\gamma'(t)\|
\end{align*}

Frequently, $\gamma$ is parameterized by the arc-length $s=t$ so that $(f'(t)^2) + (g'(t)^2) = 1$, if so 

$$\|N(t,\theta)\| = f(t)$$


## Ruled Surfaces
A ruled surface is a union of straight lines called __rullings of the surface__ along some curve $\gamma$, where the curve is often unit-speed. 

Let $\gamma:(a,b)\rightarrow \mathbb R^3$ parameterizes the curve, and $d:(a,b)\rightarrow \mathbb R^3$ parameterize the direction of the line. Conveniently, assume $\gamma, d$ are both unit-speed. Then, the surface is parameterized by 

$$\sigma(u, v) = \gamma(u) + vd(u)$$

where $u\in (a, b), v\in\mathbb R$

\begin{align*}
\sigma_u &= \gamma'(u) + vd'(u)\\
\sigma_v &= d(u)
\end{align*}

Therefore, we need that $d\neq 0, \gamma'(u) + vd'(u)$ are $d(u)$ are linearly independent to satisfy the regularity conditions. 
One way to ensure that is to require $\gamma'$ and $d$ being linearly independent and $v$ sufficiently small, say $v\in (-\epsilon, \epsilon)$.  

Oppositely, one can consider surfaces where $d$ is parallel to $\gamma'$ and $d'\neq 0$ (since $d$ is unit-speed, this means $d\perp d'$).  
Then, we can replace $d$ with $\gamma'$ so that 

$$\sigma_u = \gamma' + vd', \sigma_v = \gamma'$$

is linearly independent IFF $\gamma'$ is not parallel to $d'$ IFF $d$ is not parallel to $d'$ and $v\in\mathbb R - \{0\}$

### Examples of Ruled Surface
Mobius band is a ruled surface with 

$$\gamma(u) = (\cos u, \sin u, 0), d(v) = (\sin u, 0, \cos u)$$

A __generalized cylinder__ is when the rulings is constant, $d(u) = \mathbf c$, so that the rulings are always parallel. Then, $\sigma_u = \gamma'(u), \sigma_v = \mathbf c$ so that $\sigma$ is regular IFF $\gamma$ is never tangent to $\mathbf c$. 

A __generalized cone with vertex__ $\mathbf p$ is when all rulings pass through some fixed point $\mathbf p$. In this case, $d(u) = \gamma(u)-\mathbf p$ so that 

$$\sigma_u = \gamma'(u) + v\gamma'(u), \sigma_v = \gamma(u)-\mathbf p$$

Therefore, $\sigma$ is regular IFF $v\neq -1$, i.e. $\mathbf p$ is not in the surface. 
