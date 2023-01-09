# Surface Tangents and Derivatives

## Tangent Plane

The __tangent vector__ to a surface $\Sigma$ at point $p$ are tangent vector to all smooth curves on $\Sigma$ through $p$ at $p$. 

The __tangent plane__ to a surface $\Sigma$ at point $p$ is a 2-dim linear subspace of $T_p\Sigma\subset\mathbb R^3$, a.k.a. a plane in $\mathbb R^3$ pass through the origin. its points are precisely all tangent vectors to $\Sigma$ at $p$. 



### Spanning Tangent Plane


__Claim__ Let $\sigma:U\rightarrow V\cap \Sigma$ be a surface path containing $p$. If $U$ is spanned by vectors $u, v$, then $T_p\Sigma$ is spanned by $d_u\sigma, d_v\sigma$. 

_proof_. Consider a surface patch $\sigma: U\rightarrow V\cap \Sigma$ containing $p$. Let $\gamma$ be a smooth curve in $S$ with some $\gamma(t_0) = p$. Then, consider $\mathbf a:[t_0-\epsilon, t_0+\epsilon]\rightarrow U$ s.t. $\gamma(t) =\sigma(\mathbf a(t)))$, a.k.a. $\mathbf a$ is a path on $U$ that is mapped to $\gamma$. Then, we must have that $\mathbf a$ is a smooth curve on $U$. 

Let $a(t) = (u(t), v(t))$, then by chain rule, we have 

$$\frac{d\gamma}{dt} = \frac{d\sigma}{d\mathbf a}\frac{d\mathbf a}{dt} = \frac{d\sigma}{du}\frac{du}{dt} + \frac{d\sigma}{dv}\frac{dv}{dt}$$

Therefore, $\frac{d\gamma}{dt}$ is spanned by $d_u\sigma,d_v\sigma$. 

Conversely, define $\tilde \gamma(t) = \sigma(u(t_0)+\lambda t, v(t_0) + \mu t)$ for some $\lambda, \mu$. Then, $\tilde \gamma$ is a smooth curve in $\Sigma$ and $\gamma(0) = p$ we have that 

$$\frac{d\tilde \gamma}{dt} = \frac{d\sigma}{du}\lambda + \frac{d\sigma}{dv}\mu$$

Therefore, every vector in $\text{span}\{d_u\sigma, d_v\sigma\}$ is the tangent vector at $p$ of $\Sigma$. 

By regularity assumption of $\sigma$, we have that $\text{span}\{d_u\sigma, d_v\sigma\}$ are 2-dim, hence spans a plane, in which we call it the __tangent plane__. 

### Independence of surface patch choices
__Claim__ For some surface path $\sigma(u,v)$ at $p$, the spanned subset space of $d_u\sigma, d_v\sigma$ independent of the choice of $\sigma$. 

_proof_. Suppose that $\tilde \sigma: \tilde U\rightarrow V\cap \Sigma$ is a reparameterization of the surface patch. Then, note that both $\sigma, \tilde\sigma$ are bijective and smooth. Therefore, exists a bijective smooth map $\phi: U\rightarrow\tilde U$ s.t. $(\tilde u, \tilde v) = \phi(u,v)$. Then, we have 

\begin{align*}
\sigma(u,v) &= \tilde\sigma(\tilde u(u, v), \tilde v(u, v))\\
\frac{d\sigma}{du} &= \frac{d\tilde \sigma}{d\tilde u}\frac{d\tilde u}{du} + \frac{d\tilde \sigma}{d\tilde v}\frac{d\tilde v}{du}\\
\frac{d\sigma}{dv} &= \frac{d\tilde \sigma}{d\tilde u}\frac{d\tilde u}{dv} + \frac{d\tilde \sigma}{d\tilde v}\frac{d\tilde v}{dv}
\end{align*}

Therefore, $d_u\sigma$ and $d_v\sigma$ are both linear combinations of $d_{\tilde u}\tilde \sigma, d_{\tilde v}\tilde \sigma$. 

## Surface Derivatives

### Implicit Function Theorem


By inverse function theorem, for non-linear function $F$  
IF  $F(\mathbf x_0) = \mathbf y_0 ,DF(\mathbf x)$ is invertible, and $y_0 + DF(x_0)(x-x_0)$ is invertible  
THEN, the inverse exists, $F^{-1}(\mathbf y_0)= \mathbf x_0, \mathbf y = \mathbf x_0 + DF^{-1}|_{\mathbf y_0}(\mathbf y-\mathbf y_0)$



### Regularity Conditions
__Claim__ for any point $p$ on the __regular__ surface $\Sigma$, there exists an open set $V\subset \Sigma$ s.t. $p\in V$ and $V$ is the graph of a smooth function $z=\phi(x,y), y=\varphi(x,z), x=\psi(y,z)$.

In other words, for any points on a surface. Locally, the surface patch can be mapped from a standard plane. 

_proof_. Let $\sigma^{-1}(p) = (u_0, v_0)$. Consider the surface patch mapping $\sigma$, by regularity we have that 

$$D\sigma = \begin{bmatrix}\partial_u x&\partial_vx\\\partial_uy&\partial_vy\\\partial_u z&\partial_vz\end{bmatrix}$$ 

such that each of the $2\times 2$ submatrix are invertible. 

WLOG, assume that

$$
 \begin{bmatrix}
 \frac{\partial x}{\partial u} (u_0, v_0)&\frac{\partial v}{\partial u} (u_0, v_0)\\
 \frac{\partial z}{\partial u} (u_0, v_0)&\frac{\partial z}{\partial u} (u_0, v_0)
 \end{bmatrix}
$$

is invertible, then consider the orthogonal projection $\Pi_{XZ}$ of $V$ to XZ plane.  
Consider the composition $\Pi_{XZ} \circ \sigma: U\rightarrow V\rightarrow W:= (u, v)\rightarrow (x, 0, z)$ where $W$ is an open subset of XZ plane. 

Therefore, the claim is equivalent to that $\Pi_{XZ}\circ\sigma$ is locally invertible, a.k.a. 

$$\exists f: W \rightarrow U. \forall p\in V. f\circ(\Pi_{XZ}\circ\sigma)(u, v) = (u, v)$$

Consider the Taylor expansion of $\Pi_{XZ}\circ \sigma$ near $(u_0, v_0)$

\begin{align*}
\Pi_{XZ}\circ \sigma(u,v) &= \Pi_{XZ}\circ \sigma (u_0, v_0) + D[\Pi_{XZ}\circ \sigma]\vert_{(u_0, v_0)}\begin{bmatrix}u-u_0\\v-v_0\end{bmatrix} + rem.\\
&= \Pi_{XZ}\circ \sigma (u_0, v_0) + \Pi_{XZ}(D\sigma\vert_{(u_0, v_0)}) \begin{bmatrix}u-u_0\\v-v_0\end{bmatrix}+ rem.\\
&= \Pi_{XZ}\circ \sigma (u_0, v_0) + \begin{bmatrix}\frac{\partial x}{\partial u} (u_0, v_0)&\frac{\partial v}{\partial u} (u_0, v_0)\\\frac{\partial z}{\partial u} (u_0, v_0)&\frac{\partial z}{\partial u} (u_0, v_0)\end{bmatrix}\begin{bmatrix}u-u_0\\v-v_0\end{bmatrix} + rem.
\end{align*}

Therefore, we are approximating the composition by the invertible linear map. Then, by implicit funciton theorem, there exists a unique solution $y = \psi(x, z)$ near $(x_0, z_0)$ where $\psi$ is differentiable. 


__Corollary__ Regularity condition satisfies IFF the tangent plane at $p$ exists, and indeed, is a plane. 

## Smooth Maps

Consider $\Sigma_1, \Sigma_2$ to be smooth surfaces, and let $f: \Sigma_1\rightarrow \Sigma_2$ be a map.   

For some point $p_1\in \Sigma_1$, take $p_2 = f(p_1) \in \Sigma_2$. Let $\sigma_1: U_1\rightarrow V_1\cap \Sigma_1, p_1\in V_1$ and $\sigma_2: U_2\rightarrow V_2\cap \Sigma_2, p_2\in V_2$.  
Consider the composition function $g:=\sigma_2^{-1}\circ f\circ \sigma_1: U_1\subset \mathbb R^2\rightarrow U_2\subset \mathbb R^2$, i.e. 

$$g(u,v) = \sigma_2^{-1}\circ f\circ \sigma_1 (u,v) = (a(u,v), \beta(u,v))$$


Then, we define $f$ is __differentiable (smooth)__ at $p = \sigma(u,v)$ if $g$ is differentiable as $Dg = \begin{bmatrix}\partial_u a&\partial_va \\\partial_u \beta&\partial_v\beta\end{bmatrix}$, and $f$ is a __differentiable (smooth)__ map if $\forall p$ is differentiable. 

If we linearize $f$ near a point $p_1$, then we have that 

$$Df : T_{p_1}\Sigma_1\rightarrow T_{p_2}\Sigma_2$$

maps from a a tangent plane $T_{p_1}\Sigma_1 = \text{span}\{\partial_u\sigma_1, \partial_v\sigma_1\}$ to $T_{p_2}\Sigma_2 = \text{span}\{\partial_u\sigma_2, \partial_v\sigma_2\}$
