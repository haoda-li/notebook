# Granger Causality and Co-integration

## Granger causality

Consider a VAR(p) model of 2-d variables, i.e. $y_t = [y_{i,t},  y_{2,t}]^T$
$y_t = A_0 + \sum_1^p A_i y_{t-i} + a_t$, 
and each $A_i = \begin{bmatrix}\phi_{i,11}&\phi_{i,12}\\\phi_{i,21}&\phi_{i,22}\end{bmatrix}$

Then, if $y_{2,t}$ does not Granger cause $y_{1,t}$, then all $\phi_{i, 12} = 0$ since it will only be contributing to the equation of $y_{1,t}$

Similarly, if $y_{1,t}$ does not Granger cause $y_{2,t}$, then all of $\phi_{i,21}=0$

### Portmanteau test
Let $X_t, Y_t$ be causal and invertible univariate ARMA processes and be given by 

$$\Phi_1(B)(X_{1,t}-\mu_1)=\Theta_1(B)a_{1,t}$$

$$\Phi_2(B)(X_{2,t}-\mu_2)=\Theta_2(B)a_{2,t}$$

The cross-correlation 

$$\rho_{X_1X_2}(k) = \frac{E(a_{1,t}, a_{2,t+k})}{\sqrt{\sigma_1^2\sigma_2^2}}$$

If $\rho(k)=0$ for $k<0$, then $X_2$ does not cause $X_1$

## Cointegration
__I(d) process__ For a time series $X_t$

 - A stationary and invertible time series is said to be an I(0) process
 - A time series is said to be an integrated process of order one, i.e. I(1) process, if $(1-B)X_t$ is stationary and invertible. 
 - I(d) process, if $(1-B)^d X_t$ is stationary and invertible, $d>0$ and order $d$ is referred to as the order of integration or the multiplicity of a unit root. 

Consider a multi time series $X_t$. If $\forall i, X_{i,t}$ are I(1) but a nontrivial linear combination $\beta'X_t$ is I(0), then $X_t$ is said to be cointegrated of order one and the linear combination vector $\beta$ is called a cointegrating vector. 

## Granger Representation Theorem
$X_t, Y_t$ are cointegrated, IFF exists an ECM representation. 

### Implications

1. Vector autoregression on differenced I(1) processes will be a misspecification if the component series are cointegrated
2. An equilibrium specification is missing from a VAR representation
3. When lagged disequilibrium terms are included as explanatory variables, the model becomes well specified
4. Such as model is called an error correction model because the model is structured so that short-rum deviation from the long-run equilibrium will be corrected. 
