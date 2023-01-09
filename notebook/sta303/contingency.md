# Factor independence and Contingency Table

## Case Study: Framingham Heart Study

Data considered:

- n = 1329 men
- X = Cholesterol measurement in 1948 (mg/dl)
- Y = after 10 years, did they developed CVD (present/absernt)

### Binomial Sampling
Let $\pi_H=p(present\mid high),\pi_L = P(present\mid low)$.

Hypothese: $H_0: \pi_H = \pi_L, H_a: \pi_H \neq \pi_L$

Assumptions: 

 - depending on level of cholesterol, each person is a Bernoulli trial with chance of developing CVD as $n_H = 284, n_L = 1043$. 
 - Then for fixed $n_H, n_L$, the count of the number of people who develop CVD $y_H\sim Binomial(n_H=286,\pi_H)$ $y_L\sim Binomial(n_L=1043,\pi_L)$
 - Then estimate of $\pi_H-\pi_L$ is $\hat\pi_H-\hat\pi_L$ where $\hat\pi_H = y_H/n_H, \hat\pi_L = y_L/n_L$ are the sample proportions.
 - $var(\hat\pi_H-\hat\pi_L) = var(\hat\pi_H) + var(\hat\pi_L)\\=n_H\pi_H(1-\pi_H)/n^2_H + n_L\pi_L(1-\pi_L)/n^2_L\\= \pi_H(1-\pi_H)/n_H+\pi_L(1-\pi_L)/n_L$
 - $se(\hat\pi_H-\hat\pi_L) = \sqrt{\hat\pi_c(1-\hat\pi_c)(n_H^{-1}+n_L^{-1})}$ where $\hat\pi_c=\frac{y_L+y_H}{n+L + n_H}$ is the combined sample proportion
 - By CLT, the test statistic $\sim N(0,1)$

Test statistic: $\frac{\hat\pi_H-\hat\pi_L}{se(\hat\pi_H-\hat\pi_L)}=5.575$

p-value $2P(Z\geq 5.575)<0.05$

Conclusion: We have strong evidence that the probability of developing CVD is not the same for High and Low cholesterol groups.



```R
cvd<-matrix(c(41,245,51,992), nrow=2,byrow=TRUE)
dimnames(cvd)<-list(c("High","Low"), c("Present","Absent"))
names(dimnames(cvd))<-c("Cholesterol","Cardio Vascular Disease")
print(cvd)
```

               Cardio Vascular Disease
    Cholesterol Present Absent
           High      41    245
           Low       51    992
    


```R
# estimate for pi
pi_h = 41/(41+245)
pi_l = 51/(51+992)
print(pi_h)
print(pi_l)
```

    [1] 0.1433566
    [1] 0.04889741
    


```R
# sample size 
n_h = 41 + 245
n_l = 51 + 992
conf.level = 0.95
crit.val = qnorm(1-(1-conf.level)/2)
crit.val
```


    1.95996398454005



```R
# standard error
se.hat = sqrt(pi_h * (1 - pi_h)/n_h + pi_l * (1 - pi_l)/n_l)
se.hat
```


    0.0217710596635901



```R
# 95% CI
c((pi_h-pi_l)-crit.val*se.hat, (pi_h-pi_l)+crit.val*se.hat)
```

    0.0517887391972153
    0.137129724889034




```R
# easier way for bonimial sampling
prop.test(cvd, correct=FALSE)
```


    
    	2-sample test for equality of proportions without continuity
    	correction
    
    data:  cvd
    X-squared = 31.082, df = 1, p-value = 2.474e-08
    alternative hypothesis: two.sided
    95 percent confidence interval:
     0.05178874 0.13712972
    sample estimates:
        prop 1     prop 2 
    0.14335664 0.04889741 
    



```R
# or chisq test
chisq.test(cvd, correct=F)
```


    
    	Pearson's Chi-squared test
    
    data:  cvd
    X-squared = 31.082, df = 1, p-value = 2.474e-08
    



```R
# Don't use this, provide different result from the manual way
prop.test(cvd)
```


    
    	2-sample test for equality of proportions with continuity correction
    
    data:  cvd
    X-squared = 29.633, df = 1, p-value = 5.221e-08
    alternative hypothesis: two.sided
    95 percent confidence interval:
     0.0495611 0.1393574
    sample estimates:
        prop 1     prop 2 
    0.14335664 0.04889741 
    


The CI does not include 0. 

## Contingency Table
Have a row factor with $I$ levels and a column factor with $J$ levels

Then, define $P(C=i,R=j)=\pi_{ij}, P(C=i)=\pi_{i\cdot}, P(R=j)=\pi_{\cdot j}$

Hypothesis: $H_0: \pi_{ij} = \pi_{i\cdot}\pi_{\cdot j}, H_a: \pi_{ij} \neq\pi_{i\cdot}\pi_{\cdot j}$
null: there is no relationship between the two factors

For each cell, estimated expected cell count $\hat\mu_{ij} = n\hat\pi_i\hat\pi_j = y_{i\cdot}y_{\cdot j}/n$

Test statistic: $X^2 = \sum_{j=1}^J\sum_{i=1}^I \frac{(y_{ij}-\hat\mu_{ij})^2}{\hat\mu_{ij}}\sim \chi^2_{(I-1)(J-1)}$

If $var(y)=E(y)=\mu\Rightarrow y\sim Poisson(\mu)$

For this case, test statistic: $31.08\sim \chi^2_{(2-1)(2-1)}$, p-value $<0.0001$

Strong evidence that the two factors are not independent, CVD status depends on cholesterol level.

When $I=J=2$, the chi-square test of independence is equivalent to comparing two proportions.

### Formal approach
Let $Y_{ij}$ be r.v. representing the number of observations in cell $(i,j)$.

Observe $y_{ij}$ be observed cell counts

Then multinomial 

$$P(Y=y)=\frac{n!\pi_{11}^{y_{11}}\pi_{12}^{y_{12}}\pi_{21}^{y_{21}}\pi_{22}^{y_{22}}} {y_{11}!y_{12}!y_{21}!y_{22}!}\sim Multinomial(n,\pi_{11},\pi_{12},\pi_{21},\pi_{22})$$

Log-likelihood is 

$$\log\mathcal{L}=\sum_{j=1}^2\sum_{i=1}^2 y_{ij}\log\pi_{ij}+\log{n\choose y_{11}y_{12}y_{21}y_{22}}$$

Maximize $\log\mathcal{L}$ w.r.t. $\pi$'s and $\sum\sum\pi_{ij}=1$, then $\hat\pi_{ij}=y_{ij}/n$

Under $H_0: \pi_{ij}=\pi_{i\cdot}\pi_{\cdot j}$, can substitute $\pi_{ij}$ and maximize the column and row $\pi$'s. 

$$G^2 = -2\log(\mathcal{L}_R/\mathcal{L}_F)\sim\chi^2_{(I-1)(J-1)}$$

To obtain the d.f.  
`df(Unrestrcited / FULL)`$-$`df(Independence/REDUCED)`  
$=$`#parameters in FULL`($\pi_{ij}$) $-$ `#parameters in REDUCED`($\pi_{i\cdot},\pi_{\cdot j}$)  
$= IJ-1-(I+J-2)$  
$-1$ because constraint $\sum\sum\pi_{ij}=1$  
$-2$ because constraint $\sum\pi_{i\cdot}=1,\sum\pi_{\cdot j}=1$

## Case Study 7: Three Way Contingency

__A__ alcohol use 1 = True, 2 = False  

**M** marijuana use

__C__ cigarette use


```R
A=c(1,1,1,1,2,2,2,2)
C=c(1,1,2,2,1,1,2,2)
M=c(1,2,1,2,1,2,1,2)
Y=c(911,538,44,456,3,43,2,279)
A=as.factor(A)
C=as.factor(C)
M=as.factor(M)
ACM=cbind(A,C,M, Y)
ACM
```


<table>
<caption>A matrix: 8 × 4 of type dbl</caption>
<thead>
	<tr><th scope=col>A</th><th scope=col>C</th><th scope=col>M</th><th scope=col>Y</th></tr>
</thead>
<tbody>
	<tr><td>1</td><td>1</td><td>1</td><td>911</td></tr>
	<tr><td>1</td><td>1</td><td>2</td><td>538</td></tr>
	<tr><td>1</td><td>2</td><td>1</td><td> 44</td></tr>
	<tr><td>1</td><td>2</td><td>2</td><td>456</td></tr>
	<tr><td>2</td><td>1</td><td>1</td><td>  3</td></tr>
	<tr><td>2</td><td>1</td><td>2</td><td> 43</td></tr>
	<tr><td>2</td><td>2</td><td>1</td><td>  2</td></tr>
	<tr><td>2</td><td>2</td><td>2</td><td>279</td></tr>
</tbody>
</table>



### Model 1. Complete Independence 
$P(ACM)=P(A)P(C)P(M)$ - the three factors are mutually independent

$H_0: \pi_{ijk} = \pi_{i..}\pi_{.j.}\pi_{k..}$ for all $i,j,k$.   
$H_a: \pi_{ijk} \neq \pi_{i..}\pi_{.j.}\pi_{k..}$

$\log(\mu_{ijk}) = \beta_0+\beta_1 \mathbb{I}_C + \beta_2 \mathbb{I}_C + \beta_3 \mathbb{I}_M$

MLE 

$$\hat\mu_{ijk}=n\hat\pi_{ijk} = n\hat\pi_{i..}\hat\pi_{.j.}\hat\pi_{..k}=\frac{ny_{i..}y_{.j.}y_{..k}}{nnn}$$


```R
mod_A.C.M=glm(Y~A+C+M, family=poisson) # Additive
summary(mod_A.C.M)
```


    
    Call:
    glm(formula = Y ~ A + C + M, family = poisson)
    
    Deviance Residuals: 
          1        2        3        4        5        6        7        8  
     14.522   -7.817  -17.683    3.426  -12.440   -8.436   -8.832   19.639  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.29154    0.03667 171.558  < 2e-16 ***
    A2          -1.78511    0.05976 -29.872  < 2e-16 ***
    C2          -0.64931    0.04415 -14.707  < 2e-16 ***
    M2           0.31542    0.04244   7.431 1.08e-13 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.5  on 7  degrees of freedom
    Residual deviance: 1286.0  on 4  degrees of freedom
    AIC: 1343.1
    
    Number of Fisher Scoring iterations: 6
    


### Model 2. Block Independence 
$P(AC\mid M)= P(AC)$ - Joint probability of alcohol and cigarette use is independent of marijuana use; Alcohol and cigarette use
are associated. 

$H_0: \pi_{ijk} = \pi_{ij.}\pi_{k..}$ for all $i,j,k$.   
$H_a: \pi_{ijk} \neq \pi_{ij.}\pi_{k..}$

$\log(\mu_{ijk}) = \beta_0+\beta_1 \mathbb{I}_C + \beta_2 \mathbb{I}_C + \beta_3 \mathbb{I}_M+\beta_4\mathbb{I}_A\mathbb{I}_C$

MLE

$$\hat\mu_{ijk}=n\hat\pi_{ijk} = n\hat\pi_{ij.}\hat\pi_{..k}=\frac{ny_{ij.}y_{..k}}{nn}$$


```R
mod_AC.M=glm(Y~M+A*C, family=poisson) #Block AC
summary(mod_AC.M)
```


    
    Call:
    glm(formula = Y ~ M + A * C, family = poisson)
    
    Deviance Residuals: 
          1        2        3        4        5        6        7        8  
     11.297  -11.092  -13.996    9.045   -4.648    2.917  -14.721    8.286  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.41539    0.03595 178.451  < 2e-16 ***
    M2           0.31542    0.04244   7.431 1.08e-13 ***
    A2          -3.44999    0.14976 -23.036  < 2e-16 ***
    C2          -1.06402    0.05187 -20.515  < 2e-16 ***
    A2:C2        2.87373    0.16730  17.178  < 2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46  on 7  degrees of freedom
    Residual deviance:  843.83  on 3  degrees of freedom
    AIC: 902.87
    
    Number of Fisher Scoring iterations: 6
    



```R
mod_AM.C=glm(Y~C+A*M, family=poisson) #Block AM
summary(mod_AM.C)
```


    
    Call:
    glm(formula = Y ~ C + A * M, family = poisson)
    
    Deviance Residuals: 
           1         2         3         4         5         6         7         8  
     10.6031   -4.6398  -19.7664    5.9142   -0.1592  -14.1425    0.2114   13.4104  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.44142    0.03573 180.280   <2e-16 ***
    C2          -0.64931    0.04415 -14.707   <2e-16 ***
    A2          -5.25227    0.44838 -11.714   <2e-16 ***
    M2           0.04003    0.04531   0.883    0.377    
    A2:M2        4.12509    0.45294   9.107   <2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46  on 7  degrees of freedom
    Residual deviance:  939.56  on 3  degrees of freedom
    AIC: 998.61
    
    Number of Fisher Scoring iterations: 5
    



```R
mod_A.CM=glm(Y~A+C*M, family=poisson) #Block CM
summary(mod_A.CM)
```


    
    Call:
    glm(formula = Y ~ A + C * M, family = poisson)
    
    Deviance Residuals: 
           1         2         3         4         5         6         7         8  
      4.4691    1.7907    0.7207   -7.2723  -15.2958   -4.8889   -2.1064   13.9760  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.66273    0.03417 194.969   <2e-16 ***
    A2          -1.78511    0.05976 -29.872   <2e-16 ***
    C2          -2.98919    0.15111 -19.782   <2e-16 ***
    M2          -0.45308    0.05306  -8.539   <2e-16 ***
    C2:M2        3.22431    0.16098  20.029   <2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46  on 7  degrees of freedom
    Residual deviance:  534.21  on 3  degrees of freedom
    AIC: 593.26
    
    Number of Fisher Scoring iterations: 6
    


### Model 3. Partial Independence
$P(AC\mid M)=P(A\mid M)P(C\mid M)$. Alcohol and cigarette use are conditionally independent given marijuana use; Alcohol and marijuana use are associated, and cigarette and marijuana use are associated

$H_0:\pi_{ijk} = \pi_{i.k}\pi_{.jk}/\pi_{..k}$  
$H_a:\pi_{ijk} \neq \pi_{i.k}\pi_{.jk}/\pi_{..k}$

$\log(\mu_{ijk}) = \beta_0+\beta_1 \mathbb{I}_C + \beta_2 \mathbb{I}_C + \beta_3 \mathbb{I}_M+\beta_4\mathbb{I}_A\mathbb{I}_M+\beta_5\mathbb{I}_C\mathbb{I}_M$

MLE

$$\hat\mu_{ijk}=n\hat\pi_{ijk} = n\hat\pi_{.jk}\hat\pi_{i.k} / \hat\pi_{..k}=y_{ijk}y_{i.k}/y_{..k}$$



```R
mod_AC.AM=glm(Y~A*C+A*M, family=poisson) #Partial A
summary(mod_AC.AM)
```


    
    Call:
    glm(formula = Y ~ A * C + A * M, family = poisson)
    
    Deviance Residuals: 
           1         2         3         4         5         6         7         8  
      7.2238   -7.7739  -15.8396   11.3171    2.0272   -0.3442   -1.2388    0.1379  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.56527    0.03499 187.643   <2e-16 ***
    A2          -6.91715    0.46893 -14.751   <2e-16 ***
    C2          -1.06402    0.05187 -20.515   <2e-16 ***
    M2           0.04003    0.04531   0.883    0.377    
    A2:C2        2.87373    0.16730  17.178   <2e-16 ***
    A2:M2        4.12509    0.45294   9.107   <2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46  on 7  degrees of freedom
    Residual deviance:  497.37  on 2  degrees of freedom
    AIC: 558.41
    
    Number of Fisher Scoring iterations: 5
    



```R
mod_AC.CM=glm(Y~A*C+C*M, family=poisson) #Partial C
summary(mod_AC.CM)
```


    
    Call:
    glm(formula = Y ~ A * C + C * M, family = poisson)
    
    Deviance Residuals: 
          1        2        3        4        5        6        7        8  
     0.8401  -1.0667   2.4964  -0.6743  -6.0678   5.0235  -4.5440   0.8867  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.78658    0.03340 203.212   <2e-16 ***
    A2          -3.44999    0.14976 -23.036   <2e-16 ***
    C2          -3.40390    0.15354 -22.170   <2e-16 ***
    M2          -0.45308    0.05306  -8.539   <2e-16 ***
    A2:C2        2.87373    0.16730  17.178   <2e-16 ***
    C2:M2        3.22431    0.16098  20.029   <2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.461  on 7  degrees of freedom
    Residual deviance:   92.018  on 2  degrees of freedom
    AIC: 153.06
    
    Number of Fisher Scoring iterations: 6
    



```R
mod_AM.CM=glm(Y~A*M+C*M, family=poisson) #Partial M
summary(mod_AM.CM)
```


    
    Call:
    glm(formula = Y ~ A * M + C * M, family = poisson)
    
    Deviance Residuals: 
          1        2        3        4        5        6        7        8  
     0.0584   4.5702  -0.2619  -4.3441  -0.8663  -9.7716   2.2287   6.8353  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.81261    0.03316 205.450   <2e-16 ***
    A2          -5.25227    0.44837 -11.714   <2e-16 ***
    M2          -0.72847    0.05538 -13.154   <2e-16 ***
    C2          -2.98919    0.15111 -19.782   <2e-16 ***
    A2:M2        4.12509    0.45294   9.107   <2e-16 ***
    M2:C2        3.22431    0.16098  20.029   <2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46  on 7  degrees of freedom
    Residual deviance:  187.75  on 2  degrees of freedom
    AIC: 248.8
    
    Number of Fisher Scoring iterations: 5
    


### Model 4. Uniform Association
Association among all pairs

$$\log(\mu_{ijk}) = \beta_0+\beta_1 \mathbb{I}_C + \beta_2 \mathbb{I}_C + \beta_3 \mathbb{I}_M+\beta_4\mathbb{I}_A\mathbb{I}_M+\beta_5\mathbb{I}_C\mathbb{I}_M + \beta_6\mathbb{I}_A\mathbb{I}_C$$


```R
mod_AM.AC.CM=glm(Y~A*M+A*C+C*M, family=poisson) #Uniform
summary(mod_AM.AC.CM)
```


    
    Call:
    glm(formula = Y ~ A * M + A * C + C * M, family = poisson)
    
    Deviance Residuals: 
           1         2         3         4         5         6         7         8  
     0.02044  -0.02658  -0.09256   0.02890  -0.33428   0.09452   0.49134  -0.03690  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.81387    0.03313 205.699  < 2e-16 ***
    A2          -5.52827    0.45221 -12.225  < 2e-16 ***
    M2          -0.52486    0.05428  -9.669  < 2e-16 ***
    C2          -3.01575    0.15162 -19.891  < 2e-16 ***
    A2:M2        2.98601    0.46468   6.426 1.31e-10 ***
    A2:C2        2.05453    0.17406  11.803  < 2e-16 ***
    M2:C2        2.84789    0.16384  17.382  < 2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46098  on 7  degrees of freedom
    Residual deviance:    0.37399  on 1  degrees of freedom
    AIC: 63.417
    
    Number of Fisher Scoring iterations: 4
    


### Saturated Model
$$\log(\mu_{ijk}) = \beta_0+\beta_1 \mathbb{I}_C + \beta_2 \mathbb{I}_C + \beta_3 \mathbb{I}_M+\beta_4\mathbb{I}_A\mathbb{I}_M+\beta_5\mathbb{I}_C\mathbb{I}_M + \beta_6\mathbb{I}_A\mathbb{I}_C + \beta_7\mathbb{I}_A\mathbb{I}_C\mathbb{I}_M$$

this always fits the data perfectly


```R
mod_ACM=glm(Y~A*C*M, family=poisson) #Saturated
summary(mod_ACM)
```


    
    Call:
    glm(formula = Y ~ A * C * M, family = poisson)
    
    Deviance Residuals: 
    [1]  0  0  0  0  0  0  0  0
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.81454    0.03313 205.682  < 2e-16 ***
    A2          -5.71593    0.57830  -9.884  < 2e-16 ***
    C2          -3.03035    0.15435 -19.633  < 2e-16 ***
    M2          -0.52668    0.05437  -9.686  < 2e-16 ***
    A2:C2        2.62489    0.92583   2.835  0.00458 ** 
    A2:M2        3.18927    0.59962   5.319 1.04e-07 ***
    C2:M2        2.86499    0.16696  17.159  < 2e-16 ***
    A2:C2:M2    -0.58951    0.94236  -0.626  0.53160    
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance:  2.8515e+03  on 7  degrees of freedom
    Residual deviance: -4.1522e-14  on 0  degrees of freedom
    AIC: 65.043
    
    Number of Fisher Scoring iterations: 3
    



```R
muhats<-predict.glm(mod_AM.AC.CM, type="response")
cbind(A, C, M, Y, muhats)
```


<table>
<caption>A matrix: 8 × 5 of type dbl</caption>
<thead>
	<tr><th></th><th scope=col>A</th><th scope=col>C</th><th scope=col>M</th><th scope=col>Y</th><th scope=col>muhats</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>1</td><td>1</td><td>1</td><td>911</td><td>910.38317</td></tr>
	<tr><th scope=row>2</th><td>1</td><td>1</td><td>2</td><td>538</td><td>538.61683</td></tr>
	<tr><th scope=row>3</th><td>1</td><td>2</td><td>1</td><td> 44</td><td> 44.61683</td></tr>
	<tr><th scope=row>4</th><td>1</td><td>2</td><td>2</td><td>456</td><td>455.38317</td></tr>
	<tr><th scope=row>5</th><td>2</td><td>1</td><td>1</td><td>  3</td><td>  3.61683</td></tr>
	<tr><th scope=row>6</th><td>2</td><td>1</td><td>2</td><td> 43</td><td> 42.38317</td></tr>
	<tr><th scope=row>7</th><td>2</td><td>2</td><td>1</td><td>  2</td><td>  1.38317</td></tr>
	<tr><th scope=row>8</th><td>2</td><td>2</td><td>2</td><td>279</td><td>279.61683</td></tr>
</tbody>
</table>



## Inference for log-linear models

### Model assumptions
 - independent quantities being counted
 - Large enough sample size for MLE asymptotic tests to hold (most $\hat\mu_{ijk}\geq 5$)
 - Cross-classified counts follow a Poisson distribution $var(y_{ijk})=\mu_{ijk}$. If not, the deviance is very large("extra-Poisson" variation)
 - Correct form 
      - $\log(E(Y))$ is linear in $\beta$'s
      - All relevant variables included
      - No outliers
      - Agreement of predicted and observed count
      - Check deviance GOF test

### Model comparisons
__Example__ For the uniform association model, is the CM interaction needed? / Does the (AC,CM) model fit just as well?

Uniform association model
$\log(\mu_{ijk}) = \beta_0+\beta_1 \mathbb{I}_C + \beta_2 \mathbb{I}_C + \beta_3 \mathbb{I}_M+\beta_4\mathbb{I}_A\mathbb{I}_M+\beta_5\mathbb{I}_C\mathbb{I}_M + \beta_6\mathbb{I}_A\mathbb{I}_C$

$H_0: \beta_6=0$, reduced model is better no CM interaction
$H_a: \beta\neq 0$ full model is better

Wald: test-statistic: 17.382.   
$p<2\times 10^{-16}$.

LRT: test-statistic: 497.37 - 0.37399 = 497  
$p<2\times 10^{-16}$

Conclusion: Very strong evidence that we should keep the CM interaction term. The uniform association model is better than the model without CM interaction term. 



```R
mod_AM.AC=glm(Y~A+M+C+A:C + A*M, family=poisson) #Uniform
summary(mod_AM.AC)
```


    
    Call:
    glm(formula = Y ~ A + M + C + A:C + A * M, family = poisson)
    
    Deviance Residuals: 
           1         2         3         4         5         6         7         8  
      7.2238   -7.7739  -15.8396   11.3171    2.0272   -0.3442   -1.2388    0.1379  
    
    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept)  6.56527    0.03499 187.643   <2e-16 ***
    A2          -6.91715    0.46893 -14.751   <2e-16 ***
    M2           0.04003    0.04531   0.883    0.377    
    C2          -1.06402    0.05187 -20.515   <2e-16 ***
    A2:C2        2.87373    0.16730  17.178   <2e-16 ***
    A2:M2        4.12509    0.45294   9.107   <2e-16 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    (Dispersion parameter for poisson family taken to be 1)
    
        Null deviance: 2851.46  on 7  degrees of freedom
    Residual deviance:  497.37  on 2  degrees of freedom
    AIC: 558.41
    
    Number of Fisher Scoring iterations: 5
    


### Deviance GOF test
Compare fitted model to saturated model
Small deviance / large p-values

 - fitted model is adequate
 - test is not powerful enough to detect inadequacies

Large deviance / small p-value

 - Fitted model is not adequate, consider a more complex model OR
 - underlying distribution is not adequately modeled by the Poisson distribution OR
 - There are severe outliers 

### Outliers
 - raw residual: $y_{ijk} - \hat\mu_{ijk}$
 - Pearson residuals: $(y_{ijk} - \hat\mu_{ijk})/\sqrt{\hat\mu_{ijk}}$
 - Deviance residuals: $sign(y_{ijk} - \hat\mu_{ijk})\sqrt{2(y_{ijk}\log(y_{ijk}/\hat\mu_{ijk}))-y_{ijk}+\hat\mu_{ijk}}$

Rule of thumb: outliers if Pearson or Deviance residual $>3$, is the sample size if small, then $>2$. 

### Extra-Poisson variation
 - Check if $Deviance/df > 1$
 - If other problems are ruled out, then include a dispersion paramter OR use negative binomial regression
 
