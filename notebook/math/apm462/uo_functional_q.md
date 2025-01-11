# Examples: Unconstrainted Optimization on Calulus of Variations

## Example 1

!!!question

    Consider $Q+scc^T$ where $Q$ is positive definite symmetric, prove that the largest eigenvalue $\mu_n(s)$ of $Q+scc^T$ is bounded by $a_2 + \beta s \leq \mu_n(s) \leq a_1 + \beta s$.

_proof_. 

\begin{align*}
\mu_n(s) &= \max_{\|x\|=1}\big\{x^T(Q+scc^T)x\big\}\\
&= \max_{\|x\|=1} \big\{x^TQx + x^Tscc^Tx\big\}
\end{align*}

Because $Q$ is positive definite, $x^TQx \geq 0$, 

\begin{align*}
\mu_n(s) &\geq \max_{\|x\|=1} \big\{x^Tscc^Tx\big\}\\
&= \max_{\|x\|=1} \big\{x^Tcc^Tx\big\}s &s\text{ is a scalar}
\end{align*}

Also, we have 

\begin{align*}
\mu_n(s) &\leq \max_{\|x\|=1}\big\{x^TQx\big\} + \max_{\|x\|=1} \big\{x^Tscc^Tx\big\}\\
&= \max_{\|x\|=1}\big\{x^TQx\big\} + \max_{\|x\|=1} \big\{x^Tcc^Tx\big\}s
\end{align*}

Let $\alpha_2 = 0, \alpha_1 = \max_{\|x\|=1}\big\{x^TQx\big\}, \beta = \max_{\|x\|=1} \big\{x^Tcc^Tx\big\}$, since $c\neq 0, \beta > 0$. Therefore, 

$$a_2 + \beta s \leq \mu_n(s) \leq a_1 + \beta s$$


## Example 2
!!!question

    Derive the formula $p(t):\mathbb R\rightarrow \mathbb R^2 := (x(t), y(t))$ where $p(t)$ is the position of point on the rim of a circle of radius $R$, the circle is rolling along the $x$-axis at a constant speed $a$. Assume $c(t) = (at, R)$ is the position of the center of the circle at $t$ and $p(0) = (0, 0)$.

Let $f(\theta):\mathbb R\rightarrow \mathbb R^2 := (R\cos\theta, R\sin\theta)$ be the parametric equation of the circle.

Consider the point $q(t) = (at, 0)$ on the rim of the circle at time $t$, let 

$$q_c(t) = q(t) - c(t) = (at, 0) - (at, R) = (0, -R)$$

be its position relative to the center of the circle, note that 

$$q_c(t) = f(-\pi/2) = (\cos(-\frac{\pi}{2}), \sin(-\frac{\pi}{2}))$$

Then, let $L$ be the arc of the circle between $q_c$ and $p_c$ and $\theta(t)$ be the angle subtended by arc $L$ from the center of the circle. Since the arc length is $at$, we have

\begin{align*}
\theta(0) - \theta(t) &= \frac{at}{R}\\
\theta(t) &= \theta(0) - \frac{at}{R}\\
\theta(t) &= -\frac{\pi}{2} - \frac{at}{R}
\end{align*}

Therefore, let $q_c(t)$ be $p$'s position relative to the center of the circle, 

$$q_c(t) = f(\theta(t)) = \big(R\cos(-\frac{\pi}{2} - \frac{at}{R}), R\sin(-\frac{\pi}{2} - \frac{at}{R})\big)$$

so that 

$$p(t) = p_c(t) + c(t) = \big(at + R\cos(-\frac{\pi}{2} - \frac{at}{R}), R\sin(-\frac{\pi}{2} - \frac{at}{R})\big)$$


## Example 3

!!!question

    $$F[\mu[\cdot] = \int_a^b L(x, \mu(x), \mu'(x))dx, x(a)=A, x(b)=B$$

    $L, \mu \in C^2$, partition $[a,b]$ into $x_0, ..., x_{n+1}$ where $x_i = a + \frac{b-a}{n+1}i$ so that we can approximate the functional by

    $$F:\mathbb R^n\rightarrow \mathbb R, F(\mu_1, ..., \mu_n) :=\sum_{i=1}^{n+1}L(x_i, \mu_i, \frac{\mu_i - \mu_{i-1}}{h})h$$


!!!abstract "Part (a)"

    Calculate $\frac{dF}{d\mu_i}(\mu)$.

\begin{align*}
\frac{dF}{d\mu_i}(\mu) &= \sum_{j=1}^{n+1}\frac{d}{d\mu_i}L(x_j, \mu_j, \frac{\mu_j - \mu_{j-1}}{h})h\\
&= \frac{d}{d\mu_i}L(x_{i}, \mu_{i}, \frac{\mu_i - \mu_{i-1}}{h})h + \frac{d}{d\mu_i}L(x_{i+1}, \mu_{i+1}, \frac{\mu_{i+1} - \mu_{i}}{h})h\\
&= L_z(x_{i}, \mu_{i}, \frac{\mu_i - \mu_{i-1}}{h})h\frac{d}{d\mu_i}\mu_i + L_p(x_{i}, \mu_{i}, \frac{\mu_i - \mu_{i-1}}{h})h\frac{d}{d\mu_i}\frac{\mu_i - \mu_{i-1}}{h}\\
&\quad+L_p(x_{i+1}, \mu_{i+1}, \frac{\mu_{i+1} - \mu_{i}}{h})h\frac{d}{d\mu_i}\frac{\mu_{i+1} - \mu_{i}}{h}\\
&= hL_z(x_{i}, \mu_{i}, \frac{\mu_i - \mu_{i-1}}{h}) - (L_p(x_{i+1}, \mu_{i+1}, \frac{\mu_{i+1} - \mu_{i}}{h})- L_p(x_{i}, \mu_{i}, \frac{\mu_i - \mu_{i-1}}{h}))
\end{align*}


!!!abstract "Part (b)"

    Take $h\rightarrow 0$, show that $\frac{dF}{d\mu_i}(\mu) = 0\Rightarrow L_z(x, \mu(x), \mu'(x) - \frac{d}{dx}L_p(x, \mu(x), \mu'(x))) = 0$.

_proof_. Since $\frac{dF}{d\mu_i}(\mu) = 0$

\begin{align*}
\lim_{h\rightarrow 0} \frac{1}{h}\frac{dF}{d\mu_i}(\mu) &= \lim_{h\rightarrow 0}L_z(x_i, \mu_i, \frac{\mu_i-\mu_{i-1}}h) \\
&\quad- \lim_{h\rightarrow 0}\frac{L_p(x_{i+1}, \mu_{i+1}, \frac{\mu_{i+1} - \mu_{i}}{h})- L_p(x_{i}, \mu_{i}, \frac{\mu_i - \mu_{i-1}}{h})}{h}\\
&= L_z(x_i, \mu(x_i), \mu(x_i)')\\
&\quad - \lim_{h\rightarrow 0}\frac{L_p(x_i+h, \mu(x_i+h), \mu'(x_i+h))- L_p(x_{i}, \mu(x_i), \mu'(x_i))}{h}\\
&\text{by definition of derivative}\\
&= L_z(x_i, \mu(x_i), \mu(x_i)') - \frac{d}{dx}L_p(x_i, \mu(x_i), \mu(x_i)')
\end{align*}

Therefore, for some $x\in[a,b]$, since $h\rightarrow 0$, we can partition $[a,b]$ s.t. $x\in \text{partition}(a, b)$, so that we have 

$$L_z(x_i, \mu(x_i), \mu(x_i)') - \frac{d}{dx}L_p(x_i, \mu(x_i), \mu(x_i)') = \lim_{h\rightarrow 0} \frac{1}{h}\frac{dF}{d\mu_i}(\mu) = 0$$




## Example 4

!!!question

    Find FONC of

    \begin{align*}
    \text{minimize}\quad &F[\mu(\cdot)] := \int_a^b L(x, u(x), u'(x))dx\\
    \text{subject to}\quad &\mu\in \mathcal A:= \{\mu:[a,b]\rightarrow\mathbb R\mid \mu\in C^2, \mu(a) = A\}
    \end{align*}


Let $\mu_*$ be the minimizer of the problem.  
Let $\mathcal T:= \{v:[a, b]\rightarrow\mathbb R\mid v\in C^2, v(a) = 0\}$ be the set of test functions so that $\forall v\in \mathcal T. \forall s\in\mathbb R. u_*+sv \in \mathcal A$.  
Then as what have been done in the class till the integrations by parts 

\begin{align*}
\frac{d}{ds}F[u_*+sv]
&=\int_a^b \big[L_z(...) - \frac{d}{dx}L_p(...)\big]v(x)dx + \big[L_p(...)\mid_a^b\big]
\end{align*}

Since $v(a) = 0$, note that 

\begin{align*}
\big[L_p(x, u_*(x), u_*'(x))v(x)\mid_a^b\big] &= L_p(b, u_*(b), u_*'(b))v(b) - L_p(a, u_*(a), u_*'(a))v(a)\\
&= L_p(b, u_*(b), u_*'(b))v(b)
\end{align*}

Consider $v_1\in\mathcal T$ s.t. $v(b) = 0$, hence

$$\big[L_p(x, u_*(x), u_*'(x))v(x)\mid_a^b\big] = 0$$

Given $u_*$ is the minimizer,  

$$0 = \frac{d}{ds}F[u_*+sv] =\int_a^b \big[L_z(...) - \frac{d}{dx}L_p(...)\big]v(x)dx$$

follows the original Euler-Lagrange equation, i.e. 

$$L_z(x, u_*(x), u_*'(x)) - \frac{d}{dx}L_p(x, u_*(x), u_*'(x)) = 0$$

Consider $v_2\in\mathcal T, v_2(b)\neq 0$, since we have to fulfill the necessary conditions for cases like $v_1$, we have 

$$L_z(x, u(x), u'(x)) - \frac{d}{dx}L_p(x, u(x), u'(x)) = 0$$

so that 

$$0 = \frac{d}{ds}F[u_*+sv] = 0 + L_p(b, u(b), u'(b))v(b)$$

Therefore, there are two FONC as

$$L_z(x, u_*(x), u_*'(x)) - \frac{d}{dx}L_p(x, u_*(x), u_*'(x)) = 0$$

$$L_p(b, u(b), u'(b))v(b) = 0$$


