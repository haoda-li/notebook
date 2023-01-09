# Surface Reconstruction

[Link to paper](http://hhoppe.com/poissonrecon.pdf)

Note that the notes is a simplified version of the paper's implementation. We use fixed unit grid node instead of adaptive grid node. Also, we use the trilinear interpolation instead of more complex weighted methods. 

## Problem Setup
Given a set of scanned point samples $P$ on the surface of an object and the estimated point normals $N$, we want to find an explicit continuous surface representation, i.e. a triangle mesh. 

### Voxel-based Implicit Surface
However, if we directly convert the point cloud to a mesh by connecting points together, it's difficult to ensure the certain topological postconditions, i.e. a closed manifold with a small number of holes. Instead we will first convert the point cloud sampling representation into an implicit surface representation. Let the unknown surface be the level set of some function $g:\mathbb R^3\rightarrow\mathbb R$, i.e. 

$$\partial S = \{x\in\mathbb R^3\mid g(x) = c\}$$

Then, we discretize an implicit function by defining a regular 3D grid of voxels containing at least the bounding box of $S$. At each node in the grid $x_{i,j,k}$ we store the value of the implicit function $g(x_{i,j,k}) and then we can get the value everywhere by trilinear interpolation over the grid cell. 

#### <a href="https://en.wikipedia.org/wiki/Marching_cubes">Matching Cubes Algorithm</a>
We want the implicit surface representation so that we can contoured into a triangle mesh via Marching Cubes Algorithm. 


### Characteristic Function of Solids
Assume that our set of point $P$ lies on the surface $\partial S$. This solid object $S$ must have some non-trivial volume that we can calculate as the integral of unit density over the solid 

$$\int_S dA = \int_{\mathbb R^3}\mathcal x_S(x)dA = \int_{\mathbb R^3}\mathbb I(x\in S)dA$$

From the <a href="http://hhoppe.com/poissonrecon.pdf">Poisson Surface Reconstruction [Kazhdan et al. 2006] </a>, the gradient of a infinitesimally mollified characteristic function 

 - points in the direction of the normal near the surface $\partial S$
 - is zero everywhere else
 
Therefore, using points $P$ and normals $N$, we can optimize an implicit function $g$ over a regular grid, so that $\nabla g$ meets the two properties above, and $g$ will be an approximation of the mollified characteristic function. 

## Poisson Surface Reconstruction
Starting from some unrealistic assumptions (note that these assumptions are not to be made but to make the description more intuitive)

 - We know each of $\nabla g(x_{i,j,k})$
 - All of input points lies perfectly at grid nodes: $\forall p\in P. \exists x_{i,j,k} = p$

With these assumptions, we simply have 

$$\nabla g(x_{i,j,k}):\mathbb R^3\rightarrow\mathbb R^3:= v_{i,j,k} = \mathbb I(x_{i,j,k}\mid \exists p_l = x_{i,j,k}) \:n_l$$

So that $g$ is defined via a simple set of linear equations

Since our system is over determined, this can be turned into an optimization problem. 

$$\min_g \sum_i\sum_j\sum_k \frac12\|g(x_{i,j,k}) - v_{i,j,k}\|^2$$

where $g$ is a vector of unknown grid nodes values, $g_{i,j,k} = g(x_{i,j,k})$

With the assumptions, we can compute approximations of the x,y,z components of $\nabla g$ via a matrix multiplication of a "gradient matrix" $G$ and vector unknown grid value $g$, so that the optimization problem becomes

$$\min_g \frac12\|Gg - v\|^2 = \min_g\frac12 g^TG^TGg - g^TG^Tv + v^Tv$$

This is a quadratic function, so that we can set the gradient being 0

$$\frac{\partial}{\partial g} \frac12 g^TG^TGg - g^TG^Tv + v^Tv = G^TGg - G^Tv = 0$$

### Gradient estimated from regular grid
Since we have a grid, it's straightforward to estimate the gradient as a finite difference. For example, 
$\frac{\partial g}{\partial x}(x_{i-1/2, j, k}) = \frac1h(g_{i,j,k} - g_{i-1,j,k})$.  
With this observation, we can construct a partial difference matrix $D^x \in \mathbb R^{(n_x -1)n_yn_z\times n_xn_yn_z}$, where each row $D^x_{i-1/2,j,k}$ computes the partial derivative at $x_{i-1/2,j,k}$, i.e. 

$$D^x_{i-1/2,j,k}(l) = \begin{cases}-1 &l=i-1\\1 &l=1\\0&\text{otherwise}\end{cases}$$

We can do similar things on $D^y, D^z$ and obtain the desired 

$$G = \begin{pmatrix}D^x\\D^y\\D^z\end{pmatrix} \in \mathbb R^{(n_x-1)n_yn_z + n_x(n_y-1)n_z + n_xn_y(n_z-1)\times n_xn_yn_z}$$

Of course, when we implement this, we cannot have indexing as $0.5$, so we can shift the indexing down by $0.5$, and do the same for the vector $v$.

### Estimate v
Note that our normals $N$ does not lie on the grid node. In order to obtain $v$ on the ideal grid, we can distribute each $\vec n$ to its 8 neighboring grid nodes via trilinear interpolation weights, for example

\begin{align*}
n_x =\:& w_{ \frac12 ,0,0}( \mathbf{x}_{1,\frac14 ,\frac12 } ) \  v^x_{ \frac12 ,0,0} +  \\
  &w_{\frac32 ,0,0}( \mathbf{x}_{1,\frac14 ,\frac12 } ) \  v^x_{1\frac12 ,0,0} +  \\
  &\vdots \\
  &w_{\frac32 ,1,1}( \mathbf{x}_{1,\frac14 ,\frac12 } )\ v^x_{1\frac12 ,1,1}.
\end{align*}

we can do this for each input normal and assmeble a parse matrix $W^x\in n\times (n_x-1)n_yn_z$
Then, we can have $v^x = (W^x)^TN^x$. Doing similar for $v^y, v^z$ and stack them together, we can obtain $v$

### Poisson Equation
Consider some discrete energy minimization problem 

$$E(g) = \int_{\Omega}\|\nabla g - V\|^2 dA$$

the Poisson's equation states that the minimizers on $\Omega$ will satisfy

$$\nabla\cdot \nabla g = \nabla\cdot v$$
