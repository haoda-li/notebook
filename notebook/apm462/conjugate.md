# Conjugate Directions and Conjugate Gradients

## Method of Conjugate Directions

### _Defn_. Q-Conjugate
Let $Q$ be symmetric. We say that $d,d'$ are $Q$-conjugate or $Q$-orthogonal if $d^TQd' = 0$. A finite set $d_0, \dots, d_k$ of vectors is called $Q$-orthogonal if $d_i^TQd_j = 0$ for all $i \geq j$.

For example, if $Q = I$, then $Q$-orthogonality is equivalent to regular orthogonality. For another example, if $Q$ has more than one distinct eigenvalue, let $d$ and $d'$ be eigenvectors corresponding to distinct eigenvalues. Then $d^TQd' = \lambda' d^Td' = 0$, since the distinct eigenspaces of a symmetric matrix are orthogonal subspaces.

Recall that any symmetric matrix $Q$ may the orthogonally diagonalized; there exists an orthonormal basis $d_0, \dots, d_{n-1}$ of eigenvectors of $Q$. These eigenvectors are also $Q$-orthogonal. Hence to any symmetric matrix is a basis of orthonormal vectors that are also orthogonal with respect to the matrix, as just defined.

### Examples of Q-conjugate set

__Claim__. If $Q$ is symmetric and positive definite, then any set of non-zero $Q$-orthogonal vectors $\{d_i\}$ is linearly independent.

_proof_. If $\sum \alpha_i d_i = 0$, then left-multiplying by $d_j^TQ$ gives $\alpha_j d_j^T Q d_j = 0$. Positive definiteness implies $\alpha_j = 0$. 

Let $Q$ be an $n \times n$ symmetric positive definite matrix. Recall that $f(x) = \frac{1}{2}x^TQx - b^Tx$ has the unique global minimizer $x_* = Q^{-1}b$. Let $d_0, \dots, d_{n-1}$ be non-zero $Q$-orthogonal vectors. Then $d_0, \dots, d_{n-1}$ form a basis of $\mathbb R^n$. Thus there are scalars $\alpha_0, \dots, \alpha_{n-1}$ such that $x_* = \sum \alpha_i d_i$. We would like a formula for the $\alpha_i$'s.

Multiplying both sides of the sum $x_* = \sum \alpha_i d_i$ by $d_j^TQ$ implies that $d_j^TQx_* = \alpha_j d_j^TQd_j$, implying that

$$\alpha_j = \frac{d_j^T b}{d_j^TQd_j}$$

Therefore

$$x_* = \sum_{i=1}^{n-1} \frac{d_i^Tb}{d_i^TQd_i}  d_i$$

This implies that we can actually solve for $x_*$ by computing the $d_0, \dots, d_{n-1}$ and the coefficients above. Computationally, computing inner products is very easy. The disadvantage is that we do not know how to find the vectors $d_0, \dots, d_{n-1}$.


### _Thrm_. Conjugate Directions

__Claim__. Let $d_0, \dots, d_{n-1}$ be a set of non-zero $Q$-orthogonal vectors.  
For a starting point $x_0 \in \mathbb R^n$, consider the sequence $\{x_l\}$ defined by 

$$x_{k+1} = x_k + \alpha_k d_k$$

where 

$$\alpha_k = -\frac{g_k^Td_k}{d_k^TQd_k}, g_k = Qx_k - b$$

The sequence $\{x_k\}$ converges to the minimizer $x_*$ it at most $n$ steps; $x_n = x_*$.

_proof_. Write $x_* - x_0 = \alpha_0' d_0 + \cdots + \alpha_{n-1}'d_{n-1}$. Multiply both sides by $d_i^TQ$ to get

$$d_i^TQ(x_* - x_0) = \alpha_i d_i^TQd_i$$

giving us the expression

$$\alpha_i' = \frac{d_i^TQ(x_*-x_0)}{d_i^TQd_i}\:(*)$$

Note that

\begin{align*}
x_1 &= x_0 + \alpha_0 d_0 \\
x_2 &= x_0 + \alpha_0 d_0 + \alpha_1 d_1 \\
&\vdots \\
x_k &= x_0 + \alpha_0 d_0 + \cdots + \alpha_{k-1}d_{k-1},
\end{align*}

implying that

$$x_k - x_0 = \alpha_0 d_0 + \cdots + \alpha_{k-1}d_{k-1}$$

Multiplying both sides by $d_k^TQ$ gives $d_k^TQ(x_k-x_0) = 0$. By (*) we have

$$\alpha_k' = \frac{d_k^T Q(x_* - x_0) - d_k^TQ(x_k - x_0)}{d_k^TQd_k} = \frac{d_k^TQ(x_* - x_k)}{d_k^TQd_k} = -\frac{(Qx_k - Qx_*)^T d_k}{d_k^TQd_k}$$

simplifying to

$$\alpha_k' = -\frac{g_k^T d_k}{d_k^TQd_k} = \alpha_k$$

$$\implies x_* = x_0 + \alpha_0 d_0 + \cdots + \alpha_{n-1}d_{n-1} = x_n$$

So after $n$ steps, we reach the minimizer.

### _Thrm_. Geometric Interpretation
Let $d_0, \dots, d_{n-1}$ be a set of non-zero $Q$-orthogonal vectors in $\mathbb R^n$, where $Q$ is symmetric and positive definite. Note that these vectors are linearly independent by a result from last lecture. Let $B_k$ denote the subspace spanned by the first $k$ vectors. We have an increasing sequence

$$B_0 \subsetneq B_1 \subsetneq \cdots \subsetneq B_n$$

and $\dim(B_k) = k$.

__Lemma__. Let $f$ be a $C^1$ convex function defined on a convex domain $\Omega \subseteq \mathbb R^n$. Suppose there is an $x_* \in \Omega$ such that $\nabla f(x_*) \cdot (y - x_*) \geq 0$ for all $y \in \Omega$. Then $x_*$ is a global minimizer of $f$ on $\Omega$. The converse is obviously true.

_Geometrically, this means that if we move in any feasible direction from the point $x_*$, the function is increasing. Hence $x_*$ is a local minimizer; convexity implies it is global. With this result in mind, we prove the theorem._

_proof_. The affine subspace $\Omega = x_0 + B_k$ is convex. \textbf{(This proof could not be finished as attention had to be diverted from the lecture.)}

__Corollary__. $x_n$ minimizes $f(x)$ on $\mathbb R^n$. That is, $x_n = x_*$; the method of conjugate directions for this function $f$ terminates in at most $n$ steps. 

__Claim__. The sequence $\{x_k\}_{k=0}^\infty$ generated from $x_0$ by the method of conjugate directions has the property that $x_k$ minimizes $f(x) = \frac{1}{2}x^TQx - b^Tx$ on the affine subspace $x_0 + B_k$.

When $Q = I$, then $q(x)$ is half the distance squared from $x$ to $x_*$. What if $Q \neq I$. $q$ is still a metric on $\mathbb R^n$. Thus $x_k$ is the point "closest" to $x_*$ on the affine subspace $x_0 + B_k$.

## Conjugate Gradients

Start at $x_0 \in \mathbb R^n$. Choose $d_0 = -g_0 = -\nabla f(x_0) = b - Qx_0$. Recursively define $d_{k+1} = -g_{k+1} + \beta_k d_k$, where $g_{k+1} = Qx_{k+1} - b$ and

$$\beta_k = \frac{g_{k+1}^T Q d_k}{d_k^TQd_k}$$

and

$$x_{k+1} = x_k + \alpha_k d_k$$

where

$$\alpha_k = -\frac{g_k^T d_k}{d_k^T Q d_k}$$

Given an initial point $x_0$, take $d_0 = -g_0 = b - Qx_0$. By definition, $x_1 = x_0 + \alpha_0 d_0$; we need to find $\alpha_0$. This is

$$\alpha_0 = -\frac{g_0^Td_0}{g_0^TQg_0}$$

Then $x_2 = x_1 + \alpha_1 d_1$. By definition, $\alpha_1 = -\frac{g_1^T d_1}{d_1^TQd_1}$, where $d_1 = -g_1 + \beta_0 d_0$, where $\beta_0 = \frac{g_1^TQd_0}{d_0^TQd_0}$.

Some remarks:

- Like the other conjugate direction methods, this method converges to the minimizer $x_*$ in $n$ steps.
- We have a procedure to find the direction vectors $d_k$.
- This method makes good uniform progress towards the solution at every step.

### _Thrm_. Bound on Convergence
__Claim__. consider $q(x) = \frac{1}{2}(x-x_*)^TQ(x-x_*) = f(x) + \text{const}$. It's better to look at $q$ rather than $f$, since $q$ behaves like a distance function relative to $x_*$.

$$q(x_{k+1}) \leq \left( \max_{\substack{\lambda \\ \text{eigval of Q}}} (1 + \lambda P_k(\lambda))^2 \right) q(x_k)$$

where $P_k$ is any polynomial of degree $k$.

For example, suppose $Q$ has $m \leq n$ distinct eigenvalues. Choose a polynomial $P_{m-1}$ such that $1 + \lambda P_{m-1}(\lambda)$ has its $m$ zeroes at the $m$ eigenvalues of $Q$. With such a polynomial, we would get $q(x_m) \leq 0$, implying that $q(x_m) = 0$; the conjugate gradient method terminates at the $m$th step, i.e. $x_m=x_*$.
