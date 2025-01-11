# Space Curves

## Torsion

Let $\gamma$ be a unit-speed curve in $\mathbb R^3$, $\mathbf t = \gamma'$ be its unit tangent vector.  

If $\kappa$ is non-zero, then we define the __principal normal__ of $\gamma$ at the point $\gamma(s)$ to be 

$$\mathbf n(s) = \frac{1}{\kappa(s)} \mathbf t'(s)$$

Note that the principal normal is a unit vector, or normalized $\gamma''$. 

Then, define the __binormal vector__   of $\gamma$ at the point $\gamma(s)$ to be $\mathbf b = \mathbf t\times \mathbf n$, we then obtain an orthonormal, right-handed basis $\{\mathbf t, \mathbf n, \mathbf b\}$, i.e.,

$$\mathbf b = \mathbf t\times \mathbf n, \mathbf n = \mathbf b\times \mathbf t, \mathbf t = \mathbf n \times \mathbf b$$


Then, if we differentiate $\mathbf b$, we get 

\begin{align*}
\mathbf b' &= (\mathbf t\times \mathbf n)' \\
&=\mathbf t' \times \mathbf n + \mathbf t \times \mathbf n'\\
&= \mathbf t \times \mathbf n' &\mathbf t' = \kappa \mathbf n \text{, parallel to } \mathbf n
\end{align*}

So that $\mathbf b'\perp \mathbf t$.  In addition, note that $\mathbf b'\perp \mathbf b$ since $\mathbf b$ is unit-length. Hence it must follows that 

$$\mathbf b' = -\tau \mathbf n$$

We define such $\tau$ as __torsion__.

Note that the torsion is only defined if the curvature is non-zero. 

### Formulas for Torsion

__Theorem__ Let $\gamma: (a,b)\rightarrow\mathbb R^3$ be a regular curve with nowhere-vanishing curvature. Then its torsion is given by 

$$\tau = \frac{(\gamma' \times \gamma'')\cdot \gamma'''}{\|\gamma'\times \gamma''\|^2}$$


_proof_. We first sketch the proof by assuming $\gamma$ is unit-speed so that

\begin{align*}
-\tau \mathbf n\cdot \mathbf n &= -\mathbf n\cdot \mathbf b' \\
\tau &= \mathbf n \cdot (\mathbf t \times \mathbf n')\\
\tau &= \frac{1}{\kappa}\gamma''\cdot \big(\gamma' \times (\frac{1}{\kappa}\gamma''' - \frac{\kappa'}{\kappa^2}\gamma'')\big)\\
&= \kappa^{-2}\gamma'''\cdot (\gamma'\times \gamma'')\\
&= \frac{(\gamma' \times \gamma'')\cdot \gamma'''}{\|\gamma'\times \gamma''\|^2}
\end{align*}

In general, we can use $s$ to be the arc-length along $\gamma$ so that $\frac{d\gamma}{dt} = \frac{d\gamma}{ds}\frac{ds}{dt}$ and so on, and replaces each differentials. 

### Torsion for plane curves

__Theorem__ For some $\gamma$ be a regular curve in $\mathbb R^3$ with nowhere vanishing curvature, $\tau(s) = 0$ for all $s$ IFF the image of $\gamma$ is contained in some plane.

_proof_. Assume $\gamma((a,b))$ is contained in some plane $\{v: \mathbf v\cdot \mathbf N = d\}$ so that we have 

\begin{align*}
\gamma\cdot N &= d\\
\frac{d}{ds}(\gamma\cdot N) &= 0\\
\mathbf t \cdot \mathbf N &= 0\\
\mathbf t' \cdot \mathbf N &= 0\\
\kappa \mathbf n\cdot \mathbf N &= 0
\end{align*}

Therefore, both $\mathbf t \perp\mathbf N$ and $\mathbf n \perp\mathbf N$. Hence $\mathbf b = \mathbf t\times \mathbf n$ is parallel to $\mathbf N$. Since $\mathbf N, \mathbf b$ are both unit vectors and $\mathbf b(s)$ is smooth, we have $\mathbf b = \mathbf N$ or $\mathbf b = -\mathbf N$. So that $\mathbf b' = 0\implies \tau = 0$.

Assume $\tau = 0$ everywhere, so that $\mathbf b' = 0$ and $\mathbf b$ is constant. Then consider 

$$\frac{d}{ds}(\gamma\cdot \mathbf n) = \gamma' \cdot \mathbf b = \mathbf t\times \mathbf b = 0$$

Hence $\gamma\cdot \mathbf n = d$ for some constant $d$.  

## Frenet-Serret Equations

__Theorem__ Let $\gamma$ be a unit speed curve in $\mathbb R^3$ with nowhere vanishing curvature. Then 

$$\begin{bmatrix}\mathbf t' \\\mathbf n' \\\mathbf b' \end{bmatrix} = 
\begin{bmatrix}0&\kappa&0\\-\kappa&0&\tau\\0&-\tau&0\end{bmatrix}
\begin{bmatrix}\mathbf t \\\mathbf n \\\mathbf b \end{bmatrix} = 
\begin{bmatrix}\kappa\mathbf n \\-\kappa \mathbf t + \tau \mathbf b \\-\tau\mathbf n \end{bmatrix}$$

_proof_. We have already obtained $\mathbf t', \mathbf n'$, for $\mathbf n'$ we have 

$$\mathbf n' = \mathbf b'\times \mathbf t + \mathbf b\times \mathbf t' = -\tau\mathbf n\times \mathbf t + \kappa\mathbf b \times \mathbf n = \tau \mathbf b - \kappa\mathbf t$$



### Example: k = c, t = 0

__Claim__ For $\gamma$ be a unit-speed curve in 3D, if $\kappa$ is a constant and $\tau = 0$ for all $s$, then, $\gamma$ parameterizes a circle or an arc of a circle.

_proof_. Since $\tau = 0$, let $\Pi$ be the plane that $\gamma$ lies, and $\Pi$ has its plane normal be $\mathbf b$.  
By FS equation, $\mathbf n' = -\kappa\mathbf t + \tau\mathbf b = -\kappa \mathbf t$. Then, 

$$\frac{d}{ds}(\gamma + \frac{1}{\kappa}\mathbf n) = \mathbf t + \frac{1}{\kappa}\mathbf n' = \mathbf t- \mathbf t = 0$$

So that $\gamma + \kappa^{-1}\mathbf n$ is a constant, and 

$$\|\gamma - (\gamma + \frac{1}{k}\mathbf n)\|  = \|-\frac{1}{k}\mathbf n\| = \kappa^{-1}$$

So that $\gamma$ lies on the sphere $S$ with center $\gamma + \frac{1}{k}\mathbf n$ and radius $\kappa^{-1}$ and the intersection of $\Pi$.


## Space Curve via k and t

__Lemma__ Let $A$ be a skew-symmetric $3\times 3$ matrix ($a_{ij} = -a_{ji}$). Let $v_1,v_2,v_3$ be smooth functions of a parameter $s$ satisfying the differential equations $v_i' = \sum_{j=1}^3 a_{ij}v_j$ and suppose that for some $s_0$, $v_1(s_0), v_2(s_0), v_3(s_0)$ are orthonormal. Show $\forall s. v_1(s), v_2(s), v_3(s)$ are orthonormal. 

_proof_. We aim to show that $v_i\cdot v_j = 1$ for all $i\neq j$. Note that 

\begin{align*}
\frac{d}{ds}(v_i\cdot v_j) &= v_i'\cdot v_j + v_i\cdot v_j' \\
&= \sum_{k=1}^3 a_{ik}v_k\cdot v_j + \sum_{k=1}^3 a_{jk}v_k \cdot v_i \\
&= \sum_{k=1}^3 a_{ik}v_k\cdot v_j - \sum_{k=1}^3 a_{kj}v_k \cdot v_i
\end{align*}

Have a unique solution given that the condition satisfies for $s=s_0$. 

__Theorem__ For $k:\mathbb R\rightarrow \mathbb R^{>0}$ and $t:\mathbb R\rightarrow \mathbb R$ be two smooth function, there is a unit-speed curve in $\mathbb R^3$ whose curvature is $k$ and torsion is $t$.

_proof_. Following from FS equations, we want to solve for functions $\mathbf T, \mathbf N, \mathbf B$ for some point $s_0$ s.t. $\mathbf T(s_0) = e_1, \mathbf N(s_0) = e_2, \mathbf B(s_0) = e_3$. Note that the FS matrix is skew-symmetric so that by lemma we have a unique solution for $\mathbf T,\mathbf N, \mathbf B$ s.t. they are orthonormal for all $s$. Then, let 

$$\gamma(s) = \int_{s_0}^s \mathbf T(u)du$$

and we can verify all of $\mathbf T, \mathbf N, \mathbf B, \gamma$ are unit-length. 


__Theorem__ And all curves with the same curvature and torsion are isomorphic to each other. 
