# Gaussian  Curvatures


## Gaussian and Mean Curvatures

Let $W$ be the Weingarten maps of some oriented surface $\Sigma$ at point $p\in \Sigma$. The __Gaussian curvature__ $K$ and mean curvature $H$ of $\Sigma$ at $p$ are defined as 

$$K = \det (W), H = \frac{1}{2}Tr(W)$$


### Theorem 1
Let $\sigma$ be a surface patch of $\Sigma$. Then, $W_{p,\Sigma}$ w.r.t. basis $\{\sigma_u, \sigma_v\}$ of $T_p\Sigma$ is 

$$W = \begin{bmatrix}E&F\\F&G\end{bmatrix}^{-1}\begin{bmatrix}L&M\\M&N\end{bmatrix} = F_I^{-1}F_{II}$$


_proof_. Known that $W(\sigma_u) = -\mathbf N_u, W(\sigma_v) = -\mathbf N_v$. Let the linear matrix with 4 unknowns $W = \begin{bmatrix}a&b\\c&d\end{bmatrix}$ so that we have equations 

$$-\mathbf N_u = a\sigma_u + b\sigma_v, -\mathbf N_v = c\sigma_u + d\sigma_v$$

We also have that 

\begin{align*}
L &= -\sigma_{u}\mathbf N_u = \sigma_u (a\sigma_u + b\sigma_v) = aE + bF\\
M &= -\sigma_u\mathbf N_v = \sigma_u (c\sigma_u + d\sigma_v) = cE+dF\\
&= -\sigma_v\mathbf N_u = aF+bG\\
N &= -\sigma_v\mathbf N_v = \sigma_v(c\sigma_u + d\sigma_v) = cF + dG
\end{align*}

Thus, we can solve the 4 unknowns with 4 equations as 

$$\begin{bmatrix}L&M\\M&N\end{bmatrix} = \begin{bmatrix}E&F\\F&G\end{bmatrix}\begin{bmatrix}a&b\\c&d\end{bmatrix}$$




### Corollary 2

\begin{align*}
K &= \det(W) = \det(F_I)^{-1}\det(F_{II}) = \frac{LN-M^2}{EG-F^2}\\
H&= \frac{1}{2}tr(F_I^{-1}F_{II}) \\
&= \frac{1}{2(EG-F^2)}tr(\begin{bmatrix}G&-F\\-F&E\end{bmatrix}\begin{bmatrix}L&M\\M&N\end{bmatrix})\\
&= \frac{1}{2(EG-F^2)}tr\begin{pmatrix}LG-MF&MG-NF\\ME-LF&NE-MF\end{pmatrix}\\
&= \frac{LG-2MF+NE}{2(EG-F^2)}
\end{align*}

### Example: Surface z=f(x,y)

For surface $\Sigma = \{(x,y,z): z=f(x,y)\}$, define $\sigma(u,v) = (u,v,f(u,v))$. We have that 

\begin{align*}
\sigma_u &= (1, 0, f_x), \sigma_v = (0, 1, f_y)\\
\mathbf N &= \frac{(-f_x,-f_y,1)}{\sqrt{1+f_x^2+f_y^2} }\\
E &= 1+f_x^2, F = f_xfy, G = 1+f_y^2\\
\sigma_{uu} &= (0, 0, f_{xx}), \sigma_{uv} = (0, 0, f_{xy}), \sigma_{vv} = (0, 0, f_{yy})\\
L &= \frac{f_{xx} }{\sqrt{1+f_x^2+f_y^2} },
M  = \frac{f_{xy} }{\sqrt{1+f_x^2+f_y^2} },
N  = \frac{f_{yy} }{\sqrt{1+f_x^2+f_y^2} }\\
K &= \frac{LN-M^2}{EG-F^2} \\
  &= \frac{f_{xx}f_{yy} - f_{xy}^2}{1+f_x^2+f_y^2}\frac{1}{(1+f_x^2)(1+f_y^2) - f_x^2f_y^2}\\
  &= \frac{f_{xx}f_{yy} - f_{xy}^2}{(1+f_x^2+f_y^2)^2}\\
H &= \frac{1}{2(1+x^2+y^2)}\frac{(1+f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1+f_x^2)f_{yy} }{\sqrt{1+f_x^2+f_y^2} }\\
  &= \frac{(1+f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1+f_x^2)f_{yy} }{2(1+f_x^2+f_y^2)^{3/2} }
\end{align*}


## Principal Curvatures

Observe that $W$ is self-adjoint $2\times 2$ matrix, by eigen decomposition, we have that 

$$W(\mathbf t_1) = \kappa_1\mathbf t_1, W(\mathbf t_2) = \kappa_2\mathbf t_2$$

Call the eigenvalues $\kappa_1, \kappa_2$ the __principal curvatures__ and eigen vectors $\mathbf t_1,\mathbf t_2$ the __principal vectors__.

In addition, using linear algebra, determinant is the product of all eigen values, trace is the sum of all eigen values, 

$$K = \det(W) = \kappa_1\kappa_2, H = \frac{1}{2}Tr(W) = \frac{\kappa_1+\kappa_2}{2}$$


Also, by eigen decomposition, another corollary is that $\mathbf t_1,\mathbf t_2$ forms a orthonormal basis of $T_p\Sigma$.

Finding the principal values and principal vectors follow the standard approach for eigen decomposition, i.e. solve 

\begin{align*}\det(F_I^{-1}F_{II} - \kappa I)  &= \det(F_I^{-1}(F_{II} - \kappa F_I))\\
&= \det(F_{II} - \kappa F_I)\\ 
&= (L-\kappa E)(N-\kappa G) - (M-\kappa F)^2\\ 
&= 0\end{align*}

and each of the corresponding null space on $T_p\Sigma$. 


### Euler's Theorem
__Theorem__ Let $\Sigma$ be an oriented surface, $\gamma:\mathbb R\rightarrow\Sigma$ be a curve on $\Sigma$. Then, the normal curvature of $\gamma$ is 

$$\kappa_n = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta, \theta = \arccos(\mathbf t_1\cdot \gamma')$$


_proof_. Note that $\mathbf t_1,\mathbf t_2$ is a orthonormal basis, WLOG assume $\mathbf t_1\cdot\mathbf t_2 = \pi/2$ (otherwise, flip one of them). Therefore, by the turning angle 

$$\gamma' = \cos\theta\mathbf t_1 + \sin\theta \mathbf t_2$$

and the normal curvature, by bilinearity, is 

$$\kappa_n = II(\gamma', \gamma') = \cos^2\theta II(\mathbf t_1,\mathbf t_1) + 2\sin\theta\cos\theta II(\mathbf t_1,\mathbf t_2) +\sin^2\theta II(\mathbf t_2,\mathbf t_2 )$$

By orthonormal,

$$II(\mathbf t_1, \mathbf t_1) = \mathbf t_1 \kappa_1 \mathbf t_1 = \kappa_1, II(\mathbf t_1, \mathbf t_2) = 0, II(\mathbf t_2, \mathbf t_2) \mathbf t_2 \kappa_2 \mathbf t_2 =\kappa_2$$


__Corollary__ WLOG assume $\kappa_1 \geq \kappa_2$, then 

$$\kappa_1 = \arg\max_{\gamma:\mathbb R\rightarrow \Sigma}\kappa_{n,\gamma}, \kappa_2 = \arg\min_{\gamma:\mathbb R\rightarrow \Sigma}\kappa_{n, \gamma}$$ 

_proof_. By Eulers' Theorem, 

$$\kappa_n = \kappa_1 - (\kappa_1 - \kappa_2) \sin^2\theta$$

Since $\kappa_1\geq \kappa_2, \sin^2\theta \in [0, 1]$. The maximum is at $\sin^2\theta = 0\implies \kappa_n = \kappa_1$ and minimum is at $\sin^2\theta = 1\implies \kappa_n = \kappa_2$

### Example: Helicoid
$\sigma(u,v) = (v\cos u, v\sin u, \lambda u)$. 

$$\sigma_u = (-v\sin u, v\cos u, \lambda), \sigma_v = (\cos u, \sin u, 0), \mathbf N = \frac{(-\lambda \sin u, \lambda \cos u, -v)}{\sqrt{\lambda^2+v^2} }$$

$$E = v^2 + \lambda^2, F = 0, G = 1$$

$$\sigma_{uu} = (-v\cos u, -v\sin u, 0), \sigma_{uv} = (-\sin u, \cos u, 0), \sigma_{vv} = 0$$

$$L = (1-1)(v\lambda \cos u\sin u) + 0 = 0, M = \frac{\lambda}{\sqrt{\lambda^2+v^2} }, N = 0$$

$$K = \frac{1}{\lambda^2+v^2} \frac{-\lambda^2}{\lambda^2+v^2}= \frac{-\lambda^2}{(\lambda^2+v^2)^2}$$

$$(-\kappa (v^2 + \lambda^2))(-\kappa) - (\frac{\lambda}{\sqrt{\lambda^2+v^2} })^2 = \kappa^2 (v^2 + \lambda^2) - \lambda^2 (v^2 + \lambda^2)^{-1} = 0$$

$$\implies \kappa = \pm\lambda (v^2 + \lambda^2)^{-1}$$


### Example: Catenoid
$\sigma(u, v) = (\cosh u\cos v, \cosh u \sin v, u)$  


$$\sigma_u = (\sinh u\cos v, \sinh u\sin v, 1), \sigma_v = (-\cosh u\sin v, \cosh u\cos v, 0)$$


$$E = \sinh^2 u + 1 = \cosh^2 u, F = (-1 + 1)(\cdots) + 0 = 0, G = \cosh ^2 u$$


$$\mathbf N = \cosh^{-1}  u (-cos v, -\sin v, \sinh u)$$


\begin{align*}
\sigma_{uu} &= (\cosh u\cos v, \cosh u\sin v, 0)\\
\sigma_{uv} &= (-\sinh u \sin v, \sinh u\cos v, 0)\\
\sigma_{vv} &= (-\cosh u \cos v, -\cosh u \sin v, 0)
\end{align*}

\begin{align*}
L &= -\cosh^{-1}u(\cosh u) = -1\\
M &= (-1+1)(\cdots) + 0 = 0\\
N &= -\cosh^{-1}u(-\cosh u) = 1
\end{align*}

$$K = \frac{-1}{\cosh^4 u}$$


$$(-1 -\kappa \cosh^2 u)(1 - \kappa \cosh ^2 u) = 0\implies \kappa = \pm \cosh^{-2} u$$


## Umbilics


When $\kappa_1 = \kappa_2=:\kappa$, we must have that $W = \kappa I$, where $\mathbf t$ can be any tangent vector on $T_p\Sigma$. We define such point $p\in\Sigma$ being __umbilics__ IFF $W_{p,\Sigma} = \kappa I$ IFF principal curvatures $\kappa_1 = \kappa_2$.

__Theorem__ If all points $p\in \Sigma$ is an umbilic, then $\Sigma$ is an open subset of a plane or a sphere. 

_proof_. By the assumption, we have that $W\mathbf t = \kappa\mathbf t$ for all $p$ and all tangent vector $\mathbf t(p)$. Parameterize $\Sigma$ with $\sigma$, then 

$$W(\sigma_u)  = -\mathbf N_u = \kappa \sigma_u, W(\sigma_v) = -\mathbf N_v = \kappa\sigma_v$$

Then, note that $\mathbf N_{uv} = \mathbf N_{vu}$ where 

$$\mathbf N_{uv} = -\frac{\partial N_u}{\partial v} = -(\kappa_v \sigma_u + \kappa \sigma_{uv}) = -\frac{\partial N_v}{\partial u} = -(\kappa_u \sigma_v + \kappa \sigma_{uv})$$

Then, we have that $\kappa_v \sigma_u = \kappa_u \sigma_v$. However, $\sigma_u, \sigma_v$ is linearly independent, the equation holds IFF $\kappa_u = \kappa_v = 0\implies \kappa = c$. 

Suppose $\kappa = 0$, then $\mathbf N_u = \mathbf N_v = 0\implies \mathbf N$ is constant, hence $\sigma$ is an open subset of plane.  
Suppose $\kappa \neq 0$, then $\mathbf N = \kappa\sigma + \mathbf a$, hence $\sigma$ is an open subset of sphere. 

## Characterize the Points on the Surface

Principal values provides local information at $p$ and its neighborhood.  Let $p\in \Sigma$

By applying suitable translations, Euler angle rotations, reflections around the standard planes, WLOG, assume that 

 - $p = \mathbf 0$
 - $T_p\Sigma = \Pi_{XY}$ 
 - $\mathbf t_1 =  \mathbf e_1, \mathbf t_2 = \mathbf e_2$
 - $\mathbf N = \mathbf e_3$
 - $\sigma_0 = \sigma(0, 0) = p = \mathbf 0$

Then, the neighborhood $\sigma(u,v)$ of $p = \sigma_0$ can be approximated by 

$$\sigma(u,v) = u\sigma_u + v\sigma_v + \frac{1}{2}(u^2 \sigma_{uu} + 2uv\sigma_{uv} + v^2\sigma_{vv}) + rem.$$

The first-orders are on the $T_p\Sigma = \Pi_{XY}$ plane, and the second order terms are perpendicular to $xy$ plane, hence 

\begin{align*}
z &= \frac{1}{2}(u^2 \sigma_{uu} + 2uv\sigma_{uv} + v^2\sigma_{vv})\cdot \mathbf N \\
  &= \frac{1}{2}(Lu^2 + 2M uv + Nv^2)\\
  &= \frac{1}{2}II(u\sigma_u +v\sigma_v, u\sigma_u +v\sigma_v)
\end{align*}

Change the basis from $\sigma_u, \sigma_v$ to $\mathbf e_1,\mathbf e_2$, i.e. $u\sigma_u + v\sigma_v = x\mathbf e_1 + y\mathbf e_2$. 

\begin{align*}
z &= \frac{1}{2}II(u\sigma_u +v\sigma_v, u\sigma_u +v\sigma_v) \\
&= \frac{1}{2}W( x\mathbf e_1 + y\mathbf e_2)\cdot ( x\mathbf e_1 + y\mathbf e_2) \\
&= \frac{1}{2}(xW(\mathbf t_1) + yW(\mathbf t_2)) \cdot  ( x\mathbf e_1 + y\mathbf e_2)\\
&= \frac{1}{2}(\kappa_1 x,\kappa_2 y, 0)\cdot (x, y, 0)\\
&= \frac{\kappa_1 x^2 + \kappa_2x^2}{2}
\end{align*}

Therefore, we have 4 cases, the point $p$ is
1. __elliptic__ if $\kappa_1,\kappa_2$ are both non-zero and have the same sign 
2. __hyperbolic__ if $\kappa_1,\kappa_2$ are both non-zero and have different sign
3. __parabolic__ if exactly one of $\kappa_1,\kappa_2$ is 0.
4. __planar__ if both of $\kappa_1,\kappa_2$ are 0.

### Line of Curvature

A curve $\gamma: \mathbb R\rightarrow \Sigma$ is a __line of curvature__ if the tangent vector of $\gamma$ is a principal vector of $\Sigma$ at all $\gamma(t)$.  

__Claim__ This definition is equivalent to $\mathbf N' = -\lambda \gamma'$ for some constant $\lambda\in\mathbb R$

_proof_. By definition of principal vector, $\forall t. W(\gamma(t)) = \kappa \mathbf t(t)$ for some principal value $\kappa$. Note that $\mathbf N'= -W$ and $\mathbf t = \gamma' / \|\gamma'\|$, take $\lambda = \kappa / \|\gamma'\|$ we have the equality. 

__Claim__ This definition if equivalent to that for $\gamma(t) = \sigma(u(t), v(t))$

$$(EM-FL)u'^2 + (EN-GL)u'v' + (FN-GM)v'^2 = 0$$

_proof_. Note that $\gamma' = u'\sigma_u + v'\sigma_v$, we have that $F_I^{-1}F_{II} = \lambda I\implies F_{II} = \lambda F_I$
