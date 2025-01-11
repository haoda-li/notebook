# Autoregressive (AR) and Moving Average (MA) model

## Autoregressive(AR) and moving average(MA) model 
A process $\{X_t\}$ is said to be an ARMA(p,q) process if 
 
 - $\{X_t\}$ is stationary
 - $\forall t. X_t - \phi_1X_{t-1}-...-\phi_qX_{t-p} = a_t + \theta_1a_{t-1}+...+\theta_qa_{t-q}$  
 using backward shift operation notation $B^h=x_{t-h}$:  
 $\Phi(B)x_t = (1-\phi_1B - ... - \phi_p B^p)x_t = (1+\theta_1B + ...+\theta_qB^q)a_t = \Theta(B)a_t$
 where $a_t \sim NID(0, \sigma^2)$  
 
$\{X_t\}$ is an ARMA(p,q) process with mean $\mu$ if $\{X_t-\mu\}$ is an ARMA(p,q) process. 

## Moving average model(MA(q))
__MA($\infty$)__ If $\{a_t\}\sim NID(0, \sigma^2)$ then we say that $\{X_t\}$ is a MA($\infty$) process of $\{a_t\}$ if $\exists\{\psi_n\}, \sum^\infty |\psi_j|<\infty$ and $X_t = \sum^\infty \psi_j a_{t-j}$ where $t\in\mathbb{Z}$.  

We can calculate ACF of a stochastic process $\{X_t\}$ a.l.s. $\{X_t\}$ can be writtin in the form of a MA($\infty$) process

Also, MA($\infty$) is a required condition for $\{X_t\}$ to be stationary. 

__Theorem__  The MA($\infty$) process is stationary with 0 mean and autocovariance function $\gamma(k) = \sigma^2 \sum^\infty \psi_j\psi_{j+|k|}$ 

__MA(q)__ $X_t = \sum_{i=0}^q \theta_i a_{t-i} = \Theta(B)a_t$  $\theta_0 = 1, B$ is the backward shift operator, $B^hX_t = X_{t-h}$ and $a_t\sim NID(0, \sigma^2)$

Under MA(q) model  

\begin{align*}
\gamma(1) = cov(X_t, X_{t+1})&=cov(\sum_{i=0}^q\theta_i a_{t-i}, \sum_{i=0}^q \theta_ia_{t+1-i})\\
&=E(\sum_{i=0}^{q-1}\theta_i\theta_{i+1}a_{t-i}a_{t-i}) &a\sim NID, cov(a_i,a_j) =0\\  
&=\sigma^2(\sum_{i=0}^{q-1}\theta_i\theta_{i+1})
\end{align*}

Similarly,  

\begin{align*}
\gamma(k)=cov(X_t, X_{t+k})
&=cov(\sum_{i=0}^q \theta_t a_{t-i}, \sum_{i=0}^q \theta_i a_{t+k - i})\\
&=\sigma^2 \sum_{i=0}^{q-k}\theta_i\theta_{i+k}\mathbb{I}(|k|\leq q)
\end{align*}

Then, the autocorrelation function (ACF) will be  

\begin{align*}
\rho_k &= \gamma_k/\sqrt{var(X_t)var(X_{t+k})}\\
& = \gamma_k / \sigma^2\sum_{i=0}^{q} \theta_i^2\\
& =\sigma^2 \sum_{i=0}^{q-k}\theta_i\theta_{i+k}\mathbb{I}(|k|\leq q) / \sigma^2\sum_{i=0}^{q} \theta_i^2\\
& = \sum_{i=0}^{q-k}\theta_i\theta_{i+k}\mathbb{I}(k\leq q) / \sum_{i=0}^{q} \theta_i^2
\end{align*}

## Autoregressive model of order p (AR(p))
$X_t - \phi_1X_{t-1}-...-\phi_pX_{t-p} = \Phi(B)X_t = a_t$  
where $a_t\sim NID(0, \sigma^2), B^hX_t = X_{t-h}, h\in\mathbb{Z}, \Phi(B)=(1-\phi_1B-...-\phi_p B^p)$

### AR(1)
Notice that for a $AR(1)$ process, $a\sim NID(0, \sigma^2)$ and $a_t$ is uncorrelated with all previous $X_s, s<t$

\begin{align*}
X_t &= \phi X_{t-1} + a_t\\
&=\phi(\phi X_{t-2}+a_{t-1})+a_t&\text{ replace }X_{t-1}\\  
&...&\text{repeated replacing}\\
&=\sum_0^\infty \phi^i a_{t-i}
\end{align*}

is a $MA(\infty)$ process

\begin{align*}
\gamma(k) 
&= cov(X_t, X_{t+k})\\
&=cov(\sum_0^\infty \phi^i a_{t-i}, \sum_0^\infty \phi^i a_{t+k-i})\\  
&=cov(\sum_0^\infty \phi^i a_{t-i}, \sum_0^\infty \phi^{i+k} a_{t-i} + \sum_0^{k-1} \phi^i a_{t+k-i})\\
&= \phi^k\sum_0^\infty (\phi^ia_{t-i})^2\\
&=\phi^k \gamma(0)=\phi^k var(X_t)
\end{align*}

\begin{align*}
\gamma(0)
&=var(X_t)\\
&=\sum^\infty \phi^{2i}a^2_{t-i}\\
&=\sigma^2(\sum^\infty (\phi^2)^i) &a\sim NID(0,\sigma^2)\\
&=\sigma^2(1-\phi^2)^{-1} &\text{when }\phi^2<1 \text{, by Maclaurin's series}
\end{align*}

__Causal__ or future independent AR process when $|\phi|< 1$ for an $AR(1)$

## Checking stationarity of AR(p)
$\Phi(B) = 1-\phi_1B-...-\phi_pB^p=0$ must have all the roots line outside the unit circle. 


## ACF 
### AR(1) Case  

$$X_t = \phi X_{t-1} + a_t, a_t\sim NID(0,\sigma^2)$$  

For $k\in\mathbb{Z}^+$, multiply $X_{t-k}$ on both sides  

$$X_t X_{t-k} = \phi X_{t-1}X_{t-k} + a_t X_{t-k}$$

Taking expectation, consider $E(a_tX_{t-k})$  

 \begin{align*}
 cov(a_t, X_{t-k}) &= E(a_t X_{t-k})-E(a_t)E(X_{t-k})\\
 &= E(a_t X_{t-k}) - 0\\
  &= cov(a_t, \sum_0^\infty \phi^i a_{t-k-i}) = 0
  \end{align*}

$a_t$ is uncorrelated with previous $a$'s. 
 
$$E(X_t X_{t-k}) = \phi E(X_{t-1}X_{t-k})$$

since $cov(X_t,X_{t-k}) = E(X_tX_{t-k})-0$  

$$\gamma(k)=\phi\gamma(k-1)$$

By induction, $\gamma(k)=\phi^k\gamma(0)$



### AR(2) Case  

$$X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + a_t$$

Multiple both sides by $X_t$  

$$X_t^2 = \phi_1 X_{t-1}X_t + \phi_2 X_{t-2}X_t + X_t a_t$$  

Taking expectation, note that $X_t$ is a lin.comb of $a$.   

$$\gamma(0) = \gamma(1) + \gamma(2) + \sigma^2$$    

$$\gamma(0)(1-\phi_1\rho(1)-\phi_2\rho(2)) = \sigma^2 \text{ since }\rho(k)=\gamma(k)/\gamma(0)$$  

Multiple both sides by $X_{t-1}$ and take expectations  

$$E(X_tX_{t-1}) = \phi_1 E(X_{t-1}X_{t-1}) + \phi_2E(X_{t-2}X_{t-1}) + E(a_t X_{t-1})$$  

$$\gamma(1) = \phi_1\gamma(0) + \phi_2\gamma(1)$$  

$$\rho(1) = \phi_1 + \phi_2\rho(1)$$  

$$\rho(1) = \frac{\phi_1}{1-\phi_2}$$  

Multiple both sides by $X_{t-2}$ and take expectations

$$E(X_tX_{t-2}) = \phi_1 E(X_{t-1}X_{t-2}) + \phi_2E(X_{t-2}X_{t-2}) + E(a_t X_{t-2})$$  

$$\gamma(2) = \phi_1\gamma(1) + \phi_2\gamma(0)$$  

$$\rho(2) = \phi_1\rho(1) + \phi_2$$  

... Using this pattern  

$$\rho(h) = \phi_1\rho(h-1)+\phi_2\rho(h-2)$$

with base case 

$$\rho(0)=1, \rho(1) = \frac{\phi_1}{1-\phi_2}$$


### AR(p) case
Given $X_t = (\sum_1^p \phi_iX_{t-i}) + a_t$, is stationary is all $p$ roots lie outside of the unit circle  

__Yule-Walker equations__  
For the first $p$ autocorrelations:

$$\rho(k) = \sum_1^p \phi_i\rho_{|k-i|}$$

## Partial Autocorrelation Function (PACF)

$\phi_{kk} = corr(X_t, X_{t+k}\mid X_{t+1},...,X_{t+k-1})$  
the correlation between $X_t, X_{t+k}$ after their mutual linear dependency on the intervening variables has been removed. 

For a given lag $k$, $\forall j \in \{1,2,...,k\}$.  

$$\rho_i = \sum_1^k\phi_{ki}\rho_{j-i}$$

We regard the ACFs are given, take regression parameters $\phi_{ki}$ and wish to solve for $\phi_{kk}$.  
which all together forms the Yule-Walker equations. 

__Example__  
For lag 1, $\rho_1 = \phi_{11},\rho_0\Rightarrow \rho_1=\phi_{11}$

For lag 2,  

$$\rho_1 = \phi_{21} + \phi_{22}\rho_1$$  

$$\rho_2 = \phi_{21}\rho_1 + \phi_{22}$$    

$$\Rightarrow \phi_{22} = \frac{\rho_2 - \rho_1^2}{1-\rho_1^2}$$

## Causal and invertible
__Causal/stationary__ if $X_t$ can be expressed as an MA($\infty$) process

__Invertible__ if $X_t$ can be expressed as an AR($\infty$) process. 

## Duality between AR amd MA processes
A finite-order stationary AR(p) process corresponds to a MA($\infty$) process, and a finite-order invertible MA(q) corresponds to an AR($\infty$) process. 

### Example
Given model $X_t - \phi_1 X_{t-1} - \phi_2 X_{t-2} = a_t = \theta a_{t-1}$

Assume the process is causal, then $X_t = \sum_0^\infty \psi_i a_{t-i} = a_t\sum_0^\infty \psi_i B^i = \psi(B)a_t$ by causal process  
$\phi(B)X_t = \theta(B) a_t \Rightarrow X_t = \frac{\theta(B)a_t}{\phi(B)}$ by ARMA model  
$\Rightarrow \Theta(B)/\Phi(B)=\Psi(B)$  

Replace back into the model
$1+\theta B = (\sum_0^\infty \psi_iB^i)(1-\phi_1B - \phi_2B^2)$

Consider $B$, $\theta B = \psi_1B -\phi_1B\Rightarrow \psi_1 = \phi_1 + \theta$

Consider $B^2$, $0 = -\theta_2B^2-\psi_1\theta_1B +\psi_2B^2\Rightarrow \psi_2 = \phi_2 + \phi_1(\phi_1+ \theta)$

Assume the process is invertible, then  
$a_t = \sum_0^\infty \pi_i X_{t-i} = X_t\sum_0^\infty \pi_i B^i$,  
similarly we get $\Phi(B)=\Theta(B)\Pi(B)$

## Wold Decomposition
Any zero-mean process $\{X_t\}$ wgucg us bit deterministic can be expressed as a sum of $X_t = U_t + V_t$ where $\{U_t\}$ denotes an MA($\infty$) process and $\{V_t\}$ is a deterministic process which is uncorrelated with $\{U_t\}$
 - __deterministic__ if the values $X_{n+j}, j\geq 1$ of the process $\{X_t\}$ were perfectly predicatable in term of $\mu_n=sp\{X_t\}$
 - If $X_n$ comes from a deterministic process, it can be predicted (or determined) by its past observations of the process

## Model identification

| process | ACF | PACF | 
| --- | --- | --- | 
|AR(p) | tails off | cuts off after lag p|
|MA(q) | cuts off after lag q | tails off | 
|ARMA(p,q)| tails off after (q-p)| tails off after (p-q)|

## Model Adequacy
The overall tests that check an entire group of residual autocorrelation functions are called portmanteau tests.

__Box and Pierce__ $Q = n \sum_1^m \hat\rho_k^2 \sim \chi^2_{m-(p+q)}$  
__Ljung and Box__ $Q=\sum_1^m \frac{n(n+2)\hat\rho_k^2}{n-k}\sim \chi^2_{m-(p+q)}$  
$n$ is the number of observations  
$m$ is the max lag  
$p,q$ are fitted model



## Model selection
$$AIC = -2\log ML + 2k$$

$$BIC = -2 \log ML + k \log n$$

BIC puts more penalties on the number of parameters

## Example: Application of ARMA in Investment

### Alternative assets modeling
$y_t$ and $r_t$ denote observable appraisal and latent economic returns. 

__Goal__ to infer unobservable economic returns using appraisal returns 

__Geltner method__ commercial real state 

$$y_t = \phi y_{t-1} + (1-\phi)r_t = \sum^\infty \phi^j(1-\phi)r_{t-j} = \sum^\infty w_jr_{t-j}$$ 

(by substitute $y_{t-1}$) where $\phi\in (0,1), w_j := \phi^j (1-\phi)$ is the weight   

$$y_t = \hat\phi y_{t-1}+\hat a_t , \hat r_t = \frac{\hat a_t}{1-\hat\phi}$$  

$$var(\hat r_t)=\frac{\sigma^2}{(1-\hat\phi)^2} $$

__Gertmansky, Low, & Markorov__ 

$$y_t = \sum^q w_i r_{t-i}$$ 

where $w_i\in(0,1), \sum w_i = 1$  
Since $y_t$ is a linear combination of white noise

$$y_t = \sum^q \theta_i a_{t-i} = \sum_i^q \left(\frac{\theta_i}{\sum_j^q \theta_j}\sum_j^q \theta_j a_{t-i}\right) = \sum^q w_i r_{t-i}$$

__Factor Modeling__  
The economic returns can be regressed by the market returns

$$r_t = \alpha + \beta r_{Mt} + e_t$$

$$y_t = \sum^q w_i (\alpha + \beta r_{M_,t-i} + e_{t-i}) $$

$$= \sum^q w_i a + \beta \sum^q w_i r_{M,t-i} + \sum^q w_i e_{t-i} =\alpha + \beta \sum^q w_i r_{M,t-i} + \sum^q w_i e_{t-i}$$
