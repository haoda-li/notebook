# Parallel Transport

## Christoffel Symbols (Gauss Equations)

Consider some surface $\Sigma$ with (locally) parameterization $\sigma$. Note that $\sigma_u, \sigma_v, \mathbf N$ spans $\mathbb R^3$, hence we can write the second order derivatives as

\begin{align*}
\sigma_{uu} &= a_1\sigma_u + a_2\sigma_v + a_3\mathbf N\\
\sigma_{uv} &= b_1\sigma_u + b_2\sigma_v + b_3\mathbf N\\
\sigma_{vv} &= c_1\sigma_u + c_2\sigma_v + c_3\mathbf N\\
\end{align*}

Now, consider the second fundamental form

$$L = \sigma_{uu}\cdot N = a_1\sigma_u\cdot N + a_2\sigma_v \cdot N + a_3\mathbf N\cdot \mathbf N = 0 + 0 + a_3  = a_3$$

we have that 

$$a_3 = L, b_3 = M, c_3 = N$$

Then, we take dot product with $\sigma_u, \sigma_v$

\begin{align*}
\sigma_{uu}\cdot \sigma_u &= a_1 (\sigma_u\cdot\sigma_u) + a_2(\sigma_v\cdot \sigma_u) + a_3 (\mathbf N\cdot\sigma_u) = Ea_1 + Fa_2\\
\sigma_{uu}\cdot \sigma_v &= F a_1 + Ga_2\\
\sigma_{uv}\cdot\sigma_u &= Eb_1 + Fb_2\\
\sigma_{uv}\cdot\sigma_v &= Fb_1 + Gb_2\\
\sigma_{vv}\cdot\sigma_u &= Ec_1+ Gc_2\\
\sigma_{vv}\cdot\sigma_v &= Fc_1+Gc_2\\
\end{align*}

On the other hand, we have that 

\begin{align*}
&E_u = (\sigma_u\cdot\sigma_u)_u = 2 \sigma_{uu}\cdot\sigma_{u} &E_v = 2\sigma_{uv} \cdot\sigma_{u}\\
&F_u = \sigma_{uu}\cdot \sigma_{uv} &F_v = \sigma_{vv}\cdot\sigma_{uv}\\
&G_u = 2\sigma_{uv}\cdot \sigma_{v} &G_v = 2\sigma_{vv}\cdot \sigma_{v}
\end{align*}

Combine the equations, we have 6 equations w.r.t. to the 6 unknowns

\begin{align*}
E a_1 + F a_2 &= \frac{1}{2}E_u&F a_1 + G a_2 = F_u - \frac{1}{2}E_v\\
E b_1 + F b_2 &= \frac{1}{2}E_v&F b_1 + G b_2 = \frac{1}{2}G_u\\
E c_1 + F c_2 &= F_v - \frac{1}{2}G_u&F c_1 + G c_2 = \frac{1}{2}G_v
\end{align*}

The solution is that 

\begin{align*}
\Gamma_{11}^1 = \frac{GE_u - 2FF_u+FE_v}{2(EG-F^2)}&&\Gamma_{11}^2 = \frac{2EF_u-EEv-FEu}{2(EG-F^2)}\\
\Gamma_{12}^1 = \frac{GE_v - FG_u}{2(EG-F^2)}&&\Gamma_{12}^2 = \frac{EG_u-FE_v}{2(EG-F^2)}\\
\Gamma_{22}^1 = \frac{2GF_v-GG_u-FG_v}{2(EG-F^2)}&&\Gamma_{22}^2 = \frac{EG_v-2FF_v+FG_u}{2(EG-F^2)}
\end{align*}

so that the equations are called __Gauss Equations__ 

\begin{align*}
\sigma_{uu} &= \Gamma_{11}^1\sigma_u + \Gamma_{11}^2\sigma_v + L\mathbf N\\
\sigma_{uv} &= \Gamma_{12}^1\sigma_u + \Gamma_{12}^2\sigma_v + M\mathbf N\\
\sigma_{vv} &= \Gamma_{22}^1\sigma_u + \Gamma_{22}^2\sigma_v + N\mathbf N\\
\end{align*}

and the $\Gamma$'s are __Christoffel symbols__. 

## Covariant Derivative
Consider a particle's trajectory on some surface $\Sigma$ as $\gamma:(a, b) \rightarrow\Sigma$ and its velocity is the tangent vector $\mathbf v = \gamma'$ and acceleration $\mathbf a = \mathbf v' = \gamma''$. Suppose that $\Sigma$ is a plane, then $\gamma$ can be considered as a 2D curve, and both $\mathbf v$ and $\mathbf a$ resides on the plane. 

However, $\Sigma$ is not always a plane. For each $t, \mathbf v(t) \in T_{\gamma(t)}\Sigma$ being a vector field, which is (most likely) constantly changing. Since each tangent plane is spanned by $\sigma_u(t), \sigma_v(t)$, we can write 

$$\mathbf v(t) = a(t)\sigma_u(t) + b(t)\sigma_v(t)$$

Then, acceleration $\mathbf a= \mathbf v'$ is a 3D vector, hence can be spanned by $\{\sigma_u(t), \sigma_v(t), \mathbf N(t)\}$. Then, consider the particle's perspective, since it moves along the surface, from its perspective, it treats its movement as on a plane, and only perceive the change on this plane (think of car's velocity, while earth is actually a sphere). Therefore, we can interested in the perceived rate of change of $\mathbf v$ as the tangential component of $\mathbf v'$, a.k.a. the orthogonal projection of $\mathbf v'$ onto $T_{\gamma(t)}\Sigma$, as 

$$\nabla_\gamma \mathbf v = \mathbf v' - (\mathbf v' \cdot \mathbf N)\mathbf N$$

Note that orthogonal projection is unchanged of the sign of $\mathbf N$. 

Therefore, we define $\nabla_\gamma \mathbf v: (a,b)\rightarrow T_{\gamma(t)}\Sigma$ as the __covariant derivative__ of $\mathbf v$ along $\gamma$. If $\nabla_\gamma\mathbf v = 0$ for all $t$, then $\mathbf v$ is __parallel along__ $\gamma$. 

### Theorem 1
$\mathbf v$ is parallel along $\gamma$ IFF $\mathbf v'$ is perpendicular to the tangent plane of $\Sigma$ for all $t$. 

_proof_. This is obvious, since $\nabla_\gamma\mathbf v$ is the projection of $\mathbf v'$ onto $T_p\Sigma$, if $\mathbf v'$ is perpendicular to $T_p\Sigma$, then it is parallel to $\mathbf N$, and its projection onto $T_p\Sigma$ is always 0. 

### Theorem 2
$\mathbf v$ is parallel along $\gamma$ IFF 

$$a' + (\Gamma_{11}^1 u' +\Gamma_{12}^1v')a + (\Gamma_{12}^1u' + \Gamma_{22}^1v')b = 0$$

$$b' + (\Gamma_{11}^2 u' + \Gamma_{12}^2v')a + (\Gamma_{12}^2u' + \Gamma_{22}^2v')b = 0$$

For $\mathbf v(t) = a(t)\sigma_u (t) + b(t)\sigma_v(t), a,b$ are smooth scalar functions. 

_proof_. We have that $\mathbf v'$ 

\begin{align*}
\mathbf v' &= a' \sigma_u + a(\sigma_{uu}u'+\sigma_{uv}v') + b'\sigma_v + b(\sigma_{uv}u' + \sigma_{vv}v')\\
&= a'\sigma_u + b'\sigma_v + au'\sigma_{uu} + (av'+bu')\sigma_{uv} + bv'\sigma_{vv}
\end{align*}

where each of $\sigma_{uu}, \sigma_{uv}, \sigma_{vv}$ can be written into Gauss equations, and only involves $\sigma_u, \sigma_v, \mathbf N$.  
Then, since $\mathbf v$ is parallel along $\gamma$, we must have that $\mathbf v' = \lambda N$ and all coefficient of $\sigma_{u}, \sigma_{v}$ must be $0$, a.k.a the equations in the statement must be zero. 

### Theorem 3
Let $\gamma: (a,b)\rightarrow \Sigma$ and some $\mathbf v_0$ be a tangent vector of $\Sigma$ at $\gamma(t_0)$, then $\exists !\mathbf v$ s.t. $\mathbf v$ is parallel along $\gamma$ and $\mathbf v(t_0) = \mathbf v_0$. 

_proof_. Note that the statement is equivalent to say that there exists unique scalar function $a,b$ s.t. 

$$a(t_0)\sigma_u(t_0) + b(t_0) \sigma_v(t_0) = \mathbf v_0$$

$$a' + (\Gamma_{11}^1 u' +\Gamma_{12}^1v')a + (\Gamma_{12}^1u' + \Gamma_{22}^1v')b = 0$$

$$b' + (\Gamma_{11}^2 u' + \Gamma_{12}^2v')a + (\Gamma_{12}^2u' + \Gamma_{22}^2v')b = 0$$

Then, this is a ODE

$$a' = f(a(t), b(t), t) = -((\Gamma_{11}^1 u' +\Gamma_{12}^1v')a + (\Gamma_{12}^1u' + \Gamma_{22}^1v')b)$$

$$b' = g(a(t), b(t), t) = -((\Gamma_{11}^2 u' + \Gamma_{12}^2v')a + (\Gamma_{12}^2u' + \Gamma_{22}^2v')b)$$

given the initial conditions, it is proven to have a unique solution. 

### Example: circle on sphere

Let $\gamma$ be a circle of latitute $\theta_0 \in (-\pi/2, \pi)$ on the standard unit sphere. $\gamma(t) = \sigma(\theta_0, t)$, and the first fundamental form is $E=1, F=0, G=\cos^2\theta$.  
The Christoffel symbosls are then 

$$\Gamma_{12}^1 = -\tan\theta, \Gamma_{22}^1 =\sin\theta\cos\theta$$

others are all 0. 

Therefore, we have that 

$$a' = -(\cos\theta_0\sin\theta_0)b, b' = \tan\theta_0 a$$

solves to be 

$$a = A\cos(t\sin\theta_0) + B\sin(t\sin\theta_0)$$

$$b = A\frac{\sin(t\sin\theta_0)}{\cos\theta_0}  - B\frac{\cos(t\sin\theta_0)}{\sin\theta_0}$$


Consider the case when $t = 0$, then $a = 0, b = 1$, which gives $A = 0, B = -\sin\theta_0$ so that 

$$\mathbf v(t) = -\sin\theta_0 \sin(t\sin\theta_0)\sigma_\theta + \cos(t\sin\theta_0)\sigma_\phi$$

Thus the tangent vector of $\gamma$ is parallel along $\gamma$ IFF $\gamma$ is a great circle. 

### Example: Triangle on the Sphere

Suppose that a triangle $T$ on the unit sphere whose sides are arcs of great circles has vertices $p, q, r$. Let $v_0$ be a non-zero tangent vector to the arc $pq$ through $p, q$ at $p$. Show that, if we parallel transport $v_0$ along $pq$, then $qr$ and then $rp$, the result is to rotate $v_0$ through an angle $2\pi - A(T)$. 

_proof_. Since the sides of the triangle are arcs of great circle. The parallel transporting of the tirangle sides is always parallel along the arc. Suppose that the internal angles are $a,b,c$, then at each point of $p, q, r$, the angle is $\pi -a,\pi-b, \pi-c$. Therefore, the total angle made is 

$$\pi-a+\pi-b+\pi -c = 2\pi - (a+b+c - \pi) = 2\pi - A(T)$$

