# Norms of vectors and matrices

## Norms

Consider a linear system $Ax = b$ where $A,b$ are input.  

To measure the conditioning we measure the norm of output 

$$\begin{cases}
|x|&\in\mathbb R\\
\sqrt{a^2+b^2} &\in \mathbb C, a+bi\\
\sqrt{\sum^n x_i^2} = \|x\|_2 &x\in\mathbb R^n
\end{cases}$$

__Claim__ $\|x\|_\infty \leq \|x\|_2\leq \sqrt n \|x\|_\infty$  
_proof_. 

$$\|x\|_\infty = \sup|x_i| = |x_k| = \sqrt{x_k^2} \leq \sqrt{\sum x_i^2} = \|x\|_2$$

$$\|x\|_2 =\sqrt{\sum x_i^2} \leq \sqrt{\sum x_k^2} = \sqrt n \sqrt{x_k^2} = \sqrt n k = \sqrt n \|x\|_\infty$$

__Claim__ reverse triangular inequality $|\|x\| - \|y\|| \leq \|x-y\|$  

$$\|x\| - \|y\| = \|y + x -y\| - \|y\|\leq \|y\| + \|x - y\| - \|y\| = \|x-y\|$$

## Norm for matrices
One common way to get a matrix norm is from a vector norm $\|A\| = \max_{x\neq 0} \frac{\|A\vec x\|}{\|\vec x\|}$, i.e. how much $A$ can expand $\vec x$.   

__Theorem__ $\|A\| = \max_{x\neq 0} \frac{\|Ax\|}{\|x\|} = \max_{\|x\|=1} \|Ax\|$

_proof_. 

$$\max_{x\neq 0} \frac{\|Ax\|}{\|x\|} = \max\frac{\|A(x/\|x\|)\|}{\|x\|/\|x\|} = \max_{\|x\|=1}\|Ax\|$$

Matrix norm is __induced by / subordinate to__ the vector norm, 

__Examples__ Given $A_{n\times n}$ 

$$\|A\|_1 = \max \frac{\|Ax\|_1}{\|x\|_1} = \max_{j = 1...n} \sum_{i=1}^n |A_{ij}| = \text{max column sum}$$

$$\|A\|_\infty = \max_{i = 1 ... n} \sum_{j=1}^n |A_{ij}| = \text{max row sum}$$ 

$$\|A\|_2 = \max\{\sqrt \lambda\| \lambda := \text{eigenvalues of }A^TA\}$$

$$\|A\|_F = \sqrt {\sum_i\sum_j |a_{ij}|^2}$$

Note that F-norm cannot be induced by vector norm. For example $\|I\|_F = \sqrt n $   

If a norm is subordinated from a vector norm, then 
 - it follows triangular inequality  
 - $\|I\| = \max \frac{\|Ix\|}{\|x\|} = 1$

## Norm Equivalence

For any vector and matrix norms $\|\cdot\|_a, \|\cdot\|_b$,  

$$\forall n\in\mathbb Z^+. \exists c_{1, n}, c_{2, n} > 0. \forall x\in \mathbb R^n . c_{1, n}\|x\|_a \leq \|x\|_b \leq c_{2, n} \|x\|_a$$
