# Functions of Random Variable

## Change of Variable

__Theorem__ Let $X$ be a r.v. and $Y=g(X)$ where $g:\mathbb R\rightarrow\mathbb R$ is a funciton. Then

- $X$ is discrete, 
  
$$\text{pmf}_Y(y) = \sum_{x: g(x) = y} \text{pmf}_X(x)$$

- $X$ is continuous and $g$ is an appropriate transformation, 
  
$$\text{cdf}_Y(y) = \int_{x: g(x)\leq y}\text{pdf}_X(x)dx = P(\{x: g(x) \leq y\})$$

$$\text{pdf}_Y(y) = \frac{d}{dy} \text{cdf}_Y(y)$$

__Theorem__ Let $F(x) = \text{cdf}_X(x)$, then $F(X)\sim uniform(0, 1)$

_proof_. Let $Y=F(X)$, 

$$\text{cdf}_Y(y) = P(\{x:F(x) < y\}) = P(X \leq x) = F(x) = y$$

## Change of Single Variable
__Theorem (change of variable)__ Let $X$ be continuous r.v. and function $g$ be differentiable and injective. Then 

$$\text{pdf}_Y(y) = \text{pdf}_X(g^{-1}(y))|\frac{d}{dy}g^{-1}(y)|$$

_proof_. wlog assume $g$ is increasing (as a appropriate transformation function), then 
\begin{align*}
\text{pdf}_Y(y) &= \frac{d}{dy}\text{cdf}_Y(y)\\
&= \frac{d}{dy}\int_{-\infty}^{g^{-1}(y)} \text{pdf}_X(x)dx\\
&= \frac{d}{dy} \text{cdf}_X(g^{-1}(y)) \\
&= \text{pdf}_X(g^{-1}(y))|\frac{d}{dy}g^{-1}(y)|
\end{align*}

## Change of Variables for Multivariate Functions

__Theorem__ For discrete random variables $\mathbf X = (X_1,...,X_n)$, Let $\mathbf G:\mathbb R^n\rightarrow\mathbb R^m$ be the transformation s.t. $\mathbf Y = (Y_1,...,Y_m), \mathbf Y = \mathbf G(\mathbf X), Y_i = g_i(X_1, ..., X_n)$. Then

$$\text{pmf}_{\mathbf Y} = \sum_{\mathbf x: \mathbf G(\mathbf x) = \mathbf y}\text{pmf}_{\mathbf X}(\mathbf x)$$

random variables $X_1,...,X_n$ are said to be __independent and identically distributed (iid.)__ if $X_i$'s are independent and have the same distribution. 

### Example
the sum of independent Bernoulli trails follows binomial distribution. 

_proof_. Let $X_i \sim \text{Bern.}(p)$. $Y_n = \sum^n X_i$. We will prove by induction. 

Obviously $Y_1 = X_1 \sim \text{Bern.}(p)\equiv \text{binomial}(1, p)$

Assume $Y_k \sim \text{binomial}(k, p)$. Then

\begin{align*}
P(Y_{k+1} = 0) &= P(Y_k=0, X_{k+1} - 0) \\
&= P(Y_k = 0)P(X_{k+1}=0)\\
&= {k\choose 0}(1-p)^k (1-p) \\
&= {k+1\choose 0}(1-p)^{k+1}\\
P(Y_{k+1}=j) &= P((Y_k = j, X_{k+1} = 0)\cup (Y_k = j-1, X_{k+1} = 1))\\
&= P(Y_k = j)P(X_{k+1} = 0) + P(Y_k = j-1)P(X_{k+1} = 1)\\
&= {k\choose j}p^j(1-p)^{k-j}(1-p) + {k\choose j-1}p^{j-1}(1-p)^{k-(j-1)}p\\
&= {k+1\choose j}p^j(1-p)^{k+1-j}\\
Y_{k+1}&\sim \text{binomial} (k+1,p)
\end{align*}

### Theorem 
If $X,Y$ are independent continuous r.v. then 

$$\text{pdf}_{X+Y}(z) = \int \text{pdf}_X(x)\text{pdf}_Y(z-x)dx$$

_proof_. Let $Z=X+Y$

\begin{align*}
\text{cdf}_Z(z) &= P(X+Y \leq z)\\
&= P(X \leq x, Y \leq z-x)\\
&=P(X \leq x)P(Y \leq z-x)\\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{z-x}\text{pdf}_X(x)\text{pdf}_Y(y)dydx\\
&= \int_{-\infty}^{\infty} \text{pdf}_X(x) \text{cdf}_Y(z-x)dx\\
\text{pdf}_Z(z) &= \frac{d}{dz} \int_{-\infty}^{\infty} \text{pdf}_X(x) \text{cdf}_Y(z-x)dx\\
&= \int_{-\infty}^{\infty} \text{pdf}_X(x) \text{pdf}_Y(z-x)dx\\
\end{align*}

### Example
For $X_1,...,X_n$ iid, $Y_n = \max(X_1,...,X_n), Y_1 = \min(X_1,...,X_n)$. 

\begin{align*}
\text{cdf}_{Y_n}(y) &= P(\max(X_1,...,X_n) \leq y) \\
&= P(X_1 \leq y,...,X_n\leq y)\\
&= \prod^n P(X_i \leq y) \\
&= \text{cdf}_X(y)^n\\
\text{cdf}_{Y_1}(y) &= 1 - P(Y_1 > y)\\
&= 1 - P(\min(X_1,...,X_n) > y) \\
&= 1 - P(X_1 > y,...,X_n > y)\\
&= 1 - \prod^n P(X_i > y) \\
&= 1 - (1-\text{cdf}_X(y))^n\\
\text{cdf}_{Y_1,Y_n}(y_1,y_2)&= P(Y_1\leq y_1, Y_2\leq y2)\\
&= P(y_2\leq y_2) - P(Y_1 > y_1, Y_2\leq y_2)\\
&= \text{cdf}_X(y_2)^n - \prod^n P(y_1 < X_i \leq y_2)\\
&= \text{cdf}_X(y_2)^n - (\text{cdf}_X(y_2) - \text{cdf}_X(y_1))^n
\end{align*}

### Theorem (change of variables)
For random variables $\mathbf X = (X_1,...,X_n)$, Let $\mathbf G:\mathbb R^n\rightarrow\mathbb R^m$ be the transformation s.t. $\mathbf Y = (Y_1,...,Y_m), \mathbf Y = \mathbf G(\mathbf X), Y_i = g_i(X_1, ..., X_n)$. IF $\mathbf G$ is injective and differentiable, then

$$\text{pdf}_{\mathbf Y}(\mathbf y) = \text{pdf}_{\mathbf X}(\mathbf G^{-1}(\mathbf y))|\det(\frac{D}{D\mathbf y}\mathbf G^{-1}(\mathbf y))|$$
