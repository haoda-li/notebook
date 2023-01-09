# Summary Sheet

## ARMA model forecast

$$(1-0.5B)(Z_t - 3) = a_t$$

Let $X_t = Z_t - 3$, then $(1-0.5B)X_t = a_t\sim AR(1)$. And because the root $B=2$ lies outside of the unit circle, the series is stationary. Rewrite as a $MA(\infty)$

$$(1-0.5B)(1+\psi_1B + \psi_2B^2 + ...) = 1$$

$\psi_1 = 1/2$  
$\psi_2 = 1/4$  
$\psi_k = 2^{-k}$

Then, $\hat X_t(1) = \sum_{0}^\infty 2^{-(i+l)}a_{t-i}, \hat Z_t(l) = 3 + \hat X_t(l)$

$e_t(l)=\sum_{i=0}^{l-1} \psi_i a_{t+l-i}$,  
then $var(e_t(l)) = \sum_{i=0}^{l-1} \psi_i^2 a_{t+l-i}^2 = \sigma^2 \sum_0^{l-1}\psi_i^2$

$$(1-B+0.25B^2)(Z_t-1)=a_t$$

Let $X_t = Z_t -1$, $(0.25B^2 - B + 1)=(0.5B-1)^2 \Rightarrow B=2$ is a stationary $AR(2)$ model. 

$X_t = X_{t-1}+\frac{1}{4}X_{t-2} + a_t$, then  
$\hat Z_t(1) = 1+X_t + \frac{1}{4} X_{t-1}$  
$\hat Z_t(2) =1+ X_t + \frac{1}{4} X_{t-1}+ \frac{1}{4} X_t=\frac{5}{4}X_t + \frac{1}{4} X_{t-1}$  
$\hat Z_t(3) = 1+\frac{5}{4} X_t + \frac{1}{4} X_{t-1}+ \frac{1}{4}(X_t+\frac{1}{4}X_{t-1})=\frac{3}{2}X_t + \frac{5}{16}X_{t-1}$
$\hat Z_t(4) = 1+\frac{3}{2}X_t + \frac{5}{16}X_{t-1}+\frac{5}{16}X_t + \frac{1}{16}X_{t-1} = \frac{29}{16}X_{t}+\frac{3}{8}X_{t-1}$

$(1-B+0.25B^2)(1+\psi_1B+\psi_2B^2+...) = 1$  
$\psi_1 -1 = 0\Rightarrow \psi_1 = 1$  
$\psi_2 -\psi_1 +0.25 = 0\Rightarrow \psi_2 = 0.75$  
$\psi_3 -\psi_2 +0.25\psi_1 = 0\Rightarrow \psi_3 = 0.5$

Therefore,   
$var(e_t(1)) = \sigma^2$  
$var(e_t(2)) = 2\sigma^2$  
$var(e_t(3)) = \frac{41}{16}\sigma^2$

$$(1-B+0.25B^2)(Z_t + 3) = (1+0.25B)a_t$$

All B lies out of the unit circle, it's a stationary and invertible ARMA(2,1) model. 

$(1-B+0.25B^2)(1+\psi_1B+\psi_2B^2 + ...) = 1+0.25B$  
$\psi_1 = 0.25+1=1.25$  
$\psi_2 = \psi_1 = 1.25$  
$\psi_3 = \psi_2 -0.25\psi_1 = \frac{15}{16}$  
$\psi_4 = \psi_3 - 0.25\psi_2 = \frac{5}{8}$  
$\psi_5 = \psi_4 - 0.25\psi_3 = \frac{25}{64}$

$var(e_t(1)) = \sigma^2$  
$var(e_t(2)) = \frac{41}{16}\sigma^2$  
$var(e_t(3)) = \frac{33}{8}\sigma^2$


## TFN
Consider a dynamic regression model $y_t = \sum_0^k v_i x_{t-i}+n_t$
where both $x_t, n_t$ are stationary and invertible ARMA model given by $\phi_x(B)x_t = \theta(B)a_t, \phi_n(B)n_t = \theta_n(B)e_t$ and $cov(e_t,a_s)= 0$

__state the prewhitening process for how to identify the value of k__

Apply $\phi_x(B)/\theta(B)$ on the regression model, we get 

$$\frac{\phi_x(B)}{\theta(B)}y_t = \sum_0^k v_i \frac{\phi_x(B)}{\theta(B)} x_{t-i} + \frac{\phi_x(B)}{\theta(B)} n_t$$  

$$\hat y_t = v(B)a_t + \epsilon_t$$

By having $\phi_n(B)=\phi_x(B), \theta_n(B)=\theta(B)$, we have $\epsilon \sim e$ so that 

$$\hat y_t = v(B)a_t + e_t$$ 

then, multiply both sides by $a_{t-k}$ and take expectations

$$E(\hat y_t a_{t-k}) = v(B) E(a_t a_{t-k}) + E(e_t a_{t-k})$$

$$cov(\hat y_t, a_{t-k}) = v_k\sigma_a^2$$

$$v_k = cov(\hat y_t, a_{t-k}) / \sigma_a^2 = corr(\hat y_t, a_{t-k})\frac{se(\hat y_t)}{se(a_t)}\propto corr(\hat y_t, a_{t-k})$$

Therefore, we can test the statistical significance of $v_k$ by examining the statistical significance of $corr(\hat y_t, a_{t-k})$

__state the steps of using Box-Tiao transformation to estimate $v_j$__

The steps of the estimation procedures

1. Run the OLS regression on $y_t = \sum_{j=1}^s v_j x_{t-j} + e_t$ to collect the residuals $\{\hat e_t\}$
2. Identify an ARMA model for $\hat e_t$ 
3. Apply Box-Tiao transformation to filter $y_t, x_t$
4. Run regression on the transformed equation
5. check the correlation of regression residuals 

__Find the l-ahead optimal forecast of $y_{t+l}, \hat y_t(l)$ with $a_t,e_t$.__

Since $v(B)=\sum_0^k v_i B^i$ has finite terms, it can be transformed $v(B)=\delta(B)/w(B)$, then 

$$y_t = \frac{\delta(B) \theta(B)}{w(B)\phi_x(B)}a_t + \frac{\theta_n(B)}{\phi_n(B)}e_t$$

$$y_t = u(B)a_t + \psi(B)e_t$$

all of them are finite order with max K of polynomials in B. Therefore, 

$$y_{t+l} = \sum_0^k u_i a_{t+l-i} + \psi_i e_{t+l-i}$$

$$\hat y_t(l) = \sum_0^k u_{i+l}^* a_{t-i} + \psi_{i+l}^* e_{t-i}$$

__Derive the MSE__

Consider $y_{t-l} - \hat y_t(l)$, which equals to   
$=\sum_0^{l-1}u_i a_{t+l-i} + \psi_i e_{t+l - i} (i)$  after time lag $t$  
$-\sum_0^k (u_{i+l}^* - u_{i+l})a_{t-i} (ii)$  
$-(\psi_{i+l}^* - \psi_{i+l})e_{t-i} (iii)$ up to time $t$  

$E(y_l - \hat y_t(l))^2 = E(i)^2 + E(ii)^2 + E(iii)^2$  
$=\sum_0^{l-1} u_i^2 \sigma_a^2 + \psi_i^2 \sigma_e^2$  
$+ \sum_0^k \sigma_a^2(u_{i+l^*}- u_{i+l})$  
$+ \sum_0^k \sigma_e^2(\psi_{i+l^*}- \psi_{i+l})$

minimized when $u^* = u, \psi^* = \psi$

## VAR
Consider a VAR(p) model of 2-d variables, i.e. $y_t = [y_{i,t},  y_{2,t}]^T$
$y_t = \sum_1^p A_i y_{t-i} + a_t$, 
and each $A_i = \begin{bmatrix}\phi_{i,11}&\phi_{i,12}\\\phi_{i,21}&\phi_{i,22}\end{bmatrix}$



__state how to check the stationarity__

All the roots of $\det(I_k - A_1B-...-A_pB^p) = 0$ must lie outside of the unit circle, or the companion form $\xi_t = A\xi_{t-1}+v_t$ must have the moduli of the eigenvalues of $A$ being <1. 

__Describe the methods to select the order for Equation (1)__

- Selection by information criteria, for example, BIC, AIC, DIC, HQ, SC, FPE
- Using LRT for VAR(p) vs. VAR(p-1)

__State how to test Granger causality for that $X_{1t}$ Granger causes $X_{2t}$ but not the other way around. Basd on the same condition, express $X_{2t}$ as the TFN model of $X_{1t}$__

$$X_{2,t} = \sum_1^p \phi_{i,21}X_{1,t-i} + \phi_{i,22}X_{2,t-i} + a_{2,t}$$

$$X_{2,t} - \sum_1^p \phi_{i,22}X_{2,t-i} = \sum_1^p \phi_{i,21}X_{1,t-i} + a_{2,t}$$

$$\Phi_{22}(B)X_{2,t} = \Phi_{21}(B)X_{1,t}+a_{2,t}$$

$$X_{2,t} = \frac{\Phi_{21}(B)}{\Phi_{22}(B)}X_{1,t} + \frac{a_{2,t}}{\Phi_{22}(B)}$$

Let $v(B) = \frac{\Phi_{21}(B)}{\Phi_{22}(B)}, N_t = \frac{a_{2,t}}{\Phi_{22}(B)}$, the TFN model is 

$$X_{2,t}=v(B)X_{1,t} + N_t$$

To see whether $X_{1,t}$ Granger causes $X_{2,t}$, if not, then all $\phi_{i,21} = 0$

__Describe how to test Granger causality using univariate approach. Suppose $$\Phi_1(B)X_{1,t}=\Theta_1(B)a_{1,t}, \Phi_2(B)X_{2,t}=\Theta_2(B)a_{2,t}$$__

Using the Portmanteau test, 

$$\rho_{a_1a_2}(k) = \frac{E(a_{1,t}, a_{2,t+k})}{\sqrt{\sigma_1^2\sigma_2^2}}$$

If $\forall k < 0. \rho(k)=0$, then $X_2$ does not Granger cause $X_1$. 

__Suppose $X_{1,t}, X_{2,t}$ not weakly stationary. How do you model the join dynamics of $\{X_{1,t}, X_{2,t}\}$ using co-integration.__

 - differencing the two time series individually until each are stationary
 - use VAR(p) to fit the two stationary process and test the Granger causality
 - If $(X_{1,t}, X_{2,t})$ are cointegrated, use Error correction model to include lagged disequilibrium terms as explanatory variables. 

__Discuss the reasons why we have to choose different models based on the condition of integration__

If cointegration exists, if we use VAR(p) model directly fitted to the differenced stationary processes, the model will be misspecified. 

__Discuss the Engle-Granger approach for modeling cointegrated $X_{1t}$ and $X_{2t}$__

1. test whether $X_t,Y_t$ are I(1) using unit root test
2. if both I(1), regress one against the other using least squares
3. run a unit root test on regression residuals. If residuals are stationary, these two series are cointegrated. 
  - Where the regression line indicate the long-run equilibrium relationship between two variables, the disequilirium term is simply the regression residuals. 
4. Finally, consider the ECM 

$$\Delta X_t = c_1 + \rho_1(Y_{t-1} - \hat a X_{t-1}) + \beta_{x,1}\Delta X_{t-1} + ... + \beta_{y,1}\Delta Y_{t-1}+...+\epsilon_{x,t}$$

$$\Delta Y_t = c_2 + \rho_2(Y_{t-1} - \hat a X_{t-1}) + \gamma_{x,1}\Delta X_{t-1} + ... + \gamma_{y,1}\Delta Y_{t-1}+...+\epsilon_{y,t}$$

__Discuss the implication of Granger representation theorem__

We have and should use ECM to model non-stationary time series

## Bootstrap
Given an AR(2) model

$$y_t = \mu + \phi y_{t-1} + \phi_2 y_{t-2} + a_t$$

__(unconditional) parametric bootstrap__

$E(Y_t) = \mu + E(\phi_1 Y_{t-1}) + E(\phi_2 Y_{t-2}) + E(a_t)$  
$E(Y)=\mu + \phi_1 E(Y) + \phi_2 E(Y)$  
$E(Y)=\frac{\mu}{1-\phi_1-\phi_2}$

$var(Y) = 0 + \phi_1^2 var(Y) + \phi_2^2 var(Y) + E(a)^2$  
$var(Y) = \frac{\sigma^2}{1-\phi_1^2 - \phi_2^2}$

1. The unconditional distribution of $Y_t\sim N(\frac{\mu}{1-\phi_1-\phi_2}, \frac{\sigma^2}{1-\phi_1^2 - \phi_2^2})$
2. simulate $y_0, y_1$ by drawing a random number from $Y$. 
3. recursively simulate $y_2$ by the model, recursively

__pros__ easy to compute  
__cons__ don't know whether it is correlated

## GARCH

#### ARCH process
__ARCH(1)__ The first order of autoregressive conditional heteroskedastic process is 
$e_t \sim N(0, \sigma_t^2)$ where $\sigma_t^2 = a_0 + a_1 e_{t-1}^2$.  
On defining $v_t = e_t^2 - \sigma_t^2$, the model can also be written as  

$$e_t^2 = a_0 + a_1 e_{t-1}^2 + v_t$$

Since $E(v_t \mid x_{t-1}, x_{t-2},...)=0$, the model corresponds directly to an AR(1) model for the squared error $e_t^2$. 

__ARCH(q)__ Then, the ARCH(q) process is defined as 

$$\sigma_t^2 = a_0 + \sum_{t=1}^q a_i e_{t-i}^2$$ with

$$a_0 \geq 0, a_i > 0. \sum_{i=1}^q a_i < 1$$

or 

$$e_t^2 = a_0 + \sum_1^q a_i e_{t-i}^2 + v_t$$

$$e_t^2 = a_0 + a(B)e_{t-1}^2 + v_t$$

__GARCH(p,q)__

$$e_t^2 = a_0 + \sum_1^q \beta_i \sigma_{t-i}^2 + \sum_1^q a_i e_{t-i}^2$$

$$\sigma_t^2 = a_0 + a(B)e_{t-1}^2 + \beta(B)\sigma_{t-1}^2$$

with $a_0 \geq 0, a(B)$ and $\beta(B)$ have no common roots and that the roots of $1-\beta(B)$ all less than unit root. 
