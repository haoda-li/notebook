# Forecasting and Transfer Function Noise Model

## Minimized MSE Forecasts for ARMA models
Consider a stationary ARMA model (casual and invertible)  

$$\Phi(B)X_t = \Theta(B)a_t$$  

Rewrite as a MA process

$$X_t = \Psi(B)a_t$$


Then, for $t = n + h$, 

$$X_{n+h}=\sum^\infty_0 \psi_i a_{n+ h - i}$$

Suppose we have observations till $X_n, X_{n-1},...$ and wish to forecast $h$ step ahead of future values $X_{n+h}$ as a lin.comb. of the observations. Then, we define the mean square error forecaster 

$$\hat X_t(h):= \sum_{i=0}^\infty \hat\psi_i a_{t-i}$$

where $\hat\psi_i$ are parameters to be determined.  

Then MSE of the forecast is   

\begin{align*}
E(X_{t+h} - \hat X_t(h))^2  &= E(\sum^\infty \psi_i a_{t+h-i} - \sum^\infty \hat\psi_i a _{t-i})\\  
&= E(\sum^{j-1}\psi_i a_{t+h-i}) + \sum^\infty (\psi_{h+i} + \hat\psi_i)a_{t-i})^2\\
&= \sigma^2 \sum^{h-1} \psi_i^2 + \sigma^2 \sum^\infty (\psi_{h+i-\hat\psi_i})^2\\
\arg\min(E(X_{t+h} - \hat X_t(h))^2)&=\arg\min(\sum^\infty (\psi_{h+i-\hat\psi_i})^2)\\
\implies \psi_{h+i} &= \hat\psi_i
\end{align*}

### Rule of calculating conditional expectation

$$E_t(X_{t+h}) := E(X_{t+h}\mid X_t, X_{t-1}, ...) = E(\sum^\infty \psi_i a_{t+h-i}\mid X_t, X_{t-1},...)$$

Using the fact that $a_i$'s are uncorrelated

$$E(X_{t+h}\mid X_t, X_{t-1}, ...) =\sum^\infty \psi_{h+i}a_{t-i} = \hat X_t(h)$$

For $h > 0$, 

\begin{align*}
E_t(X+h) &= \hat X_t (h)\\
E_t(X_{t-h}) &= X_{t-h}\\
E_t(a_{t+h})&=E(a_{t+h}) = 0\\
E_t(a_{t-h}) &= X_{t-h} - \hat X_{t-h-1} = X_{t-h} - E_{t-h-1}(X_{t-h})\\
\end{align*}

### Example
Consider a AR(1) model $X_t = 0.5X_{t-1} + a_t$. Then  

$$\hat X_t(1)  = E_t(X_{t+1}) = 0.5 E_t(X_t) + E_t(a_{t+1}) = 0.5E_t(X_t) = 0.5X_t$$ 

$$\hat X_t(h) = 0.5 E_t(X_{t+h-1}) + E_t(a_{t+h}) = 0.5 \hat X_t(h-1) = 0.5^h X_t$$

## Transfer Function Noise model
Consider the model that 
$X_t = f(X_{t-1}, X_{t-2}, ... , Z_t, Z_{t-1},...)$, $X_t$ is a linear combination of past observations and an external variable.

A TFN model is a time series regression that predict values of a dependent variable based on both the current and lagged values of one or more explanatory variables.

### Procedure of building the single input TFN model
1. Preliminary identification of the impulse response coefficients $v_i$ (prewhitening)
2. Specification of the noise term $n_t$
3. Specification of the transfer function using a rational polynomial in B if necessary
4. Estimation of the TFN specified 
5. Model diagnostic checks

__Rational distributed lag model__
$v(B)$ can be approximated by a ratio of polynomials  

$$v(B)=\frac{\sum_0^r\delta B^i}{1-\sum_1^s\theta_i B^i} = \delta(B)/\theta(B)$$

and then, $y_t = \delta(B)x_t / \theta(B) + n_t$

### ARMAX
$y_t = v(B)x_t + n_t = v_0 x_t + v_1 x_{t-1}+v_2 x_{t-2}+...+n_t$  
where $v(B) = \sum^\infty v_j B^j$, and $x_t,n_t$ are independent. 

The coefficient $v_0, v_1,...$ are referred as the impulse response function of the system.

To make such equation to be meaningful, $\sum^\infty |v_j| = g<\infty$, which the system is stable and $g$ is called the stead-state gain. $g$ represents the impact on $Y$ when $X_{t-j}$ are held constant over time.  

__Properties__   
$x_t \sim ARMA(p,q)$, $v_i = \phi^i (1-\phi)$, $y_t = \sum^\infty v_i x_{t-i}+a_t$

### Pre-whitening
Consider $x\sim$ARMA, i.e. $\Phi_x(B)x_t = \Theta_x(B)a_t$  
Apply $\Phi_x(B)/\Theta_x(B)$ on TFN model  

$$\frac{\Phi_x(B)}{\Theta_x(B)}y_t = v(B)\frac{\Phi_x(B)}{\Theta_x(B)} x_t + \frac{\Phi_x(B)}{\Theta_x(B)}\epsilon_t$$

Let $\tau_t = \frac{\Phi_x(B)}{\Theta_x(B)} y_t, n_t = \frac{\Phi_x(B)}{\Theta_x(B)} \epsilon_t$, we get   

$$\tau_t = v(B)a_t + n_t \land n_t \perp a_t$$

To get $\gamma_{a\tau}(0)$, multiply both sides by $a_t$ and take the expectations. 

\begin{align*}
\gamma_{a\tau}(0)
&=E(a_t\tau_t)\\
&= E(a_tv(B)a_t) + E(a_tn_t)\\
&=E((v_0a_t + v_1e_{t-1}+...+v_ma_{t-m})a_t)\\
&=E(v_0a_ta_t)=v_o\gamma_a(0) = v_0\sigma^2
\end{align*}

To get $\gamma_{a\tau}(1)$, multiply both sides by $a_{t-1}$

\begin{align*}
\gamma_{a\tau}(1)&=E(a_{t-1}\tau_t)\\
&=E(a_{t-1}v(B)a_t) + E(a_{t-1}n_t)\\
&=E(a_{t-1}(v_0a_t + v_1 a_{t-1} + v_2 a_{t-2}+...+v_m a_{t-m}))\\
&= E(a_{t-1}v_1 a_{t-1})=v_1\gamma_a(0) = v_1\sigma^2
\end{align*}

Therefore, $\gamma_{a\tau(k)} = v_k\sigma^2$

Since $\rho_{a\tau}(k) = \gamma_{a\tau}(k) / \sigma_a\sigma_\tau$  

$$\rho_{a\tau}(k) = \frac{v_k \sigma_a^2}{\sigma_a\sigma_\tau} = \frac{v_k \sigma_a}{\sigma_\tau}\land v_k = \rho_{a\tau}(k)\frac{\sigma_\tau}{\sigma_a}\propto \rho_{a\tau}(k)$$

### Box-Tiao Transformation


Similarly, since $n_t\sim$ ARMA, i.e. $\Phi_n(B)n_t = \Theta_n(B)a_t$  
Which $\frac{\Phi_n(B)}{\Theta_n(B)}n_t = a_t$  
Then, apply $\frac{\Phi_n(B)}{\Theta_n(B)}$ to both sides of the equation. 

$$\frac{\Phi_n(B)}{\Theta_n(B)} y_t = v(B) \frac{\Phi_n(B)}{\Theta_n(B)} x_t + \frac{\Phi_n(B)}{\Theta_n(B)} n_t$$

$$\tilde y_t = v(B)\tilde x_t + a_t$$

is called the Box-Tiao Transformation

### Steps of The Estimation Procedure
The steps of the estimation procedures

1. Run the OLS regression on $y_t = \sum_{j=1}^s v_j x_{t-j} + e_t$ to collect the residuals $\{\hat e_t\}$
2. Identify an ARMA model for $\hat e_t$ 
3. Apply Box-Tiao transformation to filter $y_t, x_t$
4. Run regression on the transformed equation
5. check the correlation of regression residuals 
