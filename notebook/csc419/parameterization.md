# Parameterization

## Problem Setup

Given a surface embedded or immersed in $\mathbb R^3$, we want to find its flatten map in $\mathbb R^2$. With this process, the 2D flattened mesh can be interpreted as a parameterization of the 3D surface. 

More specifically, given a list of vertices $V\in\mathbb R^{n\times 3}$, we can to find some $U\in \mathbb R^{n\times 2}$, i.t. assign the $uv$ coordinates from $xyz$. 

Note that in general, because we reduce the dimension. Some parts of the surface will have to be stretched and some will be squished. Surfaces with topological handles or without a boundary must be cut. 

## Mass Spring Methods

Consider the connection between parameterization and graph drawing in infoviz. If we treat our mesh a vertices and edges, i.e. a graph, then the problem can be viewed as graph drawing. Then, we can optimize over node locations with the energy

$$\arg\min_U\sum_{(i,j) \in E} \|u_i - u_j\|^2$$

where $(i, j)$ is an edge. Note that this is equivalent tot the potential energy of a mass-spring system. 

Of course, the trivial solution will have every vertex map to $(0, 0)$, so we need to add some fixed point constraints, However, if we just choose fixed points arbitrarily, then in general we will have __fold over__, i.t. edges cross each other, overlapping of mesh triangles, and inverted normal direction. 

### Weighted Potential Energy
<a href="https://en.wikipedia.org/wiki/Tutte_embedding">By Tutte's Embedding</a>, we do have a way to avoid fold over. If the boundary of a disk-topology mesh is fixed to a convex polygon, then minimizing the energy above will give injective flattening. However, this method tends to have all edges with equal length. Combined with the boundary constraints, the flattened mesh will have a grid-like shape (smoothly varying edge lengths, near equilateral triangles) regardless the triangle shapes and sizes on the surface mesh. To improve, we introduce a varying spring stiffness $w_{ij}$ for each edge, i.e. 

$$\arg\min_U\sum_{(i,j) \in E} w_{ij}\|u_i - u_j\|^2$$

For example, let $w_{ij} = \|v_i - v_j\|^{-1}$ so that shorter edges on the 3D mesh gets more energy. This will help the length distortion problem, while we still have the area distortion and angle distortion problem. 

Let's further consider the energy, first, vectorize the energy as 

$$\arg\min_U \frac 12 tr(U^TLU), L = \begin{cases}w_{ij} &ij\in E\\-\sum_{l\neq i} L_{il} &i=j\\0&\text{otherwise}\end{cases}$$

Note that $L$ is the discrete Laplacians, if $w_{ij}=1$, then $L$ is the uniform Laplacian, if $w_{ij}$ is based on edge lengths, then $L$ corresponds to a physical static equilibrium problem for a linear spring system. 

## Dirichlet Energy
If we consider the problem as a discrete representation over a 2D surface and Wobbliness distortions in the parameterization correspond to high variation in $u,v$ function over the surface, then consider the energy minimization of the variation, 

$$\min_{u,v} \int_S \|\nabla u\|^2 + \|\nabla v\|^2 dA$$

We may discretize this problem immediately using piecewise linear functions spanned by  and  values at vertices. This corresponds to using the cotangent Laplacian as $L$ in the discrete minimization problem above.

## Least Squares Conformal Mappings

### Area Distortion
We'd like that regions on $S$ have a proportionally similarly sized region under the $u,v$ mapping. On an infinitesimal scale, a small change in $x,y$ on $S$ should incur an equally small change in $u,v$, i.e. 

$$\det\begin{bmatrix}\partial_xu &\partial_yu\\\partial_xv &\partial_yv\end{bmatrix} = 1$$

### Angle Distortion
We'd like that local regions on $S$ are parameterized without shearing. This ensures that two orthogonal directions on the surface $S$ correspond to two orthogonal directions on the parametric plane $\mathbb R^2$. We can capture this by requiring that a small change in $x,y$ on $S$ corresponds to equal magnitude, small changes in $u,v$ in perpendicular directions

$$\nabla u = \nabla v^{\perp}\Rightarrow \begin{bmatrix}\partial_xu \\\partial_yu\end{bmatrix} = \begin{bmatrix}\partial_yv \\-\partial_xv\end{bmatrix}$$

This equality is linear in $u,v$ so that we can immediately build a quadratic energy that minimizes deviation from satisfying the equation over $S$, i.e. 

$$\arg\min_{u,v}\frac12\int_S\|\nabla u - \nabla v^{\perp}\|^2 dA$$

expand it, we have 

$$\int_S \frac 12 \|\nabla u\|^2 + \frac12\|\nabla v\|^2 - \nabla u\cdot \nabla v^{\perp} dA$$

the fist part is the Dirichlet energies, and then consider the second part

\begin{align*}
\int_S\nabla u\cdot \nabla v^{\perp} dA &= \int_S \begin{pmatrix}\partial_xu&\partial_yu\\\partial_xv&\partial_yv\end{pmatrix}dA \\
&=\int_{\begin{pmatrix}u(S)\\v(S)\end{pmatrix}}dA\\
&= \frac 12 \oint_{\partial \mathbf u(S)}\mathbf u(s)\cdot \mathbf n(s)ds &\text{Stoke's theorem}
\end{align*}

$\mathbf n$ is the unit normal pointing in the outward direction along the boundary of the image of the mapping. So that we are integrating over the boundary of the image of mapping from $S$. 

### Discretization
Discretize $u,v$ using piecewise-linear functions, then

\begin{align*}
\frac 12 \oint_{\partial \mathbf u(S)}\mathbf u(s)\cdot \mathbf n(s)ds &= \frac12 \sum_{(i,j)\in\partial S} \int_0^1 (\mathbf u_i + t(\mathbf u_j -\mathbf u_i))\cdot \frac{(\mathbf u_j -\mathbf u_i)^{\perp}}{\|\mathbf u_j - \mathbf u_i\|}\frac{ds}{dt}dt\\
&= \frac12\sum_{(i,j)\in\partial S}\int_0^1 \mathbf u_i(\mathbf u_j - \mathbf u_i)^{\perp}dt\\
&= \frac12\sum_{(i,j)\in\partial S}\det(\begin{bmatrix} \mathbf u_i & \mathbf u_j\end{bmatrix})
\end{align*}

i.e. summing over all boundary edges the determinant of matrix with vertex positions as columns. This quadratic form can be written as $U^T\tilde AU$ where $U\in\mathbb R^{2n}$ is the vectorized $u, v$ coordinates and $\tilde A\in\mathbb R^{2n\times 2n}$ is the selection matrix involving only values for vertices on the boundary of $S$.

Note that $\tilde A$ is not symmetric and may cause numerical issues, replace it with $A = \frac12 (\tilde A + \tilde A^T)$ so that $A$ is symmetric, and $x^T\tilde A x = x^TAx$ since we only need the quadratic energy.

Putting all things together, we  have the discrete least square conformal mapping minimization problem as 

$$\arg\min_{U\in\mathbb R^{2n}} U^T\bigg(\begin{pmatrix}L&0\\0&L\end{pmatrix} - A\bigg)U$$

Let $Q = \bigg(\begin{pmatrix}L&0\\0&L\end{pmatrix} - A\bigg)$, since $L, A$ are fixed from $V$, we can precompute $Q$

### Free Boundary
Note that this problem still have the trivial $0$ solution, we can fix two vertices, while this will introduce bias and sometimes we might choose two vertices that the energy would rather like to place near each other and so placing them at arbitrary positions will introduce unnecessary distortion. 

Instead we'd like natural boundary conditions, i.e. minimize the given energy in the absence of explicit boundary conditions. 

Since we don't want zero norm in our solution $U$, we can enforce this by adding constraint 

$$\int_S\|u\|^2 dA = 1 \Rightarrow U^T\begin{pmatrix}M&0\\0&M\end{pmatrix}U = 1$$

where $M$ is the mass matrix for a piecewise linear triangle mesh so that $B = \begin{pmatrix}M&0\\0&M\end{pmatrix}$ is the square constraint matrix. 

### Canonical Rotation
The least squares conformal mapping energy is invariant to translation and rotation. The eigen decomposition process described above will naturally take care of "picking" a canonical translation by pulling the solution  toward the origin. The rotation it returns, however, will be arbitrary.
