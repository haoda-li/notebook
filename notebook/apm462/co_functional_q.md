# Examples: Constrainted Optimization on Calulus of Variations

## Example 1 (Proof of equality constraint EL Equation)

!!! question

    Consider the problem

    \begin{align*}
    \text{minimize}\quad &I[x(\cdot)] = \frac12\int_0^\pi [x'(t)]^2 dt\\
    \text{subject to} \quad & J[x(\cdot)] = \int_0^\pi [x(t)]^2 dt = 1\\
    \text{with conditions} \quad &x\in \mathcal A :=\{x:[0,\pi]\rightarrow \mathbb R\mid x(0) = x(\pi) = 0\}
    \end{align*}

    Suppose $x$ is a $C^2$ function that solve the problem, let $y\in \mathcal A$ be $C^2$, define

    $$a(s) = \bigg[\int_0^\pi(x(t) + sy(t))^2 dt\bigg]^{1/2}$$

    $$i(s) = I[\frac{x(\cdot) + sy(\cdot))}{a(s)}]$$

!!!abstract "Part (a)"

    Show that $a(0) = 1, i'(0) = 0$

_proof._   

$$a(0) = (\int_0^\pi (x(t) + 0y(t)^2)dt)^{1/2} = (\int_0^\pi x(t)^2dt)^{1/2}$$

Since $x$ solve the problem, it must follows the constraint $\int_0^\pi x(t) = 1$

$$a(0) = (\int_0^\pi x(t)^2dt)^{1/2} = 1$$

Since $x$ is the minimizer, FONC gives that 

$$\frac{d}{ds}\mid_{s=0}I[x(\cdot) + sy(\cdot)] = 0$$

for any test function $y\in\mathcal A$, note that 

$$\frac{d}{ds}\mid_{s=0}I[x(\cdot) + sy(\cdot)] = \frac{d}{ds}\mid_{s=0}I[\frac{x(\cdot) + sy(\cdot)}{1}] = i'(0) = 0$$


!!!abstract "Part (b)"

    Show that

    $$i'(0) = \int_0^\pi x'(t)y'(t)dt - \lambda \int_0^\pi x(t)y(t)dt$$

    for constant $\lambda$ in terms of $x(t)$.

_proof_. 
By multiplication rule

$$i'(s) = -2a(s)^{-3}a'(s)I[x + sy] + a(s)^{-2}\frac{d}{ds}I[x+sy]$$

Evaluate at $s=0$ with $a(0) = 1$, we have

$$i'(0) = -2a'(0)I[x(\cdot)] + \left.\frac{d}{ds}\right\vert_{s=0}I[x(\cdot) + sy(\cdot)]$$

Then, note that 

\begin{align*}
a'(s) &= \frac{1}{2}\bigg(\int_0^\pi(x(t) + sy(t))^2 dt\bigg)^{-1/2}\\&\quad\frac{d}{ds}\int_0^\pi(x(t) + sy(t))^2dt\\
&= \frac{1}{2}a(s)^{-1} 2\int_0^\pi (x(t) + sy(t))y(t)dt &\text{Leibniz rule}\\
a'(0) &= \int_0^\pi(x(t)+0y(t))y(t)dt \\
&= \int_0^\pi x(t)y(t)dt\\
\frac{d}{ds}I[x + sy]&= \frac{1}{2}\frac{d}{ds}\int_0^\pi(\frac d{dt} x(t)+sy(t))^2 dt\\
&= \frac12\frac{d}{ds}\int_0^\pi (x'(t) + sy'(t))^2dt\\
&= \frac12\int_0^\pi \frac{d}{ds}(x'(t) + sy'(t))^2dt&\text{Leibniz rule}\\
&= \int_0^\pi (x'(t)+sy'(t))y'(t)dt\\
\left.\frac{d}{ds}\right\vert_{s=0}I[x(\cdot) + sy(\cdot)]&= \int_0^\pi(x'(t) + 0 y'(t))y'(t)dt \\
&= \int_0^\pi x'(t)y'(t)dt\\
i'(0) &= -2I[x(\cdot)]\int_0^\pi x(t)y(t)dt + \int_0^\pi x'(t)y'(t)dt
\end{align*}

so that let $\lambda = -2 I[x(\cdot)]$ we have 

$$i'(0) = \int_0^\pi x'(t)y'(t)dt -\lambda \int_0^\pi x(t)y(t)dt$$


!!!abstract "Part (c)"

    Show that $x''(t) + \lambda x(t) = 0$ for $0 <t<\pi$.

_proof_. Note that $i'(0) = 0$
so that 

\begin{align*}
0 &= \int_0^\pi x'(t)y'(t)dt -\lambda \int_0^\pi x(t)y(t)dt\\
&= x'(t)y(t)\vert^\pi_0 - \int_0^\pi x''(t)y(t)dt -\lambda\int_0^\pi x(t)y(t)dt&\text{integration by parts}\\
&= 0 - \int_0^\pi x''(t)y(t) + \lambda x(t)y(t)dt\\
0 &= \int_0^\pi (x''(t) + \lambda x(t))y(t)dt
\end{align*}

To satisfy this equation for all $y\in\mathcal A$, we must have $x''(t) + \lambda x(t) = 0$

## Example 2

!!! question

    Let $\mathcal A = \{u:[0,1]\rightarrow\mathbb R^3\mid u\in C^1 u(0)=A, u(1)=B\}$, consider the "holonomic constraints" problem

    \begin{align*}
    \text{minimize}\quad F[u(\cdot)]:=\int_0^1 \sqrt{u'_1(t)^2 + u'_2(t)^2 + u'_3(t)^2}dt\\
    \text{subject to}\quad u\in\mathcal A, G(u(t)) = u_1(t)^2 + u_2(t)^2 = 1
    \end{align*}

    Find EL equations for this problem.


\begin{align*}
L(t, z_1,z_2,z_3,p_1,p_2,p_3) &= (p_1^2 + p_2^2+p_3^2)^{1/2}\\
L_z &= 0\\
L_{p_i} &= p_i(p_1^2 + p_2^2+p_3^2)^{-1/2} \\
&= \frac{u'_i(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2 + u'_3(t)^2}}\\
\nabla_u G &= (2u_1(t), 2u_2(t), 0)\\
\frac{\partial F}{\partial u_1} &= 0 - \frac{d}{dt}L_{p_i}\\
&= -\frac{d}{dt} \frac{u'_i(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2 + u'_3(t)^2}}
\end{align*}

Therefore, for some $\lambda:[0, 1]\rightarrow \mathbb R$, the EL equations is 

$$\begin{bmatrix}
-\frac{d}{dt} \frac{u'_1(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2 + u'_3(t)^2}}\\
-\frac{d}{dt} \frac{u'_2(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2 + u'_3(t)^2}}\\
-\frac{d}{dt} \frac{u'_3(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2 + u'_3(t)^2}}
\end{bmatrix} + \lambda(t)
\begin{bmatrix}
2u_1(t)\\
2u_2(t)\\
0
\end{bmatrix} =\begin{bmatrix}
0\\0\\0
\end{bmatrix}$$

## Example 3

!!!question

    Let $\mathcal A = \{u:[0,1]\rightarrow\mathbb R^2\mid u\in C^1, u(0)=A, u(1)=B\}$, consider the "holonomic constraints" problem.

\begin{align*}
\text{minimize}\quad F[u(\cdot)]:=\int_0^1 \sqrt{u'_1(t)^2 + u'_2(t)^2}dt\\
\text{subject to}\quad u\in\mathcal A, G(u(t)) = u_1(t) + u_2(t)^2 = 1
\end{align*}

!!!abstract "Part (a)"
    
    Find the EL Equation

We can easily have the EL equations being

$$\begin{bmatrix}
-\frac{d}{dt} \frac{u'_1(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2}}\\
-\frac{d}{dt} \frac{u'_2(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2}}
\end{bmatrix} + \lambda(t)
\begin{bmatrix}
1\\
2u_2(t)
\end{bmatrix} =\begin{bmatrix}
0\\0
\end{bmatrix}$$

!!!abstract "Part (b)"

    Solve the problem as a unconstrainted problem

Consider $u_2\in \{v:[0, 1]\rightarrow \mathbb R\mid v(0) = a, v(1) = b, v\in C^1\}$, the original problem is equivalent to minimize 

\begin{align*}
F[v(\cdot)] &= \int_0^1 \sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}dt\\
&= \int_0^1 \sqrt{u_2'(t)^2 + (-2u_2(t)u_2'(t))^2}\\
&= \int_0^1 \sqrt{(1 + 4u_2(t)^2)u_2'(t)^2}dt\\
L(x, z, p) &= \sqrt{(1+4z^2)p^2}\\
L_z &= ((1+4z^2)p^2)^{-1/2}(4p^2z)\\
&= \frac{4u_2(t)u_2'(t)^2}{\sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}}\\
L_p &= ((1+4z^2)p^2)^{-1/2}(1+4z^2)p\\
\frac{d}{dt}L_p &= \frac{d}{dt}\frac{(1 + 4u_2(t)^2)u_2'(t)}{\sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}}
\end{align*}

so that the EL equations give 

$$- \frac{d}{dt}\frac{(1 + 4u_2(t)^2)u_2'(t)}{\sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}} + \frac{4u_2(t)u_2'(t)^2}{\sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}}= 0 $$


!!!abstract "Part (c)"

    Show that (a) and (b) gives the same answer

From (a), we have 

$$\lambda(t) = \frac{d}{dt}\frac{u'_1(t)}{\sqrt{u'_1(t)^2 + u'_2(t)^2}}$$

From (b), note that $u_1' = \frac{d}{dt}(1-u_2^2) = -2u_2u_2'$
so that we can write

\begin{align*}
- \frac{d}{dt}\frac{(1 + 4u_2(t)^2)u_2'(t)}{\sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}} + \frac{4u_2(t)u_2'(t)^2}{\sqrt{u_2'(t)^2 + \big[\frac{d}{dt}(1-u_2(t)^2)\big]^2}}&= 0 \\
-\frac{d}{dt}\frac{u_2'}{\sqrt{u_1'(t)^2 + u_2'(t)^2}} + \frac{d}{dt}\frac{2u_2(t)u_1'(t)}{{\sqrt{u_1'(t)^2 + u_2'(t)^2}}} + \frac{2u_2'(t)u_1'(t)}{{\sqrt{u_1'(t)^2 + u_2'(t)^2}}}&=0\\
-\frac{d}{dt}\frac{u_2'}{\sqrt{u_1'(t)^2 + u_2'(t)^2}} + 2u_2(t)\frac{d}{dt}\frac{u_1'(t)}{{\sqrt{u_1'(t)^2 + u_2'(t)^2}}} &= 0\\
-\frac{d}{dt}\frac{u_2'}{\sqrt{u_1'(t)^2 + u_2'(t)^2}} + 2u_2(t)\lambda(t) &= 0\\
\end{align*}


## Example 4

!!!question

    Let $u\in \mathcal A = \{u:[0, 1]\rightarrow \mathbb R\mid u\in C^1, u(0) = 0\}$.

\begin{align*}\text{minimize}\quad &F[u] = \int_0^1L^F(x, u(x), u'(x))dx\\
\text{subject to}\quad &G[u] =\int_0^1 u'(x)dx = a
\end{align*}


!!!abstract "Part (a)"

    Write the EL Equation


\begin{align*}
\frac{\partial F}{\partial u} &= L^F_z(x, u(x), u'(x)) - \frac{d}{dx}L^F_p(x, u(x), u'(x))\\
L^G(x, z, p) &= p\\
\frac{d}{dt}L^G_p &= \frac{d}{dt}1 = 0\\
\frac{\partial G}{\partial u} &= 0
\end{align*}


$$L^F_z(x, u(x), u'(x)) - \frac{d}{dx}L^F_p(x, u(x), u'(x)) - \lambda\times 0= 0$$

And $G[u] = \int_0^1 u'(x)dx = u(x)\mid^1_0 = u(1) - 0 = a$, note that this constraint makes the two end points of $u$ fixed, so EL equation is the only needed first order necessary condition.  
So that we have 

$$L^F_z(x, u(x), u'(x)) - \frac{d}{dx}L^F_p(x, u(x), u'(x))= 0$$


$$u(1) = a$$


!!!abstract "Part (b)"

    Formulated the problem as a unconstrianed problem and solve it

Note that $G[u] = u(1) - u(0) = u(1) = a$ so that the problem is to minimize $F[u]$ on $u\in \{u:[0, 1]\rightarrow \mathbb R\mid u\in C^1, u(0) = 0, u(1) =a\}$, hence the EL equation is simply 

$$L^F_z(x, u(x), u'(x)) - \frac{d}{dx}L^F_p(x, u(x), u'(x)) = 0$$


!!!abstract "Part (c)"

    Show (a) and (b) gives the same answer

Trivially, 

$$L^F_z(x, u(x), u'(x)) - \frac{d}{dx}L^F_p(x, u(x), u'(x))= 0$$


$$u(1) = a$$


$$u\in \{u:[0, 1]\rightarrow \mathbb R\mid u\in C^1, u(0) = 0\}$$

Is the same as 

$$L^F_z(x, u(x), u'(x)) - \frac{d}{dx}L^F_p(x, u(x), u'(x))= 0$$


$$u\in \{u:[0, 1]\rightarrow \mathbb R\mid u\in C^1, u(0) = 0, u(1) = a\}$$


## Example 5

!!!question

    Consider the minimization problem in Q4, but the two endpoints are both unfixed, find the FONC.

Note that the constraint $G[u] = \int_0^1 u'(x)dx = u(1) - u(0) = a$, so that we are optimize $F[u]$ on $\mathcal A := \{u[0, 1]\rightarrow \mathbb R\mid u\in C^1, u(1)-u(0) = a\}$.  
Consider test function $v$ s.t. $v(0) = v(1) = 0$.  
Assume $u_*$ is a minimizer, define 

$$f(s, t):\mathbb R^2\rightarrow \mathbb R := F[u_*(\cdot) + sv(\cdot) + t] = \int_0^1 L(x, u(x)+sv(x)+t, u'(x) + sv'(x))dx$$

so that 

$$\mathcal A = \{u_*+sv+t\mid s,t\in\mathbb R\}$$

Since $u_*$ is a minimizer, we must have $\nabla f = 0$

$$\frac{\partial}{\partial s}\mid_{(s,t)=(0, 0)}F = \int_0^1 L_z^F(\cdots)v(x) + L_p^G(\cdots)v'(x)dx = \int_0^1(L_z - \frac{d}{dx}L_p)v(x)dx$$

The computation of the above equation is identical to the proof of Euler Lagrange equation, and by fundamental lemma, we have must 

$$L_z(x, u(x), u'(x)) - \frac{d}{dx}L_p(x, u(x), u'(x)) = 0$$

Then, we also need to have

$$\frac{\partial}{\partial t}\mid_{(s,t) =(0,0)}F = \int_0^1 L_z^F(x, u(x), u'(x)) dx=0$$

so that FONC are 

$$L_z(x, u(x), u'(x)) - \frac{d}{dx}L_p(x, u(x), u'(x)) = 0$$


$$\int_0^1 L_z^F(x, u(x), u'(x)) dx=0$$


## Example 6
!!!question 

    Prove Euler-Lagrange equation for isoperimetric problems.

_proof_. Take $v_2$ s.t. $\int_a^b \frac{\partial G}{\partial u}(u_*)(x)v_2(x)dx \neq 0$. Let $f(s, t) = F[u_* +sv_1 + tv_2]$ and $g(s, t) = G[u_*+sv_1+tv_2]$. 
Note that 

\begin{align*}
\frac{\partial}{\partial s}g(0, 0) &= \int_a^b \frac{\partial}{\partial s}\mid_{(s, t)=(0, 0)}L^G(x, u_* + sv_1 + tv_2, u_*'+sv_1'+tv_2')dx\\
&= \int_a^b L_z^G(\cdots)\frac{\partial}{\partial s}(u_*+sv_1+tv_2) + L_p^G(\cdots)\frac{\partial}{\partial s}(u_*'+sv_1'+tv_2')\\
&= \int_a^b L_z^G(\cdots)v_1(x) + L_p^G(\cdots)v_1'(x)\\
&=\int_a^b (L_z^G(x, u_*, u_*') - \frac{d}{dx}L_p^G(x, u_*, u_*'))v_1(x)dx\\
&= \int_{a}^b \frac{\partial G}{\partial u}(u_*)(x)v_1(x)dx
\end{align*}

The above equation is obtained by integration by parts, the steps are identical to the computation for $\frac{d}{ds}\mid_{s=0}F[u+sv]$.  
With the similar derivations, we can show that 

$$\frac{\partial}{\partial t}g(0, 0) = \int_{a}^b \frac{\partial G}{\partial u}(u_*)(x)v_2(x)dx$$


$$\frac{\partial}{\partial t}f(0,0) = \int_{a}^b \frac{\partial F}{\partial u}(u_*)(x)v_1(x)dx$$


$$\frac{\partial}{\partial t}f(0,0) = \int_{a}^b \frac{\partial F}{\partial u}(u_*)(x)v_1(x)dx$$

Note that by our assumption, $\frac{\partial}{\partial t}g(0,0) = \int_{a}^b \frac{\partial G}{\partial u}(u_*)(x)v_2(x)dx\neq 0$ so that $\nabla g(0, 0) \neq 0$, therefore we can safely apply Lagrange multipliers, i.e. for some $\lambda$

\begin{align*}0 &= \int_{a}^b \frac{\partial F}{\partial u}(u_*)(x)v_1(x)dx + \lambda \int_{a}^b \frac{\partial G}{\partial u}(u_*)(x)v_1(x)dx \\
&= \int_a^b (\frac{\partial F}{\partial u} + \lambda \frac{\partial G}{\partial u})v_1(x)dx\\
0 &= \int_{a}^b \frac{\partial F}{\partial u}(u_*)(x)v_2(x)dx + \lambda \int_{a}^b \frac{\partial G}{\partial u}(u_*)(x)v_2(x)dx \\
&= \int_a^b (\frac{\partial F}{\partial u} + \lambda \frac{\partial G}{\partial u})v_2(x)dx\\
\end{align*}

By fundamental lemma, both equations lead to 

$$\frac{\partial F}{\partial u} + \lambda \frac{\partial G}{\partial u} = 0$$

a.k.a

$$L_z^F - \frac{d}{dx}L_p^F + \lambda(L_z^G - \frac{d}{dx}L_p^G) = 0$$


$$-\frac{d}{dx}(L^G+\lambda L^G)_p(x, u_*, u'_*) + (L^F+\lambda L^G)_z(x, u_*,u_*') = 0$$

