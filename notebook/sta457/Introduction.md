# Introduction

## Stochastic Process
A family of time indexed r.v. $Z(w,t)$ where $w$ belongs to a sample space and $t$ belongs to an index set. 

For a fixed $t$, $Z(w,t)$ is a r.v.  
For a given $w$, $Z(w,t)$ is a function of $t$, and is __sample function or realization__.

## Strongly stationary 
Consider a finite set of r.v. $\{Z_{t_1},...,Z_{t_n}\}$ from a stochastic process $\{Z(w,t): t=0,\pm 1, \pm 2, ...\}$. The n-dimensional distribution function is defined by 

$$F_{Z_{t_1},...,Z_{t_n}}(x_1,...,x_n) = P\{w:Z_{t_1}\leq x_1,...,Z_{t_n}\leq x_n\}$$

A process is __strictly stationary__ if 

$$F_{Z_{t_1},...,Z_{t_k}}(x_1,...,x_n) = F_{Z_{t_1+k},...,Z_{t_k+k}}(x_1,...,x_n)$$

for any set of $\{Z_{t_1},...,Z_{t_n}\}$

## Auto-covariance Function
$\gamma_X(r,s) = cov(X_r, X_s)$  
$\rho(r,s) = \gamma_X(r,s)/\sqrt{var(X_r)var(X_s)}$ Auto-correlation function (ACF)

## Cross-covariance Function
$\gamma_{XY}(r,s)=cov(X_r, Y_s)$  
$\rho_{XY}(r,s) = \gamma_{XY}(r,s)/\sqrt{var(X_r)var(Y_s)}$


## Weakly stationary
The time series $\{X_t, t\in \mathbb{Z}\}$ is said to be stationary if 

- $var(X_t)=z<\infty$ for all $t\in Z$  
- $E(X_t) = m$ for all $t\in Z$
- $y_X(r,s) = y_X(t+r, t+s)$ for all $t,r,s\in Z$  

the covariance being functions of the time difference alone. 

## Classical decomposition model
decompose a time series into 

 - trend: loosely defined as "long-term change in the mean level"
 - seasonal variation: exhibit variation that is annual in period.
 - cyclic variation: exhibit variation at a fixed period due to some other cause. 
 - irregular fluctuations

## Steps to time series modeling

 - plot the time series and check for trend, seasonal and other cyclic components, any apparent sharp changes in behavior, as well as any outlying observations. 
 - remove trend and seasonal components to get residuals
 - choose a model to fit residuals
 - forecasting can be carried out by forecasting residual and then inverting the transformation carried out in step 2. 

## Sample autocorrelation functions (SACF)
$\hat\gamma(h)=n^{-1}\sum_{t=1}^{n-h} (x_{t+h}-\bar x)(x_t - \bar x)$  
$\hat\rho(h) = \hat\gamma(h)/\hat\gamma(0)$

For a random time series, $\hat\rho_k \sim N(0, 1/n)$ for $k\neq 0, n$ is the length of time series. Thus, if a time series is random, we can expect 19/20 of $\hat\rho_k$ to lie in $[-2/\sqrt n, 2/\sqrt n]$

## Test Zero cross-correlation
$H_0:\forall h. \rho_x(h)=\rho_y(h) = 0 \land \rho_{xy}(h) = 0$  
Both $X_t, Y_t$ contain no serial correlation and are mutually independent. 

Test statistic: $\hat\rho_{xy}(h)\sim N(0, 1/n)$


