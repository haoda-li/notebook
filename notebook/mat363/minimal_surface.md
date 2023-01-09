# Minimal Surfaces

## Minimal Surfaces

Similar to the shortest paths, we can study a family of surface patches $\sigma^{\tau}:U\rightarrow\mathbb R^3$ and let $\sigma = \sigma^0$. And the family must be smooth, a.k.a the map 

$$M: \{(u,v,\tau): (u,v) \in U, \tau\in(-\delta, \delta)\}\rightarrow \mathbb R^3, M(u,v,\tau):=\sigma^{\tau}(u,v)$$

is smooth. Then define the __surface variation__ of the family as $\varphi: U\rightarrow\mathbb R^4 := \dot\sigma^{\tau}\mid_{\tau = 0}$

For some simplse closed curve $\pi: (a,b)\rightarrow U$ where the curve and its interior is in $U$, then $\gamma^\tau := \sigma^\tau\circ \pi$ is also a closed curve in $\sigma^\tau$, we can then define the area function of the enclosed region as 

$$A(\tau) = \int_{int(\pi)}dA_{\sigma^\tau}$$


Then, if a family of surfaces has a fixed boundary curve $\gamma$, which means $\forall \tau, \gamma^\tau = \gamma$, then we have that $\varphi(u,v) = \vec 0$ for $(u,v)$ on the curve $\pi$. 

__Theorem__ If the surface variation $\varphi^tau$ vanishes along the boundary curve $\pi$, then 

$$A'(0) = -2\int_{int(\pi)} H(EG-F^2)^{1/2} (\varphi\cdot\mathbf N) dudv$$


Then, similar to how we define shortest path. Intuitively, a surface $\Sigma$ is a __minimal surface__ if $\Sigma$ has the leastarea among all surfaces with the same boundary curve. Which means its surface patches $\sigma = \sigma^0, A'(0) = 0$. Therefore, this formula is possible only if $H=0$ for all points of $U$.  

Therefore, a __minimal surface__ is a surface whose mean curvature is zero everywhere. 

## Gaussian Curvature of minimal surfaces
__Theorem__ Gaussian curvature of a minimal surface is $\leq 0$ everywhere, and $=0$ IFF the surface is a open subset of a plane. 

_proof_. By minimal surface, we have that $H = \kappa_1 + \kappa_2 = 0$ for principal curvatures $\kappa_1,\kappa_2$, thus $K=\kappa_1\kappa_2 = -\kappa_1^2 \geq 0$.  
If $K = 0$, then at least one of $\kappa_1,\kappa_2 = 0$, by minimal surface, both of them must be 0. 

## Parallel Surfaces

For an oriented surface $\Sigma$ and some $\lambda \in \mathbb R$. The __parallel surface__ $\Sigma^{\lambda}$ is 

$$\Sigma^\lambda = \{\mathbf p + \lambda \mathbf N_p:p\in\Sigma\}$$

a.k.a. translate the surface $\Sigma$ along the unit normal for a distance of $\lambda$. 





__Theorem__ $\sigma^\lambda_u\times \sigma^\lambda_v = (1-\lambda\kappa_1)(1-\lambda\kappa_2) (\sigma_u\times\sigma_v)$

_proof._ $\sigma^\lambda = \sigma + \lambda \mathbf N$, if we write derivatives of the normal in the basis of $\sigma_u,\sigma_v$, 

$$\sigma^\lambda_u = \sigma_u + \lambda \mathbf N_u =  \sigma_u + \lambda(-a\sigma_u - b\sigma_v) = (1-\lambda a)\sigma_u - \lambda b \sigma_v$$


$$\sigma_v^\lambda = (1-\lambda d)\sigma_v  - \lambda c\sigma_u$$

Therefore, the cross product is 

\begin{align*}
\sigma^\lambda_u \times \sigma^\lambda_v &= ((1-\lambda a)\sigma_u - \lambda b \sigma_v) \times ((1-\lambda d)\sigma_v  - \lambda c\sigma_u)\\
&= (1-\lambda a - \lambda d + \lambda^2 (ad-bc))(\sigma_u\times \sigma_v)\\
&= (1-\lambda tr(W) + \lambda^2 \det(W))(\sigma_u\times \sigma_v)\\
&= (1 - \lambda(\kappa_1 + \kappa_2) + \lambda^2\kappa_1\kappa_2)(\sigma_u\times \sigma_v)\\
&= (1-\lambda\kappa_1)(1-\lambda\kappa_2) (\sigma_u\times\sigma_v)
\end{align*}

__Theorem__ Let $\sigma$ be a minimal surface patch, let $U$ be some region s.t. the bounded area of the region on $\sigma$ is finite, a.k.a. $A_\sigma(U) < \infty$. Let $\lambda \neq 0$ and assume that the principal curvatures $\kappa$ of $|\lambda \kappa| < 1$ everywhere, so that the parallel surface $\sigma^\lambda$ is a regular surface patch. Then, 
$A_{\sigma^\lambda}(U) \leq A_{\sigma}(U)$ and the equality holds IFF $\sigma(U)$ is an open subset of a plane. 

\begin{align*}
A_{\sigma^\lambda}(U) &= \iint_U \|\sigma_u^\lambda \times \sigma_v^\lambda\|dudv\\
&= \iint_U |1-\lambda\kappa_1||1-\lambda\kappa_2| \|\sigma_u\times\sigma_v\|dudv\\
&= \iint_U |1-\lambda\kappa_1||1 + \lambda\kappa_1| \|\sigma_u\times\sigma_v\|dudv &\kappa_1 = -\kappa_2\\
&= \iint_U |1-\lambda^2 \kappa_1^2| \|\sigma_u\times\sigma_v\|dudv\\
&\leq \iint_U \|\sigma_u\times\sigma_v\|dudv &|1-\lambda^2 \kappa_1^2| < 1\\
&= A_{\sigma}(U)
\end{align*}

The equality IFF $|1-\lambda^2 \kappa_1^2| = 1$ for all possible $\lambda$, implying $\kappa_1 = -\kappa_2 = 0$ IFF $\sigma$ is an open subset of plane.  

## Compact Surface

A set of $\mathbb R^3$ is compact iff closed and bounded, and it attains its maximum and minimum for any continuous function $f:\mathbb R^3\rightarrow\mathbb R$. Since a surface is a subset of $\mathbb R^3$, this also applies to surfaces. 

__Theorem__ If $\Sigma$ is compact, then exists $p\in Sigma$ where $K(p) > 0$, $K$ is the Gaussian curvature. 

_proof_. Let $f(x) = \|x\|^2$, $f$ is continuous, take $p\in\Sigma$ s.t. $f(p)$ attains the maximum on $\Sigma$. Since $f(p)$ attains its maximum, it implies that the surface must be contained in the sphere center at 0 of radius $\|p\|$. Thus, the Gaussian curvature at $p$ is at least the Gaussian curvature of the sphere $K(p) \geq \|p\|^{-2} > 0$.

__Corollary__ There is no compact minimal surface. 

_proof_. Minimal surface means $K\leq 0$ for all points on the surface, contradicting with the fact that $K > 0$ for some point on the compact surface. 

## Isometry of Minimal Surfaces
__Theorem__ Applying an isometry or dilation on a minimal surface gives another minimal surface. 
_proof_. The first fundamental form does not change after the isometry, and the second fundamental form differs by a scale ($\times a$ for dilation, $a=\pm 1$ for isometry). hence $H = a0 = 0$. 

__Theorem__ Applying a local isometry does not necessarily gives another minimal surface.  
_proof_. Consider from a plane to a cylinder. 

## Examples of Minimal Surfaces


### Catenoid and Surfaces of Revolution
For catenoid $\sigma(u,v) = (\cosh u \cos v, \cosh u\sin u, u)$, we can compute its first and second fundamental form

$$E=G=\cosh^2 u, F=0, L=-1, M=0,N=1$$

thus, its mean curvature is 

$$H = \frac{LG-2MF+NE}{2(EG-F^2)} = 0$$

Catenoid is a minimal surface.

Note that the theorem only applies to closed region bounded by a curve, for example

For $a > 0, b = \cosh a$. The surface bounded by $|z| < a$ of two circles of radius $b$ has the area

$$A = \int_0^{2\pi}\int_{-a}^a \sqrt{EG-F^2} dudv = \int_0^{2\pi}\int_{-a}^a \cosh^2 u dudv = 2\pi(a+\sinh a\cosh a)$$

However, this two circles also bounds the area of two circles of radius $b$, where the total area is $2\pi b = 2\pi \cosh a$.  

__Theorem__ Any minimal surface of revolution is an open subset of a plane or a catenoid. 

### Helicoid and Ruled Surfaces

A helicoid is obtained by rotating a straight line at a constant speed, and move along an axis perpendicular to the line at constant speed. 

By isometry, we define a helicoid of a line on the x-axis at a constant angular speed $\omega$, along the z-axis at constant speed $a$. Thus the parameterization is 

$$\sigma(u,v) = (u\cos(\omega v), u\sin(\omega v), av)$$


The first and second fundamental form is 

$$E= 1, F=0, G=(u^2 + a^2), L = N = 0, M = \frac{a^2}{\sqrt{a^2 + u^2} }$$

Thus, the mean curvature is $H = 0$ since $L = F = N = 0$

__Theorem__ Any minimal ruled surface is an open subset of a plane or a helicoid. 

### Catalan's Surface
The Catalan's surface can be parameterized as 

$$\sigma(u,v) = (u-\sin u \cosh v, 1 - \cos u\cosh v, -4 \sin\frac{u}{2}\sinh\frac{v}{2})$$


The first fundamental form is 

$$(\cosh v + 1)(\cosh v - \cos u)(du^2 + dv^2)$$

Since $E=G$, to make $H = 0$, we need $L=-N$, a.k.a $\sigma_{uu} = -\sigma_{vv}$, which can be verified. 

Then, take $u = 0, \gamma(v) = (0, 1 + \cosh v, 0)$ is a straight line, it is a geodesic. 

Take $u = \pi, \gamma(v) = (\pi - \cosh v, 1, -4 \sinh(v/2))$ is the parabola $z^2 = 8(y-2)$, using the geodesic euqation, we can verify this is a geodesic. 

Take $v = 0, \gamma(u) = (u-\sin u, 1-cos u, 0)$ is a cycloid, using the geodesic euqation, we can verify this is a geodesic.

???quote "Source code"
    ```python
    --8<-- "mat363/scripts/catalan.py"
    ```



<iframe
    width="720"
    height="480"
    src="./assets/catalan.html"
    frameborder="0"
    allowfullscreen
></iframe>


