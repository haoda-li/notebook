# Real Number Construction

## Decimal expansion

Given $r\in\mathbb{R}^+$  

 1. find $q\in\mathbb{N}^+, q\leq r\le q+1$  
 2. So we find next decimal place $d_1/10 \leq r- q < d_1 / 10 + 1/10$  
 3. repeat $\frac{d_k}{10^k} \leq r - q - \sum _1^{k-1} \frac{d^m}{10^m} < \frac{d_k}{10^k} + 10^{-k}$
   
So that $r = q.d_1d_2d_3...$

### _Def'n_. Terminating and repeating 
__terminating__ decimal expansion $q.d_1d_2...d_{m_0}$  
__repeating__ decimal expansion $q.d_1...d_k\overline{d_{k+1}...d_n}$(ex. $1/35 = 0.0287154\overline{287154}$)


### Thrm. 1
__Claim__ $\forall x\in \mathbb{R}^+$ is rational IFF $x$ has a decimal expansion that is either terminating or repeating  

_proof_.   
$\Leftarrow$  
Assume $x$ is terminating, 

$$x = q.d_1...d_{n_0} = q + \sum_1^n \frac{d_m}{10^m} \in \mathbb{Q}$$

Assume $x$ is repeating, 

$$q.d_1...d_k\overline{d_{k+1}...d_m}$$

Known that $d_1...d_k$ part is rational, the remaining $0.0...0\overline{d_{k+1}...d_m}$ equals

$$10^{-k}(\sum_{m=1}^n \sum_{l=0}^\infty \frac{d'_m}{10^{nl + m}})$$ 

since the number is repeating, we denote $d'_0,...,d'_n$ be the repeated digits  

$$10^{-k}\sum_{m=1}^n d'_m 10^{-m} (\sum_{l=0}^\infty 10^{-nl})$$

Using geometeric series, we have 

$$10^{-k}\sum_{m=1}^n d'_m 10^{-m} (1 - 10^{-n})^{-1} = \sum_{m=1}^n\frac{d'_m 10^n}{10^{m+k}(10^n - 1)}$$


$\Rightarrow$  
Take $l, m \in\mathbb{Z}^+， x = l/m$.  
By Euclidean division, $l = d_0m + r_0/m$ where $d_0\in\mathbb{Z}^+$ is the quotient, $r_0\in\mathbb{Z}^+$ is the remainder, $r_0<m$.  

### Lemma 2

$$\forall n\in \mathbb{N}. l/m = \sum_{m=0}^n \frac{d_m}{ 10^{m}} + \frac{r_n} {10^{n}m}$$

_proof_. (induction by further Euclidean division)

Suppose $\exists i, r_i = 0$, then is terminated  
Suppose $\forall k$ WTS repeating.  

 - since $r_k$ is a remainder, it can only choose from $r_k \in \{1, ..., m - 1\}$. Then $\exists k_1, k_2. r_{k_1} = r_{k_2}$.  
  
 Then by uniqueness of Euclidean division, it is repeated. 


### Def'n. Irrational Numbers
$x$ is irrational if $x\in\mathbb{Q}^c$, i.e. $\not\exists l, m\in\mathbb{Z}^+ s.t. x = l/m$

### Claim 3
$\forall x, y \in \mathbb{R}, x < y \Rightarrow \exists r\in\mathbb{R}. x < r < y$ and $r$ is terminating.  

_proof_. consider the decimal expansions of $x = x_0.x_1..., y = y_0.y_1...$, then exists the smallest $k$ where $x_k + 1 \leq y_k$, then find the next $m>k$ where $x_m \neq 9$.
Then construct $r = x_0.x_1...[x_m + 1]y_{m+1}y_{m+2}...$

## Construction From Cauchy Sequence

Consider the space of Cauchy sequence $C_Q = \{(y_n): y_n\in \mathbb{Q}\}$  

$x_n, y_n$ Cauchy, then

__Proposition 1__ $x_n + y_n$ Cauchy.   
_proof._ Let $\epsilon > 0, N_\epsilon = \max(N^x_{\epsilon/2}, N^y_{\epsilon/2})$

__Proposition 2__ $x_ny_n$ Cauchy  
_proof._ 

\begin{align*}
|x_ny_n - x_my_m| &= |x_ny_m - x_my_n + x_my_n - x_my_m| \\
&\leq |y_n(x_n-x_m)| + |x_m(y_n - y_m)|\\
&\leq B_2|x_n - x_m|  B_1|y_n - y_m| &\text{Cauchy implies bounded}\\
\end{align*}

Want this to be less than $\epsilon > 0$. 
Therefore, take $|x_n - x_m| \leq \epsilon / 2B_2, |y_n - y_m|\leq \epsilon/2B_1$

__Proposition 3__ Additive identity $r_0=(0,0,0,...)$, multiplicative identity $r_1 = (1,1,1,...)$  

$$a+r_o = \{a_1 + 0, a_2 + 0,...\}=\{a_n\} = a$$

$$ar_1 = \{a_11, a_21,...\} = \{a_n\} = a$$


### Def'n. Equivalence Class
$(x_n)\sim (y_n)$ IFF $\lim_{n\rightarrow \infty}|x_n -y_n| = 0$  

__Example__ $x_n = 1/n, y_n = 0$

__Example__ Let $\pi=p_0.p_1p_2...$, take $x_n = p_0.p_1...p_n, y_n = p_0.p_1...p_n1 = x_n + 10^{-(n+1)}$. 

Let $\mathbb{R}:=$equivalence class on $C_Q$, so for any $x\in\mathbb{R}$ you can find a Cauchy sequence $(x_n)$ in $\mathbb{Q}$ s.t. $\lim_{n\rightarrow\infty}|x_n - x| = 0$
