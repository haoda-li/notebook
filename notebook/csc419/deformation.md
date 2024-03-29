# Handle-based Deformation

## Problem Setup
The user repositions a sparse set of points  and the goal is to propagate the transformations at these "handles" to the rest of the shape. 

Given the point rest position $\tilde x \in \mathbb R^3$, we will write its unknown deformed position as $x$ and the point's displacement vector $d := x - \tilde x$. 

The problem can be thought of two ways 
 - as a scattered data interpolation, where the handles are the sparse samples and we want to interpolate over the unknown displacement field
 - as a shape optimization problem, where we try to define a new shape that retains the details of the old shape but fulfill the handle constraints. 
 
### Properties to Consider In Deformation

#### Continuity
The deformation should be continuous, i.e. the shape will not tear, crack or change topological features. i.e. the face matrix $F = \tilde F$ will not change, only $V$ should be determined from $\tilde V$. 

#### Generic Distortion Minimization
A rest surface $\tilde S$ immersed in $\mathbb R^3$ can be described as a mapping $\tilde x$ from some 2D parametric domain $\Omega$. i.e. $\tilde x: \Omega \subseteq \mathbb R^2 \rightarrow \mathbb R^3$, similarly define the deformed surface as $x:\Omega \rightarrow \mathbb R^3$ and displacement vector field as $d(u, v) = x(u, v) - \tilde x(u, v)$. 

Consider distortion minimization and the handle's position as energy minimization with constraints. Suppose we have some energy functional $E(x)$ that measures the amount of distortion. A natural choice of distortion measurement is by intergrating local distortion over all points, i.e. we have the problem
\begin{align*}
\text{minimize} \quad &E(x) = \int_\Omega \|e(x)\|^2 dA\\
\text{subject to} \quad &\{x:\Omega \rightarrow \mathbb R^3\mid\forall i = \{1,...,k\}.  x(u_i, v_i) = g_i\}
\end{align*}
where $e$ is the measurement of local distortion, the function is upon our choice. 

## Gradient based Energy
If we assume that the deformation is small then we can measure the distortion as the magnitude of gradient of the displacement field, i.e. if the displacement field has large variations or sudden changes then it induces a lot of distortion. 

$$\int_\Omega \|e(x)\|^2 dA = \int_\Omega \|\mathbf Dd\|_F^2 dA $$

where $\mathbf Dd$ is the Jacobian of $d$.  

The discretized version over our triangle mesh gives 

$$tr(D^TLD)\text{ w.r.t } D_{handles} = g_{handles} - \tilde V_{handles}$$

However this methods is not smooth at constraints and the influence of handles dies off too quickly. By minimizing the Dirichlet energy, each coordinate of "displacement field" is a harmonic function. Intuitively (however abstractly) we can think of each function as diffusing the user's constraints as if they were heat values. As such, each function diffuses quickly to an average, slowly varying value over most of the domain. As a displacement field a constant value for each coordinate function would mean a translation: most of the shape is simply translated.

Note that Jacobian is a linear operator, i.e. 

$$\min_d\int \|\mathbf D d\|_F^2 dA = \min_x \int \| \mathbf D x - \mathbf D\tilde x\|_F^2 dA$$

If we think of the gradient of the position function  (with respect to the underlying parameterization) as a local geometric feature descriptor then this energy can be re-understood as measuring the difference in this feature before and after the deformation. This is very sensible as we are trying to measure distortion. We would expect that a low-distortion deformation would correspond with a small change to local features.


## Laplacian based Energy

If we model distortion as the change in a local feature descriptor, then a natural local and relative descriptor would be one that compared the position of some point on the shape to the average of its local neighborhood. Consider the Laplace operator as taking exactly the difference of a function value at a point and the average over an infinitesimal region 

$$\Delta f (x) = \big[\lim_{|B_\delta(x)|\rightarrow 0} B_\delta(x)^{-1}\int_B f(z)dz\big] - f(x)$$

When applied to the embedding function $x$ the Laplace operator computes the differences in position between a point and its local neighborhood. The vector points in the normal direction and its magnitude corresponds inversely with how flat the surface is locally. 

We can use calculus of variations apply Green's identity twice to show that minimizers of the squared Laplacian energy are _bi-harmonic_ functions ($\Delta^2 d = 0$). This will allow us to ensure continuity of first derivatives across constrained values at handles. 

### Discretized Approximation
(For more details of the discretization and symbols, go to smoothing)

We can make sure our discrete Laplacian operator $L$. This matrix computes the locally integrated Laplacian of a given function specified by per=vertex values $\mathbf f$. We can approximate the point-wise Laplacian by the local integral average of the Laplaicna $M^{-1}L\mathbf f$. Integrating this over the mesh we have the complete approximation

$$\int_\Omega \|\Delta d\|^2 dA \approx tr(D^TLM^TMM^{-1}LD) = tr(D^T\underset{Q}{L^TM^{-1}L}D)$$

where $M$ is the mass-matrix for the given mesh and $Q = L^TM^{-1}L$ can be thought of as the bi-Laplacian matrix.

## Precomputation
Without loss of generality, assume that the rows of the unknown displacement $D$ have been sorted so that displacements corresponding to handle vertices are in the bottom part, i.e. $D = \begin{pmatrix}D_u\\D_{handle}\end{pmatrix}$

Since the displacement at handles are, we can separate and eliminate it from optimization

\begin{align*}
\min_{D_u}tr(D^T Q D) &= \min_{D_u} tr\big(\begin{bmatrix}D^T_u&D_h^T\end{bmatrix}
\begin{bmatrix}Q_{u,u} & Q_{u,h}\\
Q_{h,u} &Q_{h,h}\end{bmatrix}
\begin{bmatrix}D_u\\D_{h}\end{bmatrix}\big)\\
&= \min_{D_u} tr\big(D^TQ_{u,u} D_u + 2D^T_u Q_{u,h}D_h\big)\\
&= \min_{D_u} tr(E(D_u))
\end{align*}

Then, set $\partial_{D_u}E = 0$ for the solution of the quadratic optimization

\begin{align*}
\partial_{D_u} E &= 2Q_{u,u} D_u + 2Q_{u,h} D_h\\
\Rightarrow D_u &= Q^{-1}_{u,u} Q_{u,h} D_h
\end{align*}

Since $Q_{u,u}$ does not change, we can prefactorize it so that applying its inverse is fast. 

### Problem

Biharmonic displacements works well for small deformations and deformations that do not imply a large rotation. The Laplacian of the position function $\Delta x$ as a feature descriptor is not rotation invariant. This problem is also true for all linear differential features. This means that if the user transforms all the handle locations by a rigid transformation $T$ these energies will measure zero. We would like global rotation invariant, but we should also like this property to apply locally so that parts of the shape can easily rotate. 

## As Rigid As Possible

Sure each handle $i$ are perfectly transformed by a rigid transformation $x_i = R \tilde x_i + t$. Then we could repair the gradient based energy above by 

$$\int_\Omega \|\mathbf D x - \mathbf D(R\tilde x + t)\|^2 dA = \int_\Omega \|\mathbf D x - R\mathbf D(\tilde x)\|^2dA$$

Then, we can unify and fit the best rotation $R$, i.e. 

$$\arg\min_{x, R} \int_\Omega \|\mathbf D x - R\mathbf D(\tilde x)\|^2dA$$

Optimizing this energy will ensure global rotation invariance. The ensure local rotation invariance, we can replace $R\in SO(3)$ with a spatially varying function $R:\Omega \rightarrow SO(3)$ that outputs the a rotation for any point on the shape. 

For embedded solid shapes, we can take the rest shape given by $\tilde x$ as the parameterization $\Omega$, so that $\mathbf D \tilde x = I$, thus we can writethe arap energy as the squared difference between deformation gradient and closest rotation. 

\begin{align*}
\mathbf D x - R \mathbf D \tilde x &= \mathbf (D x + I - I) - RI\\
&= (I + \mathbf D x - \mathbf D\tilde x) - R\\
&= (I + \mathbf D d) - R\\
&= F - R\\
\int_\Omega \|\mathbf D x - R\mathbf D(\tilde x)\|^2dA &= \int_\Omega \|F-R\|^2dA
\end{align*}

### Discrete Energy
For a triangle mesh with displacing vertices, the gradient of the embedding function is constant inside each triangle. In this way we can write the gradient energy as a double sum of half-edges $ij$ of all faces $f$ in the mesh

$$\int_\Omega \|\mathbf D x - \mathbf D\tilde x \|^2 dA = \frac12 \sum_{f\in F}\sum_{ij\in f}c_{ij}\|(v_i-v_j)- (\tilde v_i-\tilde v_j)\|^2$$

where $c_{ij} = \cot(\angle_{ij})$ is cotangent of the angle opposite half-edge $ij$. 

To inject localized best fit rotations, assign a unknown rotation matrix $R_k$ fora each vertex $k$ for the mesh and accounts for a third of the energy integrated over incident triangles. 

$$\int_\Omega \|\mathbf D x - \mathbf D(R\tilde x + t)\|^2 dA = \frac16\sum_{k=1}^n\sum_{ij\in F(k)} c_{ij} \| (v_i - v_j) - R_k(\tilde v_i - \tilde v_j)\|^2$$

### Optimization
Since we have $R_k$ and $V$ to be optimized, the simplest method is do alternating optimization, i.e. 

 - __local step__: find $R_k$'s first with fixed $V$, 
 - __Global step__: then use updated $R_k$'s to optimize $V$. 

The "local" step since each $R_k$ only affects the local energy and won't interact with the other rotations. The "global" step since each vertex positions in $V$ depends on each other, and requires a global solve. 

Note that the energy above can be separated into two parts

\begin{align*}
&\frac 16 \sum_{k=1}^n \sum_{ij\in F(k)}c_{ij} (v_i - v_j)^T (v_i - v_j)&\text{quadratic in }V\\
+&\frac 16 \sum_{k=1}^n \sum_{ij\in F(k)}c_{ij} (v_i - v_j)^T R_k(\tilde v_i - \tilde v_j)&\text{linear in }V\\
\end{align*}

We can stack the $R_k$ into $R_{3n\times 3}$ so that the energy is in matrix form 

$$tr(V^TLV) + tr(V^TKR)$$

$L_{\|V\|\times \|V\|}$ is hte cotangent discrete Laplacian matrix  
$K_{\|V\|\times 3\|V\|}$ is the sparse matrix containing cotangents multiplied against differences across edges in the rest mesh, i.e. 

``` python
# K matrix is |V| * 3|V|, indexing starts with 0
for f in faces:
    for (i, j) in permutations([0, 1, 2], 2):
        for k in [0, 1, 2]:
            for b in [0, 1, 2]:
                # cot[i, j] is the cotangent of angle opposite to edge i,j 
                K[f[i], 3 * f[k] + b] += cot[i, j] * (v_tilde[i] - v_tilde[j])[b]
                K[f[j], 3 * f[k] + b] -= cot[i, j] * (v_tilde[i] - v_tilde[j])[b]
```

#### Local Step
Minimizing $R$ corresponds to minimize 

$$tr\big(\underset{C^T}{(V^TK)}R\big)$$

Let $C = (V^TK)^T \in \mathbb R^{3n\times 3}$, $C_k \in \mathbb R^{3\times 3}$. Then, $C$ is the stacked weighted covariance matrix and each $C_k$  is the region covered by corresponding rotation $R_k$. To minimize, we simply want $R_k$ to be the closest rotation matrix solved via SVD, as seen in registration. 

#### Global Step
Minimizing $V$ corresponds to minimize

$$tr(V^TLV) + tr\big(V^T\underset{B}{(KR)}\big)$$

Adding the handle constraints to the corresponding rows of $V$, this is minimized by setting all partial derivatives w.r.t. the unknowns in $V$ equal to 0. 

### Pre-factorize
Note that the global step is the same regardless of the current rotations or current handle position, we can prefactorize it. The matrix $K$ also does not depend on the rotations, current positions or handle positions; so that we can prebuild $K$
