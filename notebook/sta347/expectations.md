# Expectations

(From now on, I will use $f$ for pdf/pmf and $F$ for cdf for simplicity)

## Expectations of Random Vairables

### Def'n with density function
The __expectation__ of a r.v. $X$ is defined as 

$$\mathbb E(X) = \sum_{x} x\text{pmf}_X(x) = \int_{-\infty}^\infty x\text{pdf}_X(x)dx$$

__if the summation/integral converges absolutely__. 

For $X$ without defined $pdf$ or $pmf$, we can define it via its probability space $(S, \mathcal E, P)$

$$\mathbb E(X) = \int_{S} X(s)dP(s)$$

For $X$ defined on $\mathbb R^{\geq 0}$, 

$$\mathbb E(X) = \int_0^\infty xdF(x)$$

This can be extended to negative reals by multiplying $-1$, and it's why we need the summation/integral to converge absolutely. 

Also, note that 

$$\mathbb E(X) = \int_0^\infty P(X> z)dz  = \int_0^\infty xdF(x)$$

If we do the integral via $y$ axis, instead of $x$ axis.

__Example__ Expectations may not exist. Consider Cauchy distribution 

$$\text{pdf}_X(x) = \frac{1}{\pi (1+x^2)}$$

This is a well-defined distribution, we can check via its $cdf$, note that 

$$\text{cdf}_X(x) = \frac{1}{\pi} \arctan(x) + \frac{1}{2}$$

so that $\text{cdf}_X(\infty) = 1, \text{cdf}_X(-\infty) = 0$

However, the expectation

$$\mathbb E(X) = \int_{-\infty}^\infty \frac{x}{\pi (1+x^2)}$$

Note that 

$$\int_{-\infty}^\infty |\frac{x}{\pi (1+x^2)}| \geq 2\int_1^\infty \frac{1}{\pi 2x} = \infty$$

Since the integral does not converge absolutely, its expectation is not defined

### Def'n with Probability
__Theorem__ For any r.v. $X$ with finite expectation

$$\mathbb E(X) = \int_0^\infty P(X>z)dz - \int_{-\infty}^0 P(X<z)dz = \int_{-\infty}^\infty xdF(x)$$

### Theorem 1. Expectation and Probability
$P(X\in A) = \mathbb E(\mathbb I(X\in A))$

_proof_. 

$$\mathbb E(\mathbb I(X\in A)) = 1P(X\in A) + 0 P(X\not\in A) = P(X\in A)$$

### Theorem 2. Functions of Random Variables
For r.v. $X$ and some transformation $g$, if $\mathbb E(g(X))$ is defined, then

$$\mathbb E(g(X)) = \int_{-\infty}^\infty g(x)\text{pdf}_X(x)dx = \sum_{x} g(x) \text{pmf}_X(x)$$

_proof_. We will assume $g$ is non-negative, $Y=g(X)$

\begin{align*}
\mathbb E(Y) &= \int_0^\infty P(Y > z) dz \\
&= \int_0^\infty P(g(X) > z)dz \\
&= \int_0^\infty \mathbb I(g(x) > z) d[\text{cdf}_X(x)]dz\\
&= \int_{-\infty}^\infty g(x)d[\text{cdf}_X(x)]
\end{align*}

## Properties of Expectations

### Linearity
__Claim__ $Y=aX+b\implies \mathbb E(Y) = a\mathbb E(X) + b$

_proof 1_. Using Riemann Stieltjes integral, 

$$F_Y(y) = P(Y \leq y) = P(aX+b \leq y) = P(X\leq \frac{y-b}{a}) = F_X(\frac{y-b}{a})$$

Thus, we have that 

\begin{align*}
\mathbb E(Y) &= \int_{-\infty}^\infty y dF_Y(y)\\
&= \int ydF_X(\frac{y-b}{a})\\
&= \int (az+b)dF_X(z)&z=\frac{y-b}{a}\\
&= a\int zdF_X(z) + b\\
&=  a\mathbb E(X) + b
\end{align*}

_proof 2_. Using the alternative definition of

\begin{align*}
\mathbb E(Y) &= \int_0^\infty P(Y > z) dz - \int_{-\infty}^{0}P(Y<z)dz\\
&= \int_0^\infty P(X > \frac{z-b}{a}) dz - \int_{-\infty}^{0}P(X<\frac{z-b}{a})dz\\
&= \int_{-b/a}^\infty aP(X > w) dw - \int_{-\infty}^{-b/a}aP(X<w)dw &w=\frac{z-b}{a}\\
&= a(\int_{0}^\infty P(X > w) dw -  \int_{-\infty}^0 P(X<w)dw) \\
&\quad+ a(\int_{-b/a}^0 P(X>z)dz + \int_{-b/a}^0 P(X<z)dz)\\
&= a\mathbb E(X) + a\int_{-b/a}^0 [P(X>z) +P(X<z)]dz\\
&= a\mathbb E(X)+b
\end{align*}


__Claim__ $\mathbb E(X+Y) = \mathbb E(X)+\mathbb E(Y)$

_proof_. For simplicity, we will prove only the discrete case, where the set of values is $S = \{x + y: x\in \mathcal X, y\in\mathcal Y\}$.  

\begin{align*}
\mathbb E(X+Y) &= \sum_{z\in S} z P(X+Y=z)\\
&= \sum_{z\in S} z \sum_{x\in\mathcal X, z-x\in\mathcal Y} P(X=x)P(Y=z-x)\\
&= \sum_{z\in S} \sum_{x\in\mathcal X, z-x\in\mathcal Y} (x+(z-x)) P(X=x)P(Y=z-x)\\
&= \sum_{x\in \mathcal X}\sum_{y\in\mathcal Y} (x+y)P(X=x)P(Y=y)\\
&= \sum_{x\in \mathcal X}xP(X=x)\sum_{y\in\mathcal Y}P(Y=y) + \sum_{y\in \mathcal Y}yP(Y=y)\sum_{x\in\mathcal X}P(X=x)\\
&= \sum_{x\in \mathcal X}xP(X=x) + \sum_{y\in \mathcal Y}yP(Y=y)\\
&= \mathbb E(X)+\mathbb E(Y)
\end{align*}

### Positive Expectation
__Claim__ $X\geq 0\implies \mathbb E(X)\geq 0$

_proof_. By definition,

$$\mathbb E(X) = \int_{-\infty}^{\infty}P(X>z)dz = \int_{-\infty}^{0}P(X>z)dz + \int_{0}^{\infty}P(X>z)dz$$

Since $X\geq 0$, we have $\int_{-\infty}^{0}P(X>z)dz = \int 0 dz = 0$  
By non-negativity of probability, 

$$\mathbb E(X) = \int_{0}^{\infty}P(X>z)dz \geq 0$$

### Expectation of constant
__Claim__ $\mathbb E(c) = 1$

_proof_. Let r.v. $X=c$, $\mathbb E(c) = 1P(X=c) = 1$

### Range of Expectation

__Claim__ $a\leq X\leq b \implies a\leq \mathbb E(X)\leq b$

_proof_. WLOG assume $F$ is continuously definedm

$$\mathbb E(X) = \int_{-\infty}^\infty x dF(x) = \int_a^b xdF(x)$$

Then, note that 

$$\int dF(x) = F(\infty)-F(-\infty) = 1 - 0 = 1$$

using $a\leq X\leq b$, we have that 

$$a =a\int dF(x) \leq \int xdF(x) \leq b\int dF(x) = b$$

### Product of Independent Random Variables
__Claim__ If $X,Y$ are independent, $g(X), h(Y)$ are r.v. with finite expectations. Then

$$\mathbb E(g(X)h(Y)) = \mathbb E(g(X))\mathbb E(h(Y))$$

_proof_. By definition of expecatation,

$$\mathbb E(g(X)h(Y)) = \int_{\mathbb R^2} g(x)h(y) dF_{X,Y}(x,y)$$

Since independence, 

$$\int_{x,y} g(x)h(y) dF_{X,Y}(x,y) = \iint g(x)h(y) dF_X(x)F_Y(y) = \int g(x)F_X(x)\int h(y)F_Y(y)$$

Thus, $\mathbb E(g(X)h(Y)) = \mathbb E(g(X))\mathbb E(h(Y))$

## Conditional Expectation

The __conditional expectation__ of $Y$ given $X=x$ is defined as 

$$\mathbb E(Y | X = x) = \int y dF_{Y|X}(y|x)$$

The alternative definitions for conditional expectation is very similar to unconditional ones

$$\mathbb E(Y|X=x) = \int_0^\infty P(Y>z|X=x)dz -\int_{-\infty}^0 P(Y<z|X=x)dz$$

$$\mathbb E(Y|X=x) = \sum yf_{Y|X}(y|x) = \int y f_{Y|X}(y|x)dy$$

Also, the properties hold 

$$\mathbb E(aY+bZ | X) = a\mathbb E(Y|X) + b\mathbb E(Z|X)$$

$$P(Y\geq 0 | X) = 1\implies \mathbb E(Y|X) > 0$$

$$\mathbb E(1|X) = 1$$

### Expectation of Conditional Expectation
__Claim__ $\mathbb E(\mathbb E(Y|X)) = \mathbb E(Y)$

_proof_. First, note that $\mathbb E(Y|X)$ can be seen as a function of $x$, so that

\begin{align*}
\mathbb E(\mathbb E(Y|X)) &= \iint ydF_{Y|X}(y|x) dF_X(x)\\
&= \int_{\mathbb R^2} y dF_{X,Y}(x,y)\\
&= \iint ydF_{X|Y}(x|y) dF_Y(y)\\
&= \int y dF_Y(y) = \mathbb E(Y)
\end{align*}

## Conditional Variance
Conditional variance is given by 

$$var(Y|X=x) = \mathbb E((Y- \mathbb E(Y|X=x))^2 | X=x)$$

The alternative form is very similar to unconditonal ones

$$var(Y|X) = \mathbb E(Y^2 | X) - \mathbb E(Y|X)^2$$

### Variance of Conditioanl Expectation
__Claim__ $var(Y) = \mathbb E(var(Y|X)) + var(\mathbb E(Y|X))$

_proof_. Known that $\mathbb E(Y) = \mathbb E(\mathbb E(Y|X))$, we have that 

$$\mathbb E(var(Y|X)) = \mathbb E(\mathbb E(Y^2 | X)) - \mathbb E(\mathbb E(Y|X)^2) = \mathbb E(Y^2) - \mathbb E(\mathbb E(Y|X)^2)$$

and also

$$var(\mathbb E(Y|X)) = \mathbb E(\mathbb E(Y|X)^2) - \mathbb E(\mathbb E(Y|X))^2 = \mathbb E(\mathbb E(Y|X)^2) - \mathbb E(Y)^2$$

summing them together, we have the claim

$$\mathbb E(var(Y|X)) + var(\mathbb E(Y|X)) =  \mathbb E(Y^2) - \mathbb E(Y)^2 = var(Y)$$
