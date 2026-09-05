# Geodesics

## Geodesics and Basic Properties

A curve $\gamma: (a, b)\rightarrow\Sigma$ is a __geodesic__ if $\gamma'' = 0$ or $\gamma''$ perpendicular to the tangent plane for all point (i.e., parallel to its unit normal). Equivalently, $\gamma$ is a geodesic IFF $\gamma'$ is parallel along $\gamma$. 

__Theorem__ any geodesic has constant speed. 

_proof_. 

$$\frac{d}{dt}(\gamma'\cdot \gamma') = 2\gamma''\cdot \gamma' = 0$$

since $\gamma'' = 0$ or $\gamma''$ perpendicular to the tangent plane, hence $\gamma'$ as $\gamma'$ is the tangent vector on the tangent plane. 

__Theorem__ A unit-speed curve on a surface is a geodesic IFF $\kappa_g = 0$. 

_proof_. $\Rightarrow$ Assume $\gamma$ is a geodeisc then $\gamma'' \parallel \mathbf N$, then

$$\kappa_g = \gamma''\cdot (\mathbf N\cdot \gamma') = \lambda \mathbf N \cdot (\mathbf N \cdot \gamma') = 0$$

$\Leftarrow$, if $\kappa_g = \gamma''\cdot (\mathbf N\cdot \gamma') = 0$, then $\gamma''$ is perpendicular to $\mathbf N\times \gamma'$, in addition $\gamma', \mathbf N, \mathbf N\times\gamma'$ are orthogonal, and $\gamma''$ is perpendicular to $\gamma'$, hence we have have that $\gamma''\parallel \mathbf N$

__Theorem__ Any straight line on a surface is a geodesic. 

_proof_. Any straight line can be parameterized as $\gamma(t) = \mathbf at+ \mathbf b$ so that $\gamma'' = 0$. 

__Theorem__ Any __normal section__ of a surface is a geodesic. 

_proof_. The normal section of $\Sigma$ is the intersection of $\Sigma$ and plane $\Pi$, where $\Pi$ is perpendicular to $\Sigma$ at each point of intersection. In this case, we can easily show that $\kappa_g = 0$ 

### Example: Geodesics on hyperboloid
The hyperboloid is defined as 

$$\Sigma = \{(x,y,z): x^2 + y^2 - z^2 =1\}$$

find the geodiscs passing through $(1, 0, 0)$

Known that any straight line is a geodesic, let $\gamma(t) = (a,b,c)t + (1, 0, 0)$ so that $\gamma(0) = (1, 0, 0)$, and we want $\gamma((a,b))\in\Sigma$, i.e. 

$$(at+1)^2 + (bt)^2 = 1 + (ct)^2\implies a^2 t + 2a + b^2 t = c^2 t$$

holds for any $t$, there are at least two straight lines s.t. 
$a = 0, b \neq 0, c = \pm b$

Then, consider the normal section of the surface. The two normal planes passing through $(1, 0, 0)$ will be the XY-plane and XZ-plane, where the normal section is $x^2 + y^2 = 1, x^2 - z^2 = 1$ respectively. 

## Geodesic Equations

__Theorem__ A curve $\gamma: (a,b)\rightarrow\Sigma$ is a geodesic IFF $\gamma = \sigma(u,v)$ with the equations

$$\frac{d}{dt}(Eu'+Fv') = \frac{1}{2}(E_uu'^2 + 2F_u u'v' + G_uv'^2)$$


$$\frac{d}{dt}(Fu'+Gv') = \frac{1}{2}(E_vu'^2 + 2F_vu'v' + G_v v'^2)$$


_proof_. Since $\gamma' = u'\sigma_u + v' \sigma_v$ and $\gamma'' \perp \sigma_u, \gamma''\perp\sigma_v$ by the definition of geodesic, we have that 

$$\big[\frac{d}{dt} (u'\sigma_u + v'\sigma_v)\big] \cdot \sigma_u = 0, \big[\frac{d}{dt} (u'\sigma_u + v'\sigma_v)\big] \cdot \sigma_v = 0$$

By product rule, since $d(f\cdot g) = df \cdot g + f\cdot dg$,

\begin{align*}
\big[\frac{d}{dt} (u'\sigma_u + v'\sigma_v)\big] \cdot \sigma_u &= \frac{d}{dt}((u'\sigma_u + v'\sigma_v)\cdot \sigma_u) - (u'\sigma_u + v'\sigma_v)\cdot \frac{d\sigma_u}{dt}\\
&= \frac{d}{dt}(Eu'+Fv') - (u'\sigma_u + v'\sigma_v)\cdot (u'\sigma_{uu} + v'\sigma_{uv})\\
&= \frac{d}{dt}(Eu'+Fv') - (u'^2\frac{1}{2}E_u + u'v' F_u+v'\frac{1}{2}G_u)
\end{align*}

Similarly, the equations can be derived for $\sigma_v$. 

__Theorem__ A curve $\gamma$ is a geodesic IFF the equations hold

$$u'' + \Gamma_{11}^1u'^2 + 2\Gamma_{12}^1 u'v' + \Gamma_{22}^1 v'^2 = 0$$


$$v'' + \Gamma_{11}^2 u'^2 + 2\Gamma_{12}^2 u'v' + \Gamma_{22}^2 v'^2 = 0$$

_proof_. Since $\gamma$ is a geodesic IFF $\gamma'$ is parallel along $\gamma$, and $\gamma' = u'\sigma_u + v'\sigma_v$, take $\mathbf a = u', \mathbf b = v'$ and we have the equations. 

__Theorem__ For a surface $\Sigma$, let $\mathbf t$ be a unit tangent vector of $\Sigma$ at point $p\in\Sigma$. Then, $\exists ! \gamma:\mathbb R\rightarrow \Sigma$ be a unit-speed geodesic passing through $p$ and has tangent vector $\mathbf t$. 


__Corollay__ Straight lines are the only geodesics on a plane, great circles are the only geodesics on a sphere.  
_proof_. For any point and any direction, exists a straight line / great circle, and but uniqueness, they are the only geodesics. 

__Corollay__ Any local isometry between two surfaces takes the geodesics of one surface to the geodesics of the other. 

_proof_. Since $\gamma$ is a geodesic IFF the equations holds, while the equations only involves first fundamental form, and isometry has the same first fundamental form. 

### Example: Cylinder
__Claim__ Let $p,q$ be two distinct points on a unit cylinder $\Sigma$, there are either two or infinitely many geodesics with end points $p, q$. 

_proof_. If $p=(x_0, y_0, z_0),q=(x_1, y_1, z_1) $ are on the same parallel $(z_0 = z_1)$, then the geodesics are the two arcs of a great circle. If $p, q$ are of the different parallels, WLOG $z_1 > z_0$, then we can have plane of length $2\pi k, k > 0$ and height $z_1 - z_0$, the plane is locally isometric to the cylinder, and there are infinitely many planes. 

Alternatively, we can use the geodesics equation. 

$\Sigma = (\cos v, \sin v, u)$ with first fundamental form $E=G=1,F=0$, the geodesic equations are hence $\frac{d}{dt}u' =u'' = 0, \frac{d}{dt}v' = v'' = 0$. Hence $u = a+bt, v = c+dt$ for any constants $a,b,c,d$ are geodesics on the cylinder. 

### Example: Circular Cones

For circular cone 

$$\sigma(u,v) = (u\cos v, u\sin v, u)$$

we have the local isometry from xy-plane to $\Sigma$ by 

$$(u\sqrt 2 \cos \frac{v}{\sqrt 2}, u\sqrt 2\sin\frac{v}{\sqrt 2}, 0)$$


Fix $a, b$ be two constant, straight line on the plane can be written as the level curve $ax + by = 1, x = u\sqrt 2 \cos \frac{v}{\sqrt 2}, y = u\sqrt 2 \sin \frac{v}{\sqrt 2}$, 
inserting $u = (\sqrt 2 a \cos \frac{v}{\sqrt 2} + \sqrt 2 b \sin\frac{v}{\sqrt 2})^{-1}$ so that we have the curve $\gamma(v)$ on the plane that is a straight line, taking isometry and the curve on the cone will be 

$$\gamma(v) = (\sqrt 2 a \cos \frac{v}{\sqrt 2} + \sqrt 2 b \sin\frac{v}{\sqrt 2})^{-1} (\cos v, \sin v, 1)$$


In addition, we have the $\gamma_y(u) = (u, 0, u), \gamma_x (u) = (0, u, u)$ are straight lines on the cone. 

### Example: Helicoid
For a helicoid $\sigma(u,v) = (u\cos v, u\sin v, v), \gamma$ be a curve on the surface

__Theorem__ If $\gamma$ is a geodesic, then $v' = \frac{a}{1+u^2}$. 

_proof_. The first fundamental form of $\sigma$ is $E = 1, F = 0, G = 1+u^2$, the geodesic equations gives 

$$u'' = uv'^2, \frac{d}{dt}(1+u^2)\cdot v' = 0$$ 

Thus, we have that $(1+u^2)\cdot v'  = a\implies v' = \frac{a}{1+u^2}$

In addition, by unit speed, we have that 

$$u'^2 + (1+u^2)v'^2  = 1\implies u'^2 = 1 - \frac{a^2}{1+u^2}$$

When $a = 0$, we have $v = c$, and we have a ruling.   
When $a = 1$, we have $\frac{dv}{du} = \pm\sqrt{v'^2/ u'^2} = \pm\sqrt{\frac{a / (1+u^2)}{1- a^2 / (1+u^2)} } =\pm\frac{a}{\sqrt{(1-a^2+u^2)(1+u^2)} }$, $v = \int \frac{dv}{du} = v_0 \pm \sinh^{-1}(u^{-1})$ 

## Geodesics on Surface of Revolution

For surface of revolution 

$$\sigma(u,v) = (f(u)\cos v, f(u)\sin v, g(u))$$

where $f>0, f'+g' = 1$.  
First fundamental form is $E=1,F=0, g=f^2$
using geodesics equations, we have 

$$u'' = ff'v'^2, \frac{d}{dt}(f^2 v') = 0$$

and by unit-speed, we have that 

$$u'^2 + f^2 v'^2 = 1$$


__Theorem__ Every meridian of surfaces of revolution is a geodesic.  
_proof_. meridian implies $v = v_0$, so that $v' = 0$, hence the unit-speed condition gives $u' = \pm 1$ is constant, then $u'' = 0 = ff'0$ satisfies the first equation. The second equation is obviously satisfied. 

__Theorem__ A parallel $u=u_0$ is a geodesic IFF $f'(u_0) = 0$.   
_proof_. Let $f(u_0) = c$, since $u=u_0, u' = 0, v' = \pm c^{-1}$ is a non-zero constant. Therefore, the first equation gives $0 = \pm cf'$, implying $f' = 0$, the second equation definitely holds as both $f$ and $v'$ are constant. 

### Clairaut's Theorem

Let $\Sigma$ be a surface of rotation, Let $\gamma: (a,b)\rightarrow \Sigma$ be unit-speed, $\rho: \Sigma\rightarrow\mathbb R$ be the distance of some point $p$ from the axis of rotation. Let $\psi$ be the angle between $\gamma'$ and the meridians of $\Sigma$.   


__Claim__ If $\gamma$ is a geodesic, then $\rho\sin\psi$ is constant along $\gamma$.  

_proof_. By our parameterization $\sigma$, we have that $\rho = f(u)$.  
Note that $\sigma_u = (f'\cos v, f'\sin v, g')$ is unit vector tangent to the meridians and $\rho^{-1}\sigma_v = f^{-1}(-f\sin v, f\cos v, 0)$ is unit vector tangent to the parallels. Also, we have $\sigma_u\cdot \sigma_v = 0$ so that $\sigma_u, \rho^{-1}\sigma_v$ forms a orthonormal basis.   
For $\gamma(t) = \sigma(u(t), v(t))$ being unit-speed, we have that 

$$\gamma' = \cos\psi \sigma_u + \rho^{-1}\sin\psi\sigma_v$$

Hence, 

\begin{align*}
\sigma_u\times \gamma' &= \cos \psi \sigma_u\times\sigma_u + \rho^{-1}\sin\psi (\sigma_u\times \sigma_v) \\
\sigma_u\times (u'\sigma_u + v'\sigma_v)&= \rho^{-1}\sin\psi(\sigma_u\times \sigma_v)\\
v'(\sigma_u\times \sigma_v) &= \rho^{-1}\sin\psi(\sigma_u\times \sigma_v)\\
\rho v' &= \sin \psi\\
\rho^2 v' &= \rho \sin\psi
\end{align*}

Note that $f = \rho$, so that the second geodesic equation gives 

$$\frac{d}{dt}(\rho^2 v') = 0\implies, \rho^2 v' := \Omega = \rho\sin\psi$$

for some constant $\Omega$. 

__Claim__. Conversely, if $\rho\sin\psi$ is constant along $\gamma$ and no part of $\gamma$ is part of some parallel of $\Sigma$, then $\gamma$ is a geodesic. 

_proof_. We have shown that $f^2 v' = \rho^2 v' = \rho\sin\psi$, so that if $\rho\sin\psi = c$, the second equation is satisfied.  
Consider the first equation $u'' = \rho\rho' v'^2$, we have that $v' = \frac{\rho\sin\rho}{\rho^2} = \frac{\Omega}{\rho^2}$ so that the unit-speed condition gives 

$$u'^2 = 1 - \frac{\Omega^2}{\rho^2}$$

differentiating both sides, 

$$2u'u'' = \Omega^2 (-2)\rho^{-3}\frac{d\rho}{du}u'\implies \frac{u'}{\Omega^2}(u'' - \rho\frac{d\rho}{du}v'^2) \Leftrightarrow u'(u'' - \rho\frac{d\rho}{du}v'^2)= 0$$

As long as $u'\neq 0$, we have the first equation $u'' - \rho\frac{d\rho}{du}v'^2 = u'' - ff'v'^2 = 0$ satisfied. 

__Corollary__ Assume that $\Omega > 0$, then the geodesic is confined to the part of $\Sigma$ which is at a distance $\geq \Omega$ from the axis. 

_proof_. Note that we have 

$$u'^2 = 1 - \frac{\Omega^2}{\rho^2}$$

Assume that $\Omega < \rho = f\implies u'^2 > 0$, then the geodesic will cross every parallel of $\Sigma$.   
Assume that $\Omega > \rho$, then $u$ would be bounded above or below on $\Sigma$. 

__Corollary__ For $\Omega = 0$, the geodesic is the meridian. 

$\Omega = 0\implies \sin\psi = 0\implies \psi = 0$, it is always parallel with the meridian. 

### Example: Hyperboloid
Suppose that the hyperboloid is obtained by rotating $x^2 - z^2 =1, x > 0$ around the z-axis. The distance is of $[1,\infty)$. 

For $0 < \Omega < 1$, the geodesic with angular momentum $\Omega$ crosses every parallel, and so extends for $z\in (-\infty, \infty)$.  
For $\Omega > 1$, since we must have that $\rho^2 = x^2 = 1+z^2\geq \Omega^2$, then the geodesic is confined to either $z\geq \sqrt{\Omega^2 - 1}$ or $z \leq -\sqrt{\Omega^2 -1}$.  
Consider $z\geq \sqrt{\Omega^2 - 1}$, note that $z = \sqrt{\Omega^2 - 1}$ is a circle of radius $\Omega$, and is a parallel. Therefore, for some point $p$ on the circle, the geodesic $C$ must leave head up ($dz > 0$) as it leaves $p$. Moreover, $C$ must be symmetric about $p$, since reflection in the plane through $p$ containing the z-axis takes $C$ to another geodesic that also passes through $p$ and is tangent to the circle, and then by uniqueness of geodeisc. Finally, consider that $u'^2 = 1 - \frac{\Omega^2}{\rho^2} \in (0, 1)$, the geodesic crosses every parallel for $z \geq  \sqrt{\Omega^2 - 1}$. In addition, for $z \leq - \sqrt{\Omega^2 - 1}$, the story is similar.   
For $\Omega = 1$, for $p$ on the unit-circle, we have that $\sin\psi = 1$, so that the geodesic $C$ is tangent to $\Gamma$ at $p$, so that it must coincide with $\Gamma$. For $p$ below the circle, we have that $\sin\psi = \frac{1}{\rho} < 1$ so that $\psi < \pi/2$ and leaves $p$ in one direction. It will get arbitrarily close to the circle, but never reaching it.

### Example: Geodesics of Spheroid

A spheroid is obtained by rotating a ellipse, say $\frac{x^2}{p^2} + \frac{z^2}{q^2} = 1, x > 0$ around z-axis. The distance is of $[0, p]$

For $0 < \Omega < p$, we must have that $x^2 = p^2 (1 - \frac{z^2}{q^2}) \geq \Omega^2\implies z \in [-q\sqrt{1-\frac{\Omega^2}{p^2} }, q\sqrt{1-\frac{\Omega^2}{p^2} }]$. Similar to the hyperboloid example, every point on the boundary will bounce off the boundary circle and is symmetric around $p$, and crosses every parallel in the region.  
For $\Omega = p$, it is the parallel $z=0$. 

### Example: Geodesics of Torus

Rotating $(x - a)^2 + z^2 = b^2, b > a > 0$. The distance is of $[a-b, a + b]$. 

For $\Omega < a-b$, spirals around the torus.  
For $\Omega = a - b$, if $p$ on the circle of radius $a-b$, then the geodesic is the parallel of radius $a-b$. Otherwise, spirals around and approaching the parallel of radius $a-b$ (for the similar reason of hyperboloid).  
For $a-b <\Omega < a+b$, we have that the region is the outer annular region with distance $\geq \Omega$, and bounces between parallels bounded in this region.  
For $\Omega = a+b$, the parallel of radius $a+b$. 

## Geodesics as Shortest Paths

Consider some unit-speed curve $\gamma: (a,b)\rightarrow \Sigma$, passing through fixed $p,q\in\Sigma$. If $\gamma$ is a shortest path from $p$ to $q$, then the part of $\gamma$ contained in any surface patch $\sigma$ must be the shortest path between any two of its points. Otherwise, we can have a shorter path.  

Therefore, consider a family of smooth curves $\gamma^\tau$ on some $\sigma$ passing through $p,q$, for each $\tau \in (-\delta, \delta)$ s.t. 
 - $\exists \epsilon > 0$ s.t. $\gamma^\tau$ is defined for all $t\in(-\epsilon, \epsilon)$ and for all $\tau \in (-\delta, \delta)$. 
 - $\gamma^\tau$ passing through $p, q$
 - The map $M: (-\delta,\delta)\times (-\epsilon, \epsilon). M(\tau, t) = \gamma^\tau(t)$ is smooth. 
 - $\gamma^0 = \gamma$ is the shortest path. 

And the length is defined by the arc-length $L(\tau) = \int_a^b \|\dot\gamma^{\tau}\|dt$

__Theorem__ $\gamma$ is a geodesic IFF $\frac{dL}{dt}\mid_0 = 0$.

Note that we can only assume $\gamma^0$ is unit-speed, but not for $\tau \neq 0$. 

### Implications

IF $\gamma$ is a shortest path, then $L$ must have an absolute minimum when $\tau = 0$, implying that $\frac{dL}{dt}\mid_0 = 0$, hence $\gamma$ is a geodesic. 

IF $\gamma$ is a geodeisc on $\sigma$ through $p,q$, then $L(\tau)$ has a stationary point when $\tau = 0$, but this need not to be an absolute minimum, or even a local minimum. Therefore, geodesic does NOT imply shortest path. (Thinking about the two arcs of a great circle around the sphere). 

A shortest path (minimum) on a surface may not exists, for example, a plane with a hole in the straight line connecting $p,q$.  

__Theorem__ If $\Sigma$ is a closed, connected subset of $\mathbb R^3$, then shortest path exists. 
