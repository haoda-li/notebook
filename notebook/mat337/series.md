# Series

## _Thrm 1_. 
__Claim__ For $S_n(x)= \sum_{k=1}^n a_k(x)$, $(S_n,\|\cdot\|_\infty)$ Cacuhy IFF $S_n \rightarrow^{u.c.}S$  

_proof_. $\Rightarrow$  
Find $S(x)$ s.t. $S_k(x)\rightarrow^{p.w.}S(x)$.  

\begin{align*}
|S_k(x)-S(x)| &\leq |S_k(x)-s_n(x)| + |s_n(x)-S(x)| \\
&\leq \epsilon + |S_n(x)-S(x)| &\text{by p.w. convergence} \\
&\leq \epsilon + \sup_{x\in\mathbb{R}} |S_n(x)-S(x)|\\
\end{align*}

Apply limit on $n\rightarrow\infty$, since $n$ is independent on $k$, 
$|S_k(x)-S(x)|\leq \epsilon + \lim_{n\rightarrow\infty}\sup_{x\in\mathbb{R}} |S_n(x)-S(x)| = \epsilon + 0\Rightarrow \|S_k-S\|_\infty \leq \epsilon$

### Example 1
$S_n :=\sum_{k=1}^n \frac{x^k}{k!}\rightarrow^{u.c.}\sum^\infty \frac{x^k}{k!},x\in [-R,R]$  

\begin{align*}
\|S_k - S_n\|_\infty &= \sup_{|x|\leq R} |\sum^{n+m}\frac{x^k}{k!} - \sum^n \frac{x^k}{k!}| \\
&= \sup|\sum_{n+1}^{n+m}\frac{x^k}{k!}| \\
&\leq \sum \frac{R^k}{k!} = e^R - \sum^n \frac{R^k}{k!}\rightarrow 0
\end{align*}

### Example 2
$S_n = \sum^n \frac{x^2}{k(k+x^2)}, x\in \mathbb R$  

_proof_. $S_n\rightarrow^{p.w.}S$ but $S_n \not\rightarrow^{u.c.}S$  
Fix $x_0$, $S_n \leq x^2 \sum_{k=1}^n k^{-2} \leq x^2\pi^2/6 < \infty$

\begin{align*}
\|S_n-S\|_\infty &= \|\sum_{k\geq n}\frac{x^2}{k(k+x^2)}\|_\infty \\
&= \sup_{x\in\mathbb R}|\sum_{k\geq n}\frac{x^2}{k(k+x^2)}| \\
&\geq \sup_{|x|\leq N}|\sum_{k\geq n} \frac{1}{k}\frac{x^2}{k+x^2}|\\
\text{take N large so that }\frac{x^2}{k+x^2}&\geq 1-\epsilon \text{ and k is fixed} \\
&\geq \sum_{k\geq n}\frac{1-\epsilon}{k} = \infty
\end{align*}

## _Thrm 2_. M-Test
For $S_n(x) = \sum_{k=1}^n a_k(x), \|a_k\|_\infty \leq M_k \land \sum M_k < \infty \Rightarrow S_n \rightarrow^{u.c.}S < \infty$.  

_proof_. We'll show Cauchy so that uniform convergent.  

\begin{align*}
\|S_n - S_{n+m}\|_\infty &= \sup|\sum_{n+1}^{n+m}a_k(x)| \\ 
&\leq \sum_{n+1}^{n+m} \sup|a_k(x)| \\
&\leq \sum_{n+1}^{n+m} M_k < \epsilon \text{ for N large}
\end{align*}

### Example 1
$S_n = \sum_{k=1}^n (-x^2)^k\rightarrow^{u.c.}S, x\in [-r,r]\subset (-1,1)$ but not for $x\in(-1,1)$  

_proof_. For $x\in [-r,r]$.  

$$\|(-x^2)^k\| \leq r^{2k} =:M_k$$

Since $\sum^\infty r^{2k} = (1-r^2)^{-1}-1 < \infty$, apply M-test, $S_n\rightarrow^{u.c.}S$

However, take $x\in(-1,1)$

\begin{align*}
\|S_n - S_{m+n}\|_\infty &= \sup_{x\in(-1,1)}|\sum_n^{n+m}(-x^2)^k| \\
\text{take }x_0 = 0.5^{1/2N} &\in (-1,1) \text{ and }n + m\leq N \\
&\geq |\sum_n^{n+m} (-1)^k 0.5^{k/N}| \\
&= |0.5^{n/N} + (-1)^{n+1}0.5^{\frac{n+1}{N}}| \\
&\sim 0.5^{n/N} &\text{ for N large} \\
&> \epsilon &\text{since }N\rightarrow\infty, 0.5^{n/N}\rightarrow 1
\end{align*}

Alternatively, take $\lim_{N\rightarrow\infty} = |-1+1-1+1...| = 1$ when $n+m$ is odd

### Example 2
For the series for $\arctan(x)$

\begin{align*}
\arctan(x) &= \int_0^x \frac{1}{1+t^2}dt \\
&= \int_0^x \sum (-t^2)^k dt &|x|<1 \\
&= \sum \int_0^x (-t^2)^k dt &\text{ICT} \\
&= \sum (-1)^k (\frac{t^{2k+1}}{2k+1}\Big|_0^x) \\
&= \sum (-1)^k (\frac{x^{2k+1}}{2k+1})
\end{align*}

$\arctan(1)$ is defined and $\arctan(1) = \pi/4$  

if $a_k \geq a_{k+1} > 0, |\sum^\infty a_k(-1)^k| \leq a_n$  

_proof_. 

\begin{align*}
\sup_{x\in[-1,1]}|S_n(x)-S(x)| &= \sup_{|x|\leq 1}|\sum^\infty_n (-1)^k \frac{x^{2k+1}}{2k+1}| \\
&= \sup_{|x|\leq 1} |\frac{x^{2n+1}}{2n+1}(-1)^n)|&\text{since }\frac{x^{2k+1}}{2k+1} \text{ decreasing} \\
&= \frac{1}{2n+1} \leq \epsilon
\end{align*}

### Claim  
For $f_n \in C([a,b])$ If $\exists c \in [a,b], f_n(c)\rightarrow \gamma, f'_n \rightarrow^{u.c.}g$, then $f_n \rightarrow f$ where $f'=g$  

_proof_. By FTC, 

\begin{align*}
f_n(x)&=f_n(c) + \int_c^x f'_n(t)dt \\
&\rightarrow\gamma + \int_c^x g(t)dt =:f(x) \\
|f_n(x)-f(x)| &= |f_n(x)-\gamma -\int_c^x g(t)dt| \\
&\leq |f_n(x)-\gamma| + |\int_c^x f'_n(t)-g(t)dt| \\
&\leq \epsilon/2 + \|f'_n - g\|_\infty \int_c^x dt \\
&= \epsilon/2 + \|f'_n-g\|(x-c)\\
&\leq \epsilon/2 + \frac{\epsilon}{b-a} (x-c)\\
&leq\epsilon
\end{align*}

__Corollary__ Swap derivative and sum  

$$S'_n \rightarrow^{u.c.}S\land\exists c. S_n(c)\rightarrow S(c) \Rightarrow d_x \sum a_k(x) = \sum d_x a_k(x)$$

## Def'n. Power Series
$\sum a_k x^k$


## Thrm 3. Ratio test
$\lim_\infty \frac{a_k}{a_{k+1}}< 1\Rightarrow \sum a_k < \infty$

## Thrm 4. Root test
$\lim\sup(|b_k|)^{1/k} < 1\Rightarrow \sum b_k < \infty$

### Example
$\sum \frac{x^n}{n}$ is u.c. for $x\in[-1,r], r< 1$

\begin{align*}
\sup_{x\in[-1,1)}|S_N - S| &= \sup_{x\in[-1,1)}|\sum_{n\geq N} x^n/n| \\
(i) \sup_{x\in[-1,0]}|\sum_{n\geq N}x_n /n | = \sup_{y\in[0,1]}&|\sum (-1)^n y^n/n| \leq \sup|y^N/N| \leq 1/N \quad\text{for large }N \\
(ii) \sup_{x\in[0,r]}|\sum_{n\geq N}x_n /n | = \sup_{x\in[0,r]}&\sum |x^n/n| \leq \sum r^n/n \leq \epsilon \quad\text{for large }N
\end{align*}

## Thrm 5. Hadamard's Theorem
Let $S(x)=\sum a_k x^k$ and $R^{-1} = \lim\sup(|a_n|)^{1/n}$, then $S_k \rightarrow^{u.c.}S, x\in (-R,R)$. 

_proof_. By root test, $\lim\sup (a_kx^k)^{1/k} < 1$  
$|a_k x^k|^{1/k} = |x|\lim\sup |a_k|^{1/k} = |x|R^{-1} < 1\Rightarrow |x|< R$  
Let $M_k := |a_k|r^k$ by root test, $\sum M_k < \infty$, then by M-test, $S_k \rightarrow^{u.c.}S, \forall x\in[-r,r]$

Ratio test can do the same work

### Example 1
$\sum \frac{2^{2k}}{k^2} x^{2k}$  
Let $y := x^2$,  

\begin{align*}
\frac{1}{R} &= \lim\sup (|\frac{2^{2k}}{k^2}|^{1/k}) \\
&= \lim\sup 2^2 k^{-2/k} \\
&= 4 \lim\sup k^{-2/k} &(i)\\
&= 4 \\
\Rightarrow R &= 1/4 \\ \\
(i) \log L  &= \lim\sup\log(k^{-2/k}) \\
\frac{2}{k}\log(\frac{1}{k}) \rightarrow 0 &\Rightarrow k^{-2/k}\rightarrow 1 \\
|y| \leq R = 1/4 &\Rightarrow |x|\leq 1/2
\end{align*}

So the interval of convergence $(-1/2, 1/2)$

### Example 2
__Claim__ $\sum a_k x^k$ with radius $R_1$, $\sum b_k x^k$ with radius $R_2$. Then   
(i) $\sum (a_k + b_k)x^k$ has radius $(R_1^{-1}+R_2^{-1})^{-1}$  
(ii) $\sum_{n=1}^\infty (\sum_{k=1}^n a_k b_{n-k})x^n$

Fix $\epsilon > 0$, take $N = \max(N_1, N_2)$ s.t. $\forall n \geq N_1. |a_n|^{1/n}\leq R_1^{-1} + \epsilon, \forall n \geq N_2. |b_n|^{1/n} \leq R_2^{-1}$. 

(i) _proof_. 

\begin{align*}
R^{-1} &= \lim\sup (|a_n| + |b_n|)^{1/n} \\
&\leq \lim\sup ((R_1^{-1}+\epsilon)^n + (R_2^{-1}+\epsilon)^n)^{1/n} \\
&\leq \lim\sup ((R_1^{-1}+\epsilon) + (R_2^{-1}+\epsilon))^{n/n} &\text{by }|a|^q + |b|^q \leq (|a|+|b|)^q, \forall q > 1 \\
& = R_1^{-1} + R_2^{-1} + 2\epsilon \\
&\rightarrow^{\epsilon\rightarrow 0} R_1^{-1} + R_2^{-1} \\
\Rightarrow R &= (R_1^{-1} + R_2^{-1})^{-1}
\end{align*}

(ii) _proof_.  Let $M_1 = \max(\{1\}\cup \{\frac{|a_k|}{(R_1^{-1} + \epsilon)^k}\}), M_2 = \max(\{1\}\cup \{\frac{|b_k|}{(R_2^{-1} + \epsilon)^k}\})$.  
Therefore, $|a_n|\leq M_1(R_1^{-1}+\epsilon)^n\land|b_n|\leq M_2(R_2^{-1}+\epsilon)^n. \forall n\geq 1$

\begin{align*}
R^{-1}&\leq \lim\sup (\sum^n M_1(R_1^{-1}+\epsilon)^kM_2(R_2^{-1} +\epsilon)^{n-k})^{1/n} \\
&= \lim\sup (M_1M_2)^{1/n}\lim\sup ((R_2^{-1}+\epsilon)^n \sum^n r^k)^{1/n} &r := \frac{R_1^{-1}+\epsilon}{R_2^{-1}+\epsilon} \\
\end{align*}

Take log limt for each lim sup, $\lim\sup(M_1M_2)^{1/n} = 1$.  
$\lim\sup (R_2^{-1}+\epsilon)^{n/n}\lim\sup (\frac{1-r^{n+1}}{1-r})^{1/n} = R_2^{-1}+\epsilon$  
If we swap $R_1,R_2$, similar conclusion can be made $=R_1^{-1}+\epsilon$, therefore $R^{-1} \leq \max(R_1^{-1}+\epsilon, R_2^{-1}+\epsilon)$

