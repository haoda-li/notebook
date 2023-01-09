# Surface Curvatures

## Second Fundamental Form

To define the curvature of a surface, the first attempt is to imitate the curvature of a curve. In other words, how quick the surface moves away from the plane parallel to the tangent plane and intersecting $p$. 

For a surface $\Sigma$ parameterized by $\sigma$, Consider a point $p = \sigma(u,v)$ and the tangent plane at $p$ with unit normal $\mathbf N$. The intuition above leads to 

$$(\sigma(u+\Delta u, v+\Delta v) - \sigma(u,v))\cdot \mathbf N$$

Using Taylor expansion, $(\sigma(u+\Delta u, v+\Delta v) - \sigma(u,v))$ is linearly approximated (first two orders) as 

$$(\sigma_u u' + \sigma_v v') + \frac{1}{2}(\sigma_{uu}u'^2 + 2\sigma_{uv}u'v' + \sigma_{vv}v'^2)+ rem.$$

Then, note that $N \parallel (\sigma_u\times\sigma_v)$ and $rem.$ approches 0, so that the equation becomes

$$\frac{1}{2}(\sigma_{uu}\cdot \mathbf N u'^2 + 2\sigma_{uv} \cdot \mathbf N  u'v' + \sigma_{vv}\cdot \mathbf N  v'^2)$$

Let $L = \sigma_{uu}\cdot \mathbf N , M = \sigma_{uv}\cdot \mathbf N, N = \sigma_{vv}\cdot \mathbf N$
so that we can describe curvature by 

$$Lu'^2 + 2M u'v' + N v'^2$$

which is called the __second fundamental form__ of the surface patch $\sigma$.  

### Example: Surface of Revolution

$$\sigma(u,v) = (f\cos v, f \sin v, g)$$

with assumption that $f>0$ and $\gamma(u) = (f(u), 0, g(u))$ is unit-speed. 

Known that $\sigma_u = (f'\cos v, f'\sin v, g'), \sigma_v = (-f\sin v, f\cos v, 0)$. 

\begin{align*}
\mathbf N &= \sigma_u\times \sigma_v = (-fg'cos v, -f g'\sin v, ff')\\
\|\mathbf N\| &= \sqrt{f^2g'^2(\cos^2 v + \sin^v) + f^2f'^2} = f\sqrt{f'^2+g'^2} = f\\
\hat{\mathbf N} &= (-g'\cos v, -g'\sin v, f')\\
L &= \sigma_{uu}\cdot \hat{\mathbf N} \\
&= (f''\cos v, f''\sin v, g'')\cdot (-g'\cos v, -g'\sin v, f')\\
&= f'g'' - f''g'\\
M &= \sigma_{uv}\cdot \hat{\mathbf N} \\
&= (-f'\sin v, f'\cos v, 0)\cdot (-g'\cos v, -g'\sin v, f')\\
&= 0\\
N &= \sigma_{vv}\cdot \hat{\mathbf N} \\
&= (-f\cos v, -f\sin v, 0)\cdot (-g'\cos v, -g'\sin v, f')\\
&= fg'
\end{align*}

The second fundamental form is 

$$(f'g''-f''g')u'^2 + fg' v'^2$$


For sphere using lat-long coordinate parameterization, inserting $f = \cos u, g = \sin u$ so that the second fundamental form is 

$$u'^2 + \cos^2(u)v'^2$$

which is the same as the first fundamental form. 

### Example: elliptic paraboloid

$$\sigma(u, v) = (u,v,u^2+v^2)$$


\begin{align*}
\mathbf N &= \frac{\sigma_u\times \sigma_v}{\|\sigma_u\times \sigma_v\|}\\
&= \frac{(1, 0, 2u)\times (0, 1, 2v)}{\|(1, 0, 2u)\times (0, 1, 2v)\|}\\
&= \frac{1}{\sqrt{4u^2+4v^2+1} }(-2u, -2v, 1)\\
L &= \sigma_{uu} \cdot\mathbf N \\
&= \frac{1}{\sqrt{4u^2+4v^2+1} }(0, 0, 2)\\
N &= \sigma_{vv} \cdot\mathbf N \\
&= \frac{1}{\sqrt{4u^2+4v^2+1} }(0, 0, 2)\\
M &= \sigma_{uv}\cdot {\mathbf N }  = 0
\end{align*}

## Reparameterization 
__Claim__ If $\tilde \sigma$ is a reparameterization of a surface patch $\sigma$ with map $(u,v) = \Phi(\tilde u, \tilde v)$, then 

$$\begin{bmatrix}\tilde L &\tilde M\\\tilde M&\tilde N\end{bmatrix} = \pm J(\Phi)^T \begin{bmatrix}L&M\\M&N\end{bmatrix}J(\Phi)$$


First, by reparameterization we have that $\tilde{\mathbf  N} = \pm \mathbf N$, then given that

$$\tilde\sigma(\tilde u, \tilde v) = \sigma(\Phi(\tilde u, \tilde v))$$

Differentiate both sides we have that 

$$\frac{d\tilde \sigma}{d\tilde u} = \frac{d\sigma}{d u}\frac{d u}{d\tilde u} + \frac{d\sigma}{d v}\frac{d v}{d\tilde u}, \frac{d\tilde \sigma}{d\tilde v} = \frac{d\sigma}{d u}\frac{d u}{d\tilde v} + \frac{d\sigma}{d v}\frac{d v}{d\tilde v}$$

Differentiating twice, we have that 

\begin{align*}\frac{d^2\tilde \sigma}{d \tilde u^2} &= \frac{d}{d\tilde u}(\frac{d\sigma}{d u}\frac{d u}{d\tilde u} + \frac{d\sigma}{d v}\frac{d v}{d\tilde u})\\
&= \frac{d\sigma}{d u}\frac{d^2 u}{d\tilde u^2} + \frac{d}{d\tilde u}(\frac{d\sigma}{d u})\frac{d u}{d\tilde u} + \frac{d\sigma}{d v}\frac{d^2 v}{d\tilde u^2} + \frac{d}{d\tilde u}(\frac{d\sigma}{d v})\frac{d v}{d\tilde u}\\
\frac{d}{d\tilde u}(\frac{d\sigma}{d u})&= \frac{d^2\sigma}{d u^2}\frac{d u}{d \tilde u} + \frac{d^2\sigma}{d udv}\frac{d v}{d \tilde u}\\
\frac{d}{d\tilde u}(\frac{d\sigma}{d v})&= \frac{d^2\sigma}{d v^2}\frac{d v}{d \tilde u} + \frac{d^2\sigma}{d udv}\frac{d v}{d \tilde u}
\end{align*}

Inserting all differentials back with simplified notations

$$\tilde{\sigma}_{\tilde u\tilde u} = \sigma_u \frac{d^2u}{d\tilde u^2} + \sigma_v \frac{d^2u}{d\tilde u^2} + \sigma_{uu}(\frac{d u}{d\tilde u})^2 + 2\sigma_{uv}\frac{d u}{d\tilde u}\frac{d v}{d\tilde u} + \sigma_{vv}(\frac{d v}{d\tilde u})^2$$

Note that $\tilde{\mathbf  N} = \pm \mathbf N, \sigma_u\cdot \mathbf N = \sigma_v\cdot \mathbf N = 0$, we have that 

$$\tilde L = \tilde{\sigma}_{\tilde u\tilde u} \cdot \tilde{\mathbf  N} = L(\frac{d u}{d\tilde u})^2 + 2M\frac{d u}{d\tilde u}\frac{d v}{d\tilde u} +N(\frac{d v}{d\tilde u})^2$$

Similarly, we can obtain $\tilde M,\tilde N$

### Example: Plane 
__Claim__ $\sigma$ parameterizes an open subset of a plane IFF the second fundamental form is zero everywhere. 

_proof_. $\Rightarrow$ Note that if one parameterization of the plane has second fundamental form being 0, then all of its reparameterizations have 0 second fundamental form by the reparameterization theorem ($\pm J^T \mathbf 0 J = \mathbf 0$ for any $J$).  
We simply take $\sigma(u,v) = u\mathbf a + v\mathbf b + \mathbf c$, so that $\sigma_u = \mathbf a, \sigma_v = \mathbf b, \sigma_{uu} = \sigma_{uv} = \sigma_{vv} = 0$, hence its second fundemental form is $0$. 

$\Leftarrow$ Assume that $\sigma_{uu}\cdot \mathbf N = \sigma_{uv}\cdot \mathbf N = \sigma_{vv}\cdot \mathbf N = 0$. 
Note that by product rule

$$d_u (\sigma_u \cdot\mathbf N) = \sigma_u \cdot \mathbf N_u + \sigma_{uu}\cdot\mathbf N$$

while we also have that $\sigma_u \cdot\mathbf N = 0$ since they are perpendicular, hence  

$$\sigma_u \cdot \mathbf N_u = -\sigma_{uu}\cdot\mathbf N = 0$$

Similarly, we can obtain that 

$$\sigma_u \cdot \mathbf N_u = \sigma_u \cdot \mathbf N_v= \sigma_v \cdot \mathbf N_u= \sigma_v \cdot \mathbf N_v = 0$$

Also, since $\mathbf N$ is a unit vector, its partial derivatives 

$$\mathbf N \cdot \mathbf N_u = \mathbf N \cdot \mathbf N_v = 0$$

However, $N$ is perpendicular to $\sigma_u, \sigma_v$ so that we must have that $\mathbf N_u = \mathbf N_v = 0$, hence $\mathbf N(u,v)$ is a constant.

## Gauss and Weingarten Maps

Another approach for defining curvature is the speed of change in the unit normal $\mathbf N$. Note that the values of $\mathbf N$ on a surface belongs to a unit sphere $S^2$. Therefore, we define the __Gauss map__ 

$$G: \Sigma\rightarrow S^2, G(p) = \mathbf N(p)$$

The rate of change of normal thus becomes 

$$D_pG : T_p \Sigma\rightarrow T_{N(p)}S^2$$

Note that the tangent plane $T_{N(p)}S^2$ is the tangent plane perpendicular to $N(p)$, which is the same plane as $T_p\Sigma$. 

Define the __Weingarten map__ 

$$W_p = -D_pG$$

and define the __blinear form of second fundamental form__ of $\Sigma$ at $p$ by 

$$\langle\langle v, w\rangle\rangle = \langle W_p(v), w\rangle$$


We will then show how Weingarten map is related to the second fundamental form. 

__Lemma__ $\mathbf N_u\cdot \sigma_u = -L, \mathbf N_u\cdot \sigma_v = \mathbf N_v\cdot \sigma_u = -M, \mathbf N_v\cdot \sigma_v = -N$. 

_proof_. Note that $\mathbf N = \frac{\sigma_u\times \sigma_v}{\|\sigma_u\times \sigma_v\|}$ is perpendicular to both $\sigma_u, \sigma_v$, we have that 

$$N\cdot \sigma_u = N\cdot\sigma_v = 0$$

Differentiating $N\cdot \sigma_u$, we have that 

\begin{align*}
\frac{\partial}{\partial u}(\mathbf N\cdot\sigma_u) &= \mathbf N_u\cdot \sigma_u +  \mathbf N\cdot\sigma_{uu} = 0\\
\mathbf N_u\cdot \sigma_u &= - \mathbf N\cdot\sigma_{uu} = -L
\end{align*}

Similarly, differentiate wrt. $u, v$ on each of $N\cdot \sigma_u, N\cdot\sigma_v$ will get the claim. 

__Theorem__ The inner product is  a symmetric bilinear form 

$$\langle\langle v, w\rangle\rangle_{p} = \begin{bmatrix}c\\d\end{bmatrix}\begin{bmatrix}L&M\\M&N\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix} = Lv_u w_u + M(v_u + w_v + v_v + w_v) + Nv_vw_v$$

For $v = a \sigma_u + b\sigma_v, w = c \sigma_u + d\sigma_v$. 

Note that both sides of the equation is bilinear form on $T_p\Sigma$, we only need to prove on the set $\{\sigma_u, \sigma_v\}$.  
Also, note that $W_p = -D_pG = D_p \mathbf N$, so that 

$$\frac{\partial W_p}{\partial_u} = -\frac{\partial G}{\partial u} = -\frac{\partial\mathbf N}{\partial u}, \frac{\partial W_p}{\partial_v} = -\frac{\partial \mathbf N}{\partial_u}$$


Therefore, using the lemma above

$$\langle\langle \sigma_u, \sigma_u\rangle\rangle = \langle W_p(v), w\rangle = \langle -\mathbf N_u, \sigma_u\rangle = \mathbf N \cdot \sigma_{uu}$$

And we can obtain the similar results for 

$$\langle\langle \sigma_u, \sigma_v\rangle\rangle = \langle\langle \sigma_v, \sigma_u\rangle\rangle = M, \langle\langle \sigma_v, \sigma_v\rangle\rangle = N$$

__Corollary__ Weingarten map is self adjoint. $\langle W_p(v), w\rangle =  \langle v, W_p(w)\rangle$

## Normal and Geodesic Curvatures

The third attempt to define curvature is to define via the curvature of curves on the surface. 

Let $\gamma: \mathbb R\rightarrow\Sigma$ be a unit-speed curve on $\Sigma$, parameterized by $\sigma$. Let $\mathbf t = \gamma', \mathbf n = \frac{\gamma''}{\|\gamma''\| }, \mathbf b = \mathbf t\times \mathbf n$ be the unit tangent, unit normal, and binormal, which forms the orthonormal basis.  
Also, let $\mathbf N$ be the unit normal, hence $\{\mathbf N, \mathbf t, \mathbf N\times \mathbf t\}$ forms another orthonormal basis.  
Then, note that $\gamma$ is unit-speed, hence $\gamma''\perp \mathbf t$, thus, $\gamma''$ must resides on the plane spanned by $\mathbf N, \mathbf N\times \mathbf t$, in other words

$$\gamma'' = \kappa_n \mathbf N + \kappa_g(\mathbf N\times\mathbf t)$$

Define $\kappa_n$ be the __normal curvature__ and $\kappa_g$ be the __geodesic curvature__ of $\gamma$. 

Since $\{\mathbf N, \mathbf t, \mathbf N\times \mathbf t\}$ forms a orthonormal basis, by Pythagorean theorem or trig. identities, we can easily obtain

$$\kappa^2 = \kappa_n^2 + \kappa_g^2$$


$$\kappa_n = \gamma''\cdot \mathbf N = \kappa\cos\psi, \kappa_g = \gamma'' \cdot (\mathbf N\times \gamma') = \pm\kappa\sin\psi$$

for $\psi = \arccos(\mathbf N\cdot\mathbf n)$

__Theorem__ $\kappa_n$ is invariant of reparameterization of unit-speed $\gamma$, while $\kappa_g$ changes up to the sign. 

_proof_. Let $\gamma, \tilde\gamma$ be two unit-speed parameterizations of the same curve, then the map can only be $\tilde t = \pm t + c$. 

__Theorem__ If $\gamma:\mathbb R\rightarrow\Sigma$ is unit-speed on an oriented surface $\Sigma$, then 

$$\kappa_n = II(\gamma',\gamma') = Lu'^2 + 2Mu'v' + Nv'^2$$

_proof_. Let $\gamma(t) = \sigma(u(t), v(t))$. Note that $\mathbf t = \gamma'$ is a tangent vector to $\Sigma$, 

\begin{align*}
\mathbf N\cdot \gamma' &= 0\\
\frac{d}{dt}(N\cdot \gamma') = \mathbf N\cdot \gamma'' + \mathbf N'\cdot \gamma' &= 0\\
\mathbf N\cdot \gamma'' &= -\mathbf N'\cdot \gamma'
\end{align*}

Therefore, we have that 

$$\kappa_n = \mathbf N\cdot \gamma'' = -\mathbf N'\cdot \gamma' = W(\gamma')\cdot\gamma' = II(\gamma',\gamma')$$


__Theorem__ If $\gamma$ is regular (not necessarily unit-speed), then 

$$\kappa_n = \frac{II(\gamma',\gamma')}{I(\gamma',\gamma')}. \kappa_g = \frac{\gamma''\cdot (\mathbf N\times \gamma')}{I(\gamma',\gamma')^{3/2} }$$


_proof_. Let $\hat\gamma$ be the unit-speed parameterization of $\gamma, \gamma(t) = \hat\gamma(s(t))$ where $s$ is the arc-length of $\gamma$, and $s'$ is the speed  
Therefore, we have that 

$$\frac{d\gamma}{dt} = \frac{d\hat\gamma}{ds}\frac{ds}{dt}\implies \hat\gamma' = \frac{\gamma'}{s'}$$


$$\frac{d^2\gamma}{dt^2} = \frac{d^2\hat\gamma}{ds^2}(\frac{ds}{dt})^2 + \frac{d\hat\gamma}{ds}\frac{d^2s}{dt^2}\implies \hat\gamma'' = s'^{-2}(\gamma'' - \hat\gamma's'')$$

Therefore, 

\begin{align*}
\kappa_n &= II(\hat\gamma',\hat\gamma') \\
&= II(\frac{d\gamma}{dt}(\frac{ds}{dt})^{-1}, \frac{d\gamma}{dt}(\frac{ds}{dt})^{-1}) \\
&= \frac{II(\gamma', \gamma')}{s'(t)^2} \\
&= \frac{II(\gamma',\gamma')}{I(\gamma',\gamma')}\\
\kappa_g &= \hat\gamma''\cdot (\mathbf N\times \hat\gamma') \\
&= s'^{-2}(\gamma'' - \hat\gamma's')\cdot (\mathbf N \times s'^{-1}\gamma')\\
&= s'^{-3}\gamma''\cdot (\mathbf N \times \hat\gamma')\\
&= I(\gamma',\gamma')^{-3/2}\gamma''\cdot (\mathbf N \times \hat\gamma')
\end{align*}

### Example: Sphere

__Claim__ For any curve $\gamma: \mathbb R\rightarrow S^2_R$ on the sphere of radius $R$, $\kappa_n = \pm R^{-1}$. 

_proof_. WLOG assume that the sphere is centered at origin and $\gamma$ is unit-speed. Then, the unit normal at point $p = \gamma(t) \in S^2$ is $\pm\frac{\gamma(t)}{R}$.   
Also, we have that $\gamma\cdot \gamma = R^2$, differentiate both side gives that 

$$2\gamma'\cdot \gamma = 0$$

Differentiate twice gives that 

$$\gamma''\cdot \gamma + \gamma'\cdot\gamma' = 0\implies \gamma''\cdot \gamma' = -1$$

Therefore, the normal curvature

$$\kappa_n = \mathbf N \cdot \gamma'' = \pm\frac{\gamma}{R}\cdot \gamma'' = \pm R^{-1}$$


__Claim__ For any circle $c$ on the sphere of radius $R$, its geodesic curvature is 

$$\kappa_g = \pm r^{-1}\sin(\frac{r}{R})$$


_proof_. Note that $\kappa_g$ is invariant of rotations, WLOG assume that $c(\theta) = (r\cos\theta, r\sin\theta, \sqrt{R^2-r^2})$ where $0 < r\leq R$, then we have the unit normal for curve $c$ being

$$\mathbf n(\theta) = \frac{c''}{\|c''\|} = \frac{(-r\cos\theta, -r\sin\theta, 0)}{r} = (-\cos\theta, -\sin\theta, 0)$$

The unit normal for sphere at $c(\theta)$ is simply $\pm (R^{-1} c(\theta)) = \pm(\frac{r}{R}\cos\theta, \frac{r}{R}\sin\theta, \sqrt{1-\frac{r^2}{R^2} })$.  
Known that the curvature for a circle of radius $r$ is $r^{-1}$, we have that

$$\kappa_g = \pm \kappa \sin (\mathbf n\cdot\mathbf N) = \pm r^{-1}\sin(\frac{r}{R})$$


### Asymptotic curves

A curve $\gamma:\mathbb R\rightarrow\Sigma$ is called __asymptotic__ if $\kappa_n = 0$.  

For example, any straight line on a surface is asymptotic, since $\kappa_n = \mathbf N\cdot \gamma'' = \mathbf N \cdot 0 = 0$.  

__Theorem__ $\gamma$ with positive curvature is aymptotic IFF its binormal $\mathbf b$ is parallel to the unit normal of $\Sigma$ for all points of $\gamma$. 

_proof_. Since $\mathbf b = \mathbf t\times \mathbf n$, $\mathbf b \parallel \mathbf N$ so that $\mathbf N \perp \mathbf n$ implying that $\kappa_n = \kappa (\mathbf N \cdot \mathbf n) = \kappa 0 = 0$

