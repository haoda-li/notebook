# First Fundamental Form

## First Fundamental Form

Let $E = \|\sigma_u\|^2, F = \sigma_u\cdot\sigma_v, G = \|\sigma_v\|^2$, consideer the matrix 
$M = \begin{bmatrix}E&F\\F&G\end{bmatrix}$, note that $E, G$ are always positve, and since $\det(M) = EG-F^2 > 0, M$ is always a postive definite symmetric matrix. 

Consider the inner product equipped with dot product and restricted to the tangent plane at $p$. Then, for any $v\in T_p\Sigma$, 

$$\langle v, v\rangle_{T_p\Sigma} = \|a\sigma_u + b\sigma_v\|^2 = Ea^2 + 2Fab + Gb^2$$


The First fundamentally form is the expression 

$$\langle v, v\rangle_{T_p\Sigma} = Eu'^2 + 2Fu'v' + Gv'^2$$


## Arc-length of curve on surface

Let $\gamma: \mathbb R\rightarrow \Sigma$ be some smooth curve on the surface $\Sigma$, then for some parameterization $\sigma$ (assuming the surface is covered by one patch) we have that 

$$\gamma(t) = (x(t), y(t), z(t)) = \sigma(u(t), v(t))$$

Since $\sigma$ is a homeomorphism, such $u,v$ exists and are smooth. Therefore, for some segment of the curve, 

\begin{align*}
L &= \int \|\gamma'(t)\| dt\\
&= \int \|\frac{\partial \sigma}{\partial u}\frac{du}{dt}+\frac{\partial \sigma}{\partial v}\frac{dv}{dt}\|dt\\
&= \int \sqrt{(\sigma_u\cdot\sigma_u) (u')^2+ 2(\sigma_u\sigma_v) u'v' + (\sigma_v\cdot\sigma_v) (v')^2}dt\\
&= \int \sqrt{E(u')^2 + 2F(u'v') + G(v')^2} dt
\end{align*}

## Area of Surface 
Assume doamin $\Omega \subseteq \sigma(U)$, say $\Omega = \sigma(U_1)$. The area of $U_1$ is then integrated by $\iint_{U_1}dudv$, i.e. integrate along each square $(u, v), (u+du, v+dv)$. For small $du,dv$, since $\sigma$ is a local diffeomorphism, it is approximated by the tangent plane $\sigma_u, \sigma_v$. Therefore, the area of the mapped square is $\|\partial_u\times \partial_v\|$, by change of variable, 

\begin{align*}
A(\Omega) &= \iint_{U_1} \|\partial_u\times \partial_v\| dudv\\
&= \iint_{U_1} \sqrt{(\sigma_u\cdot \sigma_u)(\sigma_v\cdot \sigma_v) - (\sigma_u\cdot\sigma_v)^2} dudv\\
&= \int_{U_1} \sqrt{EG - F^2} dudv
\end{align*}

## Angle between Curves
Let $\gamma_1: \mathbb R\rightarrow \Sigma, \gamma_2: \mathbb R\rightarrow\Sigma$ with $\gamma_1(t_1) = \gamma_2(t_2) = p\in\Sigma$. 
Then, at point $p, \gamma'_1, \gamma'_2 \in T_p\Sigma$.  

Define __angle__ two 2 curves on the surface as the angle on $T_p\Sigma$ at intersection point $p$. 

Note that for each $\gamma = \sigma(u(t), v(t))$ for $u,v:\mathbb R\rightarrow\mathbb R$, its derivative is

$$\frac{d}{dt} (\sigma(u(t), v(t))) = \sigma_u\cdot u' + \sigma_v\cdot v'$$

Therefore, the angle is defined as 

\begin{align*}
\angle(\gamma_1,\gamma_2) &= \arccos(\frac{\gamma_1'}{\|\gamma_1'\|}\cdot \frac{\gamma_1'}{\|\gamma_1'\|})\\
&= \frac{(\sigma_{u}\cdot u_1' + \sigma_{v}\cdot v_1')\cdot(\sigma_{u}\cdot u_2' + \sigma_{v}\cdot {v_2}')}{\|\gamma_1'\|\|\gamma_2'\|}\\
&= \frac{(\sigma_u\cdot\sigma_u) (u_1'\cdot u_2') + (\sigma_u\cdot\sigma_v)(u_1'v_2'+u_2'v_1') + (\sigma_v\cdot\sigma_v) (v_1'\cdot v_2')}{(E(u'_1)^2 + 2F(u_1'\cdot v_1') + G(v_1')^2)(E(u'_2)^2 + 2F(u_2'\cdot v_2') + G(v_2')^2)}\\
&= \frac{E (u_1'\cdot u_2') +F(u_1'v_2'+u_2'v_1') + G (v_1'\cdot v_2')}{(E(u'_1)^2 + 2F(u_1'\cdot v_1') + G(v_1')^2)(E(u'_2)^2 + 2F(u_2'\cdot v_2') + G(v_2')^2)}
\end{align*}

### Example: Parameter Curve
The parameter curves on a surface patch $\sigma(u,v)$ can be parametrized by 

$$\gamma_1(t) = \sigma(u_0, t), \gamma_2(t) = \sigma(t, v_0)$$

so that $D\gamma_1 = (1, 0), D\gamma_2 = (0, 1)$ 
$\cos\theta = \frac{E(0) + F(1) + G(0)}{\sqrt{EG} } = \frac{F}{\sqrt{EG} }$

## Examples 

$\sigma = (\sinh u\sinh v, \sinh u\cosh v, sinh u)$

\begin{align*}
\sigma_u &= (\cosh u\sinh v, \cosh u\cosh v, \cosh u)\\
\sigma_v &= (\sinh u\cosh v, \sinh u\sinh v, 0)\\
E = \sigma_u\cdot\sigma_v &= \cosh^2 u\sinh^2 v + \cosh^2 u\cosh^2 v + \cosh^2 u \\
&= \cosh^2 u((\sinh^2 v + 1)+\cosh^2 v)\\
&= \cosh^2 u (\cosh^2 v + \cosh^2 v)\\
&= 2\cosh^2u \cosh^2 v\\
F = \sigma_u\cdot\sigma_v &=2\cosh u\cosh v\sinh u\sinh v\\
G = \sigma_v\cdot\sigma_v &=\sinh^2 u (\cosh^2 v + \sinh^2 v) = \sinh^2 u \cosh (2v)\\
\end{align*}

$\sigma = (u-v, u+v, u^2+v^2)$

$$\sigma_u = (1, 1, 2u)\sigma_v = (-1, 1, 2v)$$

$$(2 + 4u^2)du^2 + 8uv dudv + (2+4v^2)dv^2$$


$\sigma = (\cosh u, \sinh u, v)$

$$\sigma_u = (\sinh u, \cosh u, 0)\sigma_v = (0, 0, 1)$$

$$(\sinh^2 u +\cosh^2 u)du^2 + dv^2$$


$\sigma = (u, v, u^2+v^2)$

$$\sigma_u = (1, 0, 2u)\sigma_v = (0, 1, 2v)$$

$$(1 + 4u^2)du^2 + 8uv dudv + (1+4v^2)dv^2$$


???quote "Source code"

    ```python
    --8<-- "mat363/scripts/fff.py"
    ```

```plotly
{"file_path": "mat363/assets/fff.json"}
```



## First Fundamental Forms with Reparameterization

__Theorem__ Let $\tilde \sigma(\tilde u, \tilde v)$ be a reparameterization of some $\sigma(u,v)$ with transformation map $\Phi$. Then, the first fundamental form of the reparameterization is 

$$\begin{bmatrix}\tilde E &\tilde F\\\tilde F&\tilde G\end{bmatrix} = J(\Phi)^T \begin{bmatrix}E&F\\F&G\end{bmatrix}J(\Phi)$$

where $J$ is the Jacobian matrix of $\Phi$. 

_proof_. First, by the reparameterization, we have that $(u, v) = \Phi(\tilde u, \tilde v)$, therefore 

$$\frac{\partial u}{\partial t} = \frac{\partial u}{\partial \tilde u}\frac{\partial \tilde u}{\partial t}+\frac{\partial u}{\partial \tilde v}\frac{\partial \tilde v}{\partial t}, \frac{\partial v}{\partial t} = \frac{\partial v}{\partial \tilde u}\frac{\partial \tilde u}{\partial t}+\frac{\partial v}{\partial \tilde v}\frac{\partial \tilde v}{\partial t}$$

If we plug in this, we have that the first fundamental form of $\tilde \sigma$ is

$$E(\partial_{\tilde u} u\tilde u' + \partial_{\tilde v} u\tilde v')^2 + 2F(\partial_{\tilde u} u\tilde u' + \partial_{\tilde v} u\tilde v')(\partial_{\tilde u} v\tilde u' + \partial_{\tilde v} v\tilde v') + G(\partial_{\tilde u} v\tilde u' + \partial_{\tilde v} v\tilde v')^2$$

Simplify the equation, we can have the formula as wanted

$$\begin{bmatrix}\tilde E &\tilde F\\\tilde F&\tilde G\end{bmatrix} = 
\begin{bmatrix}\partial_{\tilde u} u &\partial_{\tilde u} v\\\partial_{\tilde v} u&\partial_{\tilde v} v\end{bmatrix} 
\begin{bmatrix}E&F\\F&G\end{bmatrix}
\begin{bmatrix}\partial_{\tilde u} u &\partial_{\tilde v} u\\\partial_{\tilde u} v&\partial_{\tilde v} v\end{bmatrix}$$

### Example: Surface of Revolution
For surface pf revolution 

$$\sigma(u,v) = (f(u)\cos v, f(u)\sin v, g(u))$$

with the assumption that $\gamma(t) = (f(t), g(t))$ resides on the plane is unit-speed. 
Then, we have 

$$\sigma_u = (f'\cos v, f'\sin v, g'), \sigma_v = (-f\sin v, f\cos v, 0)$$


$$E = f'^2+g'^2 = 1, F = 0. G = f^2$$

Therefore, the first fundamental form is 

$$u'^2 + f(u)^2 v'^2$$


For sphere, we have $f(u) = \cos u$, which implies the first fundamental form is 

$$u'^2 + \cos^2 u v'^2$$

