# Dimension Reduction - PCA and Auto Encoders

## Dimension Reduction
Loss some information (e.g. spread / $\sigma$) by projecting higher dimensions onto lower ones. IN practice, the important features can be accurately captured in a low dimensional subspace.

Let $\mathcal D = \{x^{(1)},...,x^{(N)}\}\subset \mathbb R^D$, so that $N$ instances will form matrix 

$$X = \begin{bmatrix}[\vec x^{(1)}]^T\\...\\ [\vec x^{(N)}]^T\end{bmatrix}$$

each row will be one observation of $D$ faetures,  
Let $x^{(i)}\sim N(\mu, \Sigma)$

### Projection onto a subspace
Given $\mathcal D, \hat\mu=N^{-1}\sum^N x^{(i)}$ be the sample mean.  

Want to find a $K <D $ dimensional subspace $S\subset \mathcal R^D$ s.t. $x^{(n)}-\hat\mu$ is "well represented" by a projection onto $K$-dimensional $S$. 

Where __projection__ is to find the closest point $\tilde x$ on $S$ s.t. $\|x-\tilde x\|$ is minimized. 

In a 2-dimensional problem, we are looking for direction $u_1$ along with the data is well-represented, such as direction of higher variance or the direction of min difference after projection, which turns to be the same. 

### Euclidean Projection

$\text{Proj}_S(x):=$ projection of $x$ on $S$. 

In 2D case, $S$ is the line along the unit vector $u$ (1-D subspace). $u$ is a basis for $S$. 

Since $x^Tu = \|x\|\|u\|\cos\theta =\|x\|\cos\theta$

$$\text{Proj}_S(x) = x^Tu\cdot u = \|\tilde x\|u$$

In K-D case, we have $K$ basis $u_1,...,u_K \in \mathcal R^D$. and the projection will be 

$$\text{Proj}_S(x) = \sum^K (x^Tu_i) u_i = \sum^K z_i u_i$$

#### Center data
Centering by subtract the mean $\hat\mu$. i.e. the mean (center) be the origin. We need to center the data since we don't want location of data to influence the calculations. 

#### Representation/code
Combine the two above together, we have 

$$\tilde x = \hat\mu + \text{Proj}_S(x-\hat\mu) = \hat\mu + \sum^K z_i \vec u_i$$

where $z_k = \vec u_k^T(x-\hat\mu)$  

Define matrix $U_{D\times K} = [\vec u_1, ..., \vec u_K]$, then
 
$$\vec z = U^T(x-\hat\mu), \tilde x = \hat\mu + U\vec z = \hat\mu + UU^T(x-\hat\mu)$$ 

We call $UU^T$ the projector on $S$, $U^TU = I$

Both $x,\tilde x\in \mathbb R^D$ but $\tilde x$ is a linear combination of vectors in a lower dimensional subspace with representation $\vec z \in \mathbb R^K$. 

We call $\tilde x$ __reconstruction__ of $x$, $\vec z$ be its representation(code). 

### Learning a Subspace

Since we will definitely lose partial information by dimension reduction, we want a good $D\times K$ matrix $U$ with orthonormal columns. 

To measure how "good" the subspace is, propose two criteria:

__Minimize reconstruction error__: find vectors in a subspace that are closest to data points 

$$\arg\min_U \frac 1 N \sum^N \|x^{(i)} - \tilde x^{(i)}\|^2$$

__Maximize variance of reconstructions__ find a subspace where data has the most variability

$$\arg\max_U \frac 1 N \sum^N \|\tilde x^{(i)} - \hat\mu\|^2$$

Noting that 

\begin{align*}
E(\tilde x) &= E(\hat\mu + UU^T(x-\hat\mu))\\
&= \hat\mu + UU^T(E(x)-\hat\mu)\\
&= \hat\mu + UU^T0\\
&= \hat\mu
\end{align*}

So that we can still use mean of $x$ to calculate variance of the reconstruciton

#### Equivalence of the criteria
__lemma1__ Norm of centered reconstruction is equal to norm of representation

\begin{align*}
\|\tilde x^{(i)} - \hat\mu\|^2 &= (U\vec z^{(i)})^T(U\vec z^{(i)})\\
&=  (\vec z^{(i)})^T U^TU\vec z^{(i)}\\
&= (\vec z^{(i)})^T\vec z^{(i)}&U^TU = I\\
&= \|z^{(i)}\|
\end{align*}

__lemma2__ $\tilde x^{(i)}-\hat\mu$ is orthogonal to $\tilde x^{(i)} - x^{(i)}$

\begin{align*}
(\tilde x^{(i)}-\hat\mu)^T(\tilde x^{(i)} - x^{(i)}) &= (\hat\mu+UU^T(x^{(i)}-\hat\mu)-\hat\mu)^T(\hat\mu+UU^T(x^{(i)}-\hat\mu) - x^{(i)})\\
&= (x^{(i)}-\hat\mu)^TUU^T(\hat\mu- x^{(i)}+UU^T(x^{(i)}-\hat\mu) )\\
&= (x^{(i)}-\hat\mu)^TUU^T(\hat\mu - x^{(i)}) + (x^{(i)}-\hat\mu)^TUU^TUU^T(x^{(i)}-\hat\mu))\\
&= (x^{(i)}-\hat\mu)^TUU^T(\hat\mu - x^{(i)}) + (x^{(i)}-\hat\mu)^TUU^T(x^{(i)}-\hat\mu))\\
&= 0
\end{align*}

__Proposition__ The two criteria is equivalent $\frac 1 N \sum^N\|x^{(i)}- \tilde x^{(i)}\|^2 = C - \frac1N\sum^N\|\tilde x^{(i)}-\hat\mu\|^2$

By lemma2, since the two vectors are orthogonal, by Pythagorean Theorem

\begin{align*}
\|\tilde x^{(i)} - \hat\mu\|^2 + \|x^{(i)} - \tilde x^{(i)}\|^2 &= \|x^{(i)}-\hat\mu\|^2\\
\frac1N\sum^N \|\tilde x^{(i)} - \hat\mu\|^2 + \frac1N\sum^N\|x^{(i)} - \tilde x^{(i)}\|^2 &= \frac1N\sum^N\|x^{(i)}-\hat\mu\|^2\\
\text{projected variance} + \text{reconstruction error} &= C
\end{align*}

## PCA

### Spectral Decomposition (Eigendecomposition)
If $A_{n\times n}$ is a symmetric matrix (so that has a full set of eigenvectors). Then, $\exists Q_{n\times n}, \Lambda_{n\times n}$ s.t. $A = Q\Lambda Q^T$ where $Q$ is orthogonal matrix formed by $n$ eigenvectors and $\Lambda$ is diagonal with $\lambda_1,...,\lambda_n$. 

Using Eigendecomposition on the __empirical convariance matrix__ $\hat\Sigma = \frac1N \sum^N (x^{(i)}-\hat\mu)(x^{(i)}-\hat\mu)^T$, the optimal PCA subspace is then spanned by some $K$ eigenvectors of $\hat\Sigma$

These eigencectors are called principal components, analogous to the principal axes of an ellipse. 

### Deriving PCA for K = 1

\begin{align*}
\frac 1N \sum^N\|\tilde x^{(i)} - \hat\mu\|^2 &= \frac1N\sum^N [z^{(i)}]^2\\
&= \frac1N\sum^N(u^T(x^{(i)}-\hat\mu))^2\\
&=  \frac1N\sum^Nu^T(x^{(i)}-\hat\mu)(x^{(i)}-\hat\mu)^Tu\\
&= u^T\bigg[\frac1N\sum^N(x^{(i)}-\hat\mu)(x^{(i)}-\hat\mu)^T\bigg]u\\
&= u^T\hat\Sigma u= u^TQ\Lambda Q^Tu=a^T\Lambda a= \sum^D\lambda_j a_j^2
\end{align*}

For the goal of maximize $\sum^D \lambda_j a_j^2, \vec a = Q^Tu$, noting that $\sum a_j = a^Ta = u^TQQ^Tu = u^Tu = 1$. Therefore, choosing the largest $\lambda_k$, 

$$\sum \lambda_ja_j^2 \leq \sum \lambda_k a_j^2 = \lambda_d\sum a_j^2 = \lambda_k$$

And such maximum can be obtained by setting $a_i = \mathbb I(i = k)$. Therefore, $\vec u = Q\vec a = q_k$

### Decorrelation
\begin{align*}
cov(\vec z) &= cov(U^T(x-\mu))\\
&= U^Tcov(x)U\\
&= U^TQ\Lambda Q^TU\\
&= [I_k, 0_{n-k}]\Lambda [I_k, 0_{n-k}]^T&\text{orthogonality}\\
&= \text{Top left } K\times K\text{ block of }\Lambda 
\end{align*}

## Autoencoder
An autoencoder is a feed-forward neural net to take input/target pair $(\vec x, \vec x)$. In such NN, we add a bottleneck layer to reduce the dimensionality so that the weights on such layer will be our code vector. 

The whole process goes through 

```
x => Encoder => Bottleneck(code_vector) => Decoder => x_estimated
```

By doing such, we learn abstract features in an unsupervised way, and can transfer to supervised tasks. 

### Linear autoencoders
If we use linear activations and squared error loss. Say we have 1 hidden layer of $k$ weights, so that $\tilde x = W_2W_1x, W_2:D\times K, W_1: K\times D$, then $W_2$ is the PCA subspace

### Nonlinear Autoencoder
If we use non-linear activations, then they can be more powerful for a given dimensionality, comparing to PCA (but also much more computational heavy in finding an optimal subspace).
