# Inequalities Related to Expecations

## Markov's Inequality
__Claim__ If $X\geq 0$ with $\mu <\infty$. Then for all $a>0$

$$P(X\geq a) \leq \mu/a$$

_proof_. 

\begin{align*}
P(X\geq a) &= \int \mathbb I(x\geq a) dF_X(x)\\
&\leq \int \frac{x}{a}\mathbb I(x\geq a) dF_X(x)\\
&\leq \mathbb E(X/a)\\
&= \mu /a
\end{align*}

### Chebychev's Inequality

__Claim__ Let $X$ be a r.v. with mean $\mu$ and $\sigma^2$. Then, for all $a > 0$

$$P(|X-\mu| \geq a\sigma) \leq a^{-2}$$

_proof 1_. 

\begin{align*}
P(|X-\mu | \geq a\sigma) &= \int \mathbb I(|x-\mu |\geq a\sigma) dF_X(x)\\
&\leq \int (\frac{|x-\mu|}{a\sigma})^2\mathbb I(|x-\mu |\geq a\sigma) dF_X(x)\\
&\leq \mathbb E(\frac{|x-\mu|}{a\sigma})^2\\
&= \sigma^2 \frac{1}{a^2\sigma^2}\\
&= a^{-2}
\end{align*}

_proof 2_. Taking $Y = (X-\mu)^2/\sigma^2$ and $a = k^2$, using Markov's Inequality, in this case

$$P(|X-\mu| \geq a\sigma) = P((X-\mu)^2 \geq a^2\sigma^2) \leq \mathbb E((X-\mu)^2) / {a^2\sigma^2} = a^{-2}$$

## Cauchy-Schwartz Inequality
__Claim__ If $X,Y$ are r.v. with finite second moment

$$\mathbb E(XY)^2 \leq \mathbb E(X^2)\mathbb E(Y^2)$$

where the equality holds IFF $P(aX=bY) = 1$ for some $a,b\in\mathbb R$

_proof_. Note that we can consider the expectation as a inner product. 

__Corollary__ $cov(X, Y)^2 \leq var(X)var(Y)$

_proof_. By CS Ineq.

\begin{align*}
cov(X, Y)^2 &= \mathbb E[(X-\mathbb E(X))(Y-\mathbb E(Y))]^2 \\
&\leq \mathbb E[(X-\mathbb E(X))^2]\mathbb E[(Y-\mathbb E(Y))^2]\\
&= var(X)var(Y)
\end{align*}

### Range of Correlation

__Claim__ $corr(X, Y) \in [-1, 1]$

_proof_. By the definition of correlation and the corollary

$$[corr(X, Y)]^2 = \frac{cov(X, Y)^2}{var(X)var(Y)} \leq 1$$

__Corollary__ $Y=aX+b$ IFF $corr(X, Y) = 1\times \text{sign}(a)$

## Additional Inequalities

Note that the following inequalities are given without proofs. 

### Young's Inequality

For $p, q > 1$ with $p^{-1} + q^{-1} = 1$ and $x, y\geq 0$. 

$$xy \leq \frac{x^p}{p} + \frac{y^q}{q}$$

with equality holds IFF $x^p = y^q$

### Holder's Inequality
For $p, q > 1$ with $p^{-1}+q^{-1} = 1$. 

$$\mathbb E(XY) \leq \mathbb E(|X|^p)^{-p} \mathbb E(|Y|^q)^{-q}$$

_proof_. The statement is obtained by treating expectation as an inner product, and CS inequality is a special case where $p=q=2$.

### Jensen's Inequality

For a convex function $\psi$, $\psi(\mathbb E(X)) \leq \mathbb E(\psi(X))$

_proof_. This inequality can be easily derived from convexity definition

### Lyapounov's Inequality

If $\mathbb E(|X|^p)$ is finite for some $p>0$, then $\mathbb E(|X|^q) \leq \mathbb E(|X|^p)^{q/p}$ for all $0 < q \leq p$. 

_proof_. $x^{p/q}$ is convex, apply Jensen's Inequality

### Minkowski's Inequality

For $p\geq 1, \|X+Y\|_p \leq \|X\|_p + \|Y\|_p$
