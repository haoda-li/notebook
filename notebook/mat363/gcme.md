# Gauss' Remarkable Theorem

## Gauss and Codazzi-Mainardi Equations


## Codazzi-Mainardi Equations
__Theorem__ 

$$L_v - M_u = L\Gamma_{12}^1 + M (\Gamma_{12}^2 - \Gamma_{11}^1) - N\Gamma_{11}^2$$

$$M_v - N_u = L\Gamma_{22}^1 + M (\Gamma_{22}^2 - \Gamma_{12}^1) - N\Gamma_{12}^2$$

_proof_. First, consider the first equation, 

$$\sigma_{uuv} = \sigma_{uvu}$$

Using Gauss equations, 

$$\Gamma_{11}^1\sigma_u + \Gamma_{11}^2\sigma_v + LN)_v = (\Gamma_{12}^1\sigma_u + \Gamma_{12}^2\sigma_v + MN)_u$$

\begin{align*}
&(\Gamma_{11}^1)_v \sigma_u + \Gamma_{11}^1\sigma_{uv} + (\Gamma_{11}^2)_v \sigma_v + \Gamma_{11}^2\sigma_{vv} + L_v\mathbf N + L\mathbf N_v\\
&= (\Gamma_{12}^1)_u \sigma_u + \Gamma_{12}^1\sigma_{uu} + (\Gamma_{12}^2)_u \sigma_v + \Gamma_{12}^2\sigma_{uv} + M_u \mathbf N + M\mathbf N_u
\end{align*}

Then, take dot product $\mathbf N$ on both sides of the equation, note $\mathbf N$ is perpendicular to $\sigma_u,\sigma_v, \mathbf N_u, \mathbf N_v$ and $\mathbf N\cdot \mathbf N = 1$, 

$$\Gamma_{11}^1\sigma_{uv}\cdot \mathbf N + \Gamma_{11}^2\sigma_{vv}\cdot\mathbf N + L_v = \Gamma_{12}^1\sigma_{uu}\cdot\mathbf N + \Gamma_{12}^1\sigma_{uv}\cdot\mathbf N + M_u$$


$$\Gamma_{11}^1 M + \Gamma_{11}^2N + L_v = \Gamma_{12}^1L + \Gamma_{12}^1M + M_u$$

reorder the equations, we have the first equation. 

$$L_v - M_u = L\Gamma_{12}^1 + M (\Gamma_{12}^2 - \Gamma_{11}^1) - N\Gamma_{11}^2$$



Similarly, the second equation can be obtained by $\sigma_{vvu} = \sigma_{uvv}$

## Gauss Equations
__Theorem__ For $K$ be the Gaussian curvature,

\begin{align*}
EK &= (\Gamma_{11}^2)_v - (\Gamma_{12}^2)_u + \Gamma_{11}^1 \Gamma_{12}^2 + \Gamma_{11}^2 \Gamma_{22}^2 - \Gamma_{12}^1\Gamma_{11}^2 - (\Gamma_{12}^2)^2\\
FK &= (\Gamma_{12}^1)_u - (\Gamma_{11}^1)_v + \Gamma_{12}^2 \Gamma_{12}^1 + \Gamma_{11}^2 \Gamma_{22}^1\\
FK &= (\Gamma_{12}^2)_v - (\Gamma_{22}^2)_u + \Gamma_{12}^1 \Gamma_{12}^2 + \Gamma_{22}^1 \Gamma_{11}^2\\
GK &= (\Gamma_{22}^1)_u - (\Gamma_{12}^1)_v + \Gamma_{22}^1 \Gamma_{11}^1 + \Gamma_{22}^2 \Gamma_{12}^1 - (\Gamma_{12}^2)^2 - \Gamma_{12}^2\Gamma_{22}^1
\end{align*}

_proof_. 

Reconsider the equation

\begin{align*}
&(\Gamma_{11}^1)_v \sigma_u + \Gamma_{11}^1\sigma_{uv} + (\Gamma_{11}^2)_v \sigma_v + \Gamma_{11}^2\sigma_{vv} + L_v\mathbf N + L\mathbf N_v\\
&= (\Gamma_{12}^1)_u \sigma_u + \Gamma_{12}^1\sigma_{uu} + (\Gamma_{12}^2)_u \sigma_v + \Gamma_{12}^2\sigma_{uv} + M_u \mathbf N + M\mathbf N_u
\end{align*}

Now, take dot product $\sigma_u$, note that $\sigma_u\cdot\sigma_u = 1, \sigma_v\cdot \sigma_u = \mathbf N\cdot\sigma_u = 0$

\begin{align*}
&(\Gamma_{11}^1)_v + \Gamma_{11}^1\sigma_{uv}\sigma_u + \Gamma_{11}^2\sigma_{vv}\sigma_u + L\mathbf N_v\sigma_u\\
&= (\Gamma_{12}^1)_u + \Gamma_{12}^1\sigma_{uu}\sigma_u  + \Gamma_{12}^2\sigma_{uv}\sigma_u + M\mathbf N_u\sigma_u
\end{align*}

Then, note that Gauss equations represents $\sigma_{uu},\sigma_{uv}, \sigma_{vv}$ in in terms of $\sigma_u, \sigma_v, \mathbf N$, dot product $\sigma_u$ so that

$$\sigma_{uu}\sigma_u = \Gamma_{11}^1, \sigma_{uv}\sigma_u = \Gamma_{12}^1,  \sigma_{vv}\sigma_u = \Gamma_{22}^1$$

Replacing them back to the equation, 

$$(\Gamma_{11}^1)_v + \Gamma_{11}^1\Gamma_{12}^1 + \Gamma_{11}^2\Gamma_{22}^1 + L\mathbf N_v\sigma_u
= (\Gamma_{12}^1)_u + \Gamma_{12}^1\Gamma_{11}^1  + \Gamma_{12}^2\Gamma_{12}^1 + M\mathbf N_u\sigma_u$$

Finally, consider $\mathbf N_u\sigma_u, \mathbf N_v\sigma_u$, which are the coefs of Weingarden, i.e. 

$$\mathbf N_u\sigma_u = \frac{LG-MF}{EG-F^2}, \mathbf N_v\sigma_u = \frac{MG-NF}{EG-F^2}$$

Therefore, 

$$L\mathbf N_v\sigma_u - M\mathbf N_u\sigma_u = -FK$$

and re-order the equation above, we obtain the second equation in the claim.  

Similarly, we can obtain 4 equations from $\sigma_{uuv} = \sigma_{uvu}, \sigma_{uvu} = \sigma_{vvu}$ and dot product each of $\sigma_u, \sigma_v$. 

### Theorem
If two surface patches has the same first and second fundamental forms, then exists a direct isometry between them. 

Moveover, for $V\subset\mathbb R^2$ open, given $EFGLMN$ being 6 smooth functions on $V$ and $E>0,G>0,EG-F^2>0$ and the 6 equations (2 CM, 4 Gauss) hold. Then for any point $p$ on $V$, there is an open set of $U\subset V, p\in U$ and a surface patch $\sigma:U\rightarrow\mathbb R^3$ s.t. $\sigma$ has the first and second fundamental forms defined by $EFGLMN$. 

In other words, given appropriate functions for first and second fundamental forms, a surface will always exist locally, and being unique up to a direct isometry. 

### Example: Cylinder

Let the $E=G=1, F=0, L=-1, M=N=0$. We verify the conditions that $E>0,G>0, EG-F^2 >0$, all coefs are zero hence $\Gamma$'s are all 0 and CM, Gauss are all satisifed. Therefore, a surface patch must exist. 

Using Gauss equations and plug in the numbers

$$\sigma_{uu} = \Gamma_{11}^1\sigma_u + \Gamma_{11}^2\sigma_v + L\mathbf N = -\mathbf N, \sigma_{uv} = \cdots = 0, \sigma_{vv} =\cdots =  0$$


Since $\sigma_v$'s derivatives $\sigma_{vu} = \sigma_{vv} = 0$, we must have that $\sigma_v = \mathbf a$ being a constant. Since $\sigma_{uv} = 0$, we have that 

$$\sigma(u,v) = \mathbf b(u) + \mathbf a v$$

where $\mathbf N = -\mathbf b''$
Then, consider $\mathbf N_u,\mathbf N_v$ where $-\mathbf N_u = a\sigma_u + b\sigma_v, -\mathbf N_v = c\sigma_u + d\sigma_v$ where 

$$\begin{bmatrix}a&c\\b&d\end{bmatrix} = F_I^{-1}F_{II} = \begin{bmatrix}1&0\\0&1\end{bmatrix}^{-1} \begin{bmatrix}-1&0\\0&0\end{bmatrix} = \begin{bmatrix}-1&0\\0&0\end{bmatrix}$$


so that $\mathbf N_u = \sigma_u,\mathbf N_v = 0$, implying that 

$$\mathbf N_u = \frac{d}{du}(-\mathbf b'') = -\mathbf b''' =\mathbf b' = \sigma_u$$

Since $\mathbf b''' + \mathbf b' = 0$, we must also have that $\mathbf b'' + \mathbf b = -\mathbf N + \mathbf b$ being constant vector. 
Take $\mathbf b(u) = \mathbf c \sin u + \mathbf d \cos u$, and to make $\mathbf b$ and $\mathbf b''$ constant, take $\mathbf c = e_1,\mathbf d = e_2$. 

Finally, $\sigma_u\times \sigma_v = \lambda \mathbf N\implies \mathbf b' \times \mathbf a = \lambda \mathbf b\implies \mathbf a = (0, 0, \lambda)$ for any $\lambda \neq 0$, say $\lambda =1$.  
Therefore, we have that $\sigma(u,v) = (\cos u, \sin u, v)$ is a parameterization of the unit cylinder. 

### Example: Sphere

Let $E = \cos^2 v, F = 0, G = 1, L =-\cos^2 v, M = 0, N = -1$. 

First, using the Weingarten map we have that 

$$\begin{bmatrix}a&c\\b&d\end{bmatrix} = F_I^{-1}F_{II} = \begin{bmatrix}\cos^2 v&0\\0&1\end{bmatrix}^{-1} \begin{bmatrix}-\cos^2v&0\\0&-1\end{bmatrix} = \begin{bmatrix}-1&0\\0&-1\end{bmatrix}$$

so that $\sigma_u = \mathbf N_u, \sigma_v = \mathbf N_v$
Therefore, $\mathbf N = \sigma + \mathbf a$ where $\mathbf a$ is constant and $\|\sigma+\mathbf a\| = 1$. Since the surface patch is equivalent to the Weingarten map, hence the Gauss map, it is an isometry from the Gauss map, which is the unit sphere. 

The parameterization is given by 

$$\sigma(u, v) = (\cos v\cos u, \cos v\sin u, \sin v)$$


### Example: Not a surface patch
$E = 1, F = 0, G = \cos^2 u, L = \cos^2 u, M = 0, N = 1$
In first fundamental form, $G$ is the only non-constant and $F$ is 0. Therefore, the non-zero Christoffel symbol are

$$\Gamma_{12}^2 = \frac{-2\cos u\sin u}{2\cos^2 u} = -2\tan u, \Gamma_{22}^1 = \frac{GG_u}{2G} = \cos u\sin u$$

Therefore, the RHS of the second equation is 

$$\cos^2 u \cos u \sin u + 2\tan u\neq 0$$

But the LHS is $0$ since $M,N$ are constants. 

Therefore, the CM equation is not satisifed and there is no surface patch. 

## Applying Gauss Equations
__Theorem__ Suppose that a surface patch $\sigma(u,v)$ has first $E=G=v^{-2}, v > 0$, prove that $L,N$ does not depend on $u$. 

_proof_. First, the non-zero FFF derivatives are $E_v = G_v = -2v^{-3}$ so that the non-zero Christoffel symbols are 

$$\Gamma_{11}^2 = \frac{-2v^{-5} }{2v^{-4} } = 1/v, \Gamma_{12}^1 = -1/v, \Gamma_{22}^2 = -1/v$$


The CM equations then gives 

$$L_v = -Lv^{-1} - Nv^{-1} = -v^{-1}(L+N), N_u = 0$$

$N_u=0$ implies that $N$ does not depend on $u$. 

Then, consider Gauss equations, plug in the equations for $EK$ or $GK$, we have that

$$v^{-2}K= -v^{-2} - 0 + 0 + 0 - 0- 0 \implies K = -1$$

where $K$ is the Gaussian curvature 

$$K = \frac{LN-M^2}{EG-F^2} = v^4LN = -1\implies LN = -v^{-4}$$

does not depend on $u$ as well. 

Going back to the first CM equation where $L_v = -v^{-1}(L+N)$, we further get that 

$$L_v = -v^{-1}(L + L^{-1}v^{-4})\implies Lv^5 L_v = 1 - L^2 v^4$$


If $F=0, M=0$, then the Christoffel symbols are

$$\Gamma_{11}^1 = \frac{E_u}{2E}, \Gamma_{11}^2 = \frac{-E_v}{2G}$$


$$\Gamma_{12}^1 = \frac{E_v}{2E}, \Gamma_{12}^2 = \frac{G_u}{2G}$$


$$\Gamma_{22}^1 = \frac{-G_u}{2E}, \Gamma_{22}^2 = \frac{G_v}{2G}$$

Therefore, the CM equations become 

$$L_v = \frac{1}{2}\big(\frac{LE_v}{E} + \frac{NE_v}{G}\big) = \frac{1}{2}E_v(\frac{L}{E}+\frac{N}{G})$$


$$N_u = -\frac{1}{2}\big(\frac{-LG_u}{E} + \frac{-NG_u}{G}) =\frac{1}{2}G_u(\frac{L}{E}+\frac{N}{G})$$

and then note that the principal curvatures are simply the roots of $(L-\kappa E)(N-\kappa G) = 0$, since $M=F=0$, thus we have $\kappa_1 = \frac{L}{E}, \kappa_2 = \frac{N}{G}$ so that 

\begin{align*}
(\kappa_1)_v &= \frac{L_vE - LE_v}{E^2}\\ 
&= \frac{\frac{1}{2}E_v(\kappa_1+\kappa_2)E - LE_v}{E^2}\\ 
&=\frac{E}{2}\frac{E_v(\kappa_1+\kappa_2) - \frac{E}{2}\frac{2L}{E}E_v}{2E^2}\\
&= \frac{E_v}{2E}(\kappa_1 + \kappa_2 - 2\kappa_1)\\
&= \frac{E_v}{2E}(\kappa_2 - \kappa_1)\\
(\kappa_2)_u &= \frac{N_uG - NG_u}{G^2} \\
&= \frac{G_u}{2G}(\kappa_1-\kappa_2)
\end{align*}

## Gauss' Remarkable Theorem

__Theorem__ The Gaussian curvature of a surface is perserved by local isometries. 

__Theorem__ The Gaussian curvature is given by 

$$K = \frac{1}{(EG-F^2)^2}\big(\det\begin{bmatrix}
\frac{E_{vv} }{2} + F_{uv} - \frac{G_{uu} }{2} &\frac{E_u}{2}&F_u-\frac{E_v}{2}\\
F_v-\frac{G_u}{2} &E&F\\
\frac{G_v}{2}&F&G
\end{bmatrix} - \det\begin{bmatrix}
0&\frac{E_v}{2}&\frac{G_u}{2}\\
\frac{E_v}{2}&E&F\\
\frac{G_u}{2}&F&G
\end{bmatrix}\big)$$

__Corollary__ If $F=0$, 

$$K = -\frac{1}{2\sqrt{EG} } \big(\partial_u (\frac{G_u}{\sqrt{EG} }) +\partial_v (\frac{E_v}{\sqrt{EG} })\big)$$


_proof_. Using the first formula of Gauss equations, and substitute each Chrsitoffel symbol

\begin{align*}
EK &= (\Gamma_{11}^2)_v - (\Gamma_{12}^2)_u + \Gamma_{11}^1 \Gamma_{12}^2 + \Gamma_{11}^2 \Gamma_{22}^2 - \Gamma_{12}^1\Gamma_{11}^2 - (\Gamma_{12}^2)^2\\
&= (-\frac{E_v}{2G})_v - (\frac{G_u}{2G})_u + \frac{E_u}{2E} \frac{G_u}{2G} + \frac{-E_v}{2G}\frac{G_v}{2G} - \frac{E_v}{2E}(-\frac{E_v}{2G}) - (\frac{G_u}{2G})^2\\
&= \frac{E_vG_v - E_{vv} G}{2G^2} - \frac{G_{uu} G - G_u^2}{2G^2}+ \frac{E_uG_u}{4EG} - \frac{E_vG_v}{2G^2} + \frac{E_v^2}{4EG} - \frac{G_u^2}{4G^2}\\
\partial_u (\frac{G_u}{\sqrt{EG} }) &= \frac{G_{uu} }{\sqrt{EG} } - \frac{G_u(E_uG + E G_u)}{2(EG)^{3/2} }\\
\partial_v (\frac{E_v}{\sqrt{EG} }) &= \frac{E_{vv} }{\sqrt{EG} } - \frac{E_v(E_vG + E G_v)}{2(EG)^{3/2} }
\end{align*}

Take $2\sqrt{EG}$ out of the RHS, and we can obtain the equation. 

__Corollary__ If $E=1,F=0$, then $K = -\frac{1}{\sqrt G}\frac{\partial^2\sqrt G}{\partial u^2}$

### Example: Sphere
__Claim__ any plane map of any region of a sphere must distort distances. 

_proof_. The claim is equivalent to that there is no isometry between open subset of a plane to a sphere.  Known that the Gaussian curvature of plane is $0$ everywhere, while $K$ for sphere is positive constant. Therefore, such isometry cannot exist.

### Example
__Claim__ If $E=e^\lambda, F=0,G=e^\lambda$, where $\lambda$ is a smooth function of $u,v$. Then

$$\Delta \lambda + 2Ke^\lambda = 0$$

$\Delta$ is the Laplacian operator

_proof_. Note that $F=0$, so that we have that 

\begin{align*}
K &= -\frac{1}{2e^\lambda } \big(\partial_u (\frac{G_u}{e^\lambda }) +\partial_v (\frac{E_v}{e^\lambda })\big)\\
&= -\frac{1}{2e^\lambda } \big(\partial_u (\frac{e^\lambda\lambda_u}{e^\lambda }) +\partial_v (\frac{e^\lambda\lambda_v}{e^\lambda })\big)\\
&= -\frac{1}{2e^\lambda }(\lambda_{uu} + \lambda_{vv})\\
K &= -\frac{1}{2e^\lambda}\Delta \lambda
\end{align*}

