# Multivariate Distributions

## Joint Distributions
The __joint distribution__ of random variables $X_1,...,X_n$ is defined as the collection of all possible probabilities, $P((X_1,...,X_n)\in B)$ where $B$ is a Borel set in $\mathbb R^n$. When, $n=2$, we can call it __bivariate distribution__.

Then, we can define the joint pmf as 

$$\text{pmf}_{X,Y}(x,y) = P(X=x,Y=y)$$

Simiarly, the joint pdf is 

$$P((X,Y) \in B) = \iint_B f(x,y)dxdy$$

Both of them still satisifies non-negativity and total probability.

Similarly, if we have more variables, the joint pmf is 

$$\text{pmf}_{X_1,...,X_n}(x_1,...,x_n) = P(X_1=x_1, ..., X_n=x_n)$$

$$\text{pdf}_{X_1,...,X_n}(x_1,...,x_n) = \int\cdots\int_B f(x,y)dxdy$$

joint cdf is then defined as 

$$\text{cdf}_{X,Y}(x,y) = P(X\leq x, Y\leq y)$$

## Marginal Distributions

Suppose $X,Y$ are r.v. We can __marginalize__ the density functions for $X$ or $Y$ from the joint density. 

$$\text{cdf}_X(x) = \lim_{y\rightarrow\infty} \text{cdf}_{X,Y}(x,y)$$

$$\text{pdf}_X(x) = \int \text{pdf}_{X,Y}(x,y)dy$$

$$\text{pmf}_X(x) = \sum_{y} \text{pmf}_{X,Y}(x,y)$$

If we have more variables, we can marginalize one variable by taking its limit / integral / sum just as in bivariate case

random variable $X,Y$ is __independent (independence of r.v.)__ ($X\perp Y$) IFF $P(X\in A, Y\in B) = P(X\in A)P(Y\in B)$

__Theorem__ The following statements are equivalent:

$$X\perp Y$$

$$\text{cdf}_{X,Y}(x,y) = \text{cdf}_X(x) \text{cdf}_Y(y)$$

$$\text{pmf}_{X,Y}(x,y) = \text{pmf}_X(x) \text{pmf}_Y(y)$$

$$\text{pdf}_{X,Y}(x,y) = \text{pdf}_X(x) \text{pdf}_Y(y)$$

_proof_. (We will only prove for cdf since the idea is very similar using the definition)

$$\text{cdf}_{X,Y}(x,y) = P(X\leq x, Y\leq y) = P(X\in A)P(Y\in B) = \text{cdf}_X(x) \text{cdf}_Y(y)$$

If we have more variables, then they are (mutually) independent IFF

$$[cdf/pmf/pdf]_{X_1,...,X_n}(x_1,...,x_n) = \prod_i [cdf/pmf/pdf]_{X_i}(x_i)$$

### Example
$X,Y$ are independent and has the same density $2x \mathbb I(0\leq x\leq 1)$, compute $P(X+Y\leq 1)$

\begin{align*}
P(X+Y\leq 1) &= P(0\leq X\leq 1, 0\leq y\leq 1-x)\\
&= \int_0^1\int_0^{1-x}2x2ydydx\\
&= 4\int_0^1\int_0^{1-x}xydydx\\
&= 1/6
\end{align*}

### Example
$\text{pdf}_{X,Y}(x,y) = kx^2y^2 \mathbb I(x^2+y^2\leq 1)$, show $X,Y$ is not independent. 

Marginalize $X$, 

\begin{align*}
\text{pdf}_X(x) &= \int_{-\infty}^\infty  kx^2y^2 \mathbb I(x^2+y^2\leq 1)dy\\
&= kx^2\int_{-\infty}^\infty  y^2 \mathbb I(x^2+y^2\leq 1)dy \\
&= kx^2\int_{-\sqrt{1-x^2}}^{\sqrt(1-x^2)}y^2dy\\
&= \frac{2}{3}kx^2(1-x^2)^\frac{3}{2}
\end{align*}

Note that $X,Y$ is symmetric, so that 

$$\text{pdf}_X(x)\text{pdf}_Y(y) = \frac{2}{3}kx^2(1-x^2)^\frac{3}{2}\frac{2}{3}ky^2(1-y^2)^\frac{3}{2}\neq \text{pdf}_{X,Y}(x,y)$$

### Example
$\text{pdf}_{X,Y}(x,y) = ke^{-(x+2y)}\mathbb I(x\geq 0, y\geq 0)$, determine $k$ and whether $X,Y$ independent. 

To determine $k$, using the total probability 

$$\int_{-\infty}^\infty \int_{-\infty}^\infty \text{pdf}_{X,Y}(x,y) dxdy = \int_{0}^\infty \int_{0}^\infty ke^{-(x+2y)} dxdy = [-ke^{-2y}/2]^\infty_0 = \frac{0-(-k)}{2} = \frac{k}{2}$$

so that $k/2 = 1\implies k=2$

Marginalize $X$, we have 

$$\text{pdf}_Y(y) = \int_{0}^\infty 2e^{-(x+2y)} dx = 2e^{-2y}$$

Marginalize $Y$, we have 

$$\text{pdf}_X(x) = \int_{0}^\infty 2e^{-(x+2y)} dy = e^{-x}$$

Indeed, they are independent since 

$$\text{pdf}_Y(y)\text{pdf}_X(x) = 2e^{-2y}\mathbb I(y\geq 0) e^{-x}\mathbb I(x\geq 0) = 2e^{-(x+2y)}\mathbb I(x\geq 0, y\geq 0) = \text{pdf}_{X,Y}(x,y)$$

## Conditional Distributions

The conditional pmf is defined as 

$$\text{pmf}_{X|Y}(x|y) = P(X=x | Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{\text{pmf}_{X,Y}(x,y)}{\text{pmf}_Y(y)}$$

The conditional pdf is given by 

$$\text{pdf}_{X|Y}(x|y) =  \frac{\text{pdf}_{X,Y}(x,y)}{\text{pdf}_Y(y)}$$

Since in continuous case, $P(Y=y) = 0$ in general, we need to define a very small $\delta$ so that 

$$P(X\in A|Y\in B_\delta) =\frac{P(X\in A, Y\in B_\delta)}{P(Y\in B_\delta)} = \frac{\int_{B_\delta}\int_A \text{pdf}_{X,Y}(x,y)dxfy}{\int_{B_\delta}\text{pdf}_Y(y)dy}$$

Note that since $B_\delta$ is arbitrarily small, we can approximate $\int_{B_\delta}f(x)dx = 2\delta f(x)$
