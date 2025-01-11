# Isometric, Conformal, Equiareal

## Isometry
Let $f:\Sigma_1\rightarrow\Sigma_2$ be smooth. $f$ is a __local isometry__ if any curve $\gamma_1$ in $\Sigma_1$ has the same length as $\gamma_2 = f\circ \gamma_1$. Then, $\Sigma_1, \Sigma_2$ are locally isometric. 

If $f$ is a local isometry and a diffeomorphism, then $f$ is a __isometry__. 

Also, for notation, define 

$$f^*\langle v,w\rangle_p := \langle D_pf(v),D_pf(w)\rangle_{f(p)}$$


__Theorem__ $f$ is a local isometry IFF the first fundamental form for $p$ on $\Sigma_1$ is the same as $f(p)$ on $\Sigma_2$. 

_proof_. Let $\gamma_1: \mathbb R\rightarrow \Sigma_1, \gamma_2 = f\circ \gamma_1: \mathbb R\rightarrow\Sigma_2$.  
$\Rightarrow$: Assume $f$ preserves the length of the curve. Then, for any $t_0<t_1$, we have that $\int_{t_0}^{t_1}\|\gamma_1'\|dt = \int_{t_0}^{t_1}\|\gamma_2'\|dt$. Implying that $\|\gamma'_1\| = \|\gamma_2'\|$
By chain rule, 

$$\gamma'_2 = (f\circ \gamma_1)' = D_pf \gamma_1'$$

Note that $D_pf \gamma_1'$ lies on the tangent plane $T_{f(p)}\Sigma_2$ since $D_pf: T_p\Sigma_1\rightarrow T_{f(p)}\Sigma_2$.  
Therefore, we have that 

$$\|\gamma'\|_1^2 = \langle \gamma_1',\gamma_1'\rangle_{T_p\Sigma_1} = \langle  D_pf \gamma_1',  D_pf \gamma_1'\rangle_{T_f(p)\Sigma_2}$$


$\Leftarrow$: Assume $\langle \gamma_1',\gamma_1'\rangle_{T_p\Sigma_1} = \langle  D_pf \gamma_1',  D_pf \gamma_1'\rangle_{T_f(p)\Sigma_2}$, then 
$\|\gamma'_1\| = \langle \gamma_1',\gamma_1'\rangle_{T_p\Sigma_1}, \|\gamma'_2\| = \langle  D_pf \gamma_1',  D_pf \gamma_1'\rangle_{T_f(p)\Sigma_2}$ and it is proven. 

__Corollary__ $f$ is an local isometry if $\sigma_1: \mathbb R^2 \rightarrow V\cap\Sigma_1$ has the same fundamental form as $f\circ \sigma_1$.

### Example: Cylinder 
__Claim__. Cylinder is locally isometric to a plane. 

_proof_. Consider the unit cylinder $\sigma(u,v) = (\cos u, \sin u, v)$. Then, 

$$\sigma_u = (-\sin u, \cos u, 0), \sigma_v = (0, 0, 1)$$


$$E = \sin^2 u + \cos^2 u = 1, F = 0, G = 1$$

The first fundamental form is $u'^2 + v'^2$, is the same as the plane.  
However, this is not an isometry, since $\sigma(0, v) = \sigma(2\pi, v)$ is not injective. 

### Example: Tangent Developables. 
A tangent developable can be parameterized as 

$$\sigma(u,v) = \gamma(u) + v(\gamma'(u))$$

In other words, the union of all the tangent lines to a curve. 

__Claim__ Tangent developables are isometric to a plane.  
Assume $\gamma$ is unit-speed, 

$$\sigma_u = \gamma'(u) + v\gamma''(u), \sigma_v = \gamma'(u)$$

\begin{align*}
N &= \sigma_u\times \sigma_v\\
  &= (\gamma' + v\gamma'')\times (\gamma')\\
  &= (\mathbf t \times \mathbf t) + v\kappa\mathbf n\times \mathbf t\\
  &= 0 + v\kappa(-\mathbf b)\\
  &= -v\kappa\mathbf b
\end{align*}

Therefore, tangent developables are regular IFF $v\neq 0, \kappa>0$

\begin{align*}
E &= \|\gamma'\|^2 + v\gamma'\cdot\gamma'' + v^2\|\gamma''\|^2 = 1 + v^2\kappa^2\\
F &= (\gamma' + v\gamma'')\cdot \gamma' = 1\\
G &= \gamma'\cdot\gamma' = 1
\end{align*}

Note that there exists a unit-speed plane curve with signed curvature being $\kappa$. And note that it's a tangent developable in a plane, hence has the same first fundamental form. 

### Example: Cone
Consider the standard circular cone 

$$\sigma: (0, \infty)\times (0, 2\pi) \rightarrow \mathbb R^3. \sigma(u,v) = (u\cos v, u\sin v, u)$$

Find its isometry from the xy-plane. 

First, its 1st fundamental form is 

$$\sigma_u = (\cos v, \sin v, 1), \sigma_v = (-u\sin v, u\cos v, 0)$$


$$E = 2, F = 0, G = u^2$$

Then, to map from xy-plane, we want some $x(u, v)$ and $y(u,v)$ s.t. $\tilde\sigma(u, v) = (x(u, v), y(u, v), 0)$ and the same 1st fundamental form

$$x_u^2 + y_u^2 = 2, x_v^2 + y_v^2 = u^2, x_ux_v + y_uy_v = 0$$


$$x = \sqrt{2} u\cos(v/\sqrt 2), y = \sqrt{2} u\sin(v/\sqrt 2)$$


### Example: Catenoid to Helicoid
A catenoid is parameterized as $\sigma^c(u, v) = (\cosh u\cos v, \cosh u\sin v, u)$  
A helicoid is parameterized as $\sigma^t(u, v) = (u\cos v, \sin v, v)$

__Claim__ the map from $\sigma^c(u,v) \implies \sigma^t(\sinh u, v)$ is an isometry.

_proof_. (some computations are skipped)

$$E^c = \sinh^2 u + 1 = \cosh^2 u, E^t = \cosh^2 u$$


$$F^c = (-1 + 1)\sinh u\cos h u \sin v\cos v = 0 = F^c$$


$$G^c = \cosh^2 u(\cos^2 v + \sin^2 v) = \cosh^2, G^t = \sinh^2 u + 1 = \cosh^2 u$$


Define an isometric deformation of the catenoid into a helicoid. First define 

$$\sigma^{-t}(u,v) = (-\sin h u\sin v, \sinh u\cos v, -v)$$

which reflect $\sigma^{t}$ in the xy-plane and translating it by $\pi/2$ parallel to the z-axis. Then, define 

$$\sigma^{ct} = \cos(t) \sigma^c(u,v) + \sin(t)\sigma^{-t}(u,v)$$

t
__Claim__ This isometric deformation is a local isometry, regardless of the choice of $t$. 

_proof_. First, note that the first fundamental forms of $\sigma^c,\sigma^t, \sigma^{-t}$ are all the same since they are all isometric (rotation and translation are isometric transformations). 
Then, note that $\cos^2 t+ \sin^2 t = 1$ and $t$ is not related to $u,v$, hence are scalars in partial derivatives. Therefore, as $\sigma^{ct}$ is a linear transformation of $\sigma^c, \sigma^{-t}$, it is also isometric. 

## Conformal Mappings of Surfaces

For $f: \Sigma_1\rightarrow\Sigma_2$ being a local diffeomorphism, $f$ is a __conformal map__ if for any two curves $\gamma_1, \gamma_2$ on $\Sigma_1$, The angle at intersection $p$ is equal to the angle between $f(\gamma_1(\mathbb R)), f(\gamma_2(\mathbb R))$ at point $f(p)$. 

In short, $f$ is conformal IFF it preserves angles. 

__Theorem__ $f$ is conformal IFF exists $\lambda: \Sigma_1\rightarrow \mathbb R$ s.t. 

$$\forall p \in \Sigma_1. f^*\langle v,w\rangle_p = \lambda(p) \langle v,w\rangle_p$$


_proof_.  
$\Rightarrow$ Assume that the angle is preserved 

$$\frac{\langle \gamma_1', \gamma_2'\rangle}{\langle  \gamma_1', \gamma_1'\rangle^{1/2}\langle  \gamma_2', \gamma_2'\rangle^{1/2}} = \frac{f^*\langle \gamma_1', \gamma_2'\rangle}{f^*\langle  \gamma_1', \gamma_1'\rangle^{1/2}f^*\langle  \gamma_2', \gamma_2'\rangle^{1/2}}$$

Since $\gamma_1,\gamma_2$ are choose arbitrarily, this is equalent to any vecto on $T_p\Sigma_1$.  
Take $\{v_1, v_2\}$ be the orthonormal basis of $T_p\Sigma_1$. Let $v = v_1, w = \cos\theta v_1 + \sin\theta v_2$ so that $v\cdot w = \cos \theta (v_1\cdot v_1) + \sin\theta (v_1\cdot v_2) = \cos\theta$

Note that $f^*\langle \cdot, \cdot\rangle$ is also dot product restricted to $T_{f(p)}\Sigma_2$. Therefore, 

\begin{align*}
f^*\langle v, v\rangle &= f^*\langle v_1, v_1\rangle\\
f^*\langle v, w\rangle &= cos\theta f^*\langle v_1, v_1\rangle + \sin\theta  f^*\langle v_1, v_2\rangle\\
f^*\langle w, w\rangle &= cos^2\theta f^*\langle v_1, v_1\rangle  + 2\sin\theta\cos\theta f^*\langle v_1, v_2\rangle + \sin^2\theta f^*\langle v_2, v_2\rangle\\
\end{align*}

Write $\lambda = f^*\langle v_1, v_1\rangle, \mu = f^*\langle v_1, v_2\rangle, \nu = f^*\langle v_2, v_2\rangle$ and by our assumption, we have 

$$\cos\theta = \frac{\lambda \cos\theta + \mu\sin\theta}{\lambda^{1/2}(\lambda\cos^2\theta + 2\mu\sin\theta\cos\theta + \nu\sin^2\theta)^{1/2}}$$

We can solve it for $\theta = \pi/2$, implying 

$$\lambda = \lambda\cos^2\theta + \nu\sin^2\theta$$

Therefore, $\lambda = \nu\implies \lambda = f^*$

$\Leftarrow$, Assume that $\forall p \in \Sigma_1. f^*\langle v,w\rangle_p = \lambda(p) \langle v,w\rangle_p$, then $\lambda$'s cancles out in the angle equation. 

$$\frac{\lambda(p)\langle \gamma_1', \gamma_2'\rangle}{  \lambda(p)^{1/2}\langle\gamma_1', \gamma_1'\rangle^{1/2}\lambda(p)^{1/2}\langle  \gamma_2', \gamma_2'\rangle^{1/2}} = \frac{\langle \gamma_1', \gamma_2'\rangle}{\langle  \gamma_1', \gamma_1'\rangle^{1/2}\langle  \gamma_2', \gamma_2'\rangle^{1/2}}$$


__Corollary__ $f$ is conformal IFF for any patch $\sigma_1$ of $\Sigma_1$ and $\sigma_2 = f\circ \sigma_1$ of $\Sigma_2$, their first fundamental forms are proportional. 

### Example: Stereographic Projection

Consider a standard sphere $S = \{x^2 + y^2 + z^2 = 1\}$ and XY-plane. Define $\mathbf n = (0, 0, 1)$, i.e. the north pole of the sphere. The sterepographic projection maps $\mathbf q \in S$ to $\mathbf p \in \Pi_{XY}$ s.t. $n, p, q$ lie on the same straight line, i.e. 

$$\mathbf q - \mathbf n = c(\mathbf p-\mathbf n), \|\mathbf p\|^2 = 1$$

Now we have 3 equations and 3 unknowns if $\mathbf q$ known, or 4 if $\mathbf p$ known

\begin{align*}
x - 0 = c(u - 0)&\implies x &= cu\\
y - 0 = c(v - 0)&\implies y &= cv\\
z - 1 = c(0 - 1)&\implies 1 - z &= c\\
&x^2 + y^2 + z^2 &= 1
\end{align*}

Therefore, the sterepographic projection $\Pi: S^2-\{\mathbf n\} \rightarrow \Pi_{XY}$ is defined as

$$\Pi(x, y, z) = (\frac{x}{1-z}, \frac{y}{1-z}, 0)$$

and a parameterization of $S^2-\{\mathbf n\}$ is

$$\sigma_1(u, v) = \frac{1}{u^2+v^2+1}(2u, 2v, u^2+v^2-1)$$


__Claim__ sterepographic projection $\Pi$ is conformal. 
Let $\sigma_2 (u, v) = (u, v, 0)$ be a parameterization of XY-plane, and we have that $\Pi\circ\sigma_1 = \sigma_2$, we need to show that first fundamental form of $\sigma_1$ is proportional to that of $\sigma_2$.

\begin{align*}
\sigma_{1u} &= \frac{-2u}{(u^2+v^2+1)^2}(2u, 2v, u^2+v^2-1) + \frac{1}{u^2+v^2+1}(2, 0, 2u)\\
&= \frac{1}{(u^2+v^2+1)^2}(2(v^2-u^2+1), -4uv, 4u)\\
\sigma_{1v} &= \frac{1}{(u^2+v^2+1)^2}(-4uv, 2(u^2-v^2+1), 4u)\\
E_1 &= \frac{1}{(u^2+v^2+1)^4}(4(v^2-u^2+1)^2 + 16u^2v^2 + 16u^2) = \frac{4}{(u^2+v^2+1)^2}\\
G_1 &=  \frac{4}{(u^2+v^2+1)^2}\\
F_1 &=  \frac{1}{(u^2+v^2+1)^4}(-(8uv(v^2-u^2 + 1+u^2-v^2+1) + 16uv) = 0
\end{align*}

Note that $E_2= G_2 = 1, F_2 = 0$, so that take 

$$\lambda =  \frac{4}{(u^2+v^2+1)^2}$$

and we have the conclusion.


???quote "Source code"
  
    ```python 
    --8<-- "mat363/scripts/isometry.py"
    ```


```plotly
{"file_path": "mat363/assets/isometry.json"}
```

### Example: Enneper's Surface
Parameterize the surface as 

$$\sigma(u, v) = (u - \frac{u^3}{3} + uv^2, v - \frac{v^3}{3} + vu^2, u^2-v^2)$$


__Claim__ The Enneper's Surface is conformally parameterized. 
The first fundamental form is

$$\sigma_u = (1-u^2+v^2, 2uv, 2u), \sigma_v = (2uv, 1-v^2+u^2, -2v)$$


$$E = (1-u^2+v^2)^2 + 4u^2v^2+4u^2 = 1+u^2+v^2$$


$$G = E = 1+u^2+v^2$$


$$F = 4uv-4uv = 0$$

Define $\lambda(u,v) = 1+u^2+v^2$, this surface is conformal to the plane. 

### Example: Mercator Parameterization

Known that the first fundamental form for the sphere is $du^2 + \cos^2 udv'^2$, find a smooth function $\phi$ s.t. the reparameterization $\tilde \sigma (u,v) = \sigma(\phi(u), v)$ is conformal. 

Note that the Jacobian of the transformation is 

$$J = \begin{bmatrix}\partial_{\tilde u} u &\partial_{\tilde v} u\\\partial_{\tilde u} v&\partial_{\tilde v} v\end{bmatrix} = \begin{bmatrix}\phi' &0\\0&1\end{bmatrix}$$

so that the first fundamental form of $\tilde \sigma$ is

$$\tilde E = (\phi'^2 E) = \phi'^2, \tilde F = (\phi' F) = 0, \tilde G = G = \cos^2 (\phi(u)) $$

Therefore, $\tilde \sigma$ is conformal IFF $\phi'^2 = \cos(\phi)$

We can verify this on Mercator Parameterization, taking $\cos\phi = \text{sech} u$ and we can verify that this is proven. 

## Equiareal Map
For $f: \Sigma_1\rightarrow \Sigma_2$ by a local diffeomorphism, $f$ is __equiareal__ if for any open subset $W\subset \Sigma_1$ has the same area as $f(W)\subset \Sigma_2$. 

__Theorem__ $f: \Sigma_1\rightarrow \Sigma_2$ is equiareal IFF 

$$E_1G_1-F_1^2 = E_2G_2- F_2^2$$


_proof_. By the integral of area (see [First Fundamental Form](./fff.md)), and this comes directly from the equation. 

### Archimedes' Theorem
Let $S^2 = \{(x,y,z): x^2+y^2+z^2 = 1\}$ be the unit sphere and $C = \{(x,y,z): x^2+y^2 = 1\}$ be the unit cylinder. For each point $p = (x,y,z)\in S^2 -\{(0,0,1), (0, 0, -1)\}$, $p$ can be mapped to $q =(X,Y,z)= f(p)\in C$ via the ray connecting $(0, 0, z), p, q$.

$$f: (x,y,z)\rightarrow (X = \lambda(x,y,z)x, Y = \lambda(x,y,z)y, z)$$

Note that $X^2 + Y^2 = 1\implies \lambda(x^2 + y^2) = 1\implies \lambda = \frac{1}{\sqrt{x^2+y^2}}$, so that we can obtain 

$$f(x,y,z) = (\frac{x}{\sqrt{x^2+y^2}}, \frac{y}{\sqrt{x^2+y^2}}, z)$$


__Claim__ $f$ is equiareal. 

_proof_. Parameterize $S^2$ using $\sigma_1(u,v) = (\cos u \cos v, \cos u \sin v, \sin u)$, so that 

$$\sigma_2: \mathbb R^2\rightarrow C. \sigma_2 = f\circ\sigma_1 = (\cos v, \sin v, \sin u)$$

For $\sigma_1$, this is the sphere, known that $E_1 = 1, F_1 = 0, G_1 = \cos^2 u$  
For $\sigma_2$, $E_2 = \|(0, 0, \cos u)\|^2 = \cos^2 u, G_2 = \|(-\sin v, \cos v, 0)\|^2 = 1, F_2 = 0$.   
Therefore, $E_1G_1-F_1^2 = E_2G_2 - F_2^2$. Hence it is equiareal. 

__Lemma__ $A\times B \times C = (A\cdot C)B - (A\cdot B)C$

_proof_. Note that $S = A\times (B\times C)$ will be perpendicular to $A$ and $B\times C$, hence should reside on $\text{span}\{B,C\}$.  
Let $S = mB + nC$, Note that $S\cdot A = 0$, 

$$mB\cdot A + nC\cdot A = 0$$

This equation must be valid for any $A,B,C$, so that let $m =  (C\cdot A), n = - (B\cdot A)$ and we obtain the equation in the claim. 

__Theorem__ For $\sigma(u,v)$ be a surface patch, and $ N$ be the unit normal. 

$$N \times \sigma_u = \frac{E\sigma_v - F\sigma_u}{\sqrt{EG - F^2}}, N \times \sigma_v = \frac{F\sigma_v - G\sigma_v}{\sqrt{EG - F^2}}$$


_proof_. First, note that $N = \frac{\sigma_u\times\sigma_v}{\|\sigma_u \times \sigma_v\|} = \frac{\sigma_u\times\sigma_v}{\sqrt{EG-F^2}}$.  
Then, apply the lemma on the equations. 
