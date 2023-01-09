# Sampling

A sample from a distribution $p(x)$ is a single realization $x$ whose probability distribution is $p(x)$. Here, $x$ can be high-dimensional or simply real valued.

The main objectives of sampling methods is to 

- Generate random samples $\{x^{(r)}\}^N_{r=1}$ from a given probability distribution $p(x)$. 
- To estimate expectations of functions $\phi(x)$, under the distribution $p(x)$
  
    $$\Phi = E_{x\sim p(x)} [\phi(x)] = \int \phi(x)p(x)dx$$

For example, we are interested in the mean of some function $f$, under distribution $p(x)$. Then we have 

$$\Phi = E_{x\sim p(x)} [f(x)] $$

## Simple Monte Carlo

For the expectation $\Phi = E_{x\sim p(x)} [\phi(x)] = \int \phi(x)p(x)dx$, we can estimate the integral by Monte Carlo integration, i.e. generate $R$ samples $\{x^{(r)}\}_{r=1}^R$ from $p(x)$, and taking average

$$\Phi = E_{x\sim p(x)} [\phi(x)] = \int \phi(x)p(x)dx = R^{-1}\sum_{r=1}^R \phi(x^{(r)}) := \hat\Phi$$


### Properties of Simple Monte Carlo

__Claim 1__ $\hat\Phi$ is a consistent estimator of $\Phi$. 

_proof_. Directly from LLN. 

__Claim 2__ $\hat\Phi$ is a unbiased estimator of $\Phi$.  
_proof_. 

\begin{align*}
E(\hat \Phi) &= R^{-1}\sum_{r=1}^R E(\phi(x^{(r)}))\\
&= \frac{R}{R} E_{x\sim p(x)}(\phi(x))\\
&= \Phi
\end{align*}

__Claim 3__ The variance of $\hat\Phi$ decreases with rate $1/R$.  

_proof_. By consistency and unbiaseness

$$var(\hat\Phi) = \frac{1}{R^2}\sum_{r=1}^R var(\phi(x^{(r)})) = R^{-1}var(\phi(x))$$

### Normalizing Constant
Given an arbitrary continuous, positive function $f: \mathbb R^n \rightarrow \mathbb R$ and the function is integrable over $\mathbb R^n$. Say, $\int_{\mathbb R^n} f(\mathbf x)d\mathbf x=Z$. Then, we can have a density 

$$p(\mathbf x) = \frac{f(\mathbf x)}{Z}$$

However, the normalizer $Z$, in many cases, requires computing a high-dim integral, which is computationally intractable (exponential to the dimension). Also, drawing samples from $p(\mathbf x)$ is a challenge, especially in high-dim spaces. 

## Importance Sampling

__Importance__ sampling is a method for estimating the expectation of a function $\phi$. 

Suppose that we wish to draw samples from $\tilde p(x)$ by

$$p(x)=\frac{\tilde p(x)}{Z_p}$$

And we have a simpler density $q(x)$ which is easy to sample from and easy to evaluate up to normalizing constant 

$$q(x) = \frac{\tilde q(x)}{Z_q}$$

In importance sampling,  we first generate $R$ samples from $q(x)$. 

$$\{x^{(r)}\}_1^R \sim q(x)$$

Then we have an estimate of $\phi$ over density $q(x)$ as

$$\Phi = E_{x\sim q(x)}[\phi(x)] = R^{-1}\sum_{r=1}^R \phi(x^{(r)}):=\hat\Phi$$

The only problem is that the this is an estimation over $q$. However, notice that at values of $x$, we can represents $\tilde p$ with a weights function $\tilde p(x) = \tilde w(x)\tilde q(x)$, since we know $\tilde p(x), \tilde q(x)$ over their domain. 

Then, note that for our sampled points we have $\tilde p(x^{(r)}) = \tilde w(x^{(r)})\tilde q(x^{(r)})$, which 

$$R^{-1}\sum_{r=1}^R \tilde w(x^{(r)}) = E_{x\sim q(x)}[\frac{\tilde p(x^{(r)}}{\tilde q(x^{(r)})}] = \int \frac{\tilde p(x^{(r)}}{\tilde q(x^{(r)})}q(x)dx = \frac{Z_p}{Z_q}$$

and thus for our estimator under $p$ from estimator under $q$ is

\begin{align*}
\Phi &= \int\phi(x)p(x)dx\\ 
&= \int \phi(x)w(x)p(x)dx \\
&\approx R^{-1}\sum_{r=1}^R \phi(x^{(r)})w(x^{(r)})\\
&= \approx R^{-1}\sum_{r=1}^R \phi(x^{(r)})\frac{\tilde p(x^{(r)})/Z_p}{{\tilde q(x^{(r)})/Z_q}}\\
&= \frac{Z_q}{Z_p}R^{-1} \sum_{r=1}^R\phi(x^{(r)})\tilde w(x^{(r)})\\
&\approx (R^{-1}\sum_{r=1}^R \tilde w(x^{(r)}))^{-1}R^{-1}\sum_{r=1}^R\phi(x^{(r)})\tilde w(x^{(r)})\\
&=\sum_{r=1}^R\phi(x^{(r)})\frac{\tilde w(x^{(r)})}{\sum_{r=1}^R \tilde w(x^{(r)})}=:\hat\Phi_{iw}
\end{align*}

## Rejection Sampling
Another sampling method is rejection sampling. For a given $\tilde p(x)$, we find a simpler proposal density $q(x)$ and which $\tilde q(x) = Z_q q(x)$. 

Then, we further assume that we have some constant $c_0$ s.t. $c_0\tilde q(x) >\tilde p(x). \forall x\in\mathcal S$.  
The idea is that we have a simpler density $q$, such that the scaled $\tilde q$ is above to cage (over-estimate) $p$ for all input $x$, so that we can reject part of the samples. 

First, we generate a sample $x ~ q(x)$ and $u\sim \text{Uniform}[0, c\tilde q(x)]$. Then, if $u > \tilde p(x)$, then $x$ is outside of $\tilde p$ so we reject such $x$. Otherwise, we accept $x$ into $\{x^{(r)}\}$. 

__Claim__ rejection sampling samples $x\sim p(x)$. 

_proof_. Consider our sampling method, we have $x\sim q(x), u|x \sim \text{Uniform}[0, c\tilde q(x)]$, and $x$ is accepted is conditional on $u \leq \tilde p(x)$. Thus, consider the probability over any set $A\subseteq \mathcal S$. 
First note that the probability

$$P_{x\sim p}(x\in A) = \int_A p(x)dx = \int\mathbb I(x\in A)p(x)dx = E_{x\sim p}[\mathbb{I}(x\in A)]$$

Thus,

\begin{align*}
P_{x\sim p}(x\in A \mid u\leq \tilde p(x)) &= \frac{p_{x\sim p}(x\in A, u\leq \tilde p(x))}{E_{x\sim q}p(u\leq \tilde p(x) | x)}\\
&= \frac{ E_{x\sim q}[\mathbb I(x\in A) P(u\leq \tilde p(x)|x)]}{E_{x\sim q}[\frac{\tilde p(x)}{c\tilde q(x)}]}\\
&= \frac{E_{x\sim q}[\mathbb I(x\in A)\frac{\tilde p(x)}{c\tilde q(x)}]}{Z_p/cZ_q}\\
&= P_{x\sim p}(x\in A)\frac{Z_p}{cZ_q} / \frac{Z_p}{cZ_q}\\
&= P_{x\sim p}(x\in A)
\end{align*}

### Curse of Dimension
Note that in high dimensions, a caging over some function will be very hard. Therefore, $c$ will be huge and the acceptance rate $\frac{Z_p}{cZ_q}$ will be exponentially reduced with increased dimensionality. 

## Metropolis-Hastings Algorithm

Importance sampling and rejection sampling work well only if the $q\sim p$. However, such $q$ is very hard to find in high dimensions. Instead, we could make use of a proposal density $q$ which depends on the current state $x^{(t)}$. 

Given some function $\tilde p(x)$ and a proposal conditional density $q(x_t|x_{t-1})$. The procedure is

1. Generate a new state $x'$ from the proposal density $q(x'|x^{(t)})$. 
2. Compute acceptance probability
   
$$a = \min(1, \frac{\tilde p(x')q(x^{(t)}|x')}{\tilde p(x^{(t)})q(x'|x^{(t)})})$$

   the new state $x'$ is accepted with probability $a$
3. If accepted, then $x^{(t+1)} = x'$, otherwise $x^{(t+1)} = x^{(t)}$
