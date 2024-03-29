# Unconstrainted Optimization on Calulus of Variations

## Introducing The Calculus of Variations

Consider the problem

\begin{align*}
\text{minimize } &F[u] \\
&u \in \mathcal{A},
\end{align*}

where $\mathcal{A}$ is a set of functions. Here, $F$ is a function of functions, often called a __Functional__. This is the general unconstrained calculus of variations problem.

For example, consider

$$\mathcal{A} = \{ u \in C^1([0, 1], \mathbb R) : u(0) = u(1) = 1  \}$$

Define $F : \mathcal{A} \to \mathbb R$ by

$$F[u(\cdot)] := \frac{1}{2} \int_0^1 (u(x)^2 + u'(x)^2) \, dx$$

To solve the minimization problem

\begin{align*}
\text{minimize } &F[u] \\
&u \in \mathcal{A}
\end{align*}

is to find a $u^* \in \mathcal{A}$ such that $F[u^*] \leq F[u]$ for all $u \in \mathcal{A}$.

## _Thrm_. Fundamental Lemma of Calculus of Variations
__Claim__. Suppose $g \in C^0([a,b])$. If $\int_a^b g(x)v(x) \, dx = 0$ for all test functions $v$ on $[a,b]$, then $g \equiv 0$ on $[a,b]$.

_proof_. Suppose $g\not\equiv 0$. Then there is an $x_0 \in (a,b)$ such that $g(x_0) \neq 0$. (We can ensure that $x_0$ is in the interior of the interval because of continuity.) Assume without loss of generality that $g(x_0) > 0$. There exists an open neighbourhood $(c,d)$ of $x_0$ inside $(a,b)$ on which $g$ is positive. Let $v$ be a $C^1$ function on $[a,b]$ such that $v > 0$ on $(c,d)$ and $v = 0$ otherwise. Then $v$ is a test function on $[a,b]$, so by the hypotheses,
$0 = \int_a^b g(x)v(x) \, dx = \int_c^d g(x)v(x) \, dx > 0$
a contradiction.

__Intuitions__. Fix $v \in C^1([0,1],\mathbb R)$ with $v(0) = v(1) = 0$. Suppose $u^*$ is a minimizer of $F$ on $\mathcal{A}$. Clearly $u^* + sv \in \mathcal{A}$ for all $s \in \mathbb R$. Define $f : \mathbb R \to \mathbb R$ by $f(s) := F[u^* + sv]$. Then $f(s) \geq f(0)$ for all $s$, since $u^*$ is a minimizer of $F$. Then $0$ is a minimizer of $f$, implying $f'(0) = 0$. How do we actually compute $f'(0)$? Since

\begin{align*}
f(s) &= \frac{1}{2} \int_0^1 (u^*(x) + sv(x))^2 + (u^{*'}(x) + sv'(x))^2 \, dx \\
&= \frac{1}{2} \int_0^1 (u^*(x)^2 + u^{*'}(x)^2) \, dx + s\int_0^1 ( u^*(x)v(x) + u^{*'}(x)v'(x) ) \, dx + \frac{s^2}{2} \int_0^1 (v(x)^2 + v'(x)^2) \, dx,
\end{align*}

implying that

$$f'(s) = \int_0^1 ( u^*(x)v(x) + u^{*'}(x)v'(x) ) \, dx + s\int_0^1 (v(x)^2 + v'(x)^2) \, dx$$

or

$$0 = \int_0^1 ( u^*(x)v(x) + u^{*'}(x)v'(x) ) \, dx \text{ for all } v \in C^1([0,1], \mathbb R) \text{ such that } v(0)=v(1)=0 \:(*)$$

The above equality holds for all $v \in C^1([0,1], \mathbb R)$ such that $v(0)=v(1)=0$. This is a primitive form of the first order necessary conditions.

Let us call the functions $v$ described in $(*)$ the test functions on $[0,1]$. We would like to write $(*)$ in a more useful way. Let us make the simplifying assumption that $u^*$ is $C^2$. Integration by parts gives

$$\int_0^1 u^{*'}(x)v'(x) \, dx = \underset{=0}{\left. u^{*'}(x)v(x) \right|_0^1} - \int_0^1 u^{*''}(x) v(x) \, dx = \int_0^1 u^{*''}(x) v(x) \, dx$$

By substituting this into $(*)$ we obtain

$$\int_0^1 (u^*(x)v(x) - u^{*''}(x)v(x))\, dx = 0$$

Factor the common $v$ out to get

$$\int_0^1 (u^*(x) - u^{*''}(x))v(x) \, dx = 0 \text{ for all test functions } v \text{ on } [0,1]$$

So we have a continuous function $u^*(x) - u^{*''}(x)$ that is zero whenever "integrated against test functions". We claim that any function satisfying this condition must be zero. This result or its variations is called the fundamental lemma of the calculus of variations. We shall show that $u^* = u^{*''}$ on $[0,1]$; this gives us the first order necessary conditions we wanted in the first place.


### _Defn_. Variational Derivative
Given $u \in \mathcal{A}$, suppose there is a function $g : [a,b] \to \mathbb R$ such that 

$$\left. \frac{d}{ds} \right|_{s = 0} F[u + sv] = \int_a^b g(x) v(x) \, dx$$

for all test functions $v$ on $[a,b]$. Then $g$ is called the variational derivative of $F$ at $u$. We denote the function $g$ by $\frac{\delta F}{\delta u}(u)$.

We can think of $\frac{\delta F}{\delta u}(u)$ as an analogue of the gradient. We have

$$\left. \frac{d}{ds} \right|_{s = 0} F[u + sv] = \int_a^b \frac{\delta F}{\delta u}(u)(x) v(x) \, dx$$

for all test functions $v$ on $[a,b]$. Compare this with the finite-dimensional formula

$$\left. \frac{d}{ds} \right|_{s=0} f(u + sv) = \nabla f(u) \cdot v = \sum_{i=1}^n \nabla f(u)_i v_i$$

if one thinks of the integral as an "infinite sum of infinitesimally small pieces", then we can understand how the functional derivative might be an "infinite-dimensional" version of the gradient.

## Euler Lagrange Equation in 1-Dim

__Lemma__ (A corollary of Fundamental Lemma) Suppose $u_* \in \mathcal{A}$ satisfies $u_* + v \in \mathcal{A}$ for all test functions $v$ on $[a,b]$. Then if $u_*$ minimizes $F$ on $\mathcal{A}$ and if $\frac{\delta F}{\delta u}(u_*)$ exists and is continuous, then $\frac{\delta F}{\delta u}(u_*) \equiv 0$.

### _Thrm_. Euler-Lagrange equation

__Claim__. Suppose $L,u$ are $C^2$ functions. Then $\frac{\delta F}{\delta u}(u)$ exists, is continuous, and
$\frac{\delta F}{\delta u}(u)(x) = -\frac{d}{dx} L_p(x,u(x), u'(x)) + L_z(x,u(x),u'(x))$

_proof_. Let $v$ be a test function on $[a,b]$. Then

\begin{align*}
\left. \frac{d}{ds} \right|_{s=0} F[u + sv] &= \left. \frac{d}{ds} \right|_{s=0} \int_a^b L(x, u(x) + sv(x), u'(x) + sv'(x)) \, dx \\
&=  \int_a^b \left. \frac{d}{ds} \right|_{s=0} L(x, u(x) + sv(x), u'(x) + sv'(x)) \, dx \\
&= \int_a^b \left( L_x(\cdots) \frac{dx}{ds} + L_z(\cdots)\frac{d}{ds}(u(x) + sv(x)) + L_p(\cdots)\frac{d}{ds}(u'(x) + sv'(x)) \right) \, dx \\
&= \int_a^b \left( L_z(x,u(x),u'(x))v(x) + L_p(x,u(x),u'(x))v'(x) \right)\, dx \\
&= \int_a^b L_z(x,u(x),u'(x))v(x) \, dx + \int_a^b L_p(x,u(x),u'(x))v'(x) \, dx \\
&= \int_a^b \left( -\frac{d}{dx} L_p(x,u(x),u'(x)) + L_z(x,u(x),u'(x)) \right) v(x) \, dx \qquad \text{integration by parts.}
\end{align*}

Since $u$ and $L$ are $C^2$, the function in the integrand is continuous. By the definition of the variational derivative we have the desired result.


### _Thrm_. DuBois-Raymond Lemma
The lemma allows us to relax the restrictions for the Euler-Lagrange equation to hold from twice continuously differentiable to only once continuously differentiable.

__Claim__. Suppose $\alpha, \beta$ are continuous functions on $[a,b]$ such that $\int_a^b ( \alpha(x)v(x) + \beta(x)v'(x) ) \, dx = 0$
for all test functions $v$ on $[a,b]$. Then $\beta$ is $C^1$, and $\beta' = \alpha$ on $[a,b]$.

_proof_. Let $A(x) = \int_a^x \alpha(t) \, dt$ be an antiderivative of $\alpha$. Since $\alpha$ is continuous, $A$ is $C^1$. Then

$$\int_a^b \alpha(x) v(x) \, dx = \int_a^b A'(x)v(x) \, dx = -\int_a^b A(x)v'(x) \, dx$$

By the original assumption,

$$0 = \int_a^b (\alpha(x)v(x) + \beta(x)v'(x)) \, dx = \int_a^b(-A(x) + \beta(x))v'(x) \, dx$$

We are done if we are able to show that $-A(x) + \beta(x)$ is constant on $[a,b]$. Let $\gamma = -A + \beta$. Define $C$ to be the constant

$$C := \frac{1}{b-a}\int_a^b \gamma(t) \, dt$$

so that $\int_a^b (\gamma(t) - C) \, dt = 0$. Define $v(x) := \int_a^x (\gamma(t) - C) \, dt$. The function $v$ is $C^1$ since $\gamma(t) - C$ is continuous, and $v(a) = v(b) = 0$; so $v$ is a test function on $[a,b]$. By some algebra,

$$\int_a^b (\gamma(x) - C)^2 \, dx = \int_a^b (\gamma(x) - C)v'(x) \, dx = 0$$

Since $(\gamma(x) - C)^2 \geq 0$ on $[a,b]$, we must have $\gamma(x) = C$. Therefore $\gamma$ is constant, which proves the lemma.

### Example

Consider two points $(a,A), (b,B)$ in $\mathbb R^2$ with $a < b$. We seek a function $u$ on $[a,b]$ with $u(a) = A$, $u(b) = B$, and with

$$F[u] := \int_a^b \sqrt{1 + u'(x)^2} \, dx$$

minimized. Denote by $\mathcal{A}$ the set of $C^1$ functions $u$ with $u(a) = A$ and $u(b) = B$. Suppose that $u_*$ is a minimizer. Then, by the previous lemma applied to the last result of the previous lecture, $u_*$ satisfies the Euler-Lagrange equation. Let $L(x,z,p) := \sqrt{1 + p^2}$. Then $L_z = 0$, and

$$L_p = \frac{p}{\sqrt{1 + p^2}}$$

The Euler-Lagrange equation is, in this case,

$$0 = -\frac{d}{dx} L_p + L_z = -\frac{d}{dx} \frac{u_*'(x)}{\sqrt{1 + u_*'(x))^2}} \:(*)$$

This implies that 

$$u_*'(x) = C\sqrt{1 + u_*'(x)^2}$$

for some constant $C$, implying

$$u_*'(x)^2 = C(1 + u_*'(x)^2) = C + C u_*'(x)^2$$

$$\implies u_*'(x)^2(1 - C) = C$$

hence $u_*'$ is constant, or $u_*(x) = \alpha x + \beta$ for some constants $\alpha, \beta$. As expected, the minimizer is a line. This answer is expected, since the shortest path joining two points is the line joining them.


### Example: Area of Revolution

Suppose $u$ is a $C^1$ function on an interval $[a,b]$. Consider the surface of revolution obtained by rotating the graph of $u$ on $[a,b]$ about the $x$-axis. Consider the functional

$$F[u] := \text{area of the surface of revolution obtained by rotating $\Gamma_u$ about the $x$-axis}$$

which is, by some calculus,

$$F[u] = \int_a^b 2\pi u(x) \sqrt{1 + u'(x)^2} \, dx$$

With the set $\mathcal{A}$ of functions defined as in the previous example, we seek to find a function $u_* \in \mathcal{A}$ minimizing $F$ on $\mathcal{A}$.

In this example, the Lagrangian is $L(x,z,p) = 2\pi z \sqrt{1 + p^2}$, which gives

$$L_z = 2\pi \sqrt{1 + p^2}, L_p = \frac{2\pi z p}{\sqrt{1 + p^2}}$$

The Euler-Lagrange equation is, in this case,

$$0 = -\frac{d}{dx} L_p + L_z = -\frac{d}{dx} \left[ \frac{2\pi u(x)u'(x)}{\sqrt{1 + u'(x)^2}} + 2\pi \sqrt{1 + u'(x)^2} \right]$$

Cancel the $2\pi$'s to get the ODE

$$\left[ \frac{u(x)u'(x)}{\sqrt{1 + u'(x)^2}} + \sqrt{1 + u'(x)^2} \right] = 0 \:(**)$$

By magic, the general solution to this differential equation has the form

$$u(x) = \beta \cosh\left(\frac{x - \alpha}{\beta} \right)$$

for some constants $\alpha, \beta$. We won't argue why we got this solution, but we can differentiate it and check that it solves the ODE; uniqueness theorems give us what we want.

$$u'(x) = \beta \sinh \left( \frac{x - \alpha}{\beta} \right) \frac{1}{\beta} = \sinh \left( \frac{x - \alpha}{\beta} \right)$$

$$\implies \sqrt{1 + u'(x)^2} = \cosh \left( \frac{x - \alpha}{\beta} \right)$$

It is now obvious that $u$ solves $(**)$. Therefore a minimizer $u_*$ must be of the form

$$u_*(x) = \beta \cosh \left( \frac{x - \alpha}{\beta} \right)$$

We may use the boundary conditions to find $\alpha, \beta$.

Consider the special case $(a,A) = (0, 1)$ and $(b, B) = (1,0)$. The boundary conditions on $u_*$ give us the system

\begin{align*}
\beta \cosh \left( \frac{x - \alpha}{\beta} \right) &= 1 \\
\beta \cosh\left( \frac{1 - \alpha}{\beta} \right) &= 0.
\end{align*}

Since $\cosh$ is strictly positive, the second equation gives us $\beta = 0$, a contradiction. We conclude that there is no $C^1$ minimizer in this special case.


## Euler-Lagrange Equation in N-Dim

We consider a functional

$$F[u] := \int_a^b L(x, u(x), u'(x)) \, dx$$

where $u : [a,.b] \to \mathbb R^n$. In this case,

$$L : [a, b] \times \mathbb R^n \times \mathbb R^n \to \mathbb R$$

Our general space of functions will be denoted by 

$$\mathcal{A} := \{ u : [a,b] \to \mathbb R^n : u \in C^1, u(a) = A, u(b) = B \}.$$

The Euler-Lagrange equation from the real-valued case generalizes to 

\begin{align*}
-\frac{d}{dx} \nabla_p L(x, u_*(x), u_*'(x)) + \nabla_z L(x, u_*(x), u_*'(x)) = 0.
\end{align*}

The proof is a straightforward generalization of the proof given when $n = 1$.

### Example: Newton's Second Law
Let us consider an example from classical mechanics. We consider the physical situation of a point mass moving in a potential field. Denote by $V(x)$ the potential energy at a point $x$. The kinetic energy of a point of mass $m$ with velocity $v$ is $\frac{1}{2} m |v|^2$. Define the Lagrangian

$$L(t,x,v) = \frac{1}{2} m |v|^2 - V(x)$$

as the difference between the kinetic and potential energies. Suppose our particle is moving along a path $x = x(t)$ parametrized by time in $\R^n$. Our functional is

$$F[x] := \int_{t_1}^{t_2} \left( \frac{1}{2} m |\dot{x}(t)|^2 - V(x(t)) \right) \, dt$$

This represents the difference between the kinetic energy and the potential energy \emph{along the entire path}. We can think of it as the net change in energy from the kinetic energy to potential energy along the path.

In this case, the Euler-Lagrange equations for a a minimizing path $x(t)$ are

$$0 = -\frac{d}{dt} \nabla_v L(t, x(t), \dot{x}(t)) + \nabla_x L(t, x(t), \dot{x}(t))$$

One computes that 

\begin{align*}
\nabla_v L(t,x,v) &= mv \\
\nabla_x L(t,x,v) &= -\nabla V(x).
\end{align*}

Then the Euler-Lagrange equations are

$${m \ddot{x}(t) = -\nabla V(x).}$$

