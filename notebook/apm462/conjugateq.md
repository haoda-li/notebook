# Examples: Conjugate Directions and Conjugate Gradients

## Example 1
!!! question

    Let $c\in\mathbb R^n - \{0\}, f(x) = \frac12x^TQx-b^Tx, Q = I +cc^T$. Using conjugate gradient method, what's the smallest $k$ that guarantees $x_k$ is the minimizer of $f$.

__Claim__. $k=2$

_proof_. First, consider some eigenvalues $\lambda$ and corresponding eigenvector $x$, by definition, we have 

\begin{align*}
\lambda x &= Qx\\
\lambda x &= (I + cc^T)x\\
\lambda x &= x + cc^Tx\\
(\lambda - 1)x &= (c^Tx)c &\text{Note that }c^Tx\in\mathbb R
\end{align*}

If $\lambda - 1 = 0$, we must have $c^Tx = 0$, so that $\lambda = 1$ is a eigenvalue,  
If $\lambda - 1 \neq 0$, then $x$ and $c$ are linearly dependent, hence the eigenvector is $c$ and we have 

\begin{align*}
\lambda c &= (I + cc^T)c\\
\lambda c &= c + cc^Tc\\
\lambda &= 1 + c^Tc
\end{align*}

Therefore, there are only 2 distinct eigenvalues for $Q = I + cc^T$.  

Then, we can take $P_1(\lambda) = a + b\lambda$ be a polynomial of degree 1 s.t. 

$$\begin{bmatrix}
1&1\\
1&1+c^Tc
\end{bmatrix}\begin{bmatrix}
a\\b
\end{bmatrix}=\begin{bmatrix}
-1\\-\frac{1}{1+c^Tc}
\end{bmatrix}$$

so that $1+P(1) = 0$ and $1+(1+cc^T)P(1+cc^T) =0$. 
Therefore, we have 

$$q(x_2) \leq \max_{\lambda \in \{1, 1+c^Tc\}}(1+\lambda P_1(\lambda))q(x_0) = 0$$

Therefore, $k = 2$ guarantees $x_2$ is the minimizer of $f$. 

## Example 2

!!! question

    Let $Q = \begin{bmatrix}2&-5\\-5&2\end{bmatrix}, b = \begin{bmatrix}25&8\end{bmatrix}, f = \frac{1}{2}x^TQx - b^Tx$.

!!! abstract "Part (a)"
    
    Find eigenvalues $\lambda_0\leq \lambda_1$ of $Q$ and corresponding eigenvectors.

First, find its characteristic polynomial as 

$$(2-\lambda)^2 - 25 = \lambda^2 - 4\lambda + 4 -25 = \lambda^2 - 4\lambda+21=(\lambda-7)(\lambda+3)$$

set the equation to $0$ and solve to get

$$\lambda_0 = -3, \lambda_1 = 7$$

Then, 

\begin{align*}
(Q - \lambda_0I)d_0 &= 0\\
\begin{bmatrix}5&-5\\-5&5\end{bmatrix}d_0 &= 0\\
d_0&= \begin{bmatrix}1\\1\end{bmatrix}\\
(Q - \lambda_1I)d_1 &= 0\\
\begin{bmatrix}-5&-5\\-5&-5\end{bmatrix}d_1 &= 0\\
d_1&= \begin{bmatrix}1\\-1\end{bmatrix}
\end{align*}


!!! abstract "Part (b)" 
    
    Compute the steps of conjugate directions method given directions $d_0, d_1$.


\begin{align*}
g_0 &= \begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}25\\5\end{bmatrix} - \begin{bmatrix}25\\8\end{bmatrix}= \begin{bmatrix}0\\-123\end{bmatrix}\\
a_0 &= -(\begin{bmatrix}0\\-123\end{bmatrix}^T\begin{bmatrix}1\\1\end{bmatrix}) / (\begin{bmatrix}1\\1\end{bmatrix}^T
\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix})= -\frac{41}2\\
x_1 &= \begin{bmatrix}25\\5\end{bmatrix}-\frac{41}2\begin{bmatrix}1\\1\end{bmatrix}= \begin{bmatrix}4.5\\-15.5\end{bmatrix}\\
g_1 &= 
\begin{bmatrix}2&-5\\-5&2\end{bmatrix}
\begin{bmatrix}4.5\\-15.5\end{bmatrix} - 
\begin{bmatrix}25\\8\end{bmatrix}= \begin{bmatrix}61.5\\-61.5\end{bmatrix}\\
a_1 &= -(\begin{bmatrix}61.5\\-61.5\end{bmatrix}^T\begin{bmatrix}1\\-1\end{bmatrix}) / (\begin{bmatrix}1\\-1\end{bmatrix}^T
\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}1\\-1\end{bmatrix})= -\frac{123}{14}\\
x_2 &= \begin{bmatrix}-4.5\\15.5\end{bmatrix}-\frac{123}{14}\begin{bmatrix}1\\-1\end{bmatrix}= \begin{bmatrix}-\frac{30}7\\-\frac{47}7\end{bmatrix}
\end{align*}

!!! abstract "Part (c)" 

    Compute the steps of conjugate directions method given directions $d_1, d_0$.


\begin{align*}
g_0 &= \begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}25\\5\end{bmatrix} - \begin{bmatrix}25\\8\end{bmatrix}= \begin{bmatrix}0\\-123\end{bmatrix}\\
a_0 &= -(\begin{bmatrix}0\\-123\end{bmatrix}^T\begin{bmatrix}1\\-1\end{bmatrix}) / (\begin{bmatrix}1\\-1\end{bmatrix}^T
\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}1\\-1\end{bmatrix})= -\frac{123}{14}\\
x_1 &= \begin{bmatrix}25\\5\end{bmatrix}-\frac{123}{14}\begin{bmatrix}1\\-1\end{bmatrix}= \begin{bmatrix}\frac{227}{14}\\\frac{193}{14}\end{bmatrix}\\
g_1 &= 
\begin{bmatrix}2&-5\\-5&2\end{bmatrix}
\begin{bmatrix}\frac{227}{14}\\\frac{193}{14}\end{bmatrix} - 
\begin{bmatrix}25\\8\end{bmatrix}= \begin{bmatrix}61.5\\-61.5\end{bmatrix}\\
a_1 &= -(\begin{bmatrix}61.5\\-61.5\end{bmatrix}^T\begin{bmatrix}1\\1\end{bmatrix}) / (\begin{bmatrix}1\\1\end{bmatrix}^T
\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix})= -\frac{41}{2}\\
x_2 &= \begin{bmatrix}\frac{227}{14}\\\frac{193}{14}\end{bmatrix}-\frac{41}{2}\begin{bmatrix}1\\1\end{bmatrix}= \begin{bmatrix}-\frac{30}7\\-\frac{47}7\end{bmatrix}
\end{align*}


!!! abstract "Part (d)"

    Compute the steps of conjugate gradients.


\begin{align*}
g_0 &= \begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}25\\5\end{bmatrix} - \begin{bmatrix}25\\8\end{bmatrix}= \begin{bmatrix}0\\-123\end{bmatrix}\\
d_0 &= \begin{bmatrix}0\\123\end{bmatrix}\\
a_0 &= (\begin{bmatrix}0\\123\end{bmatrix}\cdot\begin{bmatrix}0\\123\end{bmatrix}) / 
\begin{bmatrix}0\\123\end{bmatrix}\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}0\\123\end{bmatrix} = 0.5\\
x_1 &= \begin{bmatrix}25\\5\end{bmatrix} + 0.5\begin{bmatrix}0\\123\end{bmatrix}= \begin{bmatrix}25\\66.5\end{bmatrix}\\
g_1 &=\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}25\\66.5\end{bmatrix} - \begin{bmatrix}25\\8\end{bmatrix}= \begin{bmatrix}-307.5\\0\end{bmatrix}\\
\beta_0 &= (\begin{bmatrix}-307.5\\0\end{bmatrix}^T\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}0\\123\end{bmatrix}) / (\begin{bmatrix}0\\123\end{bmatrix}^T\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}0\\123\end{bmatrix})=6.25\\
d_1 &= \begin{bmatrix}307.5\\0\end{bmatrix} + 6.25\begin{bmatrix}0\\123\end{bmatrix} = \begin{bmatrix}307.5\\768.75\end{bmatrix}\\
a_1 &= (\begin{bmatrix}-307.5\\0\end{bmatrix}\cdot\begin{bmatrix}307.5\\768.75\end{bmatrix}) / 
\begin{bmatrix}307.5\\768.75\end{bmatrix}\begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}307.5\\768.75\end{bmatrix} = -\frac{2}{21}\\
x_2 &= \begin{bmatrix}25\\66.5\end{bmatrix} + \frac{2}{21}\begin{bmatrix}307.5\\768.75\end{bmatrix} = \begin{bmatrix}-\frac{30}7\\-\frac{47}7\end{bmatrix}\\
g_2 &= \begin{bmatrix}2&-5\\-5&2\end{bmatrix}\begin{bmatrix}-\frac{30}7\\-\frac{47}7\end{bmatrix} - \begin{bmatrix}25\\8\end{bmatrix} = \begin{bmatrix}0\\0\end{bmatrix}\\
\beta_1 &= \frac{0}{d_1^TQd_1} = 0\\
d_2 &= -g_2 + 0 = \begin{bmatrix}0\\0\end{bmatrix}\\
x_3 &= x_2 + a_2\begin{bmatrix}0\\0\end{bmatrix} = x_2 = \begin{bmatrix}-\frac{30}7\\-\frac{47}7\end{bmatrix}
\end{align*}


## Example 3
!!! question

    Prove that the Gram-Schmidt procedure generate a sequence of Q-conjugate directions given a linear independent set of vector $p_0,...,p_{n-1}\in\mathbb R^n$.

_proof_. Note that this statement is equal to say that $\forall k\in\{0,...,n-1\}. \forall j < k. d_k^TQd_j = 0$, and I'll prove this statement by strong induction.

First, since $Q$ is symmetric $d_k^TQd_j = d_j^TQd_k$ for any $d_j,d_k$.  Also note that since $d_k$'s are linear combinations of $p_0, ..., p_{n-1}$, $d_k\neq 0, \forall k\in\{0,...,n-1\}$, and since $Q$ is positive definite $d_K^TQd_k > 0$. 

Then, note that for $k = 0$, the statement is vacuously true.   
Fir $k \in \{1, ..., n-1\}$, assume that $\forall m < k. \forall j < m. d_m^TQd_j = d_j^TQd_m = 0$, i.e. $\forall j,m < k, j\neq m. d^T_mQd_j = 0$ Then, for some $i < k$, we have

\begin{align*}
d_{k}^TQd_{j} &= (p_k - \sum_{i=0}^{k-1}\frac{p_k^TQ d_i}{d_i^TQd_i}d_i)^TQd_j\\
&= p_k^TQd_j- \sum_{i=0}^{k-1}\frac{p_k^TQ d_i}{d_i^TQd_i}d_i^TQd_j\\
&= p_k^TQd_j - \frac{p_k^TQ d_i}{d_j^TQd_j}d_j^TQd_j\\
&= p_k^TQd_j - p_k^TQd_j\\
&= 0
\end{align*}


## Example 4

!!! question

    Let $Q$ be positive definite, $f(x) = \frac12 x^TQx - b^Tx$. Let $x_1=\arg\min_{x\in S_1}f(x), x_2=\arg\min_{x\in S_2}f(x)$, where $S_1,S_2\subset E^n$ and $d\in S_1\cap S_2$, assume $f(x_1) < f(x_2)$. Show that $(x_1-x_2)^TQd = 0$.

_proof_. Since $x_1$ is a minimizer of $S_1$, we must have $\nabla f(x_1)^T = 0$, otherwise we can have some $\epsilon > 0, f(x_1 - \epsilon d) < f(x_1)$ and $x_1-\epsilon d \in S_1$ since $x_1\in S_1, d\in S_1$. Note that the equation is expanded as

\begin{align*}
\nabla f(x_1)^T d &= (Qx_1 - b)^Td \\
&= x_1^TQ^Td - b^Td \\
&= x_1^TQd - b^Td &Q\text{ is symmetric}\\
&= 0
\end{align*}


and similarly we have $\nabla f(x_2)^T d = x_2^TQd - b^Td= 0$.    

Therefore, we have 

\begin{align*}
(x_1-x_2)^TQd &= x_1^TQd - x_2^TQd \\
&= b^Td - b^Td \\
&= 0
\end{align*}


## Example 5

!!! question 

    Let $f = \frac12x^TQx - b^Tx$ where $Q = diag(\lambda_1,...,\lambda_n)$ being a diagonal, positive definite and symmetric matrix.

!!! abstract "Part (a)"

    Show that standard basis vectors form a Q-orthogonal set.

_proof._ Let $i, j \in\{1, ...,n\}, i\neq j$.  
Denote $e_{mk}$ be the $k$th entry of $e_m$, $Q_{ij}$ be the entry on $i$th row and $j$th column of $Q$

$$e_i^TQe_j = \sum_{p=1}^n\sum_{q=1}^nQ_{pq}e_{ip}e_{jq}$$

Note that  
$Q_{pp} = \lambda_i, Q_{pq}=0$, for any $p,q\in\{1,...,n\}, p\neq q$.  
$e_{ii}=1, e_{ip}=0$ for $p\in\{1,...,n\}-\{i\}$  
$e_{jj}=1, e_{jq}=0$ for $q\in\{1,...,n\}-\{j\}$  
Therefore, consider each term of the summation, when $p\neq q, Q_{pq}=0$, when $p=q$, at least one of $e_{ip},e_{jq}$ equals 0. Therefore, all terms in the summation are 0, $e_i^TQe_j = 0$, hence $\{d_0,...,d_{n-1}\} = \{e_1,...,e_n\}$ forms a Q-orthogonal set. 


!!! abstract "Part (b)"
    
    Prove $x_k = (\frac{b_1}{\lambda_1},...,\frac{b_k}{\lambda_k}, a_{k+1},...,a_n)$ is the $k$th step of Conjugate direction method, starting from $x_0 = (a_1,...,a_n)$.

_proof_. I'll prove by induction.  
Let $k\in \{1,...,n-2\}$, assume $x_{k} = (\frac{b_1}{\lambda_1},...,\frac{b_k}{\lambda_k}, a_{k+1},...,a_n)$. Consider the $(k+1)$th step of conjugate direction method.  

$$g_k = Qx_k - b = 
\begin{bmatrix}
\lambda_1\frac{b_1}{\lambda_1} - b_1\\
\cdots\\
\lambda_k\frac{b_k}{\lambda_k} - b_k\\
\lambda_{k+1}a_{k+1} - b_{k+1}\\
\cdots\\
\lambda_{n}a_n - b_{n}
\end{bmatrix} = 
\begin{bmatrix}
0\\
\cdots\\
0\\
\lambda_{k+1}a_{k+1} - b_{k+1}\\
\cdots\\
\lambda_{n}a_n - b_{n}
\end{bmatrix}$$

$$a_k = -\frac{g_k^Td_k}{d_k^TQd_k}=-\frac{g_k^Te_{k+1}}{e_{k+1}^TQe_{k+1}}-\frac{\lambda_{k+1}a_{k+1} - b_{k+1}}{\lambda_{k+1}} = -a_{k+1}+\frac{b_{k+1}}{\lambda_{k+1}}$$

$$x_{k+1} = x_k + a_kd_k = x_k + a_ke_{k+1} 
\begin{bmatrix}
\frac{b_1}{\lambda_1}\\
\cdots\\
\frac{b_k}{\lambda_k}\\
a_{k+1} -a_{k+1}+\frac{b_{k+1}}{\lambda_{k+1}}\\
a_{k+2}\\
\cdots\\
a_n
\end{bmatrix} = 
\begin{bmatrix}
\frac{b_1}{\lambda_1}\\
\cdots\\
\frac{b_{k+1}}{\lambda_{k+1}}\\a_{k+2}\\
\cdots\\
a_n
\end{bmatrix}$$

!!! abstract "Part (c)"

    Prove that $\forall k \geq 1, x_k$ is the minimizer of $f$ in the set $x_0 + \mathcal B_k, \mathcal B_k = span\{d_0,...,d_{k-1}\} = span\{e_1,...,e_k\}$.

_proof_. Let 

\begin{align*}
\phi(y_1,...,y_k)&=f(x_0 + \sum_{i=1}^k{y_ie_i})\\
&=(x_0 + \sum_{i=1}^k{y_ie_i})^TQ(x_0 + \sum_{i=1}^k{y_ie_i})-b^T(x_0 + \sum_{i=1}^k{y_ie_i})
\end{align*}

Therefore, the problem is equivalent to minimize $\phi$ on $\in\mathbb R^k$.  
Note that 

$$\frac{\partial\phi}{\partial y_i} = Q_{i\cdot}(x_{0i}+y_i) - b_i = \lambda_i(a_i+y_i) - b_i$$

for $i=1,2,..,k$,  
Therefore, set the derivative to $0$ to satisfy the FONC, we have $k$ equations 

$$\lambda_i(a_i+y_i)-b_i=0\Rightarrow y_i =\frac{b_i}{\lambda_i}-a_i$$

Then, note that $\frac{\partial^{2}\phi}{\partial y_i^2} = \lambda_i, \frac{\partial^{2}\phi}{\partial y_i y_j} = 0$ for $i,j\in\{1,...,k\}, i\neq j$, we have $\nabla^2\phi = diag(\lambda_1,...,\lambda_k)$, i.e. the top-left $k\times k$ submatrix of $Q$, since $Q$ is positive definite, $\nabla^2\phi$ is also positive definite, SOC also holds and 

$$x_0 + \sum_{i-1}^k(\lambda_i(a_i+y_i)-b_i)e_i = (\frac{b_1}{\lambda_1},...,\frac{b_k}{\lambda_k}, a_{k+1}, ..., a_n) = x_k$$

is the minimizer of $\phi$.

## Example 6


!!! question

    Let $Q$ be a positive definite symmetric matrix.

!!! abstract "Part (a)"

    Prove $d(x, y) = [(x-y)^TQ(x-y)]^{1/2}$ is a metric.

_proof_. Let $x,y\in\mathbb R^n$.  

__positive definite__  
Since $Q$ is positive definite, 

$$\forall a\in\mathbb R^n. a^TQa \geq 0\land a^TQa = 0\Leftrightarrow a = 0$$

$$\implies (x-y)^TQ(x-y) \geq 0\land (x-y)^TQ(x-y) = 0\Leftrightarrow x-y = 0\Leftrightarrow x=y$$

Therefore, 

$$d(x,y)=[(x-y)^TQ(x-y)]^{1/2} \geq 0\land [(x-y)^TQ(x-y)]^{1/2} = 0\Leftrightarrow x=y$$


__symmetric__  

\begin{align*}
d(x,y) &= [(x-y)^TQ(x-y)]^{1/2} \\
&= [(-(y-x))^TQ(-(y-x))]^{1/2}\\
&= [-1(-1)(y-x)^TQ(y-x)]^{1/2}\\
&= [(y-x)^TQ(y-x)]^{1/2}\\
&= d(y,x)
\end{align*}


__triangular inequality__  

\begin{align*}
d(x,z)&= [(x-z)^TQ(x-z)]^{1/2}\\
&= [((x-y)+(y-z))^TQ((x-y)+(y-z))]^{1/2}\\
&= [(x-y)^TQ(x-y) + (y-z)^TQ(y-z)]^{1/2}\\
&= (d(x,y)^{2} + d(y,z)^2)^{1/2}\\
&\text{by triangular inequality on Euclidean norm of real numbers}\\
&\leq (d(x,y)^{2})^{1/2} + (d(x,y)^{2})^{1/2} \\
&= d(x,y) + d(y,z)
\end{align*}


!!! abstract "Part (b)" 
    
    For $x^*\in\mathbb R^2, a\in\mathbb R$, for $x$ on the line $L = \{x\in\mathbb R^2\mid x=(t,at), t\in\mathbb R\}$, find $x$ that minimizes $d(x,x^*)$.

Define 

$$f(x, y) = d((x, y), (x^*, y^*)) = \frac12 \begin{bmatrix}x-x^*\\y-y^*\end{bmatrix}^TQ\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix}$$

therefore minimizing $d((x,y), (x^*, y^*))$ on $L$ is equivalent to 

\begin{align*}&\text{minimize } &f(x,y)\\
&\text{subject to} &l(x,y) = ax-y = 0
\end{align*}

Note that $\nabla f = Q\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix}, \nabla l = \begin{bmatrix}a\\-1\end{bmatrix}$
using Lagrange multiplier, we have equations 

\begin{align*}
Q\begin{bmatrix}t-x^*\\at-y^*\end{bmatrix} + \lambda\begin{bmatrix}a\\-1\end{bmatrix}= 0 
\end{align*}

Therefore, since $Q$ is symmetric, write $Q = \begin{bmatrix}p&m\\m&q\end{bmatrix}$we can solve for 

$$t = \frac{(p+m)x^* + (q+m)x^*}{a^2q + 2am + p}$$

Since $Q$ is positive definite, this solution is the minimum. 
