# Summary Sheet

## pooled two sample t-tests
 - assume equal population variances
 - $s^2_p = \frac{(n_x-1)s_x^2 + (n_y-1)s_y^2}{n_x+n_y-2}$
 - $t = \frac{(\bar{x} - \bar{y} -D_0)}{\sqrt{s_p^2(n_x^{-1}+n_y^{-1})} }\sim t_{(n_x-1)(n_y-1)}$


## SLM Dummy variable
$Y_i=\beta_0+\beta_1X_i + \epsilon_i$
assumptions

 - linear model is appropriate
 - $\epsilon_i \sim N(0,\sigma^2)$
 
Hypothesis test:  
 $H_0:\beta_1 = 0, H_a:\beta_1\neq 0$  
$t=b_1/se(b_1)\sim t_{N-2}$, $N$ is the total number of observations

## One Way ANOVA  & GLM
$Y_i=\vec{X_i}\vec{\beta}+\vec{\epsilon}$

 - assumptions: same as dummy variable, jointly normally distributed errors
 - $F=MSReg/MSE = \frac{(SSR/G-1)}{SSE/(N-G)}\sim F_{G-1,N-G}$

## Multiple Comparisons

Bonferrroni's Method: 

 - $P(\cup A_i)\leq \sum P(A_i)$
 - $k= {G \choose 2}$
 - level at $a/k$

Tukey's Method: less conservative than Bonferroni's method

## Two Way ANOVA
Overall vs. Partiral F-tests  
$H_0: $ a subset of $\beta$'s are 0. $H_a: $ some of the $\beta$ in the subset are not 0.  
Let FULL model be with all explanatory variables, REDUCED be without the coefficients in testing.  

$$F=\frac{(RSS_r - RSS_f)/\# \beta \text{ tested} }{MSE_f}\sim F_{\# \beta \text{ tested}, d.f. RES_f}$$

Describing "interactions"

## GLM vs. Transformation
Transform Y so it has an approximate normal  distribution with constant variance, 

GLM: distribution of Y not restricted to Normal,  
model parameters describe $g(E(Y))$ rather than $E(g(Y))$  
GLMs provide a unified theory of modeling that encompasses the most important models for continuous and discrete variables. 

## GLM tests
Wald  
$H_0:\beta_j = 0, H_a: \beta_j\neq 0$  
$z=\hat\beta_j / se(\hat\beta_j)\sim N(0,1)$.  
CI: $\hat\beta_j \pm z_{a/2} se(\hat\beta_j)$

LRT  
$H_0:$ some $beta$ are 0, $H_a: $ at least one tested $\beta$ is not 0. 

$$G^2 = (-2\log \mathcal L_R) - (-2\log \mathcal L_F) = -2\log (\mathcal L_R / \mathcal L_F)\sim \chi^2_k$$ 

$k= \# \beta$ tested

Global LRT  
LRT comparing to the NULL model (null deviance)


## AIC, BIC
- combines log-likelihood with a penalty 
- $AIC = -2\log\mathcal L + 2(p+1)$
- $BIC =  -2\log\mathcal L + \log N(p+1)$
- $p$ number of explanatory variables, $N$ sample size
- Smaller is better
- Better = $diff(AIC) > 10$
- Same = $diff(AIC) < 2$

## SLR vs. Binary LR
 - both use MLE
 
 - Binary LR has fewer assumptions 
  - no outelires
  - no residual plots
  - non constant variance 

## Binary Logistic Regression

underlying distribution for each independent observation: $Bernoulli(\pi_i)$

We cannot estimate $\pi_i$ for individual $i$. 

- Let $\pi = P(success)$, 
- ODDS: $\pi/(1-\pi)$
- LOG ODDS: $\log(\pi/(1-\pi))$
- ODDS RATIO is the ratio of two ODDS

$E(Y\mid X)=\pi, var(Y\mid X) = \pi(1-\pi)$

The model

$$\log(\pi/(1-\pi)) = X\beta$$

$$\log(\frac{\pi_i}{1-\pi_i}) = X_i\beta \quad\text{(no error term)}$$


MLE:$P(Y_i=y_i)=\pi_i^{y_i}(1-\pi_i)^{1-y_i}$

$$\mathcal{L} = \prod_1^n\pi_i^{y_i}(1-\pi_i)^{1-y_i}$$

where $\pi_i = \frac{\exp(X_i\beta)}{1+\exp(X_i\beta)}=e^{\mu}/(1+e^\mu)$ and 

$$1-\mu_i = 1-\frac{e^\mu}{1+e^\mu} = (1+e^\mu)^{-1}$$

$$\log\mathcal{L} = 
\sum_1^ny_i(X_i\beta) - y_i\log(1+\exp(X_i\beta))-(1-y_i)\log(1+X_i\beta))$$

Let $(a,b)$ be CI, CI for Odds ratio is $e^a, e^b$, while we cannot compute CI for $\pi$ since $\pi$ is not normally distributed

Assumptions:

 - underlying model for Y is Bernoulli
 - independent observations
 - Correct form of model (linear relationship, included all relevant variables and excluded irrelevant)
 - enough large sample size

## Binomial Logistic Regression 
Let $Y$ be the count of the number of "success" 

$P(Y=y)={m\choose y}\pi^y (1-\pi)^{m-y}$

$E(Y)=m\pi, var(Y)=m\pi(1-\pi)$

Then the proportion of successes 
$E(Y/m)=\pi, var(Y/m)=\pi(1-\pi)/m$

Assume for each group of observation, it is independent. 

We can estimate $\pi_i$ is this case

MLE:  

$$P(Y_i=y_i) = {m_i\choose y_i}\pi^{y_i}(1-\pi_i)^{m_i-y_i}$$

$$\mathcal L = \prod_1^n {m_i\choose y_i}\pi^{y_i}(1-\pi_i)^{m_i-y_i}$$

where $\pi_i = \frac{e^\mu}{1+e^\mu}$

$$\log\mathcal L = \sum y_i\log(\pi_i)+(m_i-y_i)\log(1-\pi_i) + \log{m_i\choose y_i}$$

Deviance $=-2\log(\mathcal L_M/\mathcal L_S) = -2(\log \mathcal L_M - \log \mathcal L_S)$. 

Saturated model has log likelihood ratio 0. 

## Logistic Regression Problems
- Extrapolation: model outside of range of observed data may not be appropriate
- Multicollinearity
   - unstable fitted equation
   - coefficient significance and signs
   - large standard error of coefficients
   - MLR may not converge
- Influential points

Specific to logistic 

  - Complete separation
      - one of a linear combination of explanatory variables perfectly predict $Y$, then MLE cannot be computed
  - Quasi-complete separation
      - almost perfectly predict Y
      - 
 __Solution__ simplify model, or try other options
 
Extra-binomial variation

 - when Bernoulli observations are not independent
 - use quasibinomial 
 - model for variance: $var(Y_i)=\phi m_i \pi_i(1-\pi_i)$
 - $\hat\phi = $ sum of squared Pearson residuals / d.f. 

## GOF
To check model adequacy using LRT

$H_0: $ fitted model fits data as well as Saturated model. $H_a: $ saturated model is better, the fitted model is inadequate 

$G^2 = -2\log(\mathcal L_F /\mathcal L_S)\sim \chi^2_{n-(p+1)}$

## Log linear Model
- Why not linear
   - outcome is counts and small numbers
   - Won't have a normal distribution conditional on age
- Why no logistic
   - Not a binary outcome
   - Not a binomial outcome since not a fixed number of trials
   
$P(Y=y)=\mu^y e^{-\mu} / y!, E(Y)=var(Y)=\mu$

$$\mathcal L = \prod_1^n \mu_i^{y_i} e^{-\mu_i} / y_i!$$

$$\log\mathcal L = \sum_1^n y_i \log (\mu_i) -\mu_i - \log(y_i!)$$

## Two Factor Independence
__Binomial Sampling__  
For $2\times 2$ table  
$H_0: \mu_a = \mu_b, H_a: \mu_a\neq \mu_b$

$$z=\frac{\hat\mu_a - \hat\mu_b}{se(\hat\mu_a - \hat\mu_b)}\sim N(0,1)$$

Assumption: 

 - each trial is a Bernoulli
 - the number of groups are fixed
 - The underlying distribution is $y_a\sim binomial(n_a, \pi_a), y_b\sim binomial(n_b, \pi_b)$



## Contingency Table
test statistics $\chi^2 = \sum_j\sum_i (y_{ij} - \hat\mu_{ij})^2 / \hat\mu_{ij}\sim \chi^2_{(I-1)(J-1)}$ where $\hat\mu_{ij} = \pi_{i.}\pi_{.j}/n$

Contingency table model:  
$Y_{ij}$ be the r.v. representing the number of observations in the cell  
$y_{ij}$ be the observed cell counts

The underlying distribution of $Y=(Y_{11},...,Y_{nn})\sim Multinomial$

$$P(Y=y)=\frac{n!}{y_{11}!...y_{nn}!} \prod_{i,j}\pi_{ij}^{y_{ij} }$$

Using MLE subjecting to $\sum_{ij}\pi_{ij} = 1$, we get $\hat\mu_{ij} = y_{ij} / n$

With null hypothesis of independence we can get $\hat\mu_{ij} = \hat\mu_{i.}\hat\mu_{.j}$
Then we can use LRT where the full model contains the interaction terms

$$\log\mathcal L_F = \sum_{ij}y_{ij}\log(y_{ij}/n)$$

$$\log\mathcal L_R = \sum_{ij}y_{ij}\log(y_{i.}y_{.j}/nn)$$

$$d.f. = (IJ-1)-(I+J-2)$$ 

lose 1 for constraint $\sum_{ij}\pi_{ij} = 1$, lose 2 for constraints $\sum_i \pi_{i.}=1,\sum_j\pi_{.j}=1$

## Fisher's Exact Test
- randomization test
- appropriate for small sample size
- assumes the row and column totals are fixed
- p-value is calculated from hypergeometrix distribution
  
$$P=\frac{ {a+b\choose a}{c+d\choose c} }{ {n\choose a+c} }$$

## Poisson Regression
- counts aren't fixed
- treat IJ count as realizations of a Possion random variable

Compare the interactions term

Three-way interactions

 - complete independence: does not have any interaction terms
 - block independence: joint probability of two factors (say A,B) is independent of the third (C). Then include the interaction term between $AB$
 - partial independence: $P(AB\mid C)=P(A\mid C)P(B\mid C)$, AB are conditionally independent on $C$. Include interactions between $AC,BC$
 - Uniform association: include all two-way interactions
 - Saturated model: include three-way interactions


