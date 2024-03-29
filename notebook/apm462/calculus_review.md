# Calculus Review


## Limit and Continuity

Let $f, g$ be functions $\mathbb R^n \rightarrow \mathbb R$

### Claim 1 
If $f$ is continuous and $g$ is discontinuous at $a\in \mathbb R^n$, then $f+g$ must be discontinuous at $a$. 

_proof_. Assume $f$ is continuous and $g$ is discontinuous at $a\in \mathbb R^n$.  
Let $L\in\mathbb R$ be arbitrary.  
By the definition of discontinuity, take $\epsilon_g > 0$ s.t. $\forall \delta > 0. \exists x\in \mathbb R^n. |x-a|<\delta \land |g(x) -g(a)| \geq \epsilon_g$.  
By the definition of continuity, take $\delta_f > 0$ s.t. $\forall x\in \mathbb R^n. |x-a| < \delta_f\Rightarrow |f(x) -f(a)| < \epsilon_g/2$  
Then, take $\epsilon = \epsilon_g/2$. Let $\delta > 0$ be arbitrary. Take $x\in\mathbb R^n. |x-a| < \min(\delta, \delta_f)$.  Therefore, 

\begin{align*}
&\quad\|f(x) - f(a) + g(x) - g(a)\| \\&= \|(f(x) - f(a)) - (g(a) - g(x))\|  \\
&\geq \big\|\|f(x) - f(a)\| - \|g(a) - g(x)\|\big\| &\text{reverse triangle ineq.}\\
&\geq \epsilon_g/2\\
&= \epsilon
\end{align*}

Therefore, we prove that 

$$\forall L\in \mathbb R. \exists \epsilon > 0, \forall \delta > 0. \exists x\in \mathbb R^n. \|x-a\|<\delta \land \|f(x)+g(x)-(f(a)+g(a))\| \geq \epsilon$$


### Claim 2
If both $f, g$ are discontinuous at $a\in \mathbb R^n$, then $f+g$ can be either continuous or discontinuous.   

_proof_. Consider the following examples,   
Take $f_1(x) := \begin{cases}1 &x = a\\0&x\neq a\end{cases}$ and $g_1(x):= \begin{cases}-1 &x = a\\0&x\neq a\end{cases}$. Obviously $f_1+g_1$ is continuous at $a$.  
Take $f_2(x) := \begin{cases}1 &x = a\\0&x\neq a\end{cases}$ and $g_2(x):= \begin{cases}1 &x = a\\0&x\neq a\end{cases}$. Obviously $f_2+g_2$ is discontinuous at $a$. 

### Claim 3
If $f$ is continuous and $g$ is discontinuous at $a\in \mathbb R^n$, then $f\times g$ can be either continuous or discontinuous.   

_proof_. Consider the following examples,   

One of $f, g$ is continuous:  
Take $f_1(x) := 0$ and $g_1(x):= \begin{cases}1 &x = a\\0&x\neq a\end{cases}$. $f_1(x) g_1(x) = 0$ is continuous at $a$.   
Take $f_2(x) := 1$ and $g_2(x):= \begin{cases}1 &x = a\\0&x\neq a\end{cases}$. $f_2(x)g_2(x) = g_2(x)$ is discontinuous at $a$. 
 
Both $f$ and $g$ are discontinuous:  
Take $f_3(x) := \begin{cases}1 &x = a\\0&x\neq a\end{cases}$ and $g_3(x):= \begin{cases}0 &x = a\\1&x\neq a\end{cases}$. Obviously $f_1(x)g_1(x) = 0$ is continuous at $a$.   
Take $f_4(x) := \begin{cases}1 &x = a\\0&x\neq a\end{cases}$ and $g_4(x):= \begin{cases}1 &x = a\\0&x\neq a\end{cases}$. Obviously $f_4(x)g_4(x) = f_4(x)$ is continuous at $a$.  

### Claim 4 

if $f:\mathbb R^n\rightarrow \mathbb R$ is continuous, then $S = \{x\in\mathbb R^n:f(x)>0\}$ is open.

_proof_. Let $f:\mathbb R^n\rightarrow \mathbb R$ be continuous.  
Let $x_0\in\mathbb R^n$ be arbitrary, assume $f(x_0) = L > 0$.  
By continuity of $f$, take $\delta > 0$ s.t. $\forall x\in\mathbb R^n. |x-x_0| < \delta \Rightarrow |f(x) - f(x_0)| < L/2$.  
Then, note that $|f(x) - f(x_0)| < L/2 \Rightarrow f(x) > f(x_0) - L/2 = L/2 > 0$.   
This implies that $\forall x \in B(\delta, x_0). x\in S$.  
Therefore, we have shown that $\forall x_0 \in S. \exists \delta > 0. s.t. B(\delta, x_0) \subset S$, which means $S$ is open. 

### Examples 1
Find $a$ s.t. $\forall \delta > 0, \exists x \in S. 0 < |x-a| < \delta$

#### Examples 1.1
$S = \{(x, y)\in\mathbb R^2. x^2 +y^2 < 1\}\cup\{(0, 2)\}$. 


__Claim__. $\forall a\in \{(x, y)\in\mathbb R^2. x^2 +y^2 < 1\}$, the condition is satisfied. 

_proof_. Let $a = (x_0, y_0)$ s.t. $x_0^2 + y_0^2 = c < 1$ be arbitrary.  Take $\epsilon_0 = 1-c, 0 < \epsilon_0 < 1$.  
Let $\delta > 0$ be arbitrary.  
Take $\epsilon = \min(\frac{\epsilon_0}4, \frac{\epsilon_0}{4|x_0 + y_0|}, \frac{\delta}2)$, then note that 

$$|2\epsilon(x_0 + y_0)| \leq 2\frac{\epsilon_0}{4|x_0+y_0|}|x_0+y_0| \leq \epsilon_0/2$$


$$2\epsilon^2 \leq 2\frac{\epsilon_0^2}{4^2} = \epsilon_0^2/8$$

so that 

\begin{align*}
(x_0 + \epsilon)^2 + (y_0 + \epsilon)^2 &\leq x^2_0 + y^2_0  + |2\epsilon (x_0 + y_0)| + 2\epsilon^2\\
&\leq x_0^2 + y_0^2 + \epsilon_0/2 + \epsilon_0^2/8\\
&\leq x_0^2 + y_0^2 + \epsilon_0/2 + \epsilon_0/8 &0<\epsilon_0<1\\
&< x_0^2 + y_0^2 + \epsilon_0\\
&= c + 1 - c \\
& = 1\\
&\Rightarrow (x_0 + \epsilon, y_0 + \epsilon) \in S
\end{align*}

Also, 

$$|(x_0, y_0) - (x_0 + \epsilon, y_0 + \epsilon)| = \sqrt 2\epsilon \leq \sqrt 2\frac{\delta}2 = \delta/\sqrt 2 < \delta$$

Therefore, $\forall a\in S_1. \forall \delta > 0, \exists x\in S. |x-a| < \delta$

__Claim__. $a = (0, 2)$ does not satisfy the condition. 

_proof_. Let $(x_0, y_0)\in S - \{(0, 2)\} = \{(x, y)\in\mathbb R^2: x^2 +y^2 < 1\}$. 
Note that $0 < x_0^2 + y_0^2 < 1$, so that $-\sqrt1 < y_0 < \sqrt 1$.  
Therefore, $(y_0-2)^2 > (1-2)^2 = 1$


\begin{align*}
|(x_0, y_0) - (0, 2)| &= \sqrt{(x_0-0)^2 + (y_0-2)^2} \\
&\geq \sqrt{(y_0-2)^2}\\
&\geq 1
\end{align*}

Therefore, $\forall x\in S. |x-(0, 2)| \leq 0 \lor |x-(0, 2)|\geq 1$

#### Examples 1.2
$S = \{(x, y)\in\mathbb R^2. x^2 +y^2 < 1\}\cup\{(0, 1)\}$.

__Claim.__ $\forall a\in S$, the condition is satisfied.   


_proof._ We only need to show that 

$$\forall \delta > 0. \exists x\in S. 0 < |x-(0, 1)| < \delta$$

The rest are proven in (1). 

Let $\delta > 0$. Take $\delta_0 = \min(0.1, \delta/2)$.  
Then, 

$$|(0, 1-\delta_0) - (0, 1)| = 1-\delta_0 - 1 = \delta_0$$

Note that $\delta_0 \leq 2/\delta < \delta$ and $0 + (1-\delta_0)^2 = 1 - 2\delta_0 + \delta_0^2 \leq 1 - 0.2 + 0.01 < 1$
Therefore, $(0, 1-\delta_0)\in S$ and $0 < |(0, 1-\delta_0) - (0, 1)| < \delta$. 

#### Examples 1.3
$S = \{(0, 2^{-n})\in\mathbb R^2:n\in\mathbb N\}$

__Claim.__ $\forall a\in S$, the condition does NOT satisfy. 

_proof_. Let $a = (0, 2^{-n})\in S$ for some $n\in\mathbb N$.  
Take $\delta = 2^{-(n+1)} > 0$.  
Then, let $m\in\mathbb N, m\neq n$. 

$$|(0, 2^{-n}) - (0, 2^{-m})| = |2^{-n}- 2^{-m}| = 2^{-n}|1-2^{n-m}|$$

Suppose $m > n$, then $2^{n-m} \leq 2^{-1}, |1-2^{n-m}|\geq 1/2$.  
Suppose $n > m$, then $2^{n-m} \geq 2, |1-2^{n-m}| \geq 1$. 

Therefore, $|(0, 2^{-n}) - (0, 2^{-m})| \geq 2^{-n}/2 = 2^{-(n+1)}$

#### Examples 1.4
$S = \{(0, 2^{-n})\in\mathbb R^2:n\in \mathbb N\}\cup \{(0, 0)\}$

__Claim.__ $a = (0, 0)$ satisfies the condition

_proof_. For any $\delta > 0$, we can find some $n\in\mathbb N$ s.t. $2^{-n} < \delta$ so that $0 < |(0, 2^{-n}) - (0, 0)| = 2^{-n} < \delta$

__Claim.__ $\forall a\in \{(0, 2^{-n})\in\mathbb R^2. n\in\mathbb N\}, a$ does not satisfy the condition. 

_proof_. In addition to points in (3), further notice that 
$\forall n\in\mathbb N$. $|(0, 2^{-n}) - (0, 0)| = 2^{-n} > 2^{-(n+1)}$

### Claim 5
For $f:\mathbb R^n\rightarrow \mathbb R^k$ and $g: \mathbb R^k\rightarrow\mathbb R^l$, if $f$ is continuous at $a\in\mathbb R^n$ and $g$ is continuous at $f(a)$, then $g\circ f$ is continuous at $a$. 

_proof_. Let $\epsilon > 0$.  
Because $g$ is continuous at $f(a)$, take $\delta_1 > 0$ s.t. $\forall y\in\mathbb R^k. |y-f(a)| < \delta_1 \Rightarrow |g(y) - g(f(a))| < \epsilon$.  
Because $f$ is continuous at $a$, take $\delta_2 > 0$ s.t. $\forall x\in\mathbb R^n. |x - a|  < \delta_2 \Rightarrow |f(x) - f(a)| < \delta_1$  
Therefore, for any $x\in\mathbb R^n. |x-a| <\delta_2\Rightarrow |f(x) - f(a)| < \delta_1\Rightarrow |g(f(x)) - g(f(a))| < \epsilon$. 

## Sequences and completeness

### Claim 1

$\vec a_j\rightarrow \vec a \land \vec b_j\rightarrow \vec b\Rightarrow \vec a_j\cdot \vec b_j \rightarrow \vec a \cdot \vec b$

_proof_. First note that $\vec a_j \rightarrow \vec a\Rightarrow \forall i\in \{1, 2, ..., n\}. a_{ij}\rightarrow a_{i\cdot}, b_{ij}\rightarrow b_{i\cdot}$, where $a_{ij}$ is the $i$th component of $\vec a_j$ and $a_{i\cdot}$ is the $i$th component of $\vec a$. Then, note that 

$$\vec a_j\cdot \vec b_j = \sum_{i=1}^n a_{ij}b_{ij}$$

Therefore, apply limit laws for addition and multiplication for 1-D case, 

$$\lim_{j\rightarrow\infty}\sum_{i=1}^n a_{ij}b_{ij} = \sum_{i=1}^n a_{i\cdot}b_{i\cdot} = \vec a\cdot \vec b$$


### Claim 2
For $\{a_j\}_j\subset \mathbb R^n$ and function $f:\mathbb R^n\rightarrow\mathbb R^k$. If $a_j\rightarrow a$ and $f$ continuous and $a$, then $f(a_j)\rightarrow f(a)$. 

_proof_. Let $\epsilon > 0$ be arbitrary.  
Since $f$ is continuous at $a$, take $\delta > 0$ s.t. $\forall x\in\mathbb R^n. |x-a|<\delta\Rightarrow |f(x)-f(a)| < \epsilon$.   
Since $a_j\rightarrow a$, take $N\in\mathbb N^+$ s.t. $\forall n \in\mathbb N^+. n > N\Rightarrow |a_n - a| < \delta$.  
Therefore, $|a_n - a| < \delta \Rightarrow |f(a_n) - f(a)| < \epsilon$.  
We have proven that $\forall \epsilon > 0. \exists N\in\mathbb N^+. \forall n \in\mathbb N^+ . n > N \Rightarrow |f(a_n) - f(a)| < \epsilon$. By definition of convergence, $\lim_{j\rightarrow \infty}f(a_j) = f(a)$

## Compactness and applications

### Claim 1 
If $S \subseteq \mathbb R^n$ is closed and $\{x_j\}_j \subseteq\mathbb R^n$ converges to $x\not\in S$, then $\exists j\in\mathbb N^+. x_j\not\in S$. 

_proof_. First, note that $x\not\in S\Rightarrow x\in S^c$ and $S$ is closed $\Rightarrow S^c$ is open.  
By the definition of open set, take $\epsilon > 0$ s.t. $B(\epsilon, x) \subset S^c$.  
Then, note that $x_j\rightarrow x$, by the definition of convergent sequence, take $N\in\mathbb N^+$ s.t. $\forall n \in\mathbb N^+. n \geq N\Rightarrow |x_n - x| < \epsilon$.  
Therefore, note that $|x_N - x|< \epsilon \Rightarrow x_N \in B(\epsilon, x) \subset S^c\Rightarrow x_N\not\in S$

### Claim 2
If $S$ is unbounded, then exists some $\{x_j\}_j\subset S$ that has no convergent subsequence. 

_proof_. Construct $\{x_j\}_j$ by the following recursive procedure.  
Let $x_1\in S, x_1\neq 0$ be arbitrary, let $r_1 = \|x_1\|$.  
Given $x_n, r_n$, let $x_{n+1} \in S - B(2r_n, 0), r_{n+1} = \|x_{n+1}\|$.  
Note that such $x_{n+1}$ always exists since $S$ is unbounded.   
Also, note that $r_{n+1} = \|x_{n+1}\| \geq 2r_n \geq 2^{n-1} r_1$. 


Then, we will show such sequence has no convergent subsequence.   
Given any subsequence $\{x_{k_j}\}_j$,  
Let $L\in S$ be arbitrary, let $J > 0$ be arbitrary.  
Take some $j \geq J$ s.t. $2^{k_j-1}r_1  \geq 1 + \|L\|$, since $r_1 > 0$ we can always find such $j$.   
Therefore, 

\begin{align*}
\|x_{k_j} - L\| &\geq \big\| \|x_{k_j}\| - \|L\|\big\| &\text{reverse triangle ineq.} \\
&= 2^{k_j-1}r_1 - \|L\| \\
&\geq 1 + \|L\| - \|L\|\\
& = 1
\end{align*}

Therefore, $\{x_{k_j}\}_j$ diverges. 

### Lemma 3
Any subsequence of convergent sequence will also converge to the same limit.  

_proof_. Let $\{a_j\}_j$ be convergent to some $L$. Let $\{a_{k_j}\}_j$ be some subsequence.    
Let $\epsilon > 0$ be arbitrary, take $J\in\mathbb N^+$ s.t. $\forall j > J. \|a_j-L\| < \epsilon$.  
Take $J_2 \in \mathbb N^+$ s.t. $k_{J_2} \geq J$ so that $\forall j > J_2. k_j > k_{J_2} \geq J$.  
Therefore, $\forall j > J_2. \|a_{k_j}- L\| < \epsilon$. 


### Claim 4 

The Cartesian Product of two compact sets is compact. 

_proof_. Let $K_1 \subseteq \mathbb R^n, K_2 \subseteq \mathbb R^m$  be compact.  
Let $\{(x_j, y_j)\}_j$ be a sequence in $K_1\times K_2$ so that $\{x_j\}_j\in K_1, \{y_j\}_j \in K_2$.  
By compactness of $K_1$, take subsequence $\{x_{k_j}\}_j$ that converge to some $L_1\in K_1$.  
By compactness of $K_2$, further take $\{y_{l_{k_j}}\}_j$ be a subsequence of $\{y_{k_j}\}_j$ that converge to some $L_2\in K_2$.  
Then, since $\{x_{l_{k_j}}\}_j$ is a subsequence of $\{x_{k_j}\}_j$, $\{x_{l_{k_j}}\}_j$ will also converge to $L_1$ (using lemma above).  
Therefore, $\{(x_{l_{k_j}}, y_{l_{k_j}})\}_{j}\rightarrow (L_1, L_2) \in K_1\times K_2$  
By definition of compactness, $K_1\times K_2$ is compact. 

### Claim 5 
The closed subset of a compact set is compact.  

_proof 1._  If $S$ is compact, then by BW theorem $S$ is closed and bounded. so that $\forall s\in S. s\in B(R, 0)$ for some $R > 0$. Then, for any closed subset $A \subseteq S$, $s\in A\Rightarrow s\in S\Rightarrow s\in B(R, 0)$ so that $A$ is also bounded. Therefore, $A$ is also closed and bounded, hence compact. 

## Chain Rule

### Claim 1
$q(x): = |x|^2. \nabla q(x) = 2x$

_proof_ For any $x\in\mathbb R^n$, 

\begin{align*}
\lim_{h\rightarrow 0} \frac{q(x+h) - q(x) - 2x\cdot h}{|h|} &= \lim_{h\rightarrow 0} \frac{|x+h|^2 - |x|^2 - 2x\cdot h}{|h|}\\
&= \lim_{h\rightarrow 0}\frac{|x|^2 + 2x\cdot h + |h|^2 -|x|^2-2x\cdot h}{|h|}\\
&= \lim_{h\rightarrow 0} \frac{|h|^2}{|h|}\\
&= \lim_{h\rightarrow} h\\
&= 0
\end{align*}

Therefore, by the definition of derivative $\nabla q = 2x$

## Example 1
Prove chain rule for $g: \mathbb R\rightarrow \mathbb R^2, f: \mathbb R^2 \rightarrow \mathbb R. \phi = f\circ g$

Given that 

\begin{align*}
\phi(t+h) - \phi(t) = &[f(x(t+h), y(t+h)) - f(x(t+h), y(t))] &(i)\\
&\quad+ [f(x(t+h), y(t)) - f(x(t), y(t))] &(ii)
\end{align*}

First, write $g(x)=f(x, y)$ so that

\begin{align*}
(i) &= g(x(t+h)) - f(x(t)) \\
&= (x(t+h) - x(t))g'(x(t)+\theta_{11}(x(t+h) - x(t)))\\
&= h(x'(t+\theta_{12}h))g'(x(t)+\theta_{11}(x(t+h) - x(t)))\\
&= h\frac{\partial x}{\partial t}(t+\theta_{12}h)\frac{\partial f}{\partial x}(x(t) - \theta_{11}(x(t+h) - x(t)))
\end{align*}

by MVT, where $\theta_{11}, \theta_{12}\in (0, 1)$.
Similarly, 

$$(ii) = h\frac{\partial y}{\partial t}(t+\theta_{22}h)\frac{\partial f}{\partial y}(y(t) - \theta_{21}(y(t+h) - y(t)))$$


Therefore, 

\begin{align*}
\phi'(t) &= \lim_{h\rightarrow 0} h^{-1} \phi(t+h) - \phi(t)\\
&= \lim_{h\rightarrow 0} h^{-1}\\
&\quad\bigg[h\frac{\partial x}{\partial t}(t+\theta_{12}h)\frac{\partial f}{\partial x}(x(t) - \theta_{11}(x(t+h) - x(t))) \\
& \quad + h\frac{\partial y}{\partial t}(t+\theta_{22}h)\frac{\partial f}{\partial y}(y(t) - \theta_{21}(y(t+h) - y(t)))\bigg]\\
&= \lim_{h\rightarrow 0} \\
&\quad\bigg[\frac{\partial x}{\partial t}(t+\theta_{12}h)\frac{\partial f}{\partial x}(x(t) - \theta_{11}(x(t+h) - x(t))) \\
& \quad + \frac{\partial y}{\partial t}(t+\theta_{22}h)\frac{\partial f}{\partial y}(y(t) - \theta_{21}(y(t+h) - y(t)))\bigg] &(*)
\end{align*}

Then, by our assumption, $x, y$ are differentiable, hence continuous, by continuous mapping theorem, 

$$\lim_{h\rightarrow 0} x(t+h) = x(t). \lim_{h\rightarrow 0} y(t+h) = y(t)$$

In addition, $\theta_{11}, \theta_{12}, \theta_{21}, \theta_{22}\in (0, 1)$. Therefore, the limit above exists and equals to

$$(*) = \frac{\partial x}{\partial t}(t)\frac{\partial f}{\partial x}(x(t)) + \frac{\partial y}{\partial t}(t)\frac{\partial f}{\partial y}(y(t)) = \frac{\partial f}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial t}$$

