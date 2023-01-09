# Vector Series (VAR Models)

## Vector Auto-regression of order 1 VAR(1)

$$X_t = AX_{t-1}+a_t$$ 

where $A_{k\times k}$ is the coefficient matrix and $a_t$ is a K-dimensional white noise process with time-invariant positive definite covariance matrix $E(aa')=\Sigma$

We can repeatedly substitute the VAR(1) above to 

$$y_t = \sum A^i u_{t-i}$$

For the above VMA($\infty$) process to be stationary. $A^i$ must converge to zero, i.e. the all K eigenvalues of $A$ must be less than 1.

Then, the VAR(p) model is 

$$y_t = A_0 + \sum_1^p A_i y_{t-i} +a_t$$ 

OR the compact form 

$$A(B)y_t = a_t$$

Then, to be stationary, all the roots of $\det(I_k - A_1B-...-A_pB^p)=0$ are greater than 1 in absolute value. 

### Companion form
We can check the stability of a VAR(p) model using its companion form. 

$$\xi_t = A\xi_{t-1}+v_t$$ 

where $\xi_t = \begin{bmatrix} y_t \\ ... \\ y_{t-p+1} \end{bmatrix} , A = \begin{bmatrix}
        A_1 & A_2 & ... & A_{p-1} & A_p \\
        I & 0 & ... & 0 & 0 \\
        0 & I & ... & 0 & 0 \\
        ... & ... & ... & ... & ... \\
        0 & 0 & ... & I & 0
\end{bmatrix}, v_t = \begin{bmatrix} a_t \\ 0 \\...\\0\end{bmatrix}$

If the moduli of the eigenvalues of $A$ are less than 1, then the process is stable

### Example

$$
    \begin{bmatrix}y_1 \\y_2\end{bmatrix}_t
    = 
    \begin{bmatrix}5 \\ 10\end{bmatrix}
    + 
    \begin{bmatrix}0.5 &-0.2 \\-0.2 & -0.5\end{bmatrix}
    \begin{bmatrix}y_1 \\y_2\end{bmatrix}_{t-1} 
    + 
    \begin{bmatrix}0.3 &-0.7 \\-0.1 & 0.3\end{bmatrix}
    \begin{bmatrix}y_1 \\y_2\end{bmatrix}_{t-2} 
    +
    \begin{bmatrix}a_1 \\a_2\end{bmatrix}_t 
$$

Then, its companion matrix $A$ will be 

$$\begin{bmatrix}
        0.5 & 0.2 & -0.3 & -0.7 \\
        -0.2 & -0.5 & -0.1 & 0.3 \\
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0
\end{bmatrix}$$

## Order selection 
- sequential likelihood ratio tests of VAR(p) vs. VAR(p-1)
- BigVAR: dimension reduction methods for multi time series
