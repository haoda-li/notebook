# Limit, Continuity, and Differentiability

The definitions for continuity and differentiability of Complex Functions are very similar to the definition in $\mathbb R$. However, note that if we consider complex numbers as on the complex plane, it's actually a ball instead of a segment, it's somewhat similar to $\mathbb R^2$, but take special note that they are not identical to each other. 

## Limits

__Example__ evaluate limits

\begin{align*}
\lim_{z\rightarrow i} z+z^{-1} &= \lim_{z\rightarrow i} z+\frac{\bar z}{|z|} = i + \frac{-i}{1} = 0\\
\lim_{z\rightarrow i}\sinh z&= \sinh i = i\sin 1
\end{align*}

## Continuity
Known that any $f:\mathbb C\rightarrow \mathbb C$ can be decomposed into real and imaginary parts $f = u+iv, u:\mathbb R\rightarrow \mathbb R, v:\mathbb R\rightarrow \mathbb R$ with $z = x+iy$. Therefore, if $u,v$ is continuous at $(x_0, y_0)$, then f is continuous at $z_0=x_0+iy_0$ with limit

$$\lim_{z\rightarrow z_0}f(z) = \lim_{(x,y)\rightarrow (x_0, y_0)} u(x, y) + iv(x, y) = u(x_0, y_0) + iv(x_0, y_0)$$

Conversely, we can also prove $f$ continuous implies $u$ and $v$ are both continuous. 

## Differentiation Laws
Differentiation laws on sum, product, quotient, composition, power, trigonometric all hold on complex numbers. The proof is similar to real number ones, hence some are omitted. 

### Example. LHospitals Rules for both 0

If $f(z)$ and $g(z)$ have formal power series about $a$ and $f(a)=f'(a) = \cdots = f^{(k)}=g(a)=g'(a) = \cdots = g^{(k)} = 0$ with $f^{(k+1)}(a)$ and $g^{(k+1)}(a)$ note simultaneously $0$. Then, $\lim_{z\rightarrow a}f(z)/g(z) = f^{(k+1)}(a)/g^{(k+1)}(a)$. 

_proof_ For every $k$, 

\begin{align*}
\lim_{z\rightarrow a}\frac{f^{(k)}(z)}{g^{(k)}(z)} &= \lim_{z\rightarrow a}\frac{f^{(k)}(z)-f^{(k)}(a)}{g^{(k)}(z)-g^{(k)}(a)}\\&= \lim_{z\rightarrow a}\frac{\frac{f^{(k)}(z)-f^{(k)}(a)}{z-a}}{\frac{g^{(k)}(z)-g^{(k)}(a)}{z-a}}
\end{align*}

Note that $f^{(k)}(z), g^{(k)}(z)$ are differentiable, so that 

$$\lim_{z\rightarrow a}\frac{\frac{f^{(k)}(z)-f^{(k)}(a)}{z-a}}{\frac{g^{(k)}(z)-g^{(k)}(a)}{z-a}} = \lim_{z\rightarrow a}\frac{f^{(k+1)}(z)}{g^{(k+1)}(z)}$$

If $\lim_{z\rightarrow a}\frac{f^{(k+1)}(z)}{g^{(k+1)}(z)}$ exist to be $\frac{f^{(k+1)}(a)}{g^{(k+1)}(a)}$, then all limits ends to be $\frac{f^{(k+1)}(a)}{g^{(k+1)}(a)}$.


## Cauchy Riemann Equations

__Claim__  Consider some complex function $f:\mathcal R\rightarrow \mathbb C, f(z)=u(z)+iv(z)$ defined on some regions $\mathcal R\subseteq \mathbb C$. 
$f$ is differentiable IFF 

$$\partial_x u = \partial_yv \land \partial_x v = -\partial_yu$$


Note that this automatically implies that $u,v$ need to have derivative, hence also are continuous. 


Define $\tilde f: \tilde{\mathcal R}\rightarrow \mathbb R^2: f(x, y) = (\tilde u(x, y), \tilde v(x, y))$. Since $f$ is differentiable, the limit will exist from any approach, and the derivate is $f'(z) = a(x)+ib(y)$ for $a(x), b(y)\in\mathbb R$.  
Consider approach only from the real line, let $t\in\mathbb R$

\begin{align*}
&\lim_{t\rightarrow 0} \frac{f(z_0+t) - f(z_0)}{t}\\ = &\lim_{t\rightarrow 0} \frac{u(z_0+t) + iv(z_0+t)}t - \frac{u(z_0) + iv(z_0)}{t}\\ = &a(x_0) + ib(y_0)
\end{align*}

On the projected $\mathbb R^2$ function, 

$$\lim_{t\rightarrow 0}\frac{\tilde u(x_0+t, y_0) - u(x_0,y_0)}t +\frac{\tilde v(x_0+t, y_0) - v(x_0,y_0)}{t} = \partial_x\tilde u + \partial_x\tilde v$$

So that 

$$(\partial_x\tilde u ,\partial_x\tilde v) = (a, b)$$

Similarly, if we approach only from the imaginary line, we have 

\begin{align*}
\lim_{t\rightarrow 0}\frac{f(z_0+it) - f(z_0)}{it} &= \lim_{t\rightarrow 0}-i\frac{f(z_0+it) - f(z_0)}{t}\\
&= \lim_{t\rightarrow 0} \frac{v(z_0+it) - v(z_0)}t - i\frac{u(z_0+it) - u(z_0)}t
\end{align*}

So that 

$$(\partial_y\tilde v, - \partial_y\tilde u) = (a, b)$$

Therefore, we have the Jacobian as 

$$D_{\tilde f}(x_0, y_0) = \begin{bmatrix}a(z_0)&-b(z_0)\\b(z_0)&a(z_0)\end{bmatrix}$$

Therefore, we may notice that $\mathbb R^2$-differentiable only approach from $2$ lines, while $\mathbb C$-differentiable can approach from other curves. So $C$-differentiable implies $\mathbb R^2$-differentiable, but ont the converse. For example

$$f(z) = \bar z = x -iy, u = x, v = -y$$

However, 

$$\lim_{\Delta z\rightarrow 0}\frac{\overline{(z_0 + \Delta z)} - \bar z_0}{\Delta z} = \lim_{\Delta z\rightarrow 0}\frac{\overline{\Delta z}}{\Delta z}$$

Taking $\Delta z = re^{i\theta}, \overline{\Delta z} = re^{-i\theta}$, the limit becomes $\lim_{\Delta z\rightarrow 0}e^{-2i\theta}$, note that $\Delta z = r(\cos\theta + i\sin\theta)$ so that if we approach with fixed $\theta$ and $r\rightarrow 0$, it gives different limits. Hence the limit does not exist. 

### Derivative from Cauchy Riemann Equations
Note that from the proof above, we have shown that if Cauchy Riemann conditions hold, then the derivative of some complex function $f$ is

$$f'(z) = u_x + iv_x = v_y - iu_y$$

### Cauchy Riemann Equation in Polar Form
__Theorem__ $f = u+iv$ is analytic at $z = re^{i\theta}, r>0, \theta\in[0, 2\pi)$ IFF

$$u_r = r^{-1}v_\theta, v_r = -r^{-1}u_\theta$$

and the partial derivatives are continuous. 

_proof_. Note that $re^{i\theta} = r\cos(\theta) + ri\sin(\theta)$ so that $(x, y) = (r\cos\theta, r\sin\theta)$. Follow chain rule

\begin{align*}
u_r &= u_x x_r + u_yy_r= u_x\cos\theta + u_y\sin\theta\\
u_\theta &= u_x x_\theta + u_yy_\theta= -r(u_x\sin\theta + u_yr\cos\theta)\\
v_r &= v_x x_r + v_yy_r= v_x\sin\theta + u_y\cos\theta\\
v_\theta &= v_x x_\theta + v_yy_\theta= r(v_x\cos\theta - u_y\sin\theta)
\end{align*}

Then, using CR equations, we can establish the equalities

### Derivative in Polar Form
Using the relationship above, we can then apply chain rule to compute $f'$ as 

$$f'(z) = (\cos\theta - i\sin\theta)(u_r + iv_r) = e^{-i\theta}(u_r + iv_r)$$

__Corollary__ The level set of $u$, $C = \{(x, y) : u(x, y) = c_1, c_1\in\mathbb R\}$, are orthogonal to the level set of $v$, at point $z_0$. 

_proof_. $\nabla u\cdot \nabla v = u_xv_x + u_yv_y = -u_xu_y + u_yu_x = 0$, so that their gradient is orthogonal at $z_0$, and then each of the level-set is orthogonal to their gradient, hence also orthogonal to each other. 

__Example__ Show that $Re(z)$ and $Im(z)$ are nowhere differentiable.  
Let $\tilde f(x, y) = x$ so that its Jacobian is $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ hence Cauchy Riemann equations does not hold, hence not differentiable. ($Im(z)$ is similar). 

## Analytic Function

$f:\mathcal R\rightarrow \mathbb C$ is __analytic__ at $z_0$ IFF it is differentiable within the neighborhood of $z_0$. $f$ is an __analytic__ (or sometimes __holomorphic__) is it is analytic on each point on the domain. 

__Singular point__ is some point $z_0$ that $f$ fails to be analytic. 

In fact, a complex function is analytic, then it is also infinitely differentiable (as of a power series function on the reals). 

Also, take a note that the Laplacians of u and v, given CR conditions, satisfy that

$$\nabla^2 u = \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = \frac{\partial}{\partial x}\frac{\partial v}{\partial y} - \frac{\partial}{\partial y}\frac{\partial v}{\partial x} = 0, \nabla^2v = 0$$

So that $u,v$ are harmonic conjugate of each other. We can obtain $v$ given $u$, then as well as $f$. 

__Example__ Take $u(x,y) = y^2 - x^2$. Then $u_x = -2x = v_y, u_y = 2y = -v_x$, implies that $v = -2xy + c$ for some constant $c$. So that 

$$f(z) = y^2-x^2 + i(-2xy+c) = -z^2 + ic$$

## Differentiability at Infinity

The __limit at infinity__ $\lim_{z\rightarrow\infty}f(z) = L$ is defined as $\forall \epsilon > 0. \exists N > 0. \forall z\in\mathbb C. |z|> N\implies |f(z)-L| < \epsilon$.

Define $g:R\rightarrow\mathbb C, g(z):=\begin{cases}f(z^{-1})&z\neq 0\\L &z=0\end{cases}$.  
Then, $f$ is differentiable/analytic at $\infty$ is $g(z)$ is differentiable/analytic at $0$. 

__Example__ Consider $f(z) = z^{-1}$, then $g(z) = z$ is differentiable at 0, so that $z^{-1}$ is differentiable at $\infty$. $z$ is not differentiable at $\infty$, since $z^{-1}$ is not differentiable at $0$.
