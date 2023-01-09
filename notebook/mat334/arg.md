# Argument Principle and Rouche's Theorem

## Argument Principle

### Lemma 1 
If $z_i$ is a zero of order $n_i$ of $f(z)$, then 

$$\frac{f'(z)}{f(z)} = \frac{n_i}{z-z_i} + h_i(z)$$

near $z_i$ for some function $h_i(z)$ analytic at $z_i$. 

_proof_. Consider the Laurent expansion near $z_i$, since $z_i$ is a zero of order $n_i$, we have 

\begin{align*}
f(z) &= \sum_{n=n_i}^{\infty}a_n(z-z_i)^n\\
&= (z-z_i)^{n_i} \sum_{n=0}^\infty a_{n+n_i}(z-z_i)^n\\
&:= (z-z_i)^{n_i} g_i(z)
\end{align*}

Note that we have pulled out all the zeros, hence $g_i(z)\neq 0$ near $z_i$ and at $z_i$. Thus, we can write 

$$\frac{f'(z)}{f(z)} = \frac{n_i(z-z_i)^{n_i - 1} g_i(z) + (z-z_i)^{n_i}g_i'(z)}{(z-z_i)^{n_i}g_i(z)} = \frac{n_i}{z-z_i} + \frac{g'_i(z)}{g_i(z)}$$

Similarly, if $z_i$ is a pole of order $p_i$ near $z_i$, then $f(z) = \sum_{n=-n_i}^\infty c_n(z-z_n)^n$ so that 

$$\frac{f'(z)}{f(z)} = \frac{-p_i}{z-z_i} + \frac{g'_i(z)}{g_i(z)}$$

If $z_i$ is of order $0$, then $\frac{f'(z)}{f(z)}$ is already analytic using the same expansion. 

### Theorem 2 Argument Principle
Suppose $f(z)$ is analytic on a Jordon contour $C$ and meromorphic (has finitely many singularities, and each of which are poles) inside of $C$. Then

$$N - P = \frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)}dz = [\arg(f(z))]_C=:w(f(C), 0)$$

where $N$ is the number of $0$'s in $C_{int}$ counted with multiplicity, and $P$ is thue number of poles counted with multiplicity. 

_proof_. For $N - P = \frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)}dz$,

\begin{align*}
\frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)}dz &= \sum_{k=1}^m Res(\frac{f'}{f}, z_k)\\
&= \sum_{zeros} (\lim_{z\rightarrow z_i} (z-z_i)(\frac{n_i}{z-z_i} + \frac{g'_i(z)}{g_i(z)})) + \sum_{poles} (\lim_{z\rightarrow z_i} (z-z_i)(\frac{-p_i}{z-z_i} + \frac{g'_i(z)}{g_i(z)})) \\
&= \sum n_i - \sum p_i\\
&= N- P
\end{align*}

For $\frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)}dz = w(f(C), 0)$,

Let $c:[a,b]\rightarrow\mathbb C$ be some parameterization of $C$, take $\theta:[a,b]\rightarrow \mathbb R$ s.t. $f(c(t)) = |f(c(t))|e^{i\theta(t)} = r(c(t))e^{i\theta(t)}$ then, 

\begin{align*}
\oint_C \frac{f'(z)}{f(z)} dz &= \int_a^b \frac{f'(c(t))}{f(c(t))}c'(t)dt\\
&= \int_a^b \frac{r'(c(t))c'(t) e^{i\theta(t)} + r(c(t))i\theta'(t)e^{i\theta(t)} }{r(c(t))e^{i\theta(t)} }dt\\
&= \int_a^b \frac{r'(c(t))c'(t)}{r(c(t))}dt + \int_a^b \theta'(t) dt \\
&= \int_{r(c(a))}^{r(c(b))} \frac{dr}{r} + i\int_{\theta(a)}^{\theta(b)} d\theta\\
&= \log(r(c(b))) - \log(r(c(a))) + i(\theta(b) - \theta(a))\\
&= i(\theta(b) - \theta(a))
\end{align*}

So that $\frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)}dz = \frac{\theta(b) - \theta(a)}{2\pi} = w(f(C), 0)$

### Applications of Argument Principle

__Example__ Determine the number of zeros of $f(z) = z^3 + 1$ in the first quadrant.

Consider $C = C_1\cup C_2 \cup C_3$ parameterized by $c_1: [0, 1]\rightarrow \mathbb C:= Rt, c_2(t): [0, \pi/2]\rightarrow \mathbb C= Re^{it}, c_3: [0, 1]\rightarrow \mathbb C = iR(1-t)$. 

Using argument princple, note that $f$ does not have any singularities, so that number of zeros inside $C$ equals $w(f(C), 0)$. Then, compute 

$$f(c_1(t)) = 1+R^3 t^3, f(c_2(t)) = 1+ R^3 e^{i3t} f(c_3(t)) = 1 - iR(1-3)^3$$

Thus, for $R > 1$, $w(C, 0) =1$ is the number of zeros.

## Rouche's Theorem
__Theorem__ Let $f$ and $g$ by analytic on $\partial C \cup C_{int}$ for a Jordon contour $C$. If $|f(z)| > |g(z)|$ for all $z\in C$, then $f(z)$ and $f(z) + g(z)$ have the same number of zeros in $C_{int}$. 

_proof (informal)_. Since $|f(z)| > |g(z)|$ on $C$, notably have $f(z)\neq 0$ on $C$. Let $w(z) = \frac{f(z)+g(z)}{f(z)}$.  
Observe that $|w(z) - 1| = |\frac{g(z)}{f(z)}| < 1$ on $C$. i.e. $[\arg(w(z))]_C = 0$. Thus, $w(z) \in B_1(1)$ has the same number of zeros and singularities. Furthermore, $N=P=0$

### Example 1
Show that $p(z) = z^4 + z^2 + 1$ has 4 roots inside $C_2(0)$.

Let $f(z) = z^4, g(z) = z^2 + 1$. $\forall |z| = 2$, obviously $|f(z)| = 16 > 5 = |f(z)|$ so that apply Rouche's Theorem, $p = f+g$ has the same number of 0's as $f$, which is 4.

### Example 2 
Show that $h(z) = 3z^2 - \cos z$ has exactly $2$ roots inside $C_1(0)$.

Let $f(z) = 3z^2, g(z) = -\cos(z)$. $\forall |z| = 1. |f(z)| = 3$ and $|g(z)| \leq |\cos z | \leq e$. so that by Rouche's Theorem, $p = f+g$ has the 2 roots as of $f$. 

### Example 3  
Show that $h(z) = z^5 + z + 3$ has $5$ roots in $\bar A_{1,2}(0)$

Note that $|z| = 2$, $|z^5| =  32 >  5 = |z|+ 3  = |z+3|$ so that $h$ has $5$ zeros on $C_2(0)$, also note that $|h(z)| > 0$ so that no zeros on the $\partial C_2$. In addition, note that on $C_1(0)$, 
$|z+3| \geq 3 - |z| = 2 > 1 = |z^5|$ and $z+3$ has on zeros inside $C_1(0)$. Therefore, all $5$ zeros must locate in $A_{1,2}(0)$

### Fundamental Theorem of Algebra

__Theorem__ For a polynomial $p(z) = \sum_{k=0}^n a_kz^k$, $p$ has exactly $n$ roots in $\mathbb C$. 

_proof_. Note that $p(z)$ has the same number of roots as $\frac{p(z)}{a_n}$, so wlog assume $a_n = 1$.   
Let $f(z) = z^n, g(z) = \sum_{k=0}^{n-1}a_k z^k$ so that $p = f+g$.  
Then, $\forall |z| \geq 1$

\begin{align*}
|g(z)| &\leq \sum_{k=0}^{n-1} |a_k||z|^k\\
&\leq |z|^{n-1}\sum_{k=0}^{n-1}|a_k|\\
&\leq \max\{\sum_{k=0}^{n-1}|a_k|, 1\} |z|^{n-1}
\end{align*}

Let $R = \max\{\sum_{k=0}^{n-1}|a_k|, 1\}$, so that on $C_R(0)$, i.e. $\forall |z| = R$ we have 

$$|f(z)| = R^n = R  |z|^{n-1}\geq |g(z)|$$

By Rouche's Theorem, the statement is proven. 
