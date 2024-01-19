# Newton's Method and Steepest Descent

## Newton's Method

Consider a twice-differentiable function $f : I \to \mathbb R$ defined on an interval $I \subseteq \mathbb R$. We would like to find the minima of $f$. We shall do so by considering quadratic approximations of $f$. 

Let us start at a point $x_0 \in I$. Consider 

$$q(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2}f''(x_0)(x-x_0)^2$$

the (best) quadratic approximation to $f$ at $x_0$. Note that $q(x_0) = f(x_0)$, $q'(x_0) = f'(x_0)$ and $q''(x_0) = f''(x_0)$. We will now find the local minimizer $x_1$ for the quadratic $q$. That is, we would like to find $x_1$ such that

$$0 = q'(x_1) = f'(x_0) + f''(x_0)(x_1-x_0)$$

implying that, so long as $f''(x_0) \neq 0$, 

$$x_1 = x_0 - \frac{f'(x_0)}{f''(x_0)}$$

The idea of Newton's method is to iterate this procedure. (Consider the Newton's method for finding roots of functions; this is the same as finding the root of the derivative of the function.)


### Newton's Method in 1-Dim

Precisely, we pick a starting point $x_0 \in I$. Then we recursively define

$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$$

We hope that the sequence $x_n$ converges to a minimizer of $f$. For the sake of the rest of the lecture, let $g = f'$. With this notation we may write Newton's method as

\begin{align*}
x_0 &\in I \\
x_{n+1} &= x_n - \frac{g(x_n)}{g'(x_n)}.
\end{align*}


#### _Thrm_. Convergence of Newton's Method in 1-Dim
__Claim__. Let $g \in C^2(I)$ (i.e. $f \in C^3(I)$). Suppose there is an $x_* \in I$ satisfies $g(x_*) = 0$ and $g'(x_*) \neq 0$. If $x_0$ is sufficiently close to $x_*$, then the sequence $x_n$ generated by Newton's method converges to $x_*$.

_proof_. Since $g'(x_0) \neq 0$, there is, by continuity of $g'$, an $\alpha > 0$ such that  $|g'(x_1)| > \alpha$ for all $x_1$ in a neighbourhood of $x_0$ and $|g''(x_2)| < \frac{1}{\alpha}$ for all $x_2$ in the neighbourhood of $x_0$.  
The proof of the first claim is a simple continuity argument. The proof of the second claim follows from continuity of $g''$ and the extreme value theorem applied to this neighbourhood('s closure). (That is, we can choose an $\alpha$ to bound $|g'|$ from below, and then shrink it possibly to ensure $1/\alpha$ bounds $|g''|$ from above.)

Since $g(x_*) = 0$, the formula of Newton's method now implies

$$(*)\:x_{n+1} - x_* = x_n - x_* - \frac{g(x_n) - g(x_*)}{g'(x_n)} = -\frac{g(x_n) - g(x_*) - g'(x_n)(x_n-x_*)}{g'(x_n)}$$

By the second order mean value theorem, there exists a $\xi$ sufficiently close to $x_*$ such that

$$g(x_*) = g(x_n) + g'(x_n)(x_* - x_n) + \frac{1}{2}g''(\xi)(x_* - x_n)^2$$

Then $(*)$ becomes

$$x_{n+1} - x_* = \frac{1}{2}\frac{g''(\xi)}{g'(x_n)}(x_n - x_*)^2.$$

The bounds on $g'$ and $g''$ we found at the start of the proof imply that

$$(**)\: |x_{n+1} - x_*| < \frac{1}{2\alpha^2} |x_n - x_*|^2$$

Let $\rho$ be the constant $\rho = \frac{1}{\alpha^2}|x_0 - x_*|$. Choose $x_0$ close enough to $x_*$ so that $\rho < 1$. Then $(**)$ implies

$$|x_1 - x_*| < \frac{1}{2\alpha^2}|x_0 - x_*||x_0 - x_*| = \rho |x_0 - x_*| < |x_0 - x_*|$$

Similarly, $(**)$ gives

$$|x_2 - x_*| < \frac{1}{2\alpha^2}|x_1 - x_*|^2 < \frac{1}{2\alpha^2}\rho^2 |x_0-x_*|^2 < \rho^2 |x_0 - x_*|$$

Continuing in the same way we obtain

$$|x_n - x_*| < \rho^n |x_0 - x_*|$$

implying that Newton's method converges in our neighbourhood.

### Newton's Method in Higher Dimensions
Consider a function $f : \Omega \to \mathbb R$ defined on an open set $\Omega \subseteq \mathbb R^n$. We choose a starting point $x_0 \in \Omega$, and recursively define

$$x_{n+1} = x_n - \nabla^2 f(x_n)^{-1} \nabla f(x_n)$$

For a general $f$, the algorithm requires that $\nabla^2 f(x_n)$ is invertible. The algorithm stops if $\nabla f(x_n) = 0$ at some point (that is, the sequence given by Newton's method becomes constant if $\nabla f(x_n) = 0$ for some $x_n$.) Our main result is

#### _Thrm_. Convergence of Newton's Method in N-Dim 
Suppose $f \in C^3(\Omega)$. Suppose also that there is an $x_* \in \Omega$ such that $\nabla f(x_*) = 0$ and $\nabla^2 f(x_*)$ is invertible. Then the sequence $x_n$ defined by

$$x_{n+1} = x_n - \nabla^2 f(x_n)^{-1} \nabla f(x_n)$$

converges for all $x_0$ sufficiently close to $x_*$.

The goal of Newton's method was to find a minimizer of $f$, but it is possible for it to fail, for it only searches for __critical points__, not necessarily extrema.


### Things May Go Wrong

It is possible for Newton's method to fail to converge even when $f$ has a unique global minimizer $x_*$ and the initial point $x_0$ can be taken arbitrarily close to $x_*$. Consider

$$f(x) = \frac{2}{3}|x|^{3/2} = \begin{cases} 
\frac{2}{3}x^{3/2} & x \geq 0 \\
\frac{2}{3}(-x)^{3/2} & x \leq 0
\end{cases}$$

This function is differentiable, and its derivative is
$f'(x) = \begin{cases} 
x^{1/2} & x \geq 0 \\
-(-x)^{1/2} & x \leq 0
\end{cases}$
and its second derivative is
$f''(x) = \begin{cases} 
\frac{1}{2}x^{-1/2} & x > 0 \\
\frac{1}{2}(-x)^{-1/2} & x < 0 \\
\text{N/A} & x = 0
\end{cases}$
so $f \not\in C^3$ (it is not even $C^2$). Let $x_0 = \epsilon$. Then

$$x_1 = \epsilon - \frac{f'(\epsilon)}{f''(\epsilon)} = \epsilon - \frac{\epsilon^{1/2}}{\frac{1}{2}\epsilon^{-1/2}} = \epsilon - 2\epsilon = -\epsilon$$


$$x_2 = -\epsilon - \frac{f'(-\epsilon)}{f''(-\epsilon)} = -\epsilon - \frac{-\epsilon^{1/2}}{\frac{1}{2}\epsilon^{-1/2}} = -\epsilon + 2\epsilon = \epsilon$$

So Newton's method gives an alternating sequence $\epsilon, -\epsilon, \epsilon, -\epsilon, \dots$.  This definitely does not converge. This does not contradict the theorem of convergence because the function in question does not satisfy the conditions of the theorem.

Now we consider an example in which the function in question converges, just not to a minimizer. Consider $f(x) = x^3$, which has derivatives $f'(x) = 3x^2$ and $f''(x) = 6x$. Starting at $x_0$, we have

$$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} = x_n - \frac{3x_n^2}{6x_n} = x_n - \frac{1}{2}x_n = \frac{1}{2}x_n$$

So Newton's method definitely converges to the critical point $0$, no matter the choice of $x_0 \in \mathbb R$. However, the function $f$ in question does not have a global minimizer, so, while Newton's method converges, it does not converge to an extrema of any sorts.


## Steepest Descent
Consider a $C^1$ function $f : \Omega \to \mathbb R$ defined on an open set $\Omega \subseteq \mathbb R^n$. The idea is: at every point in the "landscape" of $f$ (the graph of $f$ in $\mathbb R^{n+1}$), make a step "downwards" in the steepest direction. (If you're on a mountain and want to descend to the bottom as fast as possible, how do you do so? You, at your current position, take a step down in the steepest direction, and repeat until you're done.) 

Since the gradient $\nabla f(x_0)$ represents the direction of greatest increase of $f$ at $x_0$, the vector $-\nabla f(x_0)$ represents the direction of steepest decrease at $x_0$. We would therefore like to move in the direction of the negative gradient. We will do so, with the condition that we move until we have a minimizer in the direction of the negative gradient (at which point we will stop moving and repeat).

### Algorithm

\begin{align*}
x_0 &\in \Omega \\
x_{k+1} &= x_k - \alpha_k \nabla f(x_k)
\end{align*}

where $\alpha_k \geq 0$ satisfies $f(x_k - \alpha_k \nabla f(x_k)) = \min_{\alpha \geq 0} f(x_k - \alpha \nabla f(x_k))$
We call $\alpha_k$ the __optimal step__, since it is chosen so that $x_{k+1}$ is the minimum of $f$ sufficiently close to $x_k$. We also call $x_{k+1}$ the __minimum point on the half-line__ $x_k - \alpha \nabla f(x_k), \alpha \geq 0$. We now describe some properties of the method of steepest descent.


### _Thrm_. Correctness of Steepest Descent
__Claim__. The steepest descent algorithm is actually descending; $f(x_{k+1}) < f(x_k)$ so long as $\nabla f(x_k) \neq 0$.

_proof_. We have $f(x_{k+1}) = f(x_k - \alpha_k \nabla f(x_k)) \leq f(x_k - s \nabla f(x_k))$ for all $s \in [0, \alpha_k]$.   Also,

$$\left. \frac{d}{ds} \right|_{s=0} f(x_k - s\nabla f(x_k)) = \nabla f(x_k) \cdot (-\nabla f(x_k)) = -\| \nabla f(x_k) \|^2 < 0$$

Then for sufficiently small $s \geq 0, f(x_k - s\nabla f(x_k)) < f(x_k)$

### _Thrm_. Direction of Gradient

__Claim__. The steepest descent algorithm moves in perpendicular steps; for all $k$, we have $(x_{k+2} - x_{k+1})\cdot(x_{k+1} - x_k) = 0$.

_proof_. We have 

$$(x_{k+2} - x_{k+1})\cdot(x_{k+1} - x_k) = \alpha_{k+1}\alpha_k \nabla f(x_{k+1}) \cdot \nabla f(x_k)$$

Recall that $\alpha_k \geq 0$. If $\alpha_k = 0$, then the whole expression is zero and we're done. Consider the possibility that $\alpha_k > 0$. Then

$$f(x_k - \alpha_k \nabla f(x_k)) = \min_{s > 0} f(x_k - s \nabla f(x_k))$$

implying that $\alpha_k$ is a minimizer of the function on the right in the above. Then

$$0 = \left. \frac{d}{ds} \right|_{s=\alpha_k} f(x_k - s\nabla f(x_k)) = \nabla f(x_k - \alpha_k \nabla f(x_k)) \cdot (-\nabla f(x_k)) = -\nabla f(x_{k+1}) \cdot \nabla f(x_k)$$

proving the claim.

### _Thrm_. Convergence of Steepest Descent
__Claim__. Suppose $f$ is a $C^1$ function on an open set $\Omega \subseteq \mathbb R^n$. Let $x_0 \in \Omega$, and let $\{x_k\}_{k=0}^\infty$ be the sequence generated by the method of steepest descent. If there is a compact $K \subseteq \Omega$ containing all $x_k$, then every convergent subsequence of $\{x_k\}_{k=0}^\infty$ in $K$ will converge to a critical point $x_*$ of $f$.

Choose a convergent subsequence $\{x_{k_i}\}$ converging to a point $x_* \in K$.  Note that $\{ f(x_{k_i}) \}$ decreases and converges to $f(x_*)$. Since $\{f(x_k)\}$ is a decreasing sequence, it also converges to $f(x_*)$.

Suppose for the sake of contradiction that $\nabla f(x_*) \neq 0$. Since $f$ is $C^1$, $\nabla f(x_{k_i})$ converges to $\nabla f(x_*)$. Define $y_{k_i} = x_{k_i} - \alpha_{k_i} \nabla f(x_{k_i})$ (i.e. $y_{k_i} = x_{k_1+1}$). We may therefore assume without loss of generality that $y_{k_i}$ converges to some $y_* \in K$. Since $\nabla f(x_*) \neq 0$, we may write

$$\alpha_{k_i} = \frac{|y_{k_i} - x_{k_i}|}{|\nabla f(x_{k_i})|}$$

Taking the limit as $i \to \infty$, we have

$$\alpha_* := \lim_{i \to \infty} \alpha_{k_i} = \frac{|y_* - x_*|}{|\nabla f(x_*)|}$$

Taking the same limit in the definition of $y_{k_i}$ we have

$$y_* = x_* - \alpha_* \nabla f(x_*)$$

Note that

$$f(y_{k_i}) = f(x_{k_i+1}) = \min_{\alpha \geq 0} f(x_{k_i} - \alpha \nabla f(x_{k_i}))$$

Thus $f(y_{k_i}) \leq f(x_{k_i} - \alpha \nabla f(x_{k_i}))$ for all $\alpha \geq 0$. For any fixed $\alpha \geq 0$, taking the limit $i \to \infty$ gives us

$$f(y_*) \leq f(x_* - \alpha \nabla f(x_*))$$


$$\implies f(y_*) \leq \min_{\alpha \geq 0} f(x_* - \alpha \nabla f(x_*)) < f(x_*)$$

since the function $f$ decreases in the direction of $-\nabla f(x_*) \neq 0$.

We can also argue the following: $f(x_{k_i+1}) \to f(x_*)$. But since $x_{k_i+1} = y_{k_i}$, we have $f(y_{k_i}) \to f(y_*)$, implying $f(x_*) = f(y_*)$, a contradiction.


### Steepest Descent in the Quadratic Case

Consider a function $f$ of the form $f(x) = \frac{1}{2}x^TQx - b^Tx$ for $b,x \in \mathbb R^n$ and $Q$ an $n \times n$ symmetric positive definite matrix. Let $\lambda = \lambda_1 \leq \cdots \leq \lambda_n = \Lambda$ be the eigenvalues of $Q$. (Note that they are all strictly positive.) Note that $\nabla^2 f(x) = Q$ for any $x$, so $f$ is strictly convex. There therefore exists a unique global minimizer $x_*$ of $f$ in $\mathbb R^n$ such that $Qx_* = b$. 

Let 

$$q(x) = \frac{1}{2}(x - x_*)^TQ(x-x_*) = f(x) + \frac{1}{2}x_*^TQx_*$$

So $q$ and $f$ differ by a constant. Therefore it suffices to find the minimizer of $q$, rather than $f$. Note that $q(x) \geq 0$ for all $x$, since $Q$ is positive definite. So we shall study the minimizer $x_*$ of $q$.

Note that $\nabla f(x) = \nabla q(x) = Qx - b$; let $g(x) = Qx - b$. The method of steepest descent may therefore be written as

$$x_{k+1} = x_k - \alpha_k g(x_k)$$

We would like a formula for the optimal step $\alpha_k$. Recall that $\alpha_k$ is defined to be the minimizer of the function $f(x_k - \alpha g(x_k))$ over $\alpha \geq 0$. Thus

$$0 = \left. \frac{d}{d\alpha} \right|_{\alpha = \alpha_k} f(x_k - \alpha g(x_k)) = \nabla f(x_k - \alpha_k g(x_k)) \cdot (-g(x_k))$$

This simplifies to

$$0 = (Q(x_k - \alpha_k g(x_k)) - b) \cdot (-g(x_k)) = -(\underbrace{Qx_k - b}_{=g(x_k)} - \alpha_k Q g(x_k)) \cdot g(x_k)$$

giving

$$0 = -|g(x_k)|^2 + \alpha_k g(x_k)^TQg(x_k)$$

Therefore

$$\alpha_k = \frac{|g(x_k)|^2}{g(x_k)^TQg(x_k)} \:(*)$$

#### Lemma 1
__Claim__. $q(x_{k+1}) = \left( 1 - \frac{|g(x_k)|^4}{(g(x_k)^T Q g(x_k))(g(x_k)^TQ^{-1}g(x_k))} \right)q(x_k)$

_proof_. 

\begin{align*}
q(x_{k+1}) &= q(x_k - \alpha_k g(x_k)) \\
&= \frac{1}{2}(x_k - \alpha_k g(x_k) - x_*)^T Q (x_k - \alpha_k g(x_k) - x_*) \\
&= \frac{1}{2}(x_k - x_* - \alpha_k g(x_k))^T Q (x_k - x_* - \alpha_k g(x_k)) \\
&= \frac{1}{2}(x_k - x_*)^T Q (x_k - x_*) - \alpha_k g(x_k)^TQ(x_k - x_*) + \frac{1}{2} \alpha_k^2 g(x_k)^T Q g(x_k) \\
&= q(x_k) - \alpha_k g(x_k)^TQ(x_k - x_*) + \frac{1}{2} \alpha_k^2 g(x_k)^T Q g(x_k),
\end{align*}

implying

$$q(x_k) - q(x_{k+1}) = \alpha_k g(x_k)^TQ(x_k - x_*) - \frac{1}{2} \alpha_k^2 g(x_k)^T Q g(x_k)$$

Dividing by $q(x_k)$ gives

$$\frac{q(x_k) - q(x_{k+1})}{q(x_k)} = \frac{\alpha_k g(x_k)^TQ(x_k - x_*) - \frac{1}{2} \alpha_k^2 g(x_k)^T Q g(x_k)}{\frac{1}{2}(x_k - x_*)^T Q (x_k - x_*)}$$

Let $g_k = g(x_k)$ and $y_k - x_k - x_*$. Then

$$\frac{q(x_k) - q(x_{k+1})}{q(x_k)} = \frac{\alpha_k g_k^T Q y_k - \frac{1}{2} \alpha_k^2 g_k^T Q g_k}{\frac{1}{2} y_k^T Q y_k}$$

Note that $g_k = Qx_k - b = Q(x - x_*) = Qy_k$, so $y_k = Q^{-1}g_k$. The above formula therefore simplifies to

$$\frac{q(x_k) - q(x_{k+1})}{q(x_k)} = \frac{2 \alpha_k |g_k|^2 - \alpha_k^2 g_k^TQg_k}{g_k^T Q^{-1} g_k}$$

Now recall the formula

$$\alpha_k = \frac{|g_k|^2}{g_k^TQg_k} \:(*)$$

This implies that

$$\frac{q(x_k) - q(x_{k+1})}{q(x_k)} = \frac{2 \frac{|g_k|^4}{g_k^T Q g_k} - \frac{|g_k|^4}{g_k^T Q g_k}}{g_k^T Q^{-1}g_k} = \frac{|g_k|^4}{(g_k^T Q g_k)(g_K^T Q^{-1} g_k)}$$

proving the theorem.

### _Thrm_. Convergence Speed of Steepest descent, quadratic case
__Claim__. For $x_0 \in \mathbb R^n$, the method of steepest descent starting at $x_0$ converges to the unique minimizer $x_*$ of the function $f$, and we have $q(x_{k+1}) \leq r q(x_k)$.


_proof_. We know that $q(x_{k+1}) \leq r^k q(x_0)$. Since $0 \leq r < 1$, when $k \to \infty$, $r^k \to 0$. Note that

$$x_k \in \{ x \in \mathbb R^n : q(x) \leq r^k q(x_0) \}$$

This set is a sublevel set of $q$. The sublevel sets of $q$ look like concentric filled-in ellipses centred at $x_*$, and as $k \to \infty$, they seem to "shrink" into $x_*$. Therefore steepest descent converges in the quadratic case.

Note that

$$r = \frac{(\Lambda - \lambda)^2}{(\Lambda - \lambda)^2} = \frac{( \Lambda / \lambda - 1 )^2}{(\Lambda / \lambda - 1)^2}$$

so $r$ depends only on the ratio $\Lambda / \lambda$. This number is called the \emph{condition number of $Q$}. (The condition number may be defined as $\|Q\|\|Q^{-1}\|$ in the operator norm on matrices; it is not hard to see that these numbers agree in our case.) 

If the condition number $\Lambda / \lambda \gg 1$ (large), then convergence is very slow. If $\Lambda / \lambda = 1$, then $r = 0$, and so convergence is achieved in one step.
