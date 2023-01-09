# Variance and Covariance

## Moments
For $k\in\mathbb Z^+$, the __kth moment__ of $X$ is defined as $\mathbb E(X^k)$ if it is finite and the __kth central moment__ is $\mathbb E((X-\mathbb E(X))^k)$ (if it is finite). 

__Mean__ is defined as $\mu := \mathbb E(X)$ is the expectation and as the the first moment. 

__Variance__ is defined as the 2nd central moment, a.k.a.

$$\sigma^2 = var(X) = \mathbb E[(X-\mathbb E(X))^2]$$

__skewness__ is the standardized third moment

$$\mathbb E[(X-\mu)^3] / \sigma^3$$

__kurtosis__ is the standardized fourth moment

$$\mathbb E[(X-\mu)^4] / \sigma^4$$

### Theorem 1
__Claim__. 

$$\mathbb E(|X|^k) <\infty \implies \forall s \leq k. \mathbb E(|X|^s) <\infty$$

_proof_.

$$|x|^s \leq \max(1, |x|)^{k-s} |x|^s \leq 1 + |x|^k$$

so that 

$$\mathbb E(1+|X|^k) \leq 1 + \mathbb E(|X|^k) <\infty$$

## Variance
__Variance__ is defined as the 2nd central moment, a.k.a.

$$var(X) = \mathbb E[(X-\mathbb E(X))^2]$$

__Covariance__ between $X,Y$ is 

$$cov(X, Y) = \mathbb E[(X-\mathbb E(X))(Y-\mathbb E(Y))]$$

$X, Y$ are __uncorrelated__ if $cov(X, Y) = \mathbb E(XY)-\mathbb E(X)\mathbb E(Y) = 0$

__Correlation__ of $X,Y$ (defined when $X,Y$ have finite secomd moment)

$$cor(X,Y) = \frac{cov(X,Y)}{\sqrt{var(X)var(Y)}}$$

### Alternative Form of Variance
__Claim__ $var(X) = \mathbb E(X^2)- \mathbb E(X)^2$

_proof_. 

\begin{align*}
var(X) &= \mathbb E((X-\mu)^2) \\
&= \mathbb E(X^2 - 2X\mu + \mu^2) \\
&= \mathbb E(X^2) - 2\mu \mathbb E(X) + \mu^2\\
&= \mathbb E(X^2) - \mu^2
\end{align*}

### Alternative Form of Covariance
__Claim__ $cov(X,Y) = \mathbb E(XY)-\mathbb E(X)\mathbb E(Y)$

_proof_. 

\begin{align*}
cov(X,Y) &= \mathbb E((X-\mathbb E(X))(Y - \mathbb E(Y)))\\
&= \mathbb E(XY - \mathbb E(X)Y - \mathbb E(Y) X + \mathbb E(X)\mathbb E(Y))\\
&= \mathbb E(XY) - \mathbb E(X)\mathbb E(Y) - \mathbb E(Y)\mathbb E(X) + \mathbb E(X)\mathbb E(Y)\\
&= \mathbb E(XY) - \mathbb E(X)\mathbb E(Y)
\end{align*}

### Variance under Linear transfomation 
__Claim__ $var(aX+b) = a^2var(X)$

_proof_.

\begin{align*}
var(aX+b) &= \mathbb E((aX+b)^2) -\mathbb E(aX+b)^2 \\
&= a^2\mathbb E(X^2) + 2ab\mathbb E(X) + b^2 - (a\mathbb E(X) + b)^2\\
&= a^2\mathbb E(X^2) + 2ab\mathbb E(X) + b^2 - a^2\mathbb E(X)^2 - 2ab\mathbb E(X) - b^2\\
&= a^2\mathbb E(X^2) - a^2\mathbb E(X)^2\\
&= a^2var(X)
\end{align*}

### Variance of Sums
__Claim__ $var(X+Y) = var(X)+ var(Y) + 2cov(X,Y)$

_proof_. 

\begin{align*}
var(X+Y) &= \mathbb E((X+Y)^2) - \mathbb E(X+Y)^2\\
&= \mathbb E(X^2) + 2\mathbb E(XY) + \mathbb E(Y)^2 - \mathbb E(X)^2 - 2\mathbb E(X)\mathbb E(Y) - \mathbb E(Y)^2\\
&= \mathbb E(X^2) - \mathbb E(X)^2 + \mathbb E(Y)^2 - \mathbb E(Y)^2 + 2(\mathbb E(XY) - \mathbb E(X)\mathbb E(Y))\\
&= var(X)+ var(Y) + 2cov(X,Y)
\end{align*}

__Corollary__ $var(X+Y) = var(X) + var(Y)$ IFF $X,Y$ uncorrelated. 

__Corollary__ $var(\sum^n X_i) = \sum^n var(X_i)$ if $X_i$ are pairwise uncorrelated. 

### Bounded random variable
__Claim__ If $X$ is bounded, then its variance is finite

_proof_. $X$ bounded implies $\mathbb E(X)$ bounded, and $X^2$ bounded, so that 
$\sigma^2 = \mathbb E(X^2) - \mathbb E(X)^2$ is also bounded

### Zero Variance
__Claim__ $var(X) = 0$ IFF $P(X=c) = 1$

_proof_. $\mathbb E(X - \mathbb E(X)^2) = 0$ IFF $\mathbb E(X) = c$
