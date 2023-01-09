# More Examples of Surface Regularity and Smoothness

## Examples of Surface Patches

- $\sigma(u,v) = (u,v,uv)$ is a regular surface patch  
    _proof_. $\sigma$ is clearly injective, and $\sigma_u = (1, 0, u), \sigma_v = (0, 1, v)$ is clearly linearly independent. 
- $\sigma(u,v) = (u, v^2, v^3)$ is injective, but $\sigma_u = (1, 0, 0), \sigma_v = (0, 2v, 3v^2)$ is not linearly independent when $v= 0$, hence not regular
- $\sigma(u,v) = (u+u^2 , v, v^2)$ is not injective, for example $\sigma(0, 0) = \sigma(-1, 0)$. Also, $sigma_u = (1+2u, 0, 0), \sigma_v = (0, 1, 2v)$ is not linearly independent when $u=-1/2$. 

### Example: Ellipsoid
A ellipsoid is defined as 

$$\frac{x^2}{p^2} + \frac{y^2}{q^2} + \frac{z^2}{r^2} = 1$$

Similar to how we parameterize a sphere, using the long-lat coordinate, we have 

$$\sigma\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}
p\cos\theta\cos\psi\\
q\cos\theta\sin\psi\\
r\sin\theta
\end{pmatrix}$$

We will still use the same 2 surface patches to cover the surface. 

Then, consider regularity, we have that 

$$\sigma_\theta = \begin{pmatrix}
-p\sin\theta\cos\psi\\
-q\sin\theta\sin\psi\\
r\cos\theta
\end{pmatrix}, \sigma_\psi = \begin{pmatrix}
-p\cos\theta\sin\psi\\
q\cos\theta\cos\psi\\
0
\end{pmatrix}$$

The two vectors are linearly independent for 

$$U_1 = \{(\theta, \psi): \theta\in(-\pi/2, \pi/2), \psi\in(0, 2\pi)\}$$

In addition, surface patches are still regular if taken rotations, hence the ellipsoid is smooth and regular. 

### Example: Torus

A torus is obtained by rotating a circle $C$ in plane $\Pi$ around a line $l \subset \Pi$ and $l$ does not intersect $C$. Let $\Pi = \Pi_{XZ}$, $l(t) = (0, t, 0)$, take $a > 0$ be the distance from the center of $C$ to $l$ and $b$ be the radius of $C$. 
Then, the torus is a smooth surface with parameterization 

$$\sigma(\theta, \varphi) = \begin{pmatrix}
(a+b\cos\theta)\cos\varphi\\
(a+b\cos\theta)\sin\varphi\\
b\sin\theta
\end{pmatrix}$$

_proof_. WLOG assume that the center of the circle always reside on the $XY$ plane $(z=0)$. 


Consider the circle defined on the XZ plane as $\gamma(\theta) = (a + b\cos\theta, 0, b\sin\theta)$.    
Then, rotate $\varphi$ degrees along the $z$-axis, the xy coordinate will be 

$$\begin{bmatrix}\cos\varphi&-\sin\varphi\\\sin\varphi&\cos\varphi\end{bmatrix}\begin{bmatrix}a + b\cos\theta\\0\end{bmatrix}$$

Therefore we can obtain the parameterization. 

Then, note that the torus can be cover by 4 patches. By taking each of $\theta, \varphi$ in $(0, 2\pi), (-\pi, \pi)$, and we check the regularity conditions by 

$$\sigma_\theta = (-b\sin\theta\cos\varphi, -b\sin\theta\sin\varphi, b\cos\theta)$$


$$\sigma_\varphi = (-(a+b\cos\theta)\sin\varphi, (a+b\cos\theta)\cos\varphi, 0)$$

We can easily verify that for each domain, the vectors are linearly independent. 


???quote "Source code" 

    ```python
    --8<-- "mat363/scripts/torus.py"
    ```




<iframe
    width="720"
    height="480"
    src="./assets/torus.html"
    frameborder="0"
    allowfullscreen
></iframe>



### Example: Helicoid
A helicoid can be parameterized as 

$$\sigma(u, v) = (v\cos u, v\sin u, \lambda u)$$


Then, we have that 

$$\sigma_u = (-v\sin u, v\cos u, \lambda), \sigma_v = (\cos u, \sin u, 0)$$


$$N = \sigma_u \times \sigma_v = (-\lambda \sin u, \lambda \cos u, -v)$$


$$\hat N = \frac{N}{\|N\|} = \frac{1}{\sqrt{\lambda^2 + v^2}} (-\lambda \sin u, \lambda \cos u, -v)$$




???quote "Source code" 

    ```python
    --8<-- "mat363/scripts/helicoid.py"
    ```


<iframe
    width="720"
    height="480"
    src="./assets/helicoid.html"
    frameborder="0"
    allowfullscreen
></iframe>



### Example: Tube along some curve
Let $\gamma$ be a unit-speed space curve with $\kappa \neq 0$ everywhere. The tube is parameterized by 

$$\sigma(s, \theta) = \gamma(s) + a(\mathbf n(s)\cos\theta, +\mathbf b(s)\sin \theta)$$

The tube is hence obtained by a circle of radius $a$, where the center of the circle moves through $\gamma$ and the circle is always on the plane perpendicular to the curve. 

__Claim__ $\sigma$ is regular if $\kappa < a^{-1}$ everywhere

_proof_. For $s\in\mathbb R, \theta \in (0, 2\pi)$ (or any open interval of period $2\pi$)

\begin{align*}
\sigma_s &= \gamma'(s) + a(\cos\theta \mathbf n'(s) + \sin\theta \mathbf b'(s))\\
&= \mathbf t + a(\cos\theta (-\kappa\mathbf t+ \tau \mathbf b) - \sin\theta \tau\mathbf n)\\
&= (1 - a\cos(\theta)\kappa)\mathbf t + a\cos\theta\tau\mathbf b - a\sin\theta\tau \mathbf n\\
\sigma_\theta &= a\cos\theta \mathbf b - a\sin \theta \mathbf n\\
\sigma_s \times \sigma_\theta &= (1 - a\cos(\theta)\kappa)(a\cos\theta)(\mathbf t\times \mathbf b) - (1 - a\cos(\theta)\kappa)(a\sin\theta)(\mathbf t\times \mathbf n)\\
&= -a(1-a\kappa\cos\theta)(\cos\theta\mathbf n + \sin\theta\mathbf b)
\end{align*}

Then, $\sigma$ is regular if $1-a\kappa\cos\theta\neq 0$, note that if $\cos\theta\in (-1, 1)$, so that $a\kappa < 1 \implies 1-a\kappa\cos\theta > 0$

## Tangent and Derivatives

Find the tangent plane at given point

$\sigma(u,v) = (u, v, u^2 - v^2), (1, 1, 0)$

$$\sigma_u(1, 1)= (1, 0, 2u) = (1, 0, 2), \sigma_v(1, 1) = (0, 1, 2v) = (0, 1, 2)$$


$$\sigma_u\times \sigma_v(1, 1) = (-2, 2, 1)\implies -2x+2y+z =0$$


$\sigma(r,\theta) = (r\cosh \theta, r\sinh\theta, r^2), (1, 0, 1)$

$$\sigma_r(1, 0) = (\cosh \theta, \sinh\theta, 2r) = (1, 0, 2)$$

$$\sigma_\theta(1, 0) = (r\sinh\theta, r\cosh\theta, 2) = (0, 1, 2)$$

$$\sigma_u\times \sigma_v(1, 1) = (-2, -2, 1)\implies -2x-2y+z =0$$


__Claim__ If $f:\Sigma_1\rightarrow\Sigma_2$ is a local diffeomorphism and $\gamma$ is a regular curve on $\Sigma_1$. Then $f\circ \gamma$ is regular on $\Sigma_2$. 

_proof_. Let $\tilde \gamma := f\circ\gamma : \mathbb R\rightarrow \Sigma_2$

$$\frac{d\tilde\gamma}{dt} = D_\gamma f\frac{d\gamma}{dt}$$

where $D_\gamma f$ is locally intertible and $\gamma' \neq 0$ by regularity assumption. 
Therefore, $\tilde \gamma$ is also regular. 

## Surface of Revolution and Ruled Surfaces

### Example: Catenoid

The surface is obtained by rotating $x=\cosh z$ in xz-plane around z-axis. 

Take $\gamma(t) = (\cosh t, 0, t)$ so that 

$$\sigma(t,\theta) = (\cosh t\cos \theta, \cosh t\sin\theta, t)$$

Note that we need at least 2 patches $t\in\mathbb R, \theta\in (0,2\pi)$ or $\theta\in(-\pi,\pi)$



???quote "Source code" 

    ```python
    --8<-- "mat363/scripts/catenoid.py"
    ```



<iframe
    width="720"
    height="480"
    src="./assets/catenoid.html"
    frameborder="0"
    allowfullscreen
></iframe>



### Example: Mercator's Projection

Show that $\sigma(u,v) = (\text{sech} u\cos v, \text{sech} u\sin v, \text{tanh} u)$
is a regular surface patch for $\Sigma = \{x^2 + y^2 + z^2 = 1\}$. 

\begin{align*}
\|\sigma\|^2 &= \text{sech}^2 u\cos^2 v + \text{sech}^2 u\sin^2 v + \text{tanh}^2 u\\
&= \text{sech}^2 u + \text{tanh}^2 u\\
&= 1\\
\sigma_u &= (-\text{sech}(u)\text{tanh}(u)\cos v, -\text{sech}(u)\text{tanh}(u)\sin v, \text{sech}^2 u)\\
\sigma_v &= (-\text{sech} u\sin v, \text{sech} u\cos v, \text{tanh} u)\\
\sigma_u\times \sigma_v &= -\text{sech}^2 u (\text{sech} u\cos v, \text{sech} u\sin v, \text{tanh} u) \neq 0
\end{align*}
