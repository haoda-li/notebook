# Statistical Models

## Statistical Models
Assume that the data $x_1,...,x_n$ are outcomes of r.v. $X_1,...,X_n \sim F$, which assumes to be unknown. 

A __statistical model__ is a family $\mathcal F$ of probability distributions of $(X_1,...,X_n)$. 

Theoretically, $F\in \mathcal F$ but in practice this is not always true, we are to find some $F_0 \in \mathcal F$ close enough to $F$ so that $\mathcal F$ is useful. 

### Parametric models

For a given $\mathcal F$, we can parametrize as $\mathcal F = \{F_\theta:\theta \in \Theta\}$

If $\Theta \subset \mathbb R^p$ then $\mathcal F$ is a __parametric model__ and $\theta \in \mathbb R^p = (\theta_1,...,\theta_p)$

### Non-parametric models

If $\Theta$ is not finite dimensional then the model is said to be __non-parametric__ (in this case, $\in\mathbb R^\infty$)

__Example__ $g(x)\approx \sum^p \beta_k \phi_k(x)$ for some functions $\phi_1,...,\phi_p$ and unknown parameters $\beta_1,...,\beta_p$

### Semi-parametric models
Non-parametric models often have a finite dimensional parametric component. 

__Example__ $Y_i = g(x_i) + \epsilon_i$ with $\{\epsilon_i\}$ iid. $N(0,\sigma^2)$ and $g,\sigma^2$ are unknown

### Example

Consider the linear regression $Y_i = \beta_0 + \beta_1x_i + \epsilon_i$ for observations $(x_1,Y_1), ..., (x_n, Y_n)$ where $\epsilon_i \sim N(0,\sigma^2)$ iid.  Such model is parametric model. 

However, if relax the assumption to $E(\epsilon_i) = 0, E(\epsilon_i^2) = \sigma^2$, then this will be semi-parametric model. 

### Example 
Let $X_1,...,X_n$ be iid. Exponential r.v. representing survival times.  

$$f(x;\lambda) = \lambda e^{-\lambda x}\mathbb I(x\geq 0)$$

$\lambda >0$ is unknown

Let $C_1,...,C_n$ be independent with unknown cdf $G$ (or cdfs $G_i$)  

Observe $Z_i = \min(X_i, C_i), \delta_i = \mathbb I(X_i\leq C_i)$

parameters $\lambda, G$ so that semi-parametric model.

## Bayesian models

Assume a parametric model with $\Theta \subset \mathbb R^p$, for each $\theta \in \Theta$, think of the join cdf $F_\theta$ as the conditional distribution of $\mathcal X$ given $\theta$. 

__Bayesian inference__ put a probability distribution on $\Theta$, i.e. a prior. 

After observing $x_1,...,x_n$, we can use Bayes Theorem to obtain a __posterior distribution__ of $\theta$ given $X_1 = x_1,...,X_n = x_n$

## Statistical Functionals

To estimate the characteristics of a model $F$, we often consider $\theta(F)$, i.e. a mapping $\theta: \mathcal F\rightarrow \mathbb R$

### Examples
$\theta(F) = \mathbb E_F(X_i)= \mathbb E_F(h(X_i))$  
$\theta(F) = F^{-1}(\tau)$ quantiles  
$\theta(F) = \mathbb E_F\big[\frac{X_i}{\mu(F)}\ln(\frac{X_i}{\mu(F)})\big], P(X_i > 0 ) = 1, \mu(F) = \mathbb E_F(X_i)$ Theil index

## Substitution principle 
First estimate $F\rightarrow \hat F$ and substitute $\hat F$ into $\theta (\hat F)$  
__If $\theta$ is continuous__, Using continuous mapping theorem, $\theta(\hat F) \approx \theta(F)$

__Example__ empirical distribution function (edf)  

$$\hat F(x) = \frac{1}{n} \sum^n \mathbb I(X_i \leq x) = \text{proportion of observations } \leq x$$

Note that the edf is just a sample mean and WLLN, CLT holds, for each $\mathbb I(X_i \leq x)$ is iid. Bernoulli

Therefore, 

 - $E(\hat F(x)) = F(x), var(\hat F(x)) = \frac{F(x)(1-F(x))}{n}$  
 - __WLLN__ $\hat F(x) = \hat F_n(x) \rightarrow^p F(x), \forall x$  
 - __CLT__ $\sqrt n(\hat F_n(x)-F(x))\rightarrow^f N(0, F(x)(1-F(x)))$
