# Examples: Unconstrained Finite Dimensional Optimization

## Example 1

!!!question 
    
    Let $a\in\mathbb R$ and $f_a:\mathbb R^2\rightarrow \mathbb R, f_a(x, y)= x^2 + 2y^2 + axy - y$.


!!!abstract "Part (a)"

    Find the points satisfy FOC.    

The partial derivative gives 

$$\frac{\partial f_a}{\partial x} = 2x+ay, \frac{\partial f_a}{\partial y} = 4y+ax - 1$$

Set the derivatives to 0 to meet the FOC.  
If $a = 0$, then $x = 0, y = 1/4$ satisfies FOC.  
If $a\neq 0$, then to make $\begin{bmatrix}a&4\\2&a\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}1\\0\end{bmatrix}$ has solutions, the reduced row echelon form gives  $\begin{bmatrix}a&4\\0&\frac{a^2}2- 4\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}1\\-1\end{bmatrix}$, If $a = \pm 2\sqrt{2}$, then there is no local minimum, otherwise, we have the unique solution $y = \frac{2}{8-a^2}, x = \frac1a(1-\frac{8}{8-a^2}) = \frac{-a}{8-a^2}$.   
To summarize,  
If $a = 0$, then $x=0, y=1/4$  satisfies the FOC
If $a = \pm 2\sqrt 2$, then there is no points satisfy the FOC  
If $a\neq 0$ and $a\neq \pm2\sqrt2$, then $x = \frac{-a}{8-a^2}, y = \frac{2}{8-a^2}$ satisfies the FOC.

!!!abstract "Part (b)"
    
    Find the points satisfy SOC

The Hessian matrix gives 

$$F_a = \begin{bmatrix}2&a\\a&4\end{bmatrix}$$

Note that $F_a$ is positive semidefinite iff $\det(F_a) = 2\times 4-a^2 > 0$, so that for any $a\in(-2\sqrt 2, 2\sqrt 2)$, the points satisfies the SOC. 

!!!abstract "Part (c)"
    
    Prove the local minimum is actually global minimum.

_proof 1. Prove by completing the square_  
Note that $f_a(x, y) = \frac12\begin{bmatrix}x\\y\end{bmatrix}\cdot \begin{bmatrix}2&a\\a&4\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix} - \begin{bmatrix}0\\1\end{bmatrix}\cdot\begin{bmatrix}x\\y\end{bmatrix}$  
Therefore, using completing the square method, let $x^* = \begin{bmatrix}x^*\\y^*\end{bmatrix}\frac{1}{8-a^2}\begin{bmatrix}4&-a\\-a&2\end{bmatrix}\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}\frac{-a}{8-a^2}\\\frac{2}{8-a^2}\end{bmatrix}$, then 

$$f_a(x, y) = \frac12\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix}\cdot \begin{bmatrix}2&a\\a&4\end{bmatrix}\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix} - \frac12\begin{bmatrix}x^*\\y^*\end{bmatrix}\cdot \begin{bmatrix}2&a\\a&4\end{bmatrix}\begin{bmatrix}x^*\\y^*\end{bmatrix}$$

Note that when $a\in (-2\sqrt2, 2\sqrt 2)$, the matrix $\begin{bmatrix}2&a\\a&4\end{bmatrix}$ is positive-semidefinite, i.e. for any $\begin{bmatrix}x\\y\end{bmatrix}$, we have $\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix}\cdot \begin{bmatrix}2&a\\a&4\end{bmatrix}\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix}\geq 0$. Therefore, the minimum can only be reached when $\begin{bmatrix}x-x^*\\y-y^*\end{bmatrix} = 0 \Rightarrow \begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}x^*\\y^*\end{bmatrix} = \begin{bmatrix}\frac{-a}{8-a^2}\\\frac{2}{8-a^2}\end{bmatrix}$  
_proof 2. Prove by convexity_  
Let $\vec x_1 = (x_1, y_1)\in \mathbb R^2, \vec x_2 = (x_2, y_2) \in \mathbb R^2$, let $c\in [0, 1]$.  
For $c = 1$, obviously $f_a(1x_1 +0x_2) = 1f_a(x_1) + 0 f_a(x_2)$, similarly for $c=0$.  
For $c\in(0,1)$, denote $Q = \begin{bmatrix}2&a\\a&4\end{bmatrix}$

\begin{align*}
f(c\vec x_1 + (1-c)\vec x_2) &= \frac 12(c\vec x_1 + (1-c)\vec x_2)^T Q (c\vec x_1 + (1-c)\vec x_2) - \begin{bmatrix}0\\1\end{bmatrix}(c\vec x_1 + (1-c)\vec x_2)\\
&= \frac12\big[
c^2\vec x_1^TQ\vec x_1 + c(1-c)\vec x_1^TQ\vec x_2+c(1-c)\vec x_2^TQ\vec x_1 + (1-c)^2\vec x_2^TQ\vec x_2
\big] \\
&\quad- \begin{bmatrix}0\\1\end{bmatrix}(c\vec x_1 + (1-c)\vec x_2)
\end{align*}

Therefore, 

\begin{align*}
&\quad cf_a(\vec x_1) + (1-c)f_a(\vec x_2) - f_a(c_x1+(1-c)x_2)\\
&=\frac{1}{2}(c-c^2)\vec x_1^TQx_1 - c(1-c)\vec x_1^TQ\vec x_2-c(1-c)\vec x_2^TQ\vec x_1 +((1-c)-(1-c)^2)\vec x_2^TQ\vec x_2\\
&= \frac12c(1-c)[x_1^TQx_1-x_1^TQx_2-x_2^TQx_1+x_2^TQx_2]\\
&= \frac12c(1-c)(\vec x_1-\vec x_2)^TQ(\vec x_1-\vec x_2)
\end{align*}

Note that when $a\in(-2\sqrt 2, 2\sqrt 2)$, $Q$ is positive semidefinite, hence $\frac12c(1-c)(\vec x_1-\vec x_2)^TQ(\vec x_1-\vec x_2) \geq 0$. Therefore, $cf_a(\vec x_1) + (1-c)f_a(\vec x_2) \geq f_a(c_x1+(1-c)x_2)$. By the definition of convex function, $f_a$ is convex, and the local minimum is the global minimum.

## Example 2

!!!question

    Find the local minimum point(s) for $f(x, y,z ) = (x-\frac y2)^2 + \frac34(y-2)^2 + z^2 -3$ on $S = \{(x,y,z)\in\mathbb R^3 \mid x\leq 0, y \geq 0\}$, and prove the local minimum is actually a global minimum.


First of all, let $g(x, y) = f(x, y, 0) = (x-\frac y2)^2 + \frac34(y-2)^2-3$. Obsever that $\forall z\in\mathbb R. z^2 \geq 0$, hence minimizes $f$ is equivalent to minimize $g$ as having $z=0$. 

First, the partial derivative

$$\nabla g = (2x-y, 2y-x-3)$$


1. $x < 0, y > 0$   
solves the system of equation that $\nabla f = \vec0$, 

$$x=1, y=2, z =0$$

does not lie in the set, there is no local min in the interior of $S$

2. $x = 0, y > 0$  
Let the feasible direction be $v = (v_1, v_2), v_1 \leq 0$ and want 

$$\nabla f \cdot v = (2\cdot 0-y)v_1 + (2y-0-3)v_2 =-yv_1 + (2y-3)v_2\geq 0$$

Note that for any $v_1 \leq 0, -yv_1 \geq 0$ so that the condition is equivalent to have $2y-3 = 0\Rightarrow y = \frac32$, and the candidate is $(0, \frac32)$

3. $x < 0, y = 0$
Let the feasible direction be $v = (v_1, v_2), v_2 \geq 0$ and want 

$$\nabla f \cdot v = (2x-0)v_1 + (2\cdot 0-x-3)v_2 =2xv_1 - (x+3)v_2\geq 0$$

Note that for direction $(1/2, 1), \nabla f\cdot v = 2x\cdot\frac12 - (x + 3) = -3 < 0$ for any $x$, hence there is no local min in this case. 

4. $x, y = 0$
Let the feasible direction be $v = (v_1, v_2), v_1 \leq 0, v_2 \geq 0$ and want 

$$\nabla f \cdot v = 0v_1 + (-3)v_2 = -3v_2\geq 0$$

does not hold for $v_2 \geq 0$, hence no local minimum.

## Example 3

!!! question

    Show that $xx^T$, where $x\in\mathbb R^n$, is positive semidefinite.

Let $x\in\mathbb R^n, a\in\mathbb R^n$.  

\begin{align*}
a^T(xx^T)a &= (a^Tx)(x^Ta)\\
&= (x^Ta)^T(x^Ta) &\text{take transpose}\\
&= \|x^Ta\|^2\\
&\geq 0
\end{align*}

Therefore, by definition of positive semidefinite, $xx^T$ is positive semidefinite 

## Example 4

!!!question

    Let $f(x) = b\cdot Ax$, $A$ is $n\times m$ matrix, $x\in\mathbb R^m, b\in\mathbb R^n$, show that $\nabla f(x)=A^Tb$.

First, note that

\begin{align*}
b\cdot Ax &= 
\begin{bmatrix}b_1\\\vdots\\b_n
\end{bmatrix}\cdot 
\begin{bmatrix}
A_{11}&\cdots&A_{1m}\\
\vdots&\ddots&\vdots\\
A_{n1}&\cdots&A_{nm}
\end{bmatrix}
\begin{bmatrix}x_1\\\vdots\\x_m
\end{bmatrix}\\
&= \begin{bmatrix}b_1\\\vdots\\b_n
\end{bmatrix}
\cdot 
\begin{bmatrix}\sum_{i=1}^mA_{1i}x_i\\\vdots\\\sum_{i=1}^mA_{ni}x_i
\end{bmatrix}\\
&= \sum_{j=1}^n b_j\sum_{i=1}^m A_{ji}{x_i}
\end{align*}

Therefore, for each component $x_i$, we can easily derive the partial derivative as 

$$\frac{\partial f}{\partial x_i} =\sum_{j=1}^n b_j A_{ji}$$

and so that $\nabla f = \begin{bmatrix}\sum_{j=1}^n b_j A_{j1}\\\vdots\\\sum_{j=1}^n b_j A_{jm}\end{bmatrix} = A^Tb$

!!!abstract "Part (b)"

    Let $f(x) = x\cdot Ax$, show that $\nabla f(x) = (A+A^T)x$.


\begin{align*}
\nabla (x^TAx) &= \nabla(\sum_{i=1}^n \sum_{j=1}^n A_{ij}x_ix_j)\\
&= \begin{bmatrix}\sum_{i=1}^n A_{i1}x_i + \sum_{j=1}^n A_{1j}x_j\\...\\\sum_{i=1}^n A_{in}x_i + \sum_{j=1}^n A_{nj}x_j\end{bmatrix}\\
&= Ax + A^Tx\\
&= (A+A^T)x
\end{align*}


## Example 5

!!! question

    Let $f:\mathbb R^{2n} \rightarrow \mathbb R, f(x, y) = \frac12|Ax-By|^2$, where $A,B$ are $m\times n$ matrices, $x, y\in\mathbb R^n$

!!!abstract "Part (a)"

    Find $\nabla f, \nabla^2f$

Note that $f(x, y) = \frac12 (Ax-By)^T(Ax-By)$, let $g(x, y) = Ax-By, h(a) = a^Ta$ so that $f(x, y) = \frac12h(g(x, y))$. Therefore, using chain rule, 

$$D f(x,y) = \frac12D (h\circ g)(x,y) = \frac12Dh(g(x,y)) \cdot Dg(x,y)$$

Note that $h(a) = a^T a = a^TI a$ where $I$ is the identity matrix, so that by Question 4 Part (b), $Dh(a) = (I+I^T)a = 2a$.  
Then, note that $\frac{\partial g}{\partial x} = A, \frac{\partial g}{\partial y} = -B$, hence $Df(x, y) = \begin{bmatrix}[A]&[-B]\end{bmatrix}$, i.e. matrix $A, -B$ stacked horizontally.  
Therefore, 

$$\nabla f(x, y) = \frac12 \cdot 2 [Ax-By]\cdot \begin{bmatrix}[A]\\ [-B]\end{bmatrix} = \begin{bmatrix}[A]& [-B]\end{bmatrix}^T(Ax-By)$$


Then, note that $(Ax-By)^T\begin{bmatrix}[A]& [-B]\end{bmatrix} = \begin{bmatrix}[A]& [-B]\end{bmatrix}^T Ax - \begin{bmatrix}[A]& [-B]\end{bmatrix}^TBy$. Therefore, 

$$\frac{\partial}{\partial x} \begin{bmatrix}[A]& [B]\end{bmatrix}^T Ax - \begin{bmatrix}[A]& [B]\end{bmatrix}^TBy = \begin{bmatrix}[A]& [-B]\end{bmatrix}^T A$$


$$\frac{\partial}{\partial y} \begin{bmatrix}[A]& [B]\end{bmatrix}^T Ax - \begin{bmatrix}[A]& [B]\end{bmatrix}^TBy = \begin{bmatrix}[-A]& [B]\end{bmatrix}^T B$$

Rewrite into matrix form, 

$$\nabla^2 f = \begin{bmatrix}[A^TA]& [-B^TA]\\ [-A^TB] & [B^TB]\end{bmatrix}$$


!!!abstract "Part (b)"

    If $(x_0, y_0)$ satisfies $Ax_0 = By_0$, then $(x_0, y_0)$ is a local minimum.

Note that $\nabla f(x_0, y_0) = \begin{bmatrix}[A]& [B]\end{bmatrix}^T(Ax_0-By_0) = \begin{bmatrix}[A]& [B]\end{bmatrix}^T0 = 0$ which satisfies FOC.  

Also, note that the Hessian matrix can be rewrite as 

$$\nabla^2 f = \begin{bmatrix}[A^TA]& [-B^TA]\\ [-A^TB] & [B^TB]\end{bmatrix} = \begin{bmatrix}A\\-B\end{bmatrix}^T\begin{bmatrix}A\\-B\end{bmatrix}$$ 

so that it is a positive semidefinite matrix, which satisfy the SOC.

## Example 6

!!! question
    
    Let $g$ be a convex function on $\mathbb R^n$, $f$ be a linear, nondecreasing function on a single variable.

!!!abstract "Part (a)"

    Prove $F:=f\circ g$ is convex.


\begin{align*}
F(\theta x + (1-\theta) y) = f(g(\theta x + (1- \theta) y)))
\end{align*}

By convexity of $g$, 

$$g(\theta x + (1- \theta) y) \leq \theta g(x) + (1-\theta)g(y)$$ 

By non-decreasing of $f$

$$f(g(\theta x + (1- \theta) y)) \leq f(\theta g(x) + (1-\theta)g(y))$$

By linearity of $f$

$$f(\theta g(x) + (1-\theta)g(y)) = \theta f(g(x)) + (1-\theta) f(g(y)) = \theta F(x) + (1-\theta) F(y)$$

By the definition of convex, the claim is proven. 

!!!abstract "Part (b)"

    $\nabla^2F(x)$ is positive semidefinite. 

\begin{align*}
\nabla^2F(x) &= \frac{\partial}{\partial x}(\frac{\partial f}{\partial g}\cdot \frac{\partial g}{\partial x}) &\text{chain rule}\\
&= (\frac{\partial}{\partial x}\frac{\partial f}{\partial g})\cdot \frac{\partial g}{\partial x} + \frac{\partial f}{\partial g}\cdot(\frac{\partial }{\partial x}\frac{\partial g}{\partial x})&\text{product rule}\\
&= (\frac{\partial^2 f}{\partial g^2}\cdot  \frac{\partial g}{\partial x})\cdot \frac{\partial g}{\partial x} + \frac{\partial f}{\partial g}\cdot \frac{\partial^2 g}{\partial x^2} &\text{chain rule}
\end{align*}

Rewrite the derivatives with the matrix multiplication notation

\begin{align*}
\nabla^2 F(x) &= [d^2 f(g(x)) \nabla g(x)]\nabla g(x)^T + d f(g(x))\nabla^2 g(x)\\
&= d^2 f(g(x))\nabla g(x)\nabla g(x)^T +  df(g(x))\nabla^2 g(x)
\end{align*}


Because $f$ is linear, $d^2f(g(x)) = 0$  
Because $f$ is non-decreasing, $df(g(x)) \geq 0$  
Because $g$ is convex, $\nabla^2 g(x)$ is positive semidefinite  
Also, note that $\nabla g(x) \nabla g(x)^T$ is positive semidefinite
Therefore, a positive semidefinite matrix scaled by a positive number is still positive semidefinite. 

## Example 7

!!! question 

    $f:\mathbb R^2\rightarrow \mathbb R$ is non-negative convex function, $F:\mathcal A\rightarrow \mathbb R, F(\mu) = \int_0^1f(\mu(x), \mu'(x))dx$ where $\mathcal A = \{\mu\in C^1: [0,1]\rightarrow\mathbb R\}$. Prove $F$ is convex on $\mathcal A$.


Let $a\in (0, 1), u_1, u_2\in \mathcal A$. 

$$F(au_1 + (1-a)u_2)
= \int_0^1f(au_1(x) + (1-a)u_2(x), (au_1 + (1-a)u_2)'(x)))dx$$

Using chain rule

$$= \int_0^1f(au_1(x) + (1-a)u_2(x), au_1'(x) + (1-a)u_2'(x))dx$$

Note that for any $x\in [0, 1]$, by convexity of $f$

$$f(au_1(x) + (1-a)u_2(x), au_1'(x) + (1-a)u_2'(x))
\leq af(u_1(x), u_1'(x)) + (1-a) f(u_2(x), u_2'(x))$$

Because $f$ is non-negative


\begin{align*}
&\quad\int_0^1 f(au_1(x) + (1-a)u_2(x), au_1'(x) + (1-a)u_2'(x))dx\\
&\leq \int_0^1 af(u_1(x), u_1'(x)) + (1-a) f(u_2(x), u_2'(x))dx\\
&= a\int_0^1 f(u_1(x), u_1'(x))dx + (1-a)\int_0^1 f(u_2(x), u_2'(x))dx\\
&= aF(u) + (1-a)F(u)
\end{align*}


## Example 8

!!! question 

    If $f:\Omega\rightarrow \mathbb R$ is covex on $\Omega=(a,b)$, then $f$ is also continuous. 

__lemma__ If $f:\Omega\rightarrow\mathbb R$ is convex, then $\forall x_1, x, x_2 \in \Omega, x_1\leq x\leq x_2. \frac{f(x) - f(x_1)}{x-x_1} \leq \frac{f(x_2) - f(x_1)}{x_2-x_1} \leq \frac{f(x_2) - f(x)}{x_2-x}$.  

_proof_. Let $x_1, x, x_2\in \Omega. x_1 < x < x_2$, note that $\frac{x_2 - x}{x_2 - x_1} \in [0, 1]$
Since $f$ is convex, 

$$f(x) = f(\frac{x_2 - x}{x_2 - x_1}x_1 + \frac{x-x_1}{x_2 - x_1} x_2) \leq \frac{x_2 - x}{x_2 - x_1}f(x_1) + \frac{x- x_1}{x_2 - x_1}f(x_2)$$

Then, the inequalities can be easily derived as 

\begin{align*}
\frac{f(x) - f(x_1)}{x-x_1}
&\leq \frac{1}{x-x_1}\big[\frac{x_2 - x}{x_2 - x_1}f(x_1) + \frac{x- x_1}{x_2 - x_1}f(x_2) - f(x_1)\big]\\
&= \frac1{x-x_1}\frac{x-x_1}{x_2-x_1}(f(x_2)-f(x_1))\\
&= \frac{f(x_2) - f(x_1)}{x_2-x_1}
\end{align*}

Similar derivation holds for 

$$\frac{f(x_2) - f(x)}{x_2 - x} \geq \frac{f(x_2) - f(x_1)}{x_2-x_1}$$


__Claim__ If $f$ is convex, then $\forall x_0\in (a, b), \lim_{x\rightarrow x_0} f(x) = f(x_0)$ ($f$ is continuous using the limit definition). 

_proof_. Let $c, d \in (a, b), a<c<x_0 < d<b$.  
Take functions $l_1(x) = \frac{f(x_0) - f(c)}{x_0 - c}(x-x_0) + f(x_0), l_2(x) = \frac{f(d) - f(x_0)}{d - x_0}(x-x_0) + f(x_0)$, where $l_1$ is the line pass through $(c, x_0)$ and $l_2$ is the line pass through $(x_0, d)$.  
Then, for any $x\in (x_0, d)$, since $f$ is convex and use our lemma above, we have 

$$\frac{f(x - x_0)}{x-x_0} \leq \frac{f(d) - f(x_0)}{d - x_0}$$


$$\frac{f(x) - f(c)}{x-c} \geq \frac{f(x_0) - f(c)}{x_0 - c}$$

so that 

$$f(x) = \frac{f(x - x_0)}{x-x_0}(x-x_0) + f(x_0) \leq \frac{f(d - x_0)}{d-x_0}(x-x_0) + f(x_0) = l_2(x)$$


$$f(x) = \frac{f(x) - f(c)}{x-c}(x-x_0) + f(x_0) \geq \frac{f(x_0-c)}{x_0-c}(x-x_0) + f(x_0) = l_1(x)$$

Since $\forall x\in (x_0, d), l_1(x)\leq f(x) \leq l_2(x)$ and $\lim_{x\rightarrow x_0+}l_1(x) = l_1(x_0) = f(x_0) = l_2(x_0) = \lim_{x\rightarrow x_0+}l_2(x)$, by squeeze theorem

$$\lim_{x\rightarrow x_0+}f(x) = f(x_0)$$


With the similar arguments, we can show that $\forall x\in (c, x_0), l_2(x) \leq f(x) \leq l_1(x)$, and use squeeze theorem, 

$$\lim_{x\rightarrow x_0-}f(x) = f(x_0)$$

Finally, the two limits from both sides conclude that 

$$\lim_{x\rightarrow x_0}f(x) = f(x_0)$$

Therefore, we have shown that $\forall x\in (a, b), \lim_{x\rightarrow x_0}f(x) = f(x_0)$, which means $f$ is continuous on $(a,b)$

## Example 9

!!! question 
    
    If $f:\Omega\rightarrow \mathbb R$ is continuous and convex and exists some maximum on the interior of $\Omega$, then $f$ is a constant function.

_proof._ Let $x_0 \in \Omega_{int}$ where $f(x_0)$ is the maximum.  
Assume $f$ is not constant. Take $x_1 \in \Omega$ s.t. $f(x_1) < f(x_0)$.   
Since $x_0$ is an interior point, take some $t\in(0, 1)$ s.t. $x_2 = x_0 - t(x_1 - x_0), x_2 \in B(x_0, \epsilon)\subset \Omega$ for some $\epsilon > 0$.  
Then, $x_2, x_0, x_1$ forms a line and $x_0 = \frac{t}{1+t}x_1 + \frac{1}{1+t}x_2$.   
By our assumption, $f(x_1) < f(x_0), f(x_2) \leq f(x_0)$, hence exists $c = \frac{1}{t} \in (0, 1)$

$$\frac{1}{1+t}f(x_1) + \frac{t}{1+t}f(x_2) < \frac{1}{1+t}f(x_0) + \frac{t}{1+t}f(x_0) = f(x_0)$$

This contradicts with the fact that $f$ is convex, by contradiction, $f$ must be a constant function. 

## Example 10

!!! question 

    Let $f: \Omega\rightarrow \mathbb R, f(x): a\cdot x + b$ where $\Omega$ is compact and convex subset of $\mathbb R^n$.

!!!abstract "Part (a)"

    If $a\neq 0$, then any minimizer of $f$ must be on $\partial \Omega$.

_proof_. Suppose exists some minimizer $x_0 \in \Omega_{int}$, then take some $t > 0$ s.t. $x = x_0 - ta \in B(x_0, \epsilon) \subset \Omega$ 

$$f(x) = a\cdot (x_0 - ta) + b = a\cdot x_0 - t\|a\|^2 + b = f(x_0) - t\|a\|^2$$

If $a\neq 0$, then $t\|a\|^2 > 0, f(x) < f(x_0)$, $x_0$ is not a minimizer. By contradiction, the minimizer must be on $\partial \Omega$. 


!!!abstract "Part (b)"

    Suppose $g(x) = \|x\|^2 + f(x)$, under what condition of $a$ can you guarantee that the minimizers do not occur in the interior of the set $\Omega$?

Note that $\nabla g(x) = 2x + a$. Note that a point $x_*$ is not minimizer means that exists a feasible direction $d \in \mathbb R^n$ s.t. $\nabla g(x_*) < 0$.  
Because $\|x\|^2 + f(x)$ is continuous on $\mathbb R^n$, for some interior point $x_*$, all directions are feasible, therefore $x_*$ is not a minimizer implies that $\nabla g(x_*) =2x_* + a \neq 0$.  
Therefore, to guarantee that any interior point is not a minimizer, we want $a$ to satisfy that $\forall x\in\Omega_{int}, 2x +a \neq 0$

## Example 11
!!! question 

    If $f(x):\mathbb R^n\rightarrow\mathbb R$ is convex, then $g(x, z) : \mathbb R^n \times \mathbb R \rightarrow \mathbb R, g(x, z) := f(x) + \|x+z\|^2$ is also convex.

_proof_. 
Let $x_1, z_1, x_2, z_2\in \mathbb R^n, c\in [0, 1]$, consider 

\begin{align*}
g(c(x_1, z_1) + (1-c)(x_2, z_2)) &= f(cx_1 + (1-c)x_2) + \|cx_1  + (1-c)x_2 + cz_1 + (1-c)z_2\|^2\\
&\leq cf(x_1) + (1-c)f(x_2) &f\text{ is convex}\\
&\quad + \|cx_1 + cz_1\|^2 + \|(1-c)x_2 + (1-c)z_2\|^2 &\text{triangular inequality}\\
&= cf(x_1) + c\|x_1+z_1\|^2  + (1-c)f(x_2) + (1-c)\|x_2 + z_2\|^2\\
&= cf(x_1, z_1) + (1-c)f(x_2, z_2)
\end{align*}

By definition of convexity, $g$ is convex

## Example 12

!!! question 

    For $f: \mathbb R^n \rightarrow \mathbb R$ be $C^1$ function, define $M = \{(x, f(x))\in \mathbb R^{n+1}\}$, given $p = (x_0, f(x_0)) \in M$, find the tangent space $T_pM$.

Define $g(x, z) = f(x) - z$, note that $\nabla g(x, z) = [\nabla f(x), -1]\in\mathbb R^{n}\times \mathbb R$.  
Then, note that $g(p) = 0$ and the equation of the tangent plane where $p$ is on the plane is given as 

\begin{align*}
\nabla g(x_0, f(x_0))\cdot ((x, z) - (x_0, f(x_0))) &= 0\\
\nabla f(p)\cdot(x-x_0) + (-1)(z-f(x_0))&= 0\\
\nabla f(p) \cdot(x-x_0) + f(x_0)&=z
\end{align*}

Therefore, the tangent space is given as 

$$T_pM = \{(x, \nabla f(p)\cdot(x-x_0) + f(x_0): x\in\mathbb R^n\}$$

