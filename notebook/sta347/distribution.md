# Random Variables and Single Variable Distributions

## Random Variable and Distribution

A __random variable__ is a function $X:S\rightarrow \mathbb R$ s.t. $\{s\in S: X(s)\leq r\}$ is an event for all $r\in\mathbb R$. 

__Theorem__ If $X, Y$ are random variables, then $aX, X+Y, XY$ are all random variables. 

The __distribution__ of $X$ is the collection of all probabilities of all events induced by $X$, i.e. $(B, P(X\in B))$, $B$ is the Borel set.  
Two random variables $X, Y$ are __identically distributed__ if they have the same distribution.

## Discrete Distribution
$X$ is __discrete__ if $P(X=x)=0$ or $P(X=x) > 0$ and $\sum_x P(X=x)=1$, i.e. they takes at most countably many values $x_1,x_2,...$ s.t. $P(X=x_i) > 0$ and $\sum P(X=x_i) = 1$.

Then, __probability mass function__ is defined as 

$$\text{pmf}_X(x):X(S)\rightarrow \mathbb R:=P(X=x)$$

__Theorem__ Let $X(S) = \{x_1,x_2,...\}$ be the set of possible values of a discrete random variable $X$. Then for any $A\subset\mathbb R$, 

$$P(X\in A) = \sum_{x_i\in A} P(X=x_i) = \sum_{x_i\in A}\text{pmf}_X(x_i)$$

__Bernoulli distribution__ $X\sim Bernoulli(p)$ if $X$ taking values $\{0,1\}$ with $P(X=1) = p$ and $P(X=0) = 1-p$ for $p\in[0,1]$.

__Uniform distribution__ $X\sim uniform(\mathcal X)$ is $\mathcal X$ is a non-empty finite set and $X$ takes values in $\mathcal X$ with equal probability. 

$$\text{pmf}_X(x) = |\mathcal X|^{-1}\mathbb I(x\in\mathcal X)$$

__Binomial distribution__ $X\sim binomial(n, p)$ if $X$ is identically distributed to the number of success in $n$ independent trails with success probability $p$. 

$$\text{pmf}_X(x) = {n\choose x} p^x(1-p)^{n-x} \mathbb I(x=0,...,n)$$

__Geometric distribution__ $X \sim geometric(p)$ the number of independent Bernoulli trials until the first success. 

$$\text{pmf}_X(n) = (1-p)^{n-1}p$$

__Negative binomial distribution__ $X\sim neg-bin(k, p)$ the number of independent Bernoulli trials until the kth success. 

$$\text{pmf}_X(n) = {n-1\choose k-1}(1-p)^{n-k}p^k$$

__Hypergeometric distribution__ $X\sim hypergeo(n, r, m)$ the number of black balls when $m$ balls are drawn without replacement from a jar or $n$ balls, and $r$ of them are black.

$$\text{pmf}_X(k) = \frac{ {r\choose k}{n-r\choose m-k}}{n\choose m} \mathbb I(k=0,...,\min(r,m))$$

__Poission distribution__ $X\sim Poisson(\lambda)$ the number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event. 

$$\text{pmf}_X(k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

## Continuous Distribution
$X$ is __continuous__ if for all real number interval $[a,b]$, there is some __probability density function__ $f: \mathbb R\rightarrow \mathbb R, f> 0$ s.t. 

$$P(a < X\leq b) = \int_a^b f(x)dx$$

Note that if we can find a well defined pdf for a continuous distribution, we have its definition. 

__Uniform distribution__ $X\sim uniform(a, b)$ if $P(c<X<d) = \frac{d-c}{b-a}$ for $a\leq c\leq d\leq b$.

$$\text{pdf}_X(x) = (b-a)^{-1} \mathbb I (a<x<b)$$

__Exponential distribution__ $X\sim exponential(\lambda)$ the time between events in a Poisson point process

$$\text{pdf}_X(x) = \lambda e^{-\lambda x}\mathbb I(w > 0)$$

__Gamma distribution__ $X\sim Gamma(\alpha, \beta)$ is a family of continuous distributions parameterized by  shape $\alpha$, rate $\beta$ (or scale $\theta = \beta^{-1}$)

$$\text{pdf}_X(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-\beta x} \mathbb I(x>0)$$

__Normal distribution__ $Z \sim \mathcal N(\mu, \sigma^2)$ the most common continuous distribution parameterized by mean $\mu\in\mathbb R$ and standard deviation $\sigma > 0$

$$\text{pdf}_Z(z) = (2\pi\sigma^2)^{-1/2} \exp\big(-\frac{(x-\mu)^2}{2\sigma^2}\big)$$

## Cumulative Distribution Function

The __cumulative distribution function__ of $X$ is the function 

$$\text{cdf}_X(x) = F_X(x) = P(X \leq x)$$

$F$ has the following properties
 1. __nondecreasing__: since $\forall x\leq y, \{X\leq x\} \subset \{X\leq y\} $
 2. $\lim_\infty F(x) = 1, \lim_{-\infty} F(x) = 0$: consider the two events $\{X\leq \infty\} = S, \{X\leq -\infty\} = \emptyset$
 3. $F$ is right continuous, $\lim_{y\rightarrow x-} F(y) = F(x)$
 4. $F(x-):=\lim_{y\rightarrow x+} F(y) = P(X < x)$
 5. $P(X=x) = F(x) - F(x-)$
 
Note that for any function $F$ that satisfies properties 1., 2., 3. It is a cdf. 

__p-quantile__ of a r.v. $X$ is $x$ s.t. $P(X\leq x) \geq p$ and $P(X\geq x) \geq 1-p$, and __lower quartile, median, upper quartile__ is the $0.25$-quantile, $0.5$-quantile, $0.75$-quantile, respectively. __Inter quartile range (IQR)__ is the difference between upper and lower quartile.
