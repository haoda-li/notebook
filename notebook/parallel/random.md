# Randomized Algorithms

## Dimension reduce with Random sketching
Given a high dimensional dataset, wants to find an embedding to reduce into a lower dimensional one, while preserving some geometry, with high probability. 

More formally, An __embedding__ for a set $S\subseteq \mathbb R^n$ with __distortion__ $\epsilon$ is an $l\times m$ matrix $\Omega$ s.t. 

$$\forall x \in S. (1 - \epsilon) \|x\|^2 \leq \|\Omega x\|^2 \leq (1 + \epsilon)\|x\|^2$$

A subspace embedding is an embedding for a set $S$, where $S$ is a $m$-dimensional linear subspace. 

### Obvious subspace embedding
Intuitively, an obvious subspace embedding is a subspace embedding at most times. Formally, a random matrix $\Omega \in \mathbb R^{l\times m}$ is an __obvious subspace embedding__ with parameters $\text{OSE}(n, \epsilon, \delta)$ if with probability $\geq 1 - \delta$, $\Omega$ is a subspace embedding for $S$ with distortion $\epsilon$. 

A dense Gaussian matrix $\Omega \in \mathbb R^{l\times m}$ is a matrix whose entries are i.i.d. standard Gaussian random variables $\omega_{ij} \sim N(0, 1)$, multiplied by $l^{-1/2}$ where 

$$l = O(\epsilon^{-2}(n+ \log(\frac{1}{\epsilon})))$$

Then, such $\Omega$ is $\text{OSE}(n, \epsilon, \delta)$. Which means that we can sample some matrix $\Omega$, compute $I$ from OSE parameters, and do the embedding. 

The embedding is just a matrix matrix multiplication, thus the total parallelized cost is 

$$O(\gamma(2mnl / p) + \alpha(\lg p)) + \beta(ln \lg p)$$

### Fast Johnson-Lindenstrauss Transform
The goal is to find a sparse or structured $\Omega$, we compute a __subsampled random Hadamard transform__ (SRHT).

Given $m=2^q, l < m$, the SRHT ensemble embedding $\mathbb R^m$ into $\mathbb R^l$ is defined as 

$$\Omega = \sqrt{\frac{m}{l}} P H D$$

- $D\in \mathbb R^{m\times m}$ is a diagonal matrix whose diagonals are uniformly random signs $\pm 1$. 
- $H\in\mathbb{R}^{m\times m}$ is the __normalized Walsh-Hadamard transform__. 
- $P\in \mathbb{R}^{l\times m}$ is the random choose matrix to draw $l$ rows from $HD$. 

The __normalized Walsh-Hadamard transform__ is defined that for given $m=2^q$, define the (unnormalized) WH transform as

$$H_2 = \begin{bmatrix}1&1\\1&-1\end{bmatrix}, H_m = \begin{bmatrix}H_{m/2}&H_{m/2}\\H_{m/2}&-H_{m/2}\end{bmatrix}$$

and the normalization is $H = m^{-1/2}H_m$. 

SRHT is $\text{OSE}(n,\epsilon, \delta)$ with $l = O(\epsilon^{-2}(n+\lg \frac{m}{\delta}) ln \frac{n}{\delta})$. 

Note that because of the special structure of the matrix, the actual computation time is much reduced, the parallelized cost is 

$$O(\gamma(2mn\lg m / p) + \alpha(\lg p)) + \beta(mn \lg p)$$

## Problems using random sketching

### Least squares problems

Given $A\in\mathbb R^{m\times n}$ and $b\in\mathbb R^n$ with $n << m$$, aims to solve 

$$y:= \arg\min_{x\in\mathbb R^n} \|Ax - b\|_2$$

One (deterministic) approach for this problem is to do QR factorization on $A$, or we can solve by random sketching with $\Omega \in \mathbb R^{l\times m}$ 

$$y^* := \arg\min_{x\in\mathbb R^n}\|\Omega(Ax - b)\|_2$$

Can be shown that with probability $\delta$, we have 

$$\|Ay^* - b\|_2^2 \leq (1+O(\epsilon))\|Ay-b\|_2^2$$

### Low rank matrix approximation

For a matrix $A\in\mathbb R^{m\times n}$, decompose $A$ into lower rank approximations $Z\cdot W^T$ where $Z\in \mathbb R^{m\times k}, W^T \in \mathbb R^{k\times n}$. The low rank approximation is commonly used in many problems, as the number of flops is significantly reduced ($2mn$ vs. $2(m+n)k$). 

### Singular value decomposition

One of the most common way for matrix approximation $A = U\Lambda V^T$, a rank-$k$ approximation of $A$ takes the first $k$ singular vectors $A_k = U_k \Sigma_k V_k^T$ where $U_k\in\mathbb R^{m\times k}, V_k^T \in\mathbb R^{k\times n}$ is the first $k$ columns of $U, V$ respectively, $\Sigma_k\in\mathbb R^{k\times k}$ is the first $k$ singular values.

## Rank Revealing QR factorization

Given $A \in\mathbb R^{m\times n}$, consider the QR decomposition

$$A\Pi_c = QR = \begin{bmatrix}Q_1&Q_2\end{bmatrix} \begin{bmatrix}R_{11}&R_{12}\\&R_{22}\end{bmatrix}$$

where we choose $k$ and a column permutation $\Pi_c$ so that

- $R_{11} \in\mathbb R^{k\times k}$ is well-conditioned
- $\|R_{22}\|$ is small

Then, we can have a rank-$k$ approximation of $A_{qr}$ as 

$$A_{qr} = Q_1 \begin{bmatrix}R_{11}&R_{12}\end{bmatrix} \Pi_c^T = Q_1Q_1^T A =: \mathcal P^\circ A$$

and we have the error bound $\|A - A_{qr}\|_2 = \|R_{22}\|$, which is small by construction. 

### QR with column pivoting (QRCP)
Based on the desired construction, the algorithm is

```py title="QR with column pivoting"
def QRCP(A):
    m, n = A.shape
    Q = identity()
    colnorm = A.norm(axis=1) # column-wise norm of size n
    for j in range(n):
        p = argmax(colnorm) # the column with largest norm
        if colnorm[p] > eps:
            # pivoting: swap columns of A and colnorm
            A[:, j], A[:, p] = A[:, p], A[:, j]
            colnorm[j], colnorm[p] = colnorm[p], colnorm[j]
            # reduction: determine Householder matrix Hj
            Hj = Householder(A) # Hj @ A[j:, j] = +/- norm(A[j:, j]) @ e1
            # update
            A[j:, j+1:] = Hj @ A[j:, j+1:]
            colnorm[j+1:] = colnorm[j+1:] - A[j, j+1:] ** 2
            Q = Q @ Hj
        else:
            break
    return (Q, A) # Q = Hj * ... H1, R = A
```
