# Equality Constrained Finite Dimension Optimization

## Problem Definition

Consider the minimization problem

\begin{align*}
\text{min}\quad &f(x,y) \\
\text{subject to}\quad &h(x,y) = x^2 + y^2 - 1 = 0
\end{align*}

Suppose $(x_0, y_0)$ is a local minimizer. Two cases:
1. $\nabla f(x_0, y_0) \neq 0$: we claim that $\nabla f(x_0, y_0)$ is perpendicular to the tangent space to the unit circle $h^{-1}(\{0\})$ at $(x_0, y_0)$. If this is not the case, then we obtain a contradiction by looking at the level sets of $f$, to which $\nabla f$ is perpendicular. Therefore $\nabla f(x_0, y_0) = \lambda \nabla h(x_0, y_0)$ for some $\lambda$.

2. $\nabla f(x_0, y_0) = 0$: as in the previous case, $\lambda = 0$.

In either case, at a local minimizer, the gradient of the function to be minimized is parallel to the gradient of the constraints.


### _Defn_. Surface
For us, a surface is the set of common zeroes of a finite set of $C^1$ functions. 

### _Defn_. Differentiable Curve
For us, a differentiable curve on the surface $M \subseteq \mathbb R^n$ is the image of a $C^1$ function $x : (a, b) \to M$.

### _Defn_. Tangent Vector
Let $x(s)$ be a differentiable curve on $M$ that passes through $x_0 \in M$ at time $x(0) = x_0$. The velocity vector $v = \left. \frac{d}{ds} \right|_{s=0} x(s)$ of $x(s)$ at $x_0$ is, for us, said to be a tangent vector to the surface $M$ at $x_0$. The set of all tangent vectors to $M$ at $x_0$ is called the tangent space to $M$ at $x_0$ and is denoted by $T_{x_0}M$.

### _Defn_. Regular Point
Let $M = \{x \in \mathbb R^n : h_1(x) = \cdots = h_k(x) = 0\}$ be a surface. If $\nabla h_1(x_0), \dots, \nabla h_k(x_0)$ are all linearly independent, then $x_0$ is said to be a regular point of $M$.

### Claim 1
At a regular point $x_0 \in M$, the tangent space $T_{x_0} M$ is given by

$$T_{x_0} M = \{ y \in \mathbb R^n : \nabla \mathbf{h}(x_0)y = 0 \}$$


### Claim 2
Let $f, h_1, \dots, h_k$ be $C^1$ functions on the open set $\Omega \subseteq \mathbb R^n$. Let $x_0 \in M = \{ x \in \Omega : h_1(x) = \cdots = h_k(x) = 0 \}$. Suppose $x_0$ is a local minimizer of $f$ subject to the constraints $h_i(x) = 0$. Then $\nabla f(x_0)$ is perpendicular to $T_{x_0}M$.

_proof_. Without loss of generality, suppose $\Omega = \mathbb R^n$. Let $v \in T_{x_0}M$. Then $v = \left. \frac{d}{ds} \right|_{s=0}x(s)$ for some differentiable curve $x(s)$ in $M$ with $x(0) = x_0$. Since $x_0$ is a local minimizer of $f$, $0$ is a local minimizer of $f \circ x$, so $\nabla f(x_0) \cdot x'(0) = \nabla f(x_0) \cdot v = 0$.


## _Thrm_. First Order Necessary Conditions (Lagrange Multipliers)
__Claim__. Let $f, h_1, \dots, h_k$ be $C^1$ functions on some open $\Omega \subseteq \mathbb R^n$. Suppose $x_0$ is a local minimizer of $f$ subject to the constraints $h_1(x), \dots, h_k(x) = 0$, which is also a regular point of these constraints. Then there are $\lambda_1, \dots, \lambda_k \in \mathbb R$ ("Lagrange multipliers") such that

$$\nabla f(x_0) + \lambda_1 \nabla h_1(x_0) + \cdots + \lambda_k \nabla h_k(x_0) = 0$$


_proof_. Since $x_0$ is regular, $T_{x_0}M = \mathrm{span}(\{ \nabla h_1(x_0), \dots, \nabla h_k(x_0) \})^\perp$. By a lemma from last class, $\nabla f(x_0) \in (T_{x_0}M)^\perp$. Therefore $\nabla f(x_0) \in \mathrm{span}(\{ \nabla h_1(x_0), \dots, \nabla h_k(x_0) \})$, since we are dealing with a finite dimensional vector space. We are done.

### Example: Max volume of Box with constrained surface area

Given a fixed area $A > 0$, how do we construct a box of maximum volume with surface area $A$? Suppose the volume is $V(x,y,z) = xyz$ and the area is $A(x,y,z) = 2(xy+xz+yz)$. Our problem is stated as a maximization problem, so we have to convert it to a minimization problem. Let $f = -V$. We are therefore dealing with the problem

\begin{align*}
\text{minimize } &f(x,y,z) = -xyz \\
\text{subject to } &h(x,y,z) = A(x,y,z) - A = 0, x,y,z \geq 0
\end{align*}

But we don't know how to deal with inequality constraints right now, so we have to make some changes. Note that if any one of $x,y,z$ is zero, then the volume is zero. Therefore the problem we want to consider is really the problem

\begin{align*}
\text{minimize } &f(x,y,z) \\
\text{subject to } &h(x,y,z) = 0, x,y,z > 0
\end{align*}

Now, if $\Omega = \{(x,y,z) \in \mathbb R^3 : x,y,z > 0\}$, then the above minimization problem may be solved using the first order necessary condition we gave above, for the set $\Omega$ is open.

Suppose $(x_0, y_0, z_0)$ is a local minimizer of $f$ subject to the constraint $h(x,y,z) = 0$. This point is regular because we are only considering points whose coordinates are all positive. Then there is a $\lambda \in \mathbb R$ such that $\nabla f(x_0, y_0, z_0) + \lambda \nabla h(x_0, y_0, z_0) = 0$. Therefore
\[
(-y_0z_0, -x_0z_0, -x_0y_0) + \lambda (2y_0 + 2z_0, 2x_0 + 2z_0, 2x_0 + 2y_0) = (0,0,0).
\]
Equivalently, 

\begin{align*}
2\lambda (y_0 + z_0) &= y_0z_0 \\
2\lambda (x_0 + z_0) &= x_0z_0 \\
2\lambda (x_0 + y_0) &= x_0y_0
\end{align*}

Add all of these equations together:
\[
2\lambda( 2x_0 + 2y_0 + 2z_0 ) = x_0z_0 + x_0y_0 + y_0z_0 = \frac{A}{2} > 0
\]
implying that $\lambda > 0$. The first two equations tell us that

\begin{align*}
2\lambda x_0 (y_0 + z_0) &= x_0y_0z_0 \\
2\lambda y_0 (x_0 + z_0) &= x_0y_0z_0.
\end{align*}

Subtracting these two equations gives $2\lambda (x_0z_0 - y_0z_0) = 0$. Cancelling the $z_0$'s gives $2\lambda (x_0 - y_0) = 0$, and since $\lambda > 0$, we have $x_0 = y_0$. Since we could have done the same thing with the other pairs of equations, we get $x_0 = y_0 = z_0$. 

Physically, this tells us that in order to maximize the volume of a rectangular solid of fixed area, we must make a cube. Note that we haven't actually solved the maximization problem; we've only figured out what form its solutions must take.


## _Thrm_. Second Order Necessary Conditions
__Claim__. Let $f, h_1, \dots, h_k$ be $C^2$ on some open set $\Omega \subseteq \mathbb R^n$. Suppose $x_0$ is a regular point which is a local minimizer of $f$ subject to the constraints. Then  
1. There are $\lambda_1, \dots, \lambda_k \in \mathbb R$ such that
   
    $$\nabla f(x_0) + \lambda_1 \nabla h_1(x_0) + \cdots + \lambda_k \nabla h_k(x_0) = 0$$ 

2. The "Lagrangian"

    $$L(x_0) = \nabla^2 f(x_0) + \sum \lambda_i \nabla^2 h_i(x_0)$$

    is positive semi-definite on the tangent space $T_{x_0}M$, where $M = h_1^{-1}(\{0\}) \cap \cdots \cap h_k^{-1}(\{0\})$

_proof_. Let $x(s)$ be a smooth curve with $x(0) = 0$ in $M$. Recall that, by the product rule,

\begin{align*}
\frac{d}{ds} f(x(s)) &= \nabla f(x(s)) \cdot x'(s) \\
\frac{d^2}{ds^2} f(x(s)) &= x'(s) \cdot \nabla^2 f(x(s)) x'(s) + \nabla f(x(s)) \cdot x''(s).
\end{align*}

By the second order Taylor approximation, we have

$$0 \leq f(x(s)) - f(x(0)) = s \left. \frac{d}{ds} \right|_{s=0} f(x(s)) + \frac{1}{2}s^2 \left. \frac{d^2}{ds^2} \right|_{s=0} f(x(s)) + o(s^2)$$

This is, equivalently, 

$$0 \leq f(x(s)) - f(x(0)) = s \nabla f(x_0) \cdot \underbrace{x'(0)}_{\in T_{x_0}M} + \frac{1}{2}s^2 \left. \frac{d^2}{ds^2} \right|_{s=0} f(x(s)) + o(s^2)$$

Since the gradient at a regular local minimizer is perpendicular to the tangent space there, the first-order term above vanishes. We have

$$0 \leq \frac{1}{2}s^2 \left. \frac{d^2}{ds^2} \right|_{s=0} f(x(s)) + o(s^2)$$

By the definition of $M$, we may write the above as

$$0 \leq \frac{1}{2}s^2 \left. \frac{d^2}{ds^2} \right|_{s=0} \left[ f(x(s)) + \sum \lambda_i h_i(x(s)) \right] + o(s^2)$$

Or

$$0 \leq \frac{1}{2} s^2 x'(0) \cdot \underbrace{\left(\nabla^2 f(x_0) + \sum \lambda_i \nabla^2 h(x_0)\right)}_{=L(x_0)}x'(0) + \frac{1}{2} s^2 \underbrace{\left(\nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0)\right)}_{=0} \cdot x''(0) + o(s^2)$$

Divide by $s^2$:

$$0 \leq \frac{1}{2} x'(0) \cdot L(x_0) x'(0) + \frac{o(s^2)}{s^2}$$

By taking $s$ small it follows that $0 \leq \frac{1}{2} x'(0) \cdot L(x_0) x'(0)$. Since any tangent vector $v \in T_{x_0}M$ can be described as the tangent vector to a curve in $M$ through $x_0$, it follows that $L(x_0)$ is positive semi-definite on $T_{x_0}M$.


## _Thrm_. Second Order Sufficient Conditions

__Claim__. Consider functions $f, h_1, \dots, h_k$ which are $C^2$ on the open $\Omega \subseteq \mathbb R^n$. Suppose $x_0$ is a regular point of the constraints given by $h_1(x) = \cdots = h_k(x) = 0$. Let $M = \bigcap h_i^{-1}(\{0\})$. Suppose there exist $\lambda_1, \dots, \lambda_k \in \mathbb R$ such that

1. $\nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) = 0$
2. $L(x_0) = \nabla^2 f(x_0) + \sum \lambda_i \nabla^2 h_i(x_0)$

is positive definite on $T_{x_0}M$.  

Then $x_0$ is a strict local minimizer of $f$ on $M$.

_proof_. Recall that if $L(x_0)$ is positive definite on $T_{x_0}M$, then there is an $a > 0$ such that $v \cdot L(x_0)v \geq a\|v\|^2$ for all $v \in T_{x_0}M$. (This is very easily proven by diagonalizing the matrix.) Let $x(s)$ be a smooth curve in $M$ such that $x(0) = x_0$, and normalize the curve so that $\|x'(0)\| = 1$. We have
which becomes

\begin{align*}
f(x(s)) - f(x(0)) &= s \left. \frac{d}{ds} \right|_{s=0} f(x(s)) + \frac{1}{2} s^2 \left. \frac{d^2}{ds^2} \right|_{s=0} f(x(s)) + o(s^2) \\
&= s \left. \frac{d}{ds} \right|_{s=0} \left[ f(x(s)) + \sum \lambda_i h_i(x(s)) \right]+ \frac{1}{2} s^2 \left. \frac{d^2}{ds^2} \right|_{s=0} \left[ f(x(s)) + \sum \lambda_i h_i(x(s)) \right] + o(s^2) \\
&= s \underbrace{[ \nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) ]}_{=0 \text{ by 1.}} \cdot x'(0) + \frac{1}{2} s^2x'(0) \cdot L(x_0) x'(0)  \\
&\qquad\qquad\qquad\qquad\qquad + \frac{1}{2} s^2\underbrace{[ \nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) ]}_{=0 \text{ by 1.}} \cdot x''(0) + o(s^2) \\
&= \frac{1}{2} s^2 x'(0)^T L(x_0) x'(0) + o(s^2) \\
&\geq \frac{1}{2}s^2 a\|x'(0)\|^2 + o(s^2) \\
&= \frac{1}{2}s^2 a + o(s^2) \\
&= s^2 \left( \frac{1}{2}a + \frac{o(s^2)}{s^2} \right)
\end{align*}

For sufficiently small $s$, the above is positive, so $f(x(s)) > f(x_0)$ for all sufficiently small $s$. Since $x(s)$ was arbitrary, $x_0$ is a strict local minimizer of $f$ on $M$.


### Example 1
Recall the box example: maximizing the volume of a box of sides $x,y,z\geq 0$ subject to a fixed surface area $A > 0$. We were really minimizing the negative of the volume. We got $(x_0,y_0,z_0) = (l,l,l)$, where $l = \sqrt{A/6}$. Our Lagrange multiplier was $\lambda = \frac{A}{8(x_0+y_0+z_0)} = \frac{A}{24 l} > 0$. We had (after some calculation)

$$L(x_0,y_0,z_0) = (2\lambda - l)\begin{pmatrix}
0&1&1 \\
1&0&1 \\
1&1&0
\end{pmatrix}$$

Here, $2\lambda - l < 0$. We have 

$$T_{(x_0,y_0,z_0)}M = \mathrm{span}( \nabla h(x_0,y_0,z_0) )^\perp = \{ (u,v,w) \in \mathbb R^3 : u+v+w=0 \}$$

since $\nabla h(x_0,y_0,z_0) = (4l,4l,4l)$. If $(u,v,w) \in T_{(x_0,y_0,z_0)}M$ is nonzero,

\begin{align*}
\begin{pmatrix}
u&v&w
\end{pmatrix}(2\lambda - l)\begin{pmatrix}
0&1&1 \\
1&0&1 \\
1&1&0
\end{pmatrix} \begin{pmatrix}
u\\v\\w
\end{pmatrix} &= \begin{pmatrix}
u&v&w
\end{pmatrix}(2\lambda - l) \begin{pmatrix}
v+w \\ u+w \\ u+v
\end{pmatrix} \\
&= (2\lambda - l)\begin{pmatrix}
u&v&w
\end{pmatrix} \begin{pmatrix}
-u \\ -v \\ -w
\end{pmatrix} \\
&= -(2\lambda - l)(u^2+v^2+w^2) > 0,
\end{align*}

so by the SOSC under equality constraints, our point $(x_0,y_0,z_0)$ is a strict local maximizer of the volume. In fact, it is a strict global minimum (which is yet to be seen).


### Example 2

Consider the problem

\begin{align*}
\text{minimize } &f(x,y) = x^2-y^2 \\
\text{subject to } &h(x,y) = y = 0.
\end{align*}

Then

$$\nabla f(x,y) + \lambda \nabla h(x,y) = \begin{pmatrix}
2x \\ -2y
\end{pmatrix} + \lambda \begin{pmatrix}
0 \\ 1
\end{pmatrix} = \begin{pmatrix}
0 \\ 0
\end{pmatrix}$$

implying that $\lambda = 0$ and that $(x,y) = (0,0)$ is our candidate local minimizer. Since $\nabla h(x,y) \neq (0,0)$, the candidate is a regular point. We have

$$L(0,0) = \begin{pmatrix}
2 & 0 \\ 0 & -2
\end{pmatrix} + 0 \begin{pmatrix}
0 & 0 \\ 0 & 0
\end{pmatrix} = \begin{pmatrix}
2 & 0 \\ 0 & -2
\end{pmatrix}$$

which is not positive semi-definite __everywhere__. What about on the tangent space $T_{(0,0)}(\text{x-axis})=(\text{x-axis})$? Clearly it is positive definite on the $x$-axis, so by the SOSC that we just proved, $(0,0)$ is a strict local minimizer of $f$ on the $x$-axis. Thinking of level sets, this is intuitively true.

### Example 3
Consider the problem

\begin{align*}
\text{minimize } &f(x,y) = (x-a)^2 + (y-b)^2 \\
\text{subject to } &h(x,y) = x^2+y^2-1=0.
\end{align*}

Let us assume that $(a,b)$ satisfies $a^2+b^2>1$. We have $\nabla h(x,y) = (2x,2y)$, which is non-zero on $S^1$, implying that every point of $S^1$ is a regular point. Lagrange tells us that

$$\begin{pmatrix}
2(x-a) \\ 2(y-b)
\end{pmatrix} + \lambda
\begin{pmatrix}
2x \\ 2y
\end{pmatrix} = \begin{pmatrix}
0\\0
\end{pmatrix}$$

as well as $x^2+y^2=1$. This may be written

\begin{align*}
(1+\lambda)x &= a \\
(1+\lambda)y &= b \\
x^2+y^2 &= 1
\end{align*}

By our assumption that $a^2+b^2>1$, we have $\lambda \neq -1$. Therefore

$$\begin{pmatrix}
x \\ y
\end{pmatrix} = \frac{1}{1+\lambda}\begin{pmatrix}
a \\ b
\end{pmatrix}$$

which implies that

$$\frac{1}{1+\lambda} = \frac{1}{\sqrt{a^2+b^2}}$$

by the third equation. Therefore

$$\begin{pmatrix}
x_0 \\ y_0
\end{pmatrix} = \frac{1}{\sqrt{a^2+b^2}}\begin{pmatrix}
a \\ b
\end{pmatrix}$$

Thinking of level sets, this is intuitively true. The Lagrangian is

$$L(x_0,y_0) = \begin{pmatrix}
2 & 0 \\ 0 & 2
\end{pmatrix} + \lambda \begin{pmatrix}
2 & 0 \\ 0 & 2
\end{pmatrix} = \underbrace{(1+\lambda)}_{>0}\begin{pmatrix}
2 & 0 \\ 0 & 2
\end{pmatrix}$$

which, by the SOSC that we proved, proves that $(x_0, y_0)$ is a strict local minimizer of $f$ on $S^1$. In fact, this point is a global minimizer of $f$ on $S^1$, which follows immediately by the fact that $f$ necessarily takes on a global minimum on $S^1$ and that it only takes on the point $(x_0,y_0)$.


### Example 4: Proof of Lagrange Multiplier on A Special Case
For a special case, we will derive the Lagrange multipliers equation. Suppose we are working with $C^1$ functions $f,h$. Our problem is

\begin{align*}
\text{minimize } &f(x,y,z) \\
\text{subject to } &g(x,y,z) = z-h(x,y) = 0.
\end{align*}

That is, we are minimizing $f(x,y,z)$ on the graph $\Gamma_h$ of $h$. The Lagrange equation tells us that

$$\nabla f(x,y,z) + \lambda g(x,y,z) = \begin{pmatrix}
\frac{\partial  f}{\partial  x}(x,y,z) \\ \frac{\partial  f}{\partial  y}(x,y,z) \\ \frac{\partial  f}{\partial  z}(x,y,z)
\end{pmatrix} + \lambda \begin{pmatrix}
-\frac{\partial  h}{\partial  x}(x,y,z) \\ -\frac{\partial  y}{\partial  x}(x,y,z) \\ 1
\end{pmatrix} = \begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}$$

We will derive the above formula by expressing it as an unconstrained minimization problem

$$\text{minimize }_{(x,y) \in \mathbb R^2} F(x,y)$$

for some function $F$. We will then find the first order necessary conditions for an unconstrained minimization, and then express it as the equation we would like to prove.

Define $F(x,y) = f(x,y,f(x,y))$. The constrained minimization problem is therefore equivalent to the unconstrained problem. By our theory of unconstrained minimization, $\nabla F(x_0,y_0)=(0,0)$. That is,

$$\nabla F(x_0,y_0) = \begin{pmatrix}
\frac{\partial  f}{\partial  x} + \frac{\partial  f}{\partial  z}\frac{\partial  h}{\partial  x} \\
\frac{\partial  f}{\partial  y} + \frac{\partial  f}{\partial  z}\frac{\partial  h}{\partial  y}
\end{pmatrix} = \begin{pmatrix}
0\\0
\end{pmatrix}$$

Rather,

\begin{align*}
\frac{\partial  f}{\partial  x} + \frac{\partial  f}{\partial  z}\frac{\partial  h}{\partial  x} &= 0 \\
\frac{\partial  f}{\partial  y} + \frac{\partial  f}{\partial  z}\frac{\partial  h}{\partial  y} &= 0
\end{align*}

Let $\lambda = -\frac{\partial  f}{\partial  z}$. The equation becomes

\begin{align*}
\frac{\partial  f}{\partial  x} - \lambda \frac{\partial  h}{\partial  x} &= 0 \\
\frac{\partial  f}{\partial  y} - \lambda \frac{\partial  h}{\partial  y} &= 0 \\
\frac{\partial  f}{\partial  z} + \lambda &= 0
\end{align*}

which is what we wanted.
