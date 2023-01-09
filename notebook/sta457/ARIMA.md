# Autoregressive Integrated Moving Average (ARIMA) model

## ARIMA
For nonstationary time series, applying difference operators repeatedly to the data $\{X_t\}$ until the differenced observations resemble a realization of some stationary process $\{W_t\}$

__ARIMA(p,q,d)__ $\{X_t\}$ is said to follow an ARIMA(p,q,d) model if $W_t = (1-B)^d X_t$ is stationary ARMA model. i.e. 

$$(1-B)^d \Phi(B)X_t = \Theta(B)a_t, a_t \sim NID(0,\sigma^2)$$

A series follows a stationary ARMA model after differencing $d$ times, i.e. $(1-B)^d X_t$, such process is called an $I(d)$ process. 

### Example
whether $(1-B)^2 X_y$ is stationary 

$(1-B)^2 X_t = X_t-2B X_t + B^2 X_t = X_t - 2X_{t-1}+X_{t-2}$

## Dickey Fuller unit root test
The DF test is used to test $I(1)$ processes.  
Consider $X_t = \phi X_{t-1} + a_t. a_t \sim NID(0,\sigma^2)$,  
then $\Delta X_t = (\phi - 1) X_{t-1} + a_t = \pi X_{t-1} + a_t$  
$H_0: \pi = 0, i.e. X_t\sim I(1)$

The general DF test may contain an intercept and a deterministic time trend as $\Delta X_t = a+\tau^T DR_t + \pi X_{t-1} + a_t$

## Augmented Dickey-Fuller test

Problems with basic DF  

 - The basic DF test considers only a single unit root
 - Correct model specification
     - correct specification of time trend and intercept
     - The DGP may contain both AR and MA terms 
     - There might be structural breaks in the data
   
ADF test equation

$$\Delta X_t = \tau^T DR_t + \pi X_{t-1}+\sum_{j=1}^k \gamma_j\Delta X_{t-j} + a_t$$

where $k=p-1$, the equation use the autoregression to take into account the presence of serial correlated errors. 

## Box-cov transformation
If the variance is not stationary, we can try stablize it with a Box Cox transformation, i.e. include $\lambda$ as one of the parameters 
$\Phi(B)(X_t^\lambda - \mu) = \Theta(B)a_t$, then choose $\lambda, \Phi, \Theta$ based on Minimized RMSE. 

