# Surface Normals and Orientability

## Normal Vector
Another finding is that $\partial_u\sigma(u_0, v_0)\times \partial_v\sigma(u_0, v_0)$ is perpendicular to $T_p\Sigma$ since the cross product is perpendicular to the spanning vectors of the plane. 
Therefore, define the __unit normal vector__ of $\Sigma$ at $p$ as 

$$\hat N(p) = \frac{\partial_u\sigma(u_0, v_0)\times \partial_v\sigma(u_0, v_0)}{\|\partial_u\sigma(u_0, v_0)\times \partial_v\sigma(u_0, v_0)\|}$$

Note that the tangent plane is independent of the choice of the path. Therefore, there are only 2 possible normal vectors. Say $\hat N(p) = \frac{\partial_u\sigma(u_0, v_0)\times \partial_v\sigma(u_0, v_0)}{\|\partial_u\sigma(u_0, v_0)\times \partial_v\sigma(u_0, v_0)\|}$, then another possible reparameterization of the surface patch will result in $\tilde N(p) = \frac{\partial_v\sigma(u_0, v_0)\times \partial_u\sigma(u_0, v_0)}{\|\partial_v\sigma(u_0, v_0)\times \partial_u\sigma(u_0, v_0)\|}=-\hat N(p)$

### Reparameterization of Surface Patches

Note that a corollary of the regularity condition:
Consider the intersection of the 2 surface patch of a regular surface $\sigma_1: U_1\rightarrow V_1, \sigma_2: U_2\rightarrow V_2. V_1\cap V_2\neq\emptyset$. Then, let $f:U_1\rightarrow U_2$ be the map from one plane to another. Then, $f$ is invertible, and $f$ and $f^{-1}$ are both differentiable. 

__Claim__ If $\sigma: U\rightarrow V$ is a regular coordinate patch of a surface and $f: \tilde U\rightarrow U$ is a reparameterization. Then $\sigma\circ f: \tilde U\rightarrow V$ is also a regular coordinate patch. 

Another interesting finding is that the normal vector of the reparameterized tangent plane. 

\begin{align*}
\tilde N &= (\frac{\partial \sigma}{\partial u} \frac{\partial u}{\partial \tilde u} + \frac{\partial \sigma}{\partial v} \frac{\partial v}{\partial \tilde u})\times (\frac{\partial \sigma}{\partial u} \frac{\partial u}{\partial \tilde v} + \frac{\partial \sigma}{\partial v} \frac{\partial v}{\partial \tilde v})\\
&= \frac{\partial \sigma}{\partial u} \times \frac{\partial \sigma}{\partial v} (\frac{\partial u}{\partial \tilde u}  \frac{\partial v}{\partial \tilde v} - \frac{\partial v}{\partial \tilde u}  \frac{\partial u}{\partial \tilde v})\\
&= \det(Df)(\frac{\partial \sigma}{\partial u} \times \frac{\partial \sigma}{\partial v})
\end{align*}

Therefore, the unit normal will be 

$$\hat{\tilde N} = \frac{\tilde N}{\|\tilde N\|} = \frac{\det(Df)}{|\det(Df)|}\hat N = \text{sign}(\det(Df))\hat N$$


## Orientable Surface
From the above findings, we can define an surface's orientability through its atlas
A surface $\Sigma$ is __orientable__ if exists an atlas with the property that, if $f$ is the transition map between any two surface patches, then $\det(Df) > 0$. In other words, for any two overlapping surface patches $\sigma_1: U_1\rightarrow V_1, \sigma_2: U_2\rightarrow V_2. V_1\cap V_2\neq \emptyset$ the transition map $f:= \sigma_1^{-1}\circ \sigma_2:W_2\rightarrow W_1$ where $W_i = \sigma_i^{-1}(V_1\cap V_2)\subseteq U_i$ has a positive Jacobian determinant. 

Equivalently, there exists a unit normal function $\hat N_\Sigma: \Sigma\rightarrow C = \{(x,y,z): x^2+y^2+z^2=1\}$ where $\hat N_\Sigma$ is smooth and continuous. In other words, the change is unit normal vector along any path on the surface must be continuous.

### Example: Mobius Band (Non-orientable)
The Mobius band is the surface obtained by rotating a straight line segment $l$
around its midpoint $p$ at the same time as $p$ moves around a circle $C$.

???quote "Source code"

    ```python
    --8<-- "mat363/scripts/surface_normals.py"
    ```



```plotly
{"file_path": "mat363/assets/mobius.json"}
```



As shown in the example, let $C$ be the unit circle, and $l$ be the line segment connecting $(0,0, -1/2), (0,0, 1/2)$. 

The Mobius band can be parameterized by 2 surface patches 

$$\sigma(t, \theta) = (\cos\theta(1-t\sin\frac{\theta}{2}), \sin\theta(1-t\sin\frac{\theta}{2}), t\cos\frac{\theta}{2})$$

where $U_1 = (-1/2, 1/2) \times (0,2\pi), U_2 = (-1/2, 1/2)\times (-\pi, \pi)$. 

Consider the unit normal 

\begin{align*}
\partial_t\sigma|{(0,\theta_0)} &= (-\sin\frac{\theta_0}{2}\cos\theta_0, \sin\theta_0\sin\frac{\theta_0}{2}, \cos\frac{\theta_0}{2})\\
\partial_\theta\sigma|_{(0, \theta_0)} &= (-\sin\theta_0, \cos\theta_0, 0)\\
\partial_t\sigma\times \partial_\theta\sigma &= (-\cos\frac{\theta}{2}\cos\theta, -\cos\frac{\theta}{2}\sin\theta, -\sin\frac{\theta}{2}\cos^2\theta -\sin\frac{\theta}{2}\sin^2\theta)\\
N&=  (-\cos\frac{\theta}{2}\cos\theta, -\cos\frac{\theta}{2}\sin\theta, -\sin\frac{\theta}{2})
\end{align*}

Note that the unit normal vector $\hat N = N$ since $\|N\| = 1$
Then, note that 

$$\lim_{\theta\rightarrow0+} N(0,\theta) =(-1, 0, 0) \neq (1, 0, 0) = \lim_{\theta\rightarrow 2\pi-}N(0, 
\theta)$$

contradict with the orientability assumption. 

Furthermore, a surface is non-orientable if it contains a sub surface diffeomorphic to the Mobius band. 
