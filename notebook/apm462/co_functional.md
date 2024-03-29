# Constrainted Optimization on Calulus of Variations

## Isoperimetric Constraints

### _Thrm_. First Order Necessary Conditions 


Define functionals

\begin{align*}
F[u] := \int_a^b L^F(x, u(x), u'(x)) \, dx \\
G[u] L= \int_a^b L^G(x, u(x), u'(x)) \, dx.
\end{align*}

Our problem is of the form

\begin{align*}
\min_{u \in \mathcal{A}} \qquad &F[u] \\
\text{subject to } &G[u] = \mathrm{const} \\
\mathcal{A} &= \{ u \in C^1([a, b], \mathbb R) : u(a) = A, u(b) = B \}.
\end{align*}


Suppose $u_*$ is a regular point of $G$ (i.e. $\frac{\delta G}{\delta u}(u_*) \neq 0$) which is a minimizer of $F$ subject to the equality constraint. Then there is a $\lambda \in \mathbb R$ such that

$$\frac{\delta F}{\delta u}(u_*) + \lambda \frac{\delta G}{\delta u}(u_*) = 0$$


_The completed proof is too long, you can see a proof on one case in the Additional Examples_

Recall that

$$\frac{\delta F}{\delta u}(u_*) = -\frac{d}{dx} L_p^F + L_z^F$$

and similarly for $\frac{\delta G}{\delta u}(u_*)$, so we can write the first order necessary conditions that we just described as 

$$-\frac{d}{dx} \left[ (L^F + \lambda L^G)_p \right] + \left( L^F + \lambda L^G \right)_z = 0$$

where it is understood at which point the partials of the Lagrangians are evaluated.

## Holonomic Constraints

We consider a functional $F$ depending on three functions:

$$F[\underbrace{x(\cdot), y(\cdot), z(\cdot)}_{u(\cdot)}] = \int_a^b L(t, \underbrace{x(t), y(t), z(t)}_{u(t)}, \underbrace{x'(t), y'(t), z'(t)}_{u'(t)}) \, dx$$

subject to a $C^1$constraint $H(x(t),y(t),z(t)) = 0$ for $t \in [a, b]$ with $\nabla H \neq 0$ on a space 

$$\mathcal{A} = \{ u : [a, b] \to \mathbb R^3 : u \text{ is } C^1, u(a) = A, u(b) = B \}$$

(So the function "curves" lie on a surface in $\mathbb R^3$.) We would like to minimize $F[u(\cdot)]$ where $H(u(t)) = 0$ and $u \in \mathcal{A}$. The Euler-Lagrange equations in this case are

$$\begin{pmatrix}
\frac{\delta F}{\delta x}(u)(t) \\
\frac{\delta F}{\delta y}(u)(t) \\
\frac{\delta F}{\delta z}(u)(t)
\end{pmatrix} + \lambda(t) \begin{pmatrix}
H_x(u(t)) \\
H_y(u(t)) \\
H_z(u(t))
\end{pmatrix} = \begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}$$

We may succinctly write this as

$$\frac{\delta F}{\delta u} + \lambda (t) \nabla H = 0$$

which parallels nicely with the finite-dimensional case, if we consider variational problems to be infinite-dimensional problems.

### Example: Motion of a Spherical Pendulum

Consider again the example of the spherical pendulum. The Lagrangian function is

$$L(t, x,y,z, \dot{x}, \dot{y}, \dot{z}) = \frac{1}{2} m (\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - mgz$$

(Kinetic energy minus potential energy.) Thus the functional we wish to minimize is

$$F[x(\cdot), y(\cdot), z(\cdot)] = \int_a^b L(t, x(t), y(t), \dot{x}(t), \dot{y}(t), \dot{z}(t)) \, dt$$

subject to the constraint that $(x(t), y(t), z(t))$ is on the sphere of radius $\ell$, i.e.

$$H(x(t), y(t), z(t)) = \frac{1}{2}(x(t)^2 + y(t)^2 + z(t)^2) - \frac{1}{2} \ell^2 = 0$$

This is a holonomic constraints problem. Last week we solved this by parametrizing the sphere with spherical coordinates, freeing ourselves of the constraint. Now, we can use the first order necessary constraints to solve this. 

Since the pendulum takes the path which minimizes the net difference in kinetic and potential energy, solutions to this problem will be the paths the pendulum takes depending on the initial conditions. 

To match the notation we had before, we have

\begin{align*}
L(t, z_1,z_2,z_3, p_1,p_2,p_3) &= \frac{1}{2} (p_1^2 + p_2^2 + p_3^2) - mgz_3 \\
H(x,y,z) &= \frac{1}{2} (x^2+y^2+z^2) - \frac{1}{2} \ell^2.
\end{align*}

The partials we want are are

\begin{align*}
L_{p_1} &= mp_1 &L_{p_2} &= mp_2 &L_{p_3} &= mp_3 \\
L_{z_1} &= 0 &L_{z_2} &= 0 &L_{z_3} &= -mg \\
H_x &= x &H_y &= y &H_z &= z
\end{align*}

We have

\begin{align*}
\frac{\delta F}{\delta x} = -m \ddot{x}(t) \quad\frac{\delta F}{\delta y} = -m \ddot{y}(t) \quad\frac{\delta F}{\delta y} = -m \ddot{z}(t) - mg.
\end{align*}

The Euler-Lagrange equations are

$$\begin{pmatrix}
-m \ddot{x}(t) \\
-m \ddot{y}(t) \\
-m \ddot{z}(t) - mg
\end{pmatrix} + \lambda (t) \begin{pmatrix}
x(t) \\ y(t) \\ z(t)
\end{pmatrix} \equiv \begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}$$

subject to the constraint $x(t)^2 + y(t)^2 + z(t)^2 = \ell^2$. There are four equations are four unknowns, so, in principle, the system may be solved.

We will solve this in the special case that $y \equiv 0$, $\ell = 1$, and $m = 1$. We lie in the $xy$-plane. We obtain

\begin{align*}
\ddot{x}(t) &= \lambda(t)x(t) \\
\ddot{z}(t) &= \lambda(t)z(t) - g \\
x(t)^2 + z(t)^2 &= 1.
\end{align*}

Parametrize by $x(t) = \sin \theta(t)$ and $z(t) = -\cos \theta(t)$, so that

\begin{align*}
\dot{x} &= \dot{\theta} \cos \theta \\
\dot{z} &= \dot{\theta} \sin \theta
\end{align*}

and

\begin{align*}
\ddot{x} &= \ddot{\theta} \cos \theta - \dot{\theta}^2 \sin \theta, \\
\ddot{z} &= \ddot{\theta} \sin \theta + \dot{\theta}^2 \cos \theta.
\end{align*}

Plugging these into the Euler-Lagrange equations gives

\begin{align*}
\ddot{\theta} \cos \theta - \dot{\theta}^2 \sin \theta &= \lambda \sin \theta \\
\ddot{\theta} \sin \theta + \dot{\theta}^2 \cos\theta &= -\lambda \cos \theta - g.
\end{align*}

Multiplying the second equation by $\sin \theta$ gives, after a bit of simplifying,

$$\ddot{\theta} \sin^2 \theta + \dot{\theta}^2 \sin \theta \cos \theta = -\ddot{\theta} \cos^2 \theta + \dot{\theta}^2 \sin \theta \cos \theta - g \sin \theta$$

This simplifies to

$$\ddot{\theta} = -g \sin \theta$$

the equation of motion of a planar pendulum.

## Sufficient Conditions and Convexity

Recall that if $u_* \in \mathcal{A} = \{ u \in C^1([a, b]) : u(a) = A, u(b) = B \}$ is a minimizer of the functional

$$F[u(\cdot)] := \int_a^b L(x, u(x), u'(x)) \, dx$$

Then it satisfies the "primitive" Euler-Lagrange equation

$$\int_a^b \Bigg[ L_z(x, u_*(x), u_*'(x))v(x) +  L_p(x, u_*(x), u_*'(x))v'(x) \Bigg] \, dx = 0$$

for all test functions $v$ on $[a, b]$.

__Lemma__ Assume the conditions above. Suppose $L = L(x,z,p)$ is a $C^1$ function, and that for each $x \in [a, b]$, $L(x, \cdot, \cdot)$ is convex. If $u_*$ satisfies (*) above, then $F[u_*(\cdot)] \leq F[u_*(\cdot) + v(\cdot)]$ for all test functions $v$ on $[a, b]$.

_The lemma states, roughly, that if $u_*$ is a minimizer, then it must be a global minimizer._

_proof_. Recall the $C^1$ criterion for convexity of a function $f : \mathbb R^n \to \mathbb R$: $f$ is convex if and only if $f(a + b) \geq f(a) + \nabla f(a) \cdot b$ for all $a,b \in \mathbb R^n$. We will apply this criterion to the convex function $L(x, \cdot, \cdot) : \mathbb R \times \mathbb R \to \mathbb R$. Directly applying the criterion gives

$$L(x, z + \tilde{z}, p + \tilde{p}) \geq L(x,z,p) + \underbrace{\nabla_{(z,p)}L(z,z,p) \begin{pmatrix}
\tilde{z} \\ \tilde{p}
\end{pmatrix}}_{=L_z(x,z,p)\tilde{z} + L_p(x,z,p)\tilde{p}}$$

Then

\begin{align*}
F[u_*(\cdot) + v(\cdot)] &= \int_a^b L(x, u_*(x) + v(x), u_*'(x) + v'(x)) \, dx \\
&\geq \int_a^b L(x, u_*(x), u_*'(x)) \, dx +  \underbrace{\int_a^b \Bigg[ L_z(\cdots)v(x) + L_p(\cdots)v'(x) \Bigg] \, dx}_{=0} \\
&= \int_a^b L(x, u_*(x), u_*'(x)) \, dx \\
&= L[u_*(\cdot)].
\end{align*}


### _Thrm_. Convex Domains

Recall that we were originally looking at convex functions $f : \Omega \to \mathbb R$, where $f$ is $C^1$ and convex and $\Omega \subseteq \mathbb R^n$ is convex. We had a theorem:

__Claim__. Assume the above conditions. $x_*$ is a minimizer of $f$ on $\Omega$ if and only if $\nabla f(x_*)(x - x_*) \geq 0$ for all $x \in \Omega$. 

Apply on variational 

Consider a functional

$$F[u(\cdot)] := \int_a^b L(x, u(x), u'(x)) \, dx$$

Let $\mathcal{A} = \{ u \in C^1([a, b]) : u(a) = A, u(b) = B \}$. Let $\Omega$ be a convex subset of $\mathcal{A}$, and suppose that $u_*$ is a minimizer of $F$ on $\Omega$. Then $F[u_*(\cdot) + sv(\cdot)] \geq F[u_*(\cdot)]$ for all $s$ and all test functions $v$ on $[a, b]$, and

$$\int_a^b \frac{\delta F}{\delta u}(u_*)(x)(u(x) - u_*(x))\, dx \int_a^b \frac{\delta F}{\delta u}(u_*)(x)v(x)\,dx = \left. \frac{d}{ds} \right|_{s=0} F[u_*(\cdot) + sv(\cdot)] \geq 0$$

for all $u \in \Omega$. 

### Example
Suppose $F[u(\cdot)] = \int_0^1 \frac{1}{2} \left( u'(t)^2 + u(t) \right) \, dt$
where $\mathcal{A}$ is the set of $C^1$ functions on $[0, 1]$ that are zero at the endpoints, and $\Omega = \{ u \in \mathcal{A} : u(t) \geq \sin^2(\pi t) \}$. One can check that $\Omega$ is convex. The Lagrangian function is $L(x,z,p) = \frac{1}{2}(p^2 + z)$. This is a convex function of $(z,p)$, so it satisfies the conditions of the first lemma. Then if $u_*$ minimizes $F$ on $\Omega$, let $f(s) = F[(1 - s)u_*(\cdot) + su(\cdot)]$. We are asked to show that $f'(0) \geq 0$. 
