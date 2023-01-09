# Probabilistic Models

## Likelihood Function
The density of the observed data, as a function of parameters $\theta$. 

### Approaches to classification
__Discriminative approach__ estimate parameters of decision boundary / class separator directly from labeled examples

 - How do I separate the classes
 - learn $p(t|x)$ directly (logistic regression models)
 - learn mapping from inputs to classes
 
__Generative approach__ model the distribution of inputs characteristic of the class (Bayes classifier)

 - What does each class "look" like?
 - Build a model of $p(x|t)$
 - Apply Bayes rule

## Bayes Classifier
Given features $x = [x_1,...,x_D]^T$, we want to compute class probabilities using Bayes Rule:

$$p(c|x) = \frac{p(x,c)}{p(x)} = \frac{p(x|c)p(c)}{p(x)}$$

or by text 

$$\text{posterior} = \frac{\text{class likelihood} \times {\text{prior}}}{\text{Evidence}}$$

### Bayes Nets
We can represent this model using an __directed graphical model__, or __Bayesian network__. 

This graph structure means the joint distribution factorizes as a product of conditional distribution for each variable given its parent(s). 

Intuitively, you can think of the edges as reflecting a causal structure. But mathematically, this doesn't hold without additional assumptions. 

The parameters can be learned efficiently because the log-likelihood decomposes into independent terms for each feature. 

\begin{align*}
\mathcal l(\theta) &= \sum_{i=1}^N \log p(c^{(i)}, x^{(i)})\\
&= \sum_{i=1}^N \log\{p(x^{(i)}| c^{(i)})p(c^{(i)})\}\\
&= \sum_{i=1}^N \log\{p(c^{(i)}) \prod_{j=1}^D p(x_j^{(i)}| c^{(i)})\}\\
&= \sum_{i=1}^N \bigg[\log p(c^{(i)}) + \sum_{j=1}^D \log p(x_j^{(i)}|c^{(i)})\bigg]\\
&= \underset{\text{Bernoulli log-likelihood of labels}}{\sum_{i=1}^N \log p(c^{(i)})} + \underset{\text{Bernoulli log-likelihood for feature }x_j}{\sum_j^D\sum_i^N \log p(x_j^{(i)}|c^{(i)})}
\end{align*}

Each of these log-likelihood terms depends on different set of parameters, so they can be optimized independently. 

### Bayes Inference

$$p(c|x)\propto p(c)\prod_j^D p(x_j|c)$$

For input $x$, predict by comparing the values of $p(c)\prod_j^D p(x_j|c)$ for different $c$. 

## Bayesian Parameter Estimation
Bayesian approach treats the parameters as random variables. $\beta$ is the set of parameters in the prior distribution of $\theta$

To define a Bayesian model, we need to specify two distributions:  
__prior distribution__$p(\theta)$, which encodes our beliefs about the parameters __before__ we observe the data.  
__likelihood__, same as in MLE

When we update our beliefs based on the observations, we compute the __posterior distribution__ using Bayes' rule. 

$$p(\theta|\mathcal D) = \frac{p(\theta)p(\mathcal D|\theta)}{\int p(\theta')p(\mathcal D|\theta')d\theta'}$$


### Maximum A-Posteriori Estimation
Find the most likely parameter settings under the posterior

\begin{align*}
\hat{\boldsymbol{\theta}}_{\mathrm{MAP}}&=\arg \max _{\boldsymbol{\theta}} p(\boldsymbol{\theta} | \mathcal{D})\\
&=\arg \max _{\boldsymbol{\theta}} p(\boldsymbol{\theta}) p(\mathcal{D} | \boldsymbol{\theta}) \\
&=\arg \max _{\boldsymbol{\theta}} \log p(\boldsymbol{\theta})+\log p(\mathcal{D} | \boldsymbol{\theta})
\end{align*}

## Gaussian Discriminant Analysis (Gaussian Bayes Classifier)

Make decisions by comparing class posteriors. 


$$\log p\left(t_{k} | \mathbf{x}\right)=\log p\left(\mathbf{x} | t_{k}\right)+\log p\left(t_{k}\right)-\log p(\mathbf{x})$$

Expanded as 

\begin{align*}\log p\left(t_{k} | \mathbf{x}\right) =  &-\frac{d}{2} \log (2 \pi) -\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{k}^{-1}\right| \\
&-\frac{1}{2}\left(\mathbf{x}-\boldsymbol{\mu}_{k}\right)^{T} \boldsymbol{\Sigma}_{k}^{-1}\left(\mathbf{x}-\boldsymbol{\mu}_{k}\right) \\
&+\log p\left(t_{k}\right)-\log p(\mathbf{x})
\end{align*}

Decision Boundary 

\begin{align*}&\log p\left(t_{k} | \mathbf{x}\right)=\log p\left(t_{l} | \mathbf{x}\right) \\\Rightarrow &\left(\mathbf{x}-\boldsymbol{\mu}_{k}\right)^{T} \boldsymbol{\Sigma}_{k}^{-1}\left(\mathbf{x}-\boldsymbol{\mu}_{k}\right)=\left(\mathbf{x}-\boldsymbol{\mu}_{\ell}\right)^{T} \boldsymbol{\Sigma}_{\ell}^{-1}\left(\mathbf{x}-\boldsymbol{\mu}_{\ell}\right)+C_{k, l} \\\Rightarrow&\mathbf{x}^{T} \boldsymbol{\Sigma}_{k}^{-1} \mathbf{x}-2 \boldsymbol{\mu}_{k}^{T} \mathbf{\Sigma}_{k}^{-1} \mathbf{x}=\mathbf{x}^{T} \mathbf{\Sigma}_{\ell}^{-1} \mathbf{x}-2 \boldsymbol{\mu}_{\ell}^{T} \mathbf{\Sigma}_{\ell}^{-1} \mathbf{x}+C_{k, l}
\end{align*}

Decision Boundary is quadratic since gaussian is quadratic. When we have to humps that share the same covariance, the decision boundary is linear. 

### Properties of Gaussian Distribution
$\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Sigma})$ is defined as 

$$p(\mathbf{x})=\frac{1}{(2 \pi)^{d / 2}|\mathbf{\Sigma}|^{1 / 2}} \exp \left[-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{T} \mathbf{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right]$$

__Empirical Mean__ $\hat{\boldsymbol{\mu}}=\frac{1}{N} \sum_{i=1}^{N} \mathbf{x}^{(i)}$  
__Empirical Covariance__ $\hat{\mathbf{\Sigma}}=\frac{1}{N} \sum_{i=1}^{N}\left(\mathbf{x}^{(i)}-\hat{\boldsymbol{\mu}}\right)\left(\mathbf{x}^{(i)}-\hat{\boldsymbol{\mu}}\right)^{\top}$


### GDA vs.  Logistic Regression
- GDA is generative while LR is discriminative model. 
- GDA makes stringer modelling assumptions: assumes gaussian distributon. When assumption true, GDA asymptotically efficient. - - LR more robust, less sensitive to incorrect modelling assumptions (LR uses CE, no assumption.) 
- Class-conditional distributions usually lead to logistic classifier. 
