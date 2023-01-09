# Function Approximations

## Taylor Series
$f\in C^n(\mathbb R)$, then $P_{n,a}(x):= \sum_{i=0}^n \frac{f^{(i)}(a)(x-a)^i}{i!}$ is the Taylor polynomial around $a$

### _Def'n_. Taylor Form remainder
$f\in C^n(\mathbb R)$ and $f^{(n+1)}$ exists, then $f(x) = P_{n,a}(x) + \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}, c\in [a,x]$

### _Thrm 1_. Uniqueness
__Claim__. Taylor polynomial is unique  

_proof_. Suppose $f(x) = \sum a_k(x-a)^k + \epsilon_1(x-a)^n = \sum b_k(x-a)^k + \epsilon_2(x-a)$,  
then $\sum(a_k-b_k)(x-a)^k + (\epsilon_1-\epsilon_2)(x-a)^n = 0$,  
by independence of the system of equations, $a_n = b_n, \epsilon_1 = \epsilon_2$

__Claim__. For $x,a\in [-R,R], P_{a,n}\rightarrow^{u.c.}f$  

_proof_. 

\begin{align*}
\|f(x)-P_{a,n}(x)\| &\leq \frac{|f^{(n+1)(c)}|}{(n+1)!}|x-a|^{n+1}\\
&\leq \frac{|f^{(n+1)(c)}|}{(n+1)!}|2R|^{n+1} \\
&\leq \frac{M}{(n+1)!}(2R)^{n+1} &\text{by EVT}\\
&\leq \frac{M}{n^ne^{-n}\sqrt{2\pi n}}(2R)^{n+1} &\text{Stirling's formula}\\
&\leq M(\frac{2Re}{n+1})^{n+1}\rightarrow 0 \text{ for large }n
\end{align*}



## _Thrm 2_.Weierstrass Theorem

 For any $a<b, f\in C[a,b]$, exists $p_n\rightarrow^{u.c.}f$  

_proof_. Define $g(x):[0,1]\rightarrow \mathbb R := f(a+x(b-a))$.  
Take $q_n\rightarrow^{u.c.}g$, consider $y=a+x(b-a)$, i.e. $x = \frac{y-a}{b-a}$  
Define $p_n(y):=q_n(\frac{y-a}{b-a}) = q_n(x)\rightarrow^{u.c.}f(y)$

### _Thrm 2_. 
If $f\in C^1[0,1]$, then $\exists \{p_n\}$ over $[0,1]$, $p_n\rightarrow^{u.c}f\land p_n'\rightarrow^{u.c}f'$

_proof_. Let $f\in C^1[0,1]$, then $f'\in C[0,1]$, take $q_n\rightarrow^{u.c}f'$,  
then let $p_n = \int_0^x q_n(x)dx + f(0)$, 

\begin{align*}
p_n &= \int_0^x q_n(x)dx + f(0) + f(0) \\
&\rightarrow^{u.c.}\int_0^x f'(x)dx +f(0)&\text{ICT} \\
&=f(x)-f(0) + f(0)&\text{FTC II} \\
&=f(x)
\end{align*}

### _Thrm 3_. 
If $f\in C[0,1]$ and $f(0)=0$, then you can find $p_n\rightarrow^{u.c.}f$ s.t. $p_n(0)=0, p'_n(0)=0$  

__lemma 1__ If $f\in C^1[-1,1]$ is even, then exists $\{p_n\}$ is even and $p_n\rightarrow^{u.c.}f$ 

_proof_. Take $q_n \rightarrow^{u.c.}f$ over $[-1,1]$ by Weierstrass Theorem.  
Define $p_n(x):= \frac{q_n(x)+q_n(-x)}{2}$, and by $f$ even, known $f(x)=\frac{f(x)+f(-x)}{2}$

\begin{align*}
\|p_n-f\|_\infty &= \sup_{x\in[-1,1]}|\frac{q_n(x)+q_n(-x)}{2} - \frac{q_n(x)+q_n(-x)}{2}|\\
&= \frac{1}{2}\sup|q_n(x)-f(x)+(q_n(-x)-f(-x))| \\
&\leq \frac{1}{2}(\sup|q_n(x)-f(x))| + \sup|q_n(x)-f(x))|) &\text{tri.ineq}\\
&\leq \frac{\epsilon + \epsilon}{2} = \epsilon
\end{align*}

_proof_. extend $f$ to $F=\begin{cases}f(x) &[0,1]\\f(-x)&[-1,0]\end{cases}, F$ is even. by lemma 1, take even $q_n\rightarrow F$.  
Then, take $p_n(x) := q_n(x)-q_n(0)$ and  
(i) by $f(0)=0, q_n\rightarrow F\Rightarrow q_n(0) < \epsilon/2$, $\|p_n-f\| \leq \|q_n-F\|+ \epsilon/2 = \epsilon$  
(ii) $p_n(0)=q_n(0)-q_n(0)=0$  
(iii) $p_n$ is even, hence $p_n(x)=\frac{p_n(x)+p_n(-x)}{2}$, $p_n'(x)=\frac{p_n'(x)-p_n'(-x)}{2}\Rightarrow p'_n(0)=0$


### _Thrm 4_. 
If $f\in C(\mathbb R), p_n\rightarrow f$ over $\mathbb R$, then $f$ is a polynomial  

_proof_. Since $p_n$ uniform converge, $p_n$ is also Cauchy. Take $N$ large so that $\forall n,m \geq N. \|p_m-p_n\|_\infty \leq 1$  
Then $f(x)=(f(x)-p_m(x))+(p_m(x)-p_n(x))+p_n(x)$.  
Consider $q_{n,m}(x) = p_m(x)-p_n(x)$, it will also be a polynomial, and since $\|q_{n,m}\|\leq 1$, it must converges to some $a_{n,m}\in[-1,1]$.   
By BW Theorem, take subsequence $a_{n,m_k}\rightarrow a_n$ for each $n$.  
$f(x)=\lim_{m_k\rightarrow\infty}f(x) = \lim_k(f(x)-p_{m_k}(x)) + \|p_m - p_n\| + p_n(x) = 0 + a_n + p_n(x)$
