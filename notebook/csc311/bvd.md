# Bias-Variane Decomposition

## Loss function
A loss function $L(y,t)$ defines how bad it is if, for some example $x$, the algorithm predicts $y$, but the target is actually $t$

## Bias-Variance Decomposition
Suppose the training set $\mathcal D$ consists of $N$ pairs sampled IID from a sample generating distribution, i.e. $(x^{(i)}, t^{(i)})\sim p_{sample}$  
Let $p_{\mathcal D}$ denote the induced distribution over training set $i.e. \mathcal D\sim p_{\mathcal D}$ 

Pick a fixed query point $\vec x$, then consider an experiment where we sample lots of (say $m$ times) training datasets IID from $p_{\mathcal D}$

Then, we can produce $h_{k,\mathcal D}, k\in\{1,2,...,m\}$ and we compute each classifier's prediction $h_{k,\mathcal D}(\vec x) = y$ at the chosen query point $\vec x$

Therefore, $y$ is a random variable, i.e. $D\Rightarrow h_{\mathcal D}\Rightarrow h_{\mathcal D}(\vec x)=y, \mathcal D$ is randomly chosen.

### Basic setup
Assume $t$ is deterministic given $x$  
There is a distribution over the loss at $\vec x$, with $E_{\mathcal D\sim p_{\mathcal D}}(L(h_{\mathcal D}(x), t))$  
For each query point, the expected loss is different. We are interested in quantifying how well our classifier does over $p_{sample}$ average over training set $E_{\vec x\sim p_{sample}, \mathcal D\sim p_{\mathcal D}}(L(h_{\mathcal D}(\vec x), t))$  
Then, we can decompose the expected loss 

\begin{align*}
E_{x,D}[(h_D(x) - t)^2] &= E_{x,D}\bigg[\big(h_D(x) - E_D(h_D(x)\mid x) +E_D(h_D(x)\mid x)-t\big)^2\bigg]\\
&= \quad E_{x,D}\bigg[\big(h_D(x) - E_D(h_D(x)\mid x)\big)^2\bigg] \\
&\quad+2E_{x,D}\bigg[\big(h_D(x) - E_D(h_D(x)\mid x)\big)\big(E_D(h_D(x)\mid x)-t\big)\bigg]\\
&\quad + E_{x,D}\bigg[\big(E_D(h_D(x)\mid x)-t\big)^2\bigg]\\
&= E_x\bigg[E_D\big[\big(h_D(x) - E_D(h_D(x)\mid x)\big)^2 \\
&\qquad\quad +2E_D\bigg[\big(h_D(x) - E_D(h_D(x)\mid x)\big)\big(E_D(h_D(x)\mid x)-t\big)\mid x \bigg] &(*)\\
&\qquad\quad + \big(E_D(h_D(x)\mid x)-t\big)^2\mid x\big]\bigg]\\
&= E_{x,D}\bigg[\big(h_D(x)-E_D[h_D(x)\mid x]\big)^2\bigg] + E_{x}\bigg[\big(E_D[h_D(x)\mid x] -t\big)^2\bigg]\\
&= variance + bias
\end{align*}

\begin{align*}
(*) \quad &= (E_D(h_D(x)\mid x)-t\big)&\text{indep. of }D\\
&\qquad \times 2E_D\bigg[\mid x \bigg] & (**)\\
(**) &= E_{D,x}\big(h_D(x) - E_{D_x}[h_D(x)]\big) = 0\\
(*) &= 0
\end{align*}

__Bias__ defines on average, how close is the classifier to true target

__Variance__ defines how widely dispersed are the prediction as we generate new datasets

### Bayes Optimality
What if $t$ is not deterministic given $\vec x$, i.e. $p(t\mid \vec x)$. 

Since there is a distribution over targets, we measure distance from $y_*(x) = E(t\mid \vec x)$  

\begin{align*}
E[(y-t)^2 \mid \vec x] &= E(y^2\mid x) - 2E(yt\mid x) + E(t^2\mid x)\\
&= y^2 - 2yE(t\mid x) + E(t\mid x)^2 + var(t\mid x)\\
&= y^2 - 2yy_*(x) + y_*(x)^2 + var(t\mid x)\\
&=(y - y_*(\vec x))^2 + var[t\mid \vec x]
\end{align*}

The first term show that s $y=y_*(\vec x)$ is the minimized value  

__Bayes error / irreducible error__ The second term is the inherent unpredicatability, or noise, of the target. 

If $Var[t|x] = 0$, the algorithm is __Bayes optimal__. 

We can then decompose the non-deterministic form

\begin{align*}
E_{x,D,t|x}\bigg[(h_D(x) - t)^2\bigg] &= E_D\bigg[E_{x,t|x}\big[(h_D(x)-y)^2 \mid D\big]\bigg]\\
&= \quad E_{x,D}\big[(h_D(x) - E_t[t|x])^2\big] \\
&\quad\quad + E_{x,t|x}\big[(E_{t|x}[t|x] - t)^2\big]\\
&= \quad E_{x,D}\big[(h_D(x) - E_t[t|x])^2\big]  + E_x\big[var(t\mid x)\big]
\end{align*}

Hence we decompose out the __Bayes error__, where the first two terms are identical to the deterministic case, and will be decomposed into bias and variance

## Bagging
### Intuition
Suppose we sample $m$ indep. training set $D_i$ from $p_d$, we could then learn a predictor $h_i := h_{D_i}$ based on each one, then take the average $h = \sum^m h_i /m$ 

Bias unchanged

$$E_{D_1,...,D_m \sim p_d}h(x) = \frac{1}{m} \sum^m E_{D_i\sim p_{d}}h_i(x) = E_{D\sim p_d} h_D(x)$$

Variance becomes $1/m$ of the original 

$$var_{D_1,...,D_m}(h(x)) = \frac{1}{m^2}var_{D_i}(h_i(x)) = \frac{1}{m}var_D(h_D(x))$$

However, we don't such iid datasets from $p_d$

So we have to take a single dataset $D$ with $n$ examples  
Generate $m$ new datasets by sampling $n$ training examples from $D$, with replacement  
Average the predictions of models trained on each of these

### Problem with independence
Let correlation be $\rho$, the variance with correlated datasets is 

$$var(h(x)) = \frac{1}{m}(1-\rho)\sigma^2 + \rho\sigma^2$$

Ironically, introduce additional variability reduces correlation between samples  
 - invest a diversified portfolio, not just one stock
 - help to use average over multiple algorithms, or multiple configurations

## Example: Random Forests

When choose each node of the decision tree, choose a random set of $d$ features, and only consider splits on those features

The main idea is to improve the variance reduction of bagging by reducing the correlation between the trees

One of the example for black-box ML algorithm
