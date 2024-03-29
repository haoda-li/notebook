# Inequality Constrained Finite Dimension Optimization

## Problem Definition
Our problem is of the form

\begin{align*}
\text{minimize } &f(x) \\
\text{subject to } &h_1(x) = \cdots = h_k(x) = 0 \\
&g_1(x), \dots, g_l(x) \leq 0.
\end{align*}


### _Defn_. Active Constraint
Let $x_0$ satisfy the above constraints. We call the inequality constraint $g_i(x) \leq 0$ active at $x_0$ if $g_i(x_0) = 0$. Otherwise, it is inactive at $x_0$.

### _Defn_. Regular point
Suppose there is an index $l' \leq l$ such that $g_1(x_0) =, \dots, g_{l'}(x_0) = 0$ are active, and $g_{l'+1}(x_0) \leq 0, \dots, g_l(x_0) \leq 0$ are inactive. We say that $x_0$ is a regular point of these constraints if the vectors $\nabla h_1(x_0), \dots, \nabla h_k(x_0), \nabla g_1(x_0), \dots, \nabla g_{l'}(x_0)$ are linearly independent.

## _Thrm_. First Order Necessary Conditions (Kuhn-Tucker Conditions)
__Claim__. Let $\Omega \subseteq \mathbb R^n$ be open and consider $C^1$ functions $f, h_1, \dots, h_k, g_1, \dots, g_l$ on $\Omega$. Suppose $x_0$ is a local minimizer of $f$ subject to the constraints, and that $x_0$ is regular as defined above. Then 
1. There exist $\lambda_1, \dots, \lambda_k \in \mathbb R$ and $\mu_1, \dots, \mu_l \in \mathbb R^{\geq 0}$ such that 
$\nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) + \sum \mu_j \nabla g_j(x_0) = 0$
2. (Complementary slackness conditions) For all $j$, $\mu_j g_j(x_0) = 0$, or equivalently, $\sum \mu_j g_j(x_0) = 0$.


Suppose the active constraints at $x_0$ are the first $l'$ constraints. Since each $\mu_j \geq 0$, condition (ii) is equivalent to saying that if $j \geq l'+1$, then $\mu_j = 0$. 

_proof_. If $x_0$ is a local minimizer of $f$ subject to the constraints, then it is certainly a local minimizer of $f$ subject to only the active constraints. That is, $x_0$ is also a local minimizer of $f$ subject to the equality constraints

$$h_1(x) = \cdots = h_k(x) = g_1(x) = \cdots = g_{l'} = 0$$

We know how to work with this! Let $M$ be the surface defined by these equality constraints. By the Lagrange multipliers theorem, 

$$\nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) + \sum \mu_j \nabla g_j(x_0) = 0$$

for some $\lambda_i \in \mathbb R, \mu_j \in \mathbb R$. (Note that we have not yet shown that the $\mu_j$'s are non-negative.)

Note that $g_1(x_0) = \cdots = g_{l'}(x_0) = 0$. Therefore $\mu_{l'+1} = \cdots = \mu_l = 0$, so it follows that

$$\mu_1 g_1(x_0) = 0, \dots, \mu_{l'}g_{l'}(x_0) = 0$$

which implies that $\mu_j g_j(x_0) = 0$ for all $j$. We have proven condition (ii).

We must now verify the non-negativity of the $\mu_j$'s. Suppose for the sake of contradiction that some $\mu_j < 0$; WLOG assume $j=1$. Let
 
$$\tilde{M} = \{x \in \Omega : h_i(x) = 0, g_i(x) = 0, j \neq 1\}$$

Since $x_0$ is a regular point of $M$, $x_0$ is a regular point of $\tilde{M}$. Therefore

$$T_{x_0}\tilde{M} = \mathrm{span}(\{\nabla h_1(x_0), \dots, h_k(x_0), \nabla g_2(x_0), \dots,\nabla g_l(x_0)\})^\perp$$

The vector $\nabla g_1(x_0)$ does not lie in this span, so there is a $v \in T_{x_0}\tilde{M}$ such that $\nabla g_1(x_0) \cdot v < 0$. That is, $g_1$ is strictly decreasing in the direction of $v$, or in more precise language, $g_1(x_0 + sv) < g_1(x_0)$ for all sufficiently small $s$, as we have
 
$$\left. \frac{d}{ds} \right|_{s=0} g_1(x_0 + sv) = \nabla g_1(x_0) \cdot v < 0$$

Therefore $v$ is a feasible direction for $g_1(x) \leq 0$ at $x_0$, and also, $v$ is tangential to the other constraints. Since $x_0$ is a regular point of $\tilde{M}$, we may find a curve $x(s)$ on $\tilde{M}$ such that $x(0) = x_0$ and $x'(0) = v$. Also, $s = 0$ is a local minimizer of $f \circ x$, so
 
$$\left. \frac{d}{ds}\right|_{s=0} f(x(s)) = \nabla f(x_0) \cdot v \geq 0$$

On the other hand, 

$$\nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) + \mu_1 \nabla g_1(x_0)+\sum_{j=2}^{l'} \mu_j \nabla g_j(x_0) = 0$$

Taking the dot product of the above equation by $v$ kills the two sums above and gives

$$\nabla f(x_0)\cdot v  + \mu_1 \nabla g_1(x_0)\cdot v = 0$$

implying $\nabla f(x_0)\cdot v < 0$, a contradiction. So every $\mu_j \geq 0$.

## _Thrm_. Second Order Necessary Conditions
__Claim__. Suppose $f, h_1, \dots, h_k, g_1, \dots, g_k \in C^2(\Omega)$, where $\Omega \subseteq \mathbb R^n$. Suppose $x_0$ is a regular point of the constraints. If $x_0$ is a local minimizer of $f$ subject to the constraints, then
1. There are $\lambda_1, \dots, \lambda_k \in \mathbb R$ and $\mu_1, \dots, \mu_l \geq 0$ such that $\nabla f(x_0) + \sum_i \lambda_i \nabla h_i(x_0) + \sum_j \mu_j \nabla g_j(x_0) = 0$
and $\mu_j g_j(x_0) = 0$ for each $j$.

2. The matrix $L(x_0) = \nabla^2 f(x_0) + \sum_i \lambda_i \nabla^2 h_i(x_0) + \sum_j \mu_j \nabla^2 g_j(x_0)$
is positive semi-definite on the tangent space $T_{x_0}\tilde{M}$ to the active constraints at $x_0$. (Explicitly, $L(x_0)$ is positive semi-definite on the space $T_{x_0}\tilde{M} = \{v \in \mathbb R^n : \nabla h_i(x_0) \cdot v = 0. \forall i, \nabla g_j(x_0) \cdot v = 0 \text{ where }1 \leq j \leq l\}$
where the active $g$ constraints are indexed precisely by $1, \dots, l'$

_proof_. $x_0$ is a local minimizer of $f$ subject to the constraints, so it is also a local minimizer of $f$ subject to only the active constraints. Since the Lagrange multiplies of the inactive constraints are zero, our theory of equality-constrained minimization finishes the problem.

### Example 1
Consider, for example, the problem

\begin{align*}
\text{minimize } &f(x,y) := -x \\
\text{subject to } &g_1(x,y) := x^2+y^2 \leq 1 \\
&g_2(x,y) := y+x-1 \leq 0
\end{align*}

The feasible set is the closed unit ball $\overline{B_1(0)}$ with an open semicircle removed from the top right. Geometrically, it is clear that the minimizer should be the point $(1,0)$. It is not hard to check that every feasible point is regular. Let's check that $(x_0, y_0) = (1,0)$ satisfies the first order conditions. We look at

$$\nabla f (x_0, y_0) + \mu_1 \nabla g_1 (x_0, y_0) + \mu_2 \nabla g_2 (x_0, y_0) = (0,0)$$

This becomes

$$\begin{pmatrix}
-1 \\ 0
\end{pmatrix} + \mu_1 \begin{pmatrix}
2 \\ 0
\end{pmatrix} + \mu_2 \begin{pmatrix}
1 \\ 1
\end{pmatrix} = \begin{pmatrix}
0 \\ 0
\end{pmatrix}$$

or

\begin{align*}
2\mu_1 + \mu_2 &= 1 \\
\mu_2 &= 0.
\end{align*}

So $\mu_1 = 1/2$. Also, $g_1(1,0) = 1^2 + 0^2 - 1 = 0$ and $g_(1,0) = 0$ as well, so the complementary slackness conditions are satisfied. Therefore $(1,0)$ satisfies the Kuhn-Tucker conditions, and so it is a candidate local minimizer. What about the second order conditions?

$$L(1,0) = \nabla^2 f (x_0, y_0) + \mu_1 \nabla^2 g_1 (x_0, y_0) + \mu_2 \nabla^2 g_2 (x_0, y_0) \lor L(1,0) = I$$

Clearly the second order necessary conditions are satisfied, but let's check the tangent space anyway. We have $\nabla g_1(1,0) = (2, 0)$ and $\nabla g_2(1,0) = (1,1)$; they are linearly independent, so the tangent space is a point. Therefore the second order necessary conditions are satisfied.


## _Thrm_. Second Order Sufficient Conditions

__Claim__. Suppose $\Omega \subseteq \mathbb R^n$ is open and $f, h_1, \dots, h_k, g_1, \dots, g_l \in C^2(\Omega)$. Consider the minimization problem

\begin{align*}
\text{minimize } &f(x) \\
\text{subject to } &h_1(x) = \cdots = h_k(x) = 0 \\
&g_1(x) \leq 0, \dots, g_l(x) \leq 0
\end{align*}

Suppose $x_0$ is a feasible point of the constraints. If the following three conditions are satisfied:
1. There exist $\lambda_1, \dots, \lambda_k \in \mathbb R$ and $\mu_1, \dots, \mu_l \geq 0$ such that
$\nabla f(x_0) + \sum_i \lambda_i \nabla h_i(x_0) + \sum_j \mu_j \nabla g_j(x_0) = 0$

2. $\mu_j g_j(x_0) = 0$ for each $j$.

3. The matrix $L(x_0) = \nabla^2 f(x_0) + \sum_i \lambda_i \nabla^2 h_i(x_0) + \sum_j \mu_j \nabla^2 g_j(x_0)$ is positive definite on the tangent space to the "strongly active constraints" at $x_0$. That is, it is positive definite on the space $\tilde{\tilde{T_{x_0}}} = \{ v \in \mathbb R^n : \nabla h_i(x_0) = 0 \forall i\land \forall k, 1 \leq k \leq l''\Rightarrow \nabla g_j(x_0) = 0\}$
where $\{1, \dots, l''\}$ is the set of all indices of active constraints whose Lagrange multipliers are positive.
\end{enumerate}
then $x_0$ is a strict local minimizer of $f$.

_proof_. 
Suppose $x_0$ is not a strict local minimizer of $f$. We claim that there then exists a unit vector $v \in \mathbb R^n$ such that
 1. $\nabla f(x_0) \cdot v \leq 0$.
 2. $\nabla h_i(x_0) \cdot v = 0$ for each $i = 1, \dots, k$.
 3. $\nabla g_j(x_0) \cdot v \leq 0$ for all the active constraints (hereafter labelled by $j = 1,\dots, l'$)

Since $x_0$ is not a strict local minimizer, there exists a sequence $x_k$ of feasible points unequal to $x_0$ converging to $x_0$ such that $f(x_k) \leq f(x_0)$. Then $f(x_k) - f(x_0) \leq 0$ for each $k$. Let $v_k = \frac{x_k-x_0}{\|x_k-x_0\|}$, and let $s_k = \|x_k - x_0\|$. Then $x_k = x_0 + s_kv_k$, with which we may rewrite the inequality as $f(s_kv_k + x_0) - f(x_0) \leq 0$. Since each $v_k \in S^1$, we may assume that the sequence $v_k$ is convergent and that it converges to some $v \in S^1$. We claim that this vector $v$ has the three desired properties.

By Taylor's theorem we have

\begin{align*}
0 \geq f(s_kv_k + x_0) - f(x_0) &= s_k \nabla f(x_0) \cdot v_k + o(s_k) \tag{A}\\
0 = h_i(s_kv_k + x_0) - h_i(x_0) &= s_k \nabla h_i(x_0) \cdot v_k + o(s_k) \tag{B} \\
0 \geq g_k(s_kv_k+x_0) - g_j(x_0) &= s_k \nabla g_j(x_0) \cdot v_k + o(s_k) \tag{C}
\end{align*}

(The last equation is $\leq 0$ because $g_j(x_0) = 0$.) Divide everything by $s_k$ and take the limit as $k \to \infty$. Then

\begin{align*}
0 &\geq \nabla f(x_0) \cdot v \tag{a}\\
0 &= \nabla h_i(x_0) \cdot v \tag{b}\\
0 &\geq \nabla g_j(x_0) \cdot v \tag{c},
\end{align*}

which proves the earlier claim.

We now claim that equality actually holds in (c). Suppose for the sake of contradiction that there is some $1 \leq k \leq l'$ such that $\nabla g_j(x_0) \cdot v < 0$ for some $j$ for which $g_j$ is strongly active at $x_0$. By the first condition of the theorem,

$$0 \geq \underbrace{\nabla f(x_0) \cdot v}_{\text{$\geq 0$ by (a)}} = -\underbrace{\sum \lambda_i \nabla h_i(x_0)\cdot v}_{\text{$=0$ by (b)}} \underbrace{- \sum \mu_j \nabla g_j(x_0)\cdot v}_{\text{$\geq 0$ by (c)}}$$

and so the right hand side is strictly greater than zero, because we only considered strongly active constraints. This is a contradiction, so we conclude that $\nabla g_j(x_0) = 0$ for all $j$ such that $g_j$ is strongly active at $x_0$. Therefore $v \in \tilde{\tilde{T_{x_0}}}$.

Again, by Taylor's theorem

\begin{align*}
0 \geq f(s_kv_k + x_0) - f(x_0) &= s_k \nabla f(x_0) \cdot v_k + \frac{1}{2}s_k^2 v_k^T \nabla^2 f(x_k) \cdot v_k + o(s_k^2) \\
0 = h_i(s_kv_k + x_0) - h_i(x_0) &= s_k \nabla h_i(x_0) \cdot v_k + \frac{1}{2}s_k^2 v_k^T \nabla^2 h_i(x_k) \cdot v_k + o(s_k^2) \\
0 \geq g_k(s_kv_k+x_0) - g_j(x_0) &= s_k \nabla g_j(x_0) \cdot v_k + \frac{1}{2}s_k^2 v_k^T \nabla^2 g_j(x_k) \cdot v_k + o(s_k^2) 
\end{align*}

Multiply the second line by $\lambda_i$ and the third by $\mu_j$ and add everything up to get

$$0 \geq s_k \underbrace{\left[ \nabla f(x_0) + \sum \lambda_i \nabla h_i(x_0) + \sum \mu_j \nabla g_j(x_0) \right]}_{\text{$=0$ by condition 1}} v_k + \frac{s_k^2}{2} v_k^T \underbrace{\left[ \nabla^2 f(x_0) + \sum \lambda_i \nabla^2 h_i(x_0) + \sum \mu_j \nabla^2 g_j(x_0) \right]}_{= L(x_0)}v_k + o(s_k^2)$$

Divide everything by $s_k^2$ to get

$$0 \geq \frac{1}{2} v_k^T \left[ \nabla^2 f(x_0) + \sum \lambda_i \nabla^2 h_i(x_0) + \sum \mu_j \nabla^2 g_j(x_0) \right] \cdot v_k + \frac{o(s_k^2)}{s_k^2}$$

Taking the limit $k \to \infty$ gives

$$0 \leq v^T L(x_0) \cdot v$$

which violates condition 3 of the theorem. We have a contradiction, so we conclude that $x_0$ must be a strict local minimizer.

### Example 1
Given $(a,b)$ with $a,b > 0$ and $a^2+b^2 > 1$. Consider the minimization problem:

\begin{align*}
\text{minimize } &f(x,y) := (x-a)^2 + (y-b)^2 \\
\text{subject to } &g_1(x,y) := x^2+y^2-1 \leq 0
\end{align*}

Our intuition says that the minimizer should be $\left( \frac{a}{\sqrt{a^2+b^2}}, \frac{b}{\sqrt{a^2+b^2}} \right)$. We have $\nabla g(x,y) = (2x, 2y)$, so clearly all feasible points are regular. The Kuhn-Tucker conditions are

$$\begin{pmatrix}
2(x-a) \\ 2(y-a)
\end{pmatrix} + \mu \begin{pmatrix}
2x \\ 2y
\end{pmatrix} = \begin{pmatrix}
0 \\ 0
\end{pmatrix}$$

and $\mu g(x,y) = 0$. That is,

\begin{align*}
(1+\mu)x &= a \\
(1+\mu)y &= b \\
\mu (x^2+y^2 - 1) &= 0, \mu \geq 0
\end{align*}

Suppose $\mu = 0$. Then $x = a$ and $y = b$; since we assumed $a^2+b^2 > 1$, we would have that $(x,y)$ is not feasible. Therefore $\mu \neq 0$, and so $x^2+y^2 = 1$ by the third equation. Squaring the first two equations and adding them gives

$$(1+\mu)^2 (x^2+y^2) = a^2+b^2$$

implying that $\mu = -1 + \sqrt{a^2+b^2}$ - we took the positive root because $\mu > 0$. This is actually positive, since $a^2+b^2 > 1$. Those first equations again give us

$$\begin{pmatrix}
x_0 \\ y_0
\end{pmatrix} = \frac{1}{1+\mu} \begin{pmatrix}
a \\ b
\end{pmatrix} = \frac{1}{\sqrt{a^2+b^2}} \begin{pmatrix}
a \\ b
\end{pmatrix}$$

as expected. The Lagrangian is

$$L(x_0, y_0) = 2I + 2\mu I = 2(1+\mu)I = 2\sqrt{a^2+b^2} I$$

which is everywhere positive definite. Therefore the second-order sufficient conditions are satisfied. For practice, however, let's compute the tangent space to the "strongly active constraints". The only constraint is $g$; since $g$ is active and its Lagrange multiplier $\mu$ is positive, the constraint $g$ is strongly active at $(x_0, y_0)$. Therefore the tangent space we are interested in is the tangent space to $S^1$ at $(x_0, y_0)$: that space is $\{v \in \mathbb R^2 : av_1 + bv_2 = 0\}$.


### Example 2

Consider the problem

\begin{align*}
\text{minimize } &f(x,y) := x^3 + y^2 \\
\text{subject to } &g(x,y) := (x+1)^2 + y^2 - 1 \leq 0.
\end{align*}

We have $\nabla g(x,y) = (2(x+1), 2y)$, which makes it clear that every feasible point is regular. The Kuhn-Tucker conditions are

$$\begin{pmatrix}
3x^2 \\ 2y
\end{pmatrix} + \mu \begin{pmatrix}
2(x+1) \\ 2y
\end{pmatrix} = \begin{pmatrix}
0 \\ 0
\end{pmatrix}$$

with $\mu((x+1)^2 + y^2 - 1) = 0$ and $\mu \geq 0$.

Consider $(x_0, y_0) = (0,0)$. The Kuhn-Tucker conditions imply $\mu = 0$. In particular, $g$ is active at $(0,0)$, but not strongly active there. The tangent space to the active constraint at $(0,0)$ is the y-axis. The Lagrangian at $(0,0)$ is

$$L(0,0) = \begin{pmatrix}
0 & 0 \\ 0 & 2
\end{pmatrix}$$

which is clearly positive definite on this tangent space. However, we cannot conclude anything, since the constraint $g$ is not strongly active. In fact, it is clear that $(0,0)$ is not a local minimizer: for $x<0$ sufficiently close to $0$, $f(x,0)$ is negative, yet it is $0$ at $(0,0)$.

