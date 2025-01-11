# Bayes Inference


The MoM of MLE approach cannot incorporate other information about $\theta$ into the inference. For example, information from previous studies or "common sense" on the parameters. 

## Prior and Posterior
Quantify a priori information about $\theta$ via a distribution. 
We can think of $f(x_1...x_n; \theta)$ as representing the conditional pdf of $X_1,...,X_n$ given $\theta$, where $\theta \sim \Theta$ so that 

$$f(x_1,...,x_n; \theta) = f(x_1,...x_n | \theta)$$

Such information of $\theta$ is given via a prior $\pi(\theta)$. Then, the posterior density function combines the information from the prior with the information from the data. By Bayes Theorem

\begin{align*}
\pi(\theta|x_1,...,x_n) &= \frac{\pi(\theta)f(x_1,...,x_n; \theta)}{\int_\Theta \pi(s)f(x_1,...,x_n; s) ds}\\
&= c(x_1,...,x_n)\pi(\theta)\mathcal L(\theta)\\
&\propto \pi(\theta)\mathcal L(\theta)
\end{align*}

The denominator, $c(x_1,...,x_n)$ is often called the normalizer, which depends only on the data and in practice, intractable to compute. 

## Bayesian Interval Estimation
Given a posterior $\pi(\theta|x)$, an interval $\mathcal I(x)$ is $100 p\%$ credible interval for $\theta$ if 

$$\int_{\mathcal I(x)} \pi(\theta|x)d\theta = p$$

A $100p\%$ credible interval is called a $100p\%$ highest posterior density interval for $\theta$ if 

$$\forall \theta \in \mathcal I. \forall \theta' \not\in \mathcal I. \pi(\theta|x) > \pi(\theta'|x)$$

This measurement is in real time, very close to CI

## Maximum a posteriori (MAP) estimate
$\hat\theta$ is the posterior mode

$$\pi(\hat\theta|x) \geq \pi(\theta|x), \forall \theta\in\Theta$$

MAP are often used in situation where MLE is unstable or undefined. 
The prior density is used to "regularize" the problem, i.e. force the distribution of $\hat \theta$ to stay within a bounded subset of $\Theta$. so that we reduce the variance of $\hat\theta$, in exchange of possibly increasing the bias. 

### Example: Non-regular location estimation
Let $X_1,...,X_n$ indep. r.v. with 

$$f(x;\theta) = \frac{|x-\theta|^{-1/2}}{2\sqrt \pi} \exp(-|x-\theta|)$$

The likelihood function is 

$$\mathcal L(\theta) = \prod^n \bigg\{\frac{|x_i-\theta|^{-1/2}}{2\sqrt \pi} \exp(-|x_i-\theta|)\bigg\}$$

MLE is undefined since $\lim_{\theta\rightarrow x_i}\mathcal L(\theta) = \infty$

Consider a Cauchy prior $\pi(\theta) = \frac{10}{\pi(100+\theta^2)}$ so that the posterior is 

$$\pi(\theta|x_1,...,x_n) = c(x)(100+\theta^2)^{-1}\prod^n \frac{|x_i-\theta|^{-1/2}}{2\sqrt \pi} \exp(-|x_i-\theta|)$$ 

so that we can compute the pdf

## Multiparameter Model Bayesian Inference

For the interested parameter, we can determine the posterior density of the subset of interested parameters by integrating over the others, i.e. 

$$\pi(\theta_1 | x) = \int \pi(\theta_1, \theta_1,...,\theta_k | x)d\theta_2...d\theta_k$$

### Example: Two state Markov Chain
Consider a (first order) Markov Chain $\{X_i\}$ where each $X_i \in \{0, 1\}$, by Markov assumption, 

$$f(x_1,...,x_n) = f_1(x_1)\prod_{i=2}^n f_{i | {i-1}}(x_i | x_{i-1})$$

Then, we parameterize the __transition (conditional) probabilities__ as 

|  | $X_{i} = 0$  | $X_{i} = 1$ | 
| --- | --- | --- |
|$X_{i+1} = 0$ | $1-a$ | $a$ | 
| $X_{i+1} = 1$ | $\beta$ | $1-\beta$ |

Let the table above be our transition matrix $P$, note that 
$P^k$ is used to determine $P(X_{i+k} = x | X_i = y)$, also note that the eigenvalues are $1, \rho = 1-a-\beta$ for $P$, which gives $1, \rho^k$ for $P^k$.

We can obtain the stationary distribution of the Markov Chain by looking at 

$$\lim_{k\rightarrow \infty} P^k = P_0 = \begin{bmatrix}
\frac{\beta}{a+\beta} & \frac{a}{a+\beta}\\
\frac{\beta}{a+\beta} & \frac{a}{a+\beta}
\end{bmatrix}$$

Therefore, the stationary distribution of $X_i$ is 

$$P(X_i = 1) = f(1; a, \beta) = \frac{a}{a+\beta} = \theta$$

$$P(X_i = 0) = f(0; a,\beta) = \frac{\beta}{a+\beta} = 1-\theta$$

So that 

$$corr(X_i, X_{i+1}) = \frac{cov(X_i, X_{i+1})}{var(X_i)} = 1-a-\beta = \rho$$

Then, we define a __run__ as the number of subsequence consisting of all $0$ or $1$, for example 

$$000 11 0 1111 00 111 0$$ 

gives 7 runs. 

If $X_1,...,X_n$ come from the two state MC, then the number of runs is 

$$R = 1 + \sum_{i=1}^{n-1} \mathbb I(X_i \neq X_{i+1})$$

$R$ provide some information about $\rho$, i.e. $\rho\rightarrow 1\Rightarrow R\downarrow, \rho\rightarrow -1\Rightarrow R\uparrow$ 

### MoM estimator
Note that 

\begin{align*}
E(R) &= 1 + \sum^{n-1}P(X_i\neq X_{i+1})\\
&=  1 + \frac{2(n-1)a\beta}{a+\beta}\\
&= 1 + 2(n-1)\theta(1-\theta)(1-\rho)
\end{align*}

We can use the proportion of 1s and number of runs to obtain the MoM estimator of $\theta$ and $\rho$

$$\hat\theta = n^{-1}\sum^n \mathbb I(X_i = 1), \hat\rho = 1 - \frac{R-1}{2(n-1)\hat\theta(1-\hat\theta)}$$

### MLE (MCLE)
Note that 

\begin{align*}
\mathcal L(a, \beta) &= f(x_1; a, \beta) \prod^{n-1}f(x_{i+1} | x_i ; a, \beta)\\
&= (\frac{a}{a+\beta})^{x_1}(\frac{\beta}{a+\beta})^{1-x_1} \\
&\quad\prod_{n-1} [a^{(1-x_i)x_{i+1}}(1-a)^{(1-x_i)(1-{x_{i+1}})}][\beta^{x_i(1-x_{i+1})}(1-\beta)^{x_ix_{x_i+1}}]
\end{align*}

We can also define a conditional likelihood function

$$\mathcal L_{cond}(a,\beta) = \prod^{n-1}f(x_{i+1}|x_i; a, \beta)$$

Maximizing $\mathcal L$ w.r.t. to $a,\beta$ individually is impossible, while we can maximize $\mathcal L_{cond}$, which gives 

$$\hat a = \frac{\sum^{n-1}(1-X_i)(X_{i+1})}{\sum^{n-1}(1-X_i)}; \hat\beta = \frac{\sum^{n-1}(1-X_{i+1})(X_{i})}{\sum^{n-1}X_i}$$

### Bayesian Analysis
Consider a prior $\pi(a,\beta)$, then the prior density for $(\theta, \rho)$ is 

$$\pi(\theta(1-\rho), (1-\theta)(1-\rho))\times \underset{jacobian}{(1-\rho)}$$

on the set $\{(\theta, \rho) : \rho \in (-1, 1),  \theta\in \frac{-\min(\rho, 0)}{1-\min(\rho, 0)}, \frac{1}{1-\min(\rho, 0)}\}$

However, it's hard for Bayesian to compute the normalizer. 

### Markov Chain Monte Carlo (MCMC)
To draw samples $(a_1,\beta_1), ..., (a_N, \beta_N)$ from the posterior density, gives $\rho_1,...,\rho_N$ from posterior for $\rho$ so that we can estimate the posterior on $\rho$ using  kernel density estimation. 
