# Curvature


Intuitively, curvature measures how "curved" a curve is. Suppose that $\gamma(t)$ is a pamameterized curve. As $t$ changes to $t+\Delta t$, the curve moves away from its tangent $\gamma'(t)$ by 

$$(\gamma(t+\Delta t) - \gamma(t))\cdot \hat{\mathbf n}, \|\hat{\mathbf n}\| = 1, \hat{\mathbf n}\cdot \gamma' = 0$$


Then, Taylor's theorem gives 

$$\gamma(t+\Delta t) = \gamma(t) + \gamma'(t)\Delta t + \frac{1}{2}\gamma''(t)\Delta t^2 + rem$$

By Taylor's remainder theorem, $rem$ vanishes faster than $\Delta t^2$. 

Therefore, we have 

$$(\gamma(t) + \gamma'(t)\Delta t + \frac{\Delta t^2}{2}\gamma''(t)-\gamma(t))\cdot\hat{\mathbf n} = \frac{\Delta t^2}{2}\gamma''(t)\cdot\hat{\mathbf n} $$

Then, note that $\gamma'\cdot \gamma'' = 0$ and known that $\gamma$ is unit-speed, hence $\gamma'' \parallel \hat{\mathbf n}$. So that 

$$ \frac{\Delta t^2}{2}\gamma''(t)\cdot\hat{\mathbf n}  =  \frac{\Delta t^2}{2}\|\gamma''(t)\| $$


Therefore, we can derive the definition:

If $\gamma$ is a unit-speed curve, its curvature $\kappa(t)$ at the point $\gamma(t)$ is defined as $\|\gamma''(t)\|$.

## Cross Product
For 3D vectors $\mathbf a, \mathbf b \in \mathbb R^3$, __cross product__ is a 3D vector s.t. $\mathbf a\times \mathbf b \in \mathbb R^3$ s.t. $\forall w\in\mathbb R^3. (\mathbf a\times \mathbf b)\cdot \mathbf w = \det(\begin{bmatrix}\mathbf a&\mathbf b&\mathbf w\end{bmatrix})$.  

Note that $\det(A) = \det(A^T)$, and for $3\times3$ matrices, switching two adjacent rows will flip the sign, then switch twice won't change the determinant. 

$$\det(\begin{bmatrix}\mathbf a&\mathbf b&\mathbf w\end{bmatrix}) = 
\det(\begin{bmatrix}a_1&b_1&w_1\\a_2&b_2&w_2\\a_3&b_3&w_3\end{bmatrix}) = 
\det(\begin{bmatrix}w_1&w_2&w_1\\a_1&a_2&a_3\\b_1&b_2&b_3\end{bmatrix})$$

Therefore, we can rewrite the cross product as

\begin{align*}
\mathbf a\times \mathbf b &= 
\begin{bmatrix}
    \det(\begin{bmatrix}a_2&a_3\\b_2&b_3\end{bmatrix})\\
    -\det(\begin{bmatrix}a_1&a_3\\b_1&b_3\end{bmatrix})\\
    \det(\begin{bmatrix}a_1&a_2\\b_1&b_2\end{bmatrix})
\end{bmatrix} =  
\begin{bmatrix}
a_2b_3-a_3b_2\\
a_3b_1-a_1b_3\\
a_1a_2-a_2b_1
\end{bmatrix} \\
&= (a_2b_3-a_3b_2)\mathbf e_1 - (a_1b_3-a_3b_1)\mathbf e_2 + (a_1a_2-a_2b_1)\mathbf e^3
\end{align*}


## Properties of Cross Product

### Linearity

- $\mathbf a\times (\mathbf b + \mathbf c) = \mathbf a \times \mathbf b + \mathbf a \times \mathbf c$
- $\lambda \mathbf a \times \mathbf b = \lambda (\mathbf a \times \mathbf b) = \mathbf a \times \lambda\mathbf b$
- $\mathbf a \times \mathbf b + \mathbf c \times \mathbf d = (\mathbf a - \mathbf c) \times (\mathbf b - \mathbf d) + \mathbf a \times \mathbf d + \mathbf c \times \mathbf b$

### Plane Normal

__Claim__ Cross product is perpendicular to both of its vectors. 

$$(\mathbf a \times \mathbf b) \cdot \mathbf a = (\mathbf a \times \mathbf b) \cdot \mathbf b = 0$$


_proof_. Note that 

$$(\mathbf a \times \mathbf b) \cdot \mathbf a = \det(\begin{bmatrix}\mathbf a&\mathbf b&\mathbf a\end{bmatrix}), (\mathbf a \times \mathbf b) \cdot \mathbf b = \det(\begin{bmatrix}\mathbf a&\mathbf b&\mathbf b\end{bmatrix})$$

$\begin{bmatrix}\mathbf a&\mathbf b&\mathbf a\end{bmatrix}, \begin{bmatrix}\mathbf a&\mathbf b&\mathbf b\end{bmatrix}$ are both linearly dependent, hence their determinant are both 0. 

### Geometric Meaning

__Lemma__ $(\mathbf a \times \mathbf b)\cdot (\mathbf c \times \mathbf d) = \det(\begin{bmatrix}\mathbf a\cdot\mathbf c&\mathbf b\cdot\mathbf c\\\mathbf a\cdot\mathbf d&\mathbf b\cdot\mathbf d\end{bmatrix})$.

_proof_. By linearity, it is sufficient to show only when $\mathbf a, \mathbf b, \mathbf c, \mathbf d \in \{\mathbf e_1, \mathbf e_2, \mathbf e_3\}$. Then, we can list all possible combinations and prove this claim. 

__Corollary (Lagrange's Identity in 3D)__. $\|\mathbf a\times \mathbf b\|^2 = \det(\begin{bmatrix}\mathbf a\cdot\mathbf a&\mathbf a\cdot\mathbf b\\\mathbf b\cdot\mathbf a&\mathbf b\cdot\mathbf b\end{bmatrix})$. 

_proof_. By the lemma above. 


__Corollary (Geometric Meaning of cross product in 3D)__. $\|\mathbf a\times \mathbf b\| = \|\mathbf a\|\|\mathbf b\|\sin\theta$.  

_proof_. Using Lagrange's Identity in 3D, we can then have

\begin{align*}
\|\mathbf a\times \mathbf b\|&= (\mathbf a\times \mathbf b)\cdot(\mathbf a\times \mathbf b)\\
&= \det(\begin{bmatrix}\mathbf a\cdot\mathbf a&\mathbf a\cdot\mathbf b\\\mathbf b\cdot\mathbf a&\mathbf b\cdot\mathbf b\end{bmatrix})\\
&= (\mathbf a\cdot\mathbf a) (\mathbf b\cdot\mathbf b) - (\mathbf a\cdot\mathbf b)(\mathbf b\cdot\mathbf a)\\
&= \|\mathbf a\|^2 \|\mathbf b\|^2 - (\mathbf a\cdot\mathbf b)^2\\
&= \|\mathbf a\|^2 \|\mathbf b\|^2 - \|\mathbf a\|^2 \|\mathbf b\|^2 \cos^2\theta\\
&= \|\mathbf a\|^2 \|\mathbf b\|^2 (1 - \cos^2\theta)\\
&= \|\mathbf a\|^2 \|\mathbf b\|^2 \sin^2\theta\\
\|\mathbf a\times \mathbf b\| &= \|\mathbf a\| \|\mathbf b\|\sin \theta
\end{align*}

Therefore, $\|\mathbf a\times \mathbf b\|$ can be understood are the area of the parallelogram the area of the parallelogram that $\mathbf a, \mathbf b$ span. Also, $\mathbf a\times \mathbf b, \mathbf a, \mathbf b$ forms a signed basis. 

## Curvature for 3D
Note that our definition for curvature depends on $\gamma$ being unit-speed. However, find a unit-speed parameterization is not always easy even though we know it exist. 

__Claim__ Let $\gamma(t)$ be a regular curve in $\mathbb R^3$, then its curvature is $\kappa = \frac{\|\gamma''\times \gamma'\|}{\|\gamma'\|^3}$. 

_proof_. Since $\gamma$ is regular, take $s$ be a unit-speed map for $\gamma$. 

\begin{align*}
\gamma' &= \frac{d\gamma}{dt} = \frac{d\gamma}{ds}\frac{ds}{dt}&\text{chain rule}\\
\implies \frac{d\gamma}{ds} &= \frac{d\gamma}{dt}/\frac{ds}{dt}\\
\kappa &= \|\frac{d^2\gamma}{ds^2}\|\\
&= \|\frac{d}{ds}(\frac{d\gamma}{dt}/\frac{ds}{dt})\|\\
&= \|\frac{d}{dt}(\frac{d\gamma}{dt}/\frac{ds}{dt}) / \frac{ds}{dt}\|\\
&= \| (\frac{ds}{dt}\frac{d^2\gamma}{dt^2} - \frac{d^2s}{dt^2}\frac{d\gamma}{dt})(\frac{ds}{dt})^{-3}\|
\end{align*}

Note that $s$ is the unit-length map, so that $(\frac{ds}{dt})^2 = (s')^2 = \|\gamma'\|^2 = \gamma'\cdot \gamma'$, differentiating both side gives 

$$\frac{d}{dt}((\frac{ds}{dt})^2) = \frac{ds}{dt} \frac{d^2s}{dt^2} = \gamma'\cdot\gamma''$$

Then, we can insert these back to get

\begin{align*}
\kappa &= \| (\frac{ds}{dt}\frac{d^2\gamma}{dt^2} - \frac{d^2s}{dt^2}\frac{d\gamma}{dt})(\frac{ds}{dt})^{-3}\|\\
&=  \| ((\frac{ds}{dt})^2\frac{d^2\gamma}{dt^2} - \frac{d^2s}{dt^2}\frac{ds}{dt}\frac{d\gamma}{dt})(\frac{ds}{dt})^{-4}\|\\
&= \|(\gamma'\cdot \gamma')\gamma'' - (\gamma'\cdot \gamma'')\gamma'\|\|\gamma'\|^{-4}\\
&= \frac{\|(\gamma'\cdot \gamma')\gamma'' - (\gamma'\cdot \gamma'')\gamma'\|}{\|\gamma'\|^{4} }
\end{align*}

Using vector triple product identity

$$\mathbf a\times (\mathbf b\times \mathbf c) = (\mathbf a\cdot \mathbf c)\mathbf b - (\mathbf a \cdot \mathbf b)\mathbf c$$


$$\|(\gamma'\cdot \gamma')\gamma'' - (\gamma'\cdot \gamma'')\gamma'\| = \|\gamma'\times (\gamma''\times \gamma')\| = \|\gamma'\|\|\gamma''\times \gamma'\|\sin\theta$$

Note that $\gamma'$ and $\gamma''\times \gamma'$ are orthogonal by definition of cross product, so that $\sin\theta = 1$

$$\kappa = \frac{\|\gamma'\|\|\gamma''\times \gamma'\|}{\|\gamma'\|^4} = \frac{\|\gamma''\times \gamma'\|}{\|\gamma'\|^3}$$


### Example: Compute curvature

(1) $\gamma(t) = (\frac{(1+t)^{3/2} }{3},\frac{(1-t)^{3/2} }{3}, \frac{t}{\sqrt{2} })$

\begin{align*}
\gamma'(t) &= (\frac{1}{2}\sqrt{1+t}, -\frac{1}{2}\sqrt{1-t}, \frac{1}{\sqrt{2} })\\
\|\gamma'\| &= \sqrt{\frac{1+t}{4} + \frac{1-t}{4} + \frac{1}{2} } = 1\\
\gamma''(t) &= (\frac{1}{4}(1+t)^{-1/2}, \frac{1}{4}(1-t)^{-1/2}, 0)\\
\kappa(t) = \|\gamma''(t)\| &= \sqrt{(16(1+t))^{-1} + (16(1-t))^{-1} } \\
&= \sqrt{\frac{1-t + 1+t}{16(1+t)(1-t)} } \\
&= (8(1-t^2))^{-1/2}
\end{align*}

(2) $\gamma(t) = (\frac{4\cos t}{5}, 1-\sin t, \frac{-3\cos t}{5})$

\begin{align*}
\gamma'(t) &= (-\frac{4}{5}\sin t, -\cos t, \frac{3}{5}\sin t)\\
\|\gamma'(t)\| &= (\frac{16}{25}\sin^2 t + cos^2 t + \frac{9}{25}\sin^2 t)^{1/2} = 1\\
\gamma''(t) &= (-\frac{4}{5}\cos t, \sin t, \frac{3}{5}\cos t)\\
\kappa(t) = \|\gamma''(t)\| &= (\frac{16}{25}\cos^2 t + \sin^2 t + \frac{9}{25}\cos^2 t)^{1/2} = 1
\end{align*}

(3) $\gamma(t) = (t, \cosh t)$

\begin{align*}
\gamma'(t) &= (1, \sinh t)\\
\|\gamma'(t)\| &= \sqrt{1 + \sinh^2} \neq 1\\
\gamma''(t) &= (0, \cosh t)\\
\kappa(t) &= \frac{\|\gamma''(t)\times \gamma'(t)\|}{\|\gamma'(t)\|^3}\\
&= (1 + \sinh^2)^{-3/2}\begin{vmatrix}
i&j&k\\
1&\sinh t&0\\
0&\cosh t&0
\end{vmatrix}
&= (1+\sinh^2)^{-3/2} \cosh t
\end{align*}


(4) $\gamma(t) = (\cos^3 t, \sin^3 t)$

\begin{align*}
\gamma'(t) &= (-3\cos^2 t \sin t, 3\sin^2 t \cos t)\\
\|\gamma'(t)\| &= (9\cos^4 t sin^2 t + 9 \sin^4 t \cos^2 t)^{1/2} = |3\sin t \cos t|\\
\gamma''(t) &= (6\cos t\sin^2 t - 3cos^3 t, 6\sin t\cos^2 t - 3\sin^3 t))\\
\|\gamma''(t) \times \gamma'(t)\| &= (-3\cos^2 t \sin t)(6\sin t\cos^2 t - 3\sin^3 t) - (3\sin^2 t \cos t)(6\cos t\sin^2 t - 3cos^3 t)\\
&= |-18\sin^2 t\cos^4 t + 9\sin^4 t \cos^2 t - 18\sin^4 t \cos^2 t + 9\sin^2 t \cos^4 t|\\
&= 9\sin^2 t\cos^2 t = |3\sin t \cos t|^2\\
\kappa(t) &= \frac{ |3\sin t \cos t|^2}{ |3\sin t \cos t|^3} =  |3\sin t \cos t|^{-1}
\end{align*}

???quote "Source code"

    ```python
    --8<-- "mat363/scripts/curvature.py"
    ```



```plotly
{"file_path": "./mat363/assets/curvature.json"}
```



### Claim 1
For some regular curve $\gamma$, and its curvature o$\kappa$, if $\forall t,\kappa(t) > 0$, then $\kappa$ is smooth. 

_proof_. Let $\gamma$ be regular, wlog assume $\gamma$ is unit-length so that $\kappa = \|\gamma''\|$.   
Note that $\gamma$ is smooth, hence all of its components are smooth, add is smooth, and square root is smooth on $(0, \infty)$. Therefore, $\kappa = \|\gamma''\|$ is smooth on $(0,\infty)$.
