# Conditioning of Linear Equation Systems

## Conditioning for Ax = b
Input $A,b$, output $x$

Assume $A_{n\times n}$ is non-singular (square matrix), suppose changing $b\rightarrow \hat b$, denote $\Delta b = b - \hat b$.   
Consider $\Delta x = x - \hat x$, where $A\hat x = \hat b$. Having $\frac{\|\Delta b\|}{\|b\|}$, WTF $\frac{\|\Delta x\|}{\|x\|}$

$$\|Ax\| = \frac{\|Ax\|\|x\|}{\|x\|} \leq \max_{x\neq 0}\frac{\|Ax\|\|x\|}{\|x\|} = \|A\|\|x\|$$

So that

$$\|b\| = \|Ax\| \leq \|A\|\|x\|$$

$$\|\Delta x\| = \|A^{-1}\Delta b\| \leq \|A^{-1}\|\|\Delta b\|$$

Then, using the two inequalities

$$\frac{\|\Delta x\|}{\|A\|\|x\|} \leq \frac{\|A^{-1}\|\|\Delta b\|}{\|A\|\|x\|} \leq \frac{\|A^{-1}\|\|\Delta b\|}{\|b\|}$$

$$\frac{\|\Delta x\|}{\|x\|} \leq \|A\|\|A^{-1}\|\frac{\|\Delta b\|}{\|b\|}$$

Define $\text{Cond}(A) = \|A\|\|A^{-1}\|$

Also, note that $\text{Cond}(A)^{-1} \frac{\|\Delta b\|}{\|b\|} < \frac{\|\Delta\|}{\|x\|} \leq \text{Cond}(A)\frac{\Delta b\|}{\|b\|}$  
And $\text{Cond}(A)^{-1} \leq \text{Cond}(A)\implies \text{Cond}(A)^2 \geq 1\implies \text{Cond}(A) \geq 1$

Also, noting that the __lemma__ is only true if the norm induced by vector norm 

__Theorem__ $\forall A\in \mathbb R^n \times \mathbb R^n. \text{Cond}(A) \geq 1$ (Another proof)

_proof_. $1 = \|I\| = \|A^{-1}A\| \leq \|A^{-1}\|\|A\| = \text{Cond}(A)$ by triangular inequality of the norm

__Theorem__ $\frac{\|\Delta x\|}{\|x\|} \leq \text{Cond}(A)\big(\frac{\|\Delta b\|}{\|b\|} + \frac{\|\Delta A\|}{\|A\|}\big)$

For $2\times 2$ matrices 

$$A = \begin{bmatrix} a&b\\c&d\end{bmatrix}, A^{-1} = \det(A)^{-1}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

### Example
Given $A = \begin{bmatrix}3&-1\\-2&1\end{bmatrix}$ with $\|\cdot\|_\infty$

Then, $A^{-1} = \begin{bmatrix}1&1\\2&3\end{bmatrix}$, $\|A\|_\infty = \max(3 + 1, 2 + 1)=4, \|A^{-1}\| = 5$  
Therefore, $\text{Cond}(A) = 4\times 5 = 20$, which is good-conditioning. 

Define $y:= A^{-1}x$ so that $x\neq 0 \Leftrightarrow y\neq 0$  

$$\|A^{-1}\| = \max \frac{\|A^{-1}x\|}{\|x\|} = \max\frac{\|y\|}{\|Ay\|} = \max (\frac{\|Ay\|}{\|y\|}^{-1}) = \min(\frac{\|Ax\|}{\|x\|})^{-1}$$

So that 

$$\|A\|\|A^{-1}\| = \frac{\max(\frac{\|Ax\|}{\|x\|})}{\min(\frac{\|Ax\|}{\|x\|})} = \frac{\max_{\|x\|=1}\|Ax\|}{\min_{\|x\|=1}\|Ax\|}$$

Is the ratio between how much $A$ expands $x$ and how much $A$ contracts $x$

## Properties of Conditioning Numbers
$\text{Cond}(A)\geq 1$

$\text{Cond}(I) = \|I\|\|I^{-1}\| = 1$

$\text{Cond}(\gamma A) = |\gamma|\|A\||\gamma^{-1}|\|A^{-1}\| = \text{Cond}(A)$

### Diagonal matrices
If $D$ is a diagonal matrix of $diag = \{d_1, d_2,...,d_n\}, di\neq 0$, then 

$$\text{Cond}_\infty(D) = \frac{\max(diag)}{\max(diag^{-1})} = \frac{\max(diag)}{\min(diag)}$$

### Near singular
If changing some elements of $A$ by $A+E$, then it will be singular.   

$$\frac{\|E\|}{\|A\|}\propto \text{Cond}(A)^{-1}$$

So that the larger conditioning number indicates that $A$ is closer to be near singular

$\det(A) = 0 \iff A$ is singular,  
If the $\det$ is small, then it may not be near singular ($\det(\gamma I) = \gamma$ can be arbitrarily small while still away from singular)

### Estimate matrix inverse 
Note that computing $A^{-1}$ requires $\sim n^3$ operations (by Gaussian elimination). To estimate $\|A^{-1}\|$ for computing $\text{Cond}(A)$

$$y=Az\implies z = A^{-1}y \implies \|z\| = \|A^{-1}y\| \leq \|A^{-1}\|\|y\|\implies \frac{\|z\|}{\|y\|} \leq \|A^{-1}\|$$

Therefore, choose a sequence of $z$'s to try to make $\frac{\|z\|}{\|y\|}$ as large as possible (iterative estimating)

### Rounding errors
Define $\Delta A = A - \hat A, \Delta b = b - \hat b$, then $\frac{\|\Delta A\|}{\|A\|}, \|\Delta b\| \approx \epsilon_{mach}$. Then 

$$\frac{\|x-\hat x\|}{\|x\|} \approx \text{Cond}(A)(2\epsilon_{mach})$$

Consider $Ax=b$ computed to get $\hat x$, define residual $r := b - A\hat x = b - \hat b = \Delta b$  
Define $\Delta x= x - \hat x$, then, 

$$\frac{\|\Delta x\|}{\|x\|} \leq \text{Cond}(A)\frac{\|r\|}{\|b\|}$$

Nearly all good linear equation solvers have small $\|r\|$ so it's only a matter of the conditioning number
