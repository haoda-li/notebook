# Splines

Given a set of control points, we are interested in finding a "smooth" interpolation (note that this can be $C^k$ smooth, not necessarily mathematically smooth $C^\infty$) over the control points. In general, we look at __splines__, or piecewise polynomials functions because they are easy to construct and evaluate. 

## Cubic Hermite Interpolation

Given the endpoints $P(0), P(1)$ and its derivative $P'(0), P'(1)$, we can interpolate a spline over the interval $[0, 1]$ using a cubic polynomial. 

### Polynomial basis functions

A __polynomial function__ is defined as 

$$x(u) = \sum_{i=0}^d c_i u^i = C\cdot \mathcal P^d$$

where $C = [c_0, c_1, c_2, \cdots c_d], \mathcal P^d(u) = [1, u, u^2, \cdots, u^d]$ and the elements of $P^d$ are linearly independent $\forall k. u^k \neq \sum_{i\neq k} c_i u^i$.

### Polynomial Fitting

Construct a cubic polynomial and its derivative

$$x(u) = c_0 + c_1u + c_2 u^2 + c_3 u^3, x'(u) = c_1 + 2c_2 u + 3c_3 u^2$$

Then, given the endpoints and derivative at end points

\begin{align*}
P(0) &= c_0\\
P(1) &= c_0 + c_1 + c_2 + c_3\\
P'(0) &= c_1\\
P'(1) &= c_1 + 2c_2 + 3 c_3
\end{align*}

This system of equations can be written as $\begin{bmatrix}1&0&0&0\\1&1&1&1\\0&1&0&0\\0&1&2&3\end{bmatrix} \begin{bmatrix}c_0\\c_1\\c_2\\c_3\end{bmatrix} = \begin{bmatrix}P(0)\\P(1)\\P'(0)\\P'(1)\end{bmatrix}$, or conveniently through a multiplication of the inverse matrix 

$$C = \begin{bmatrix}c_0\\c_1\\c_2\\c_3\end{bmatrix} = \begin{bmatrix}1&0&0&0\\0&0&1&0\\-3&3&-2&-1\\2&-2&1&1\end{bmatrix} \begin{bmatrix}P(0)\\P(1)\\P'(0)\\P'(1)\end{bmatrix} = \beta_{H} \cdot \mathbf h$$

$\beta_H$ is called the __Hermite basis matrix__. 

## Catmull-Rom Interpolation

Now, consider multiple control points (without knowing the derivative). Note that each points introduces one equations and we could use high-order polynomials to fit. However, high-order polynomials require more computations and is not stable. Instead, for each control point, we aim to match slop between its previous and next value. 

Consider 4 points $(u_0, x(u_0)), (u_1, x(u_1)), (u_2, x(u_2)), (u_3, x(u_3))$, set the slope at $x(u_i)$ as $d_ux|_{u_i} = \frac{1}{2}{x(u_{i+1}) - x(u_{i-1})}$ and we can use cubic Hermite interpolation to compute the curve between each pair of neighboring points. In addition, the overall curve is __$C^1$ continuous__. For each point, its derivative is defined and it's continuous from both left and right. 

### Matrix Form
Note that for every parameterized curve $(u, \mathbf x(u))$, whether $\mathbf x$ is 1D, 2D, or 3D, we have the general schema 

$$\mathbf x(u) = \mathcal P(u)^T \beta_H \cdot \mathbf h$$

where $\mathcal P(u)$ is the polynomial basis, $\beta_H$ is the Hermite basis matrix, and $\mathbf h$ are the control points values. In this case, 

$$\mathbf h = \begin{bmatrix}\mathbf x_i\\\mathbf x_{i+1}\\\frac{1}{2}(\mathbf x_{i+1} - \mathbf x_{i-1})\\\frac{1}{2}(\mathbf x_{i+2} - \mathbf x_{i})\end{bmatrix} = \begin{bmatrix}
0&1&0&0\\0&0&1&0\\-\frac{1}{2}&0&\frac{1}{2}&0\\0&-\frac{1}{2}&0&\frac{1}{2}\end{bmatrix}\begin{bmatrix}\mathbf x_{i-1}\\\mathbf x_{i}\\\mathbf x_{i+1}\\\mathbf x_{i+2}\end{bmatrix} = M_{CR\rightarrow H} \cdot\mathbf p$$

so that we can write everything in full

$$\mathbf x(u) = \mathcal P(u)^T \beta_H\cdot M_{CR\rightarrow H}\cdot\mathbf p$$

Then, note that $\beta_H\cdot M_{CR\rightarrow H}$ are both pre-defined and we can combine them into one __Catmull-Rom basis matrix__ as

$$\beta_{CR} = \beta_H\cdot M_{CR\rightarrow H} = \begin{bmatrix}0&1&0&0\\-\frac{1}{2}&0&\frac{1}{2}&0\\1&-\frac{5}{2}&2&-\frac{1}{2}\\-\frac{1}{2}&\frac{3}{2}&-\frac{3}{2}&\frac{1}{2}\end{bmatrix}$$

## Bezier Curves
Instead of finding a curve passing through 4 points, now we let $\mathbf x'(u_0) = 3(\mathbf p_1 - \mathbf p_0)$ be the tangent for $\mathbf p_0$ and $\mathbf x'(u_3) = 3(\mathbf p_3 - \mathbf p_2)$ be the tangent of $\mathbf p_3$, and __Bezier curve__ pass through $\mathbf p_0$ and $\mathbf p_3$ with slope specified before. Now, we can use cubic Hermite directly as 

$$\mathbf x(u) = \mathcal P(u)\cdot\beta_H \cdot \mathbf h$$

and similarly we have 

$$\mathbf h = \begin{bmatrix}\mathbf p_0\\\mathbf p_3\\3(\mathbf p_1 - \mathbf p_2)\\3(\mathbf p_3 - \mathbf p_2)\end{bmatrix} = \begin{bmatrix}
1&0&0&0\\1&0&0&1\\-3&3&0&0\\0&0&-3&3\end{bmatrix} \cdot\mathbf p = M_{Z\rightarrow H}\cdot \mathbf p$$

and the __cubic Bezier matrix__ as 

$$\beta_Z = \begin{bmatrix}1&0&0&0\\-3&3&0&0\\3&-6&3&0\\-1&3&-3&1\end{bmatrix}$$

### Convex hull property

__Convex hull property__ means that all points on curve are inside the convex hull formed by control points. A spline has convex hull property if for any $u$, the basis functions are all non-negative and sum to $1$. 

For example, the Bezier basis functions are 

$$\mathcal P(u)\cdot \beta_Z = \begin{bmatrix}
&1 &-3u  &+3u^2  &-u^3\\
&  &+3u  &-6u^2  &+3u^3\\
&  & &+3u^2 &-3u^3\\
&&&&+u^3
\end{bmatrix}^T$$

## Implementing splines

```python
--8<-- "cs284/scripts/splines.py:spline"
```

```plotly
{"file_path": "cs284/assets/splines.json"}
```

### de Casteljau Algorithm

Consider control points $\mathbf p^0_0, \mathbf p^0_1, \mathbf p^0_2, \mathbf p^0_3$ and $u\in[0, 1]$. Define 

$$\mathbf p_i^j = u \mathbf p_i^{j-1} + (1-u)\mathbf p_{i+1}^{j-1}$$

We can recursively compute the equation 3 times until one point left and let $\mathbf x(t) = \mathbf p^3_0$. Then, it is the value for Bezier curve. 

\begin{align*}
\mathbf p_0^3 &= u\mathbf p_0^2 + (1-u)\mathbf p_1^2\\
&= u(u\mathbf p_0^1 + (1-u)\mathbf p_1^1) + (1-u)(u\mathbf p_1^1 + (1-u)\mathbf p_2^1)\\
&= u^2 \mathbf p_0^1 + 2u(1-u)\mathbf p_1^1 + (1-u)^2 \mathbf p_2^1\\
&= u^2(u\mathbf p_0^0 + (1-u)\mathbf p_1^0) + 2u(1-u)(u\mathbf p_1^0 + (1-u)\mathbf p_2^0) + (1-u)^2(u\mathbf p_2^0 + (1-u)\mathbf p_3^0)\\
&= u^3 \mathbf p_0^0 + 3u^2(1-u)\mathbf p_1^0 + 3u(1-u)^2 p_2^0 + u^3 p3^0
\end{align*}

Note that this can be extended to $n$-order polynomials as 

$$B_i^n(u) = {n\choose i}u^i (1-u)^{n-i}$$

### Bezier Surfaces

A surface is defined by some function $\mathbf x(u, v)$. Therefore, we need $4\times 4$ control points and then for each $(u,v)$ we can interpolate per-row Bezier curves in $u$, and then per-column Bezier curve in $v$. 

We can write the surface in matrix form as

$$\mathbf x(u,v) = \mathcal P(u) \cdot \beta_Z \cdot \mathbf P \cdot (\mathcal P(v)\cdot \beta_Z)^T$$

where $P$ is the $4 \times (4 \times 3)$ matrix of all control points. 