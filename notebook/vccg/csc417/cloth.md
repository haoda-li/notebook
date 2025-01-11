# Cloth Simulation and Collision

## Triangular FEM
We often simulate cloth with triangle surfaces instead of a tetrahedron. Therefore, we cannot totally rely on the volumetric approach (while we do introduce "thickness" to adapt the mechanics).

### Finite Elements
Given the reference space in 3D, and the reference position as $\mathbf X = (X, Y, Z)^T \in \mathbb R^3$, just as tetrahedron case, we represent the finite elements at point $\mathbf X$ given by the 3 corners of the triangle $T=(\mathbf X_0, \mathbf X_1, \mathbf X_2)$

$$f(\mathbf X) = \sum_0^2 f(\mathbf X_i) \phi_i(\mathbf X)$$

where $\phi_i$ is the shape function, and as before, we apply the constraint $\phi_0 + \phi_1 + \phi_2 = 1\Rightarrow \phi_0 = 1- \phi_1 - \phi_2$. 

However, note that $\mathbf X$ may not lie exactly on the surface of the triangle. In this case, we want to find the function for the nearest point of $\mathbf X$ on triangle, i.e. $proj_{T}(\mathbf X)$. In this case, we can turn the question of solving the shape function to an optimization problem. i.e. 

\begin{align*} \min \:&\|\sum_0^2 \mathbf X_i \phi_i(\mathbf X) - \mathbf X \|^2_2\\
\text{w.r.t} \:&\{(\phi_0, \phi_1, \phi_2)\mid \phi_0 = 1 - \phi_1 - \phi_2\}
\end{align*}

And the solution to this optimization problem is
\begin{align*}

T & = \begin{pmatrix}\Delta \mathbf X_1 &\Delta \mathbf X_2\end{pmatrix}\\
T^TT\begin{pmatrix}\phi_1 \\\phi_2\end{pmatrix} &= T^T \Delta \mathbf X\\
\phi_0 &= 1 - \phi_1 - \phi_2
\end{align*}

where $\Delta \mathbf X = \mathbf X - \mathbf X_0$


Note that this shape function is the barycentric coordinate for $proj_T(\mathbf X)$, and for points off the triangle

$$\mathbf X = \sum_0^2 \mathbf X_i\phi_i(\mathbf X) + \alpha N = \sum_0^2 \mathbf X_i\phi_i(\mathbf X) + \underset{\alpha}{\Delta \mathbf X^TN}\cdot N$$

where $N$ is the normal of $T$

### Deformation

Note that we introduce $N_T$, while the world space have different normal on the deformed triangle $\mathbf n$, therefore, we can simply have the deformation as 

$$\mathbf x(\mathbf X, t) = \sum_0^x \mathbf x_i \phi_x(\mathbf X) + \Delta\mathbf X^TN\cdot \mathbf n$$

### Generalized Coordinates
As before, let the generalized coordinates and generalized velocity for the triangle as 

$$\mathbf q = \begin{pmatrix}\mathbf x_0\\\mathbf x_1\\\mathbf x_2\end{pmatrix}, \dot{\mathbf q} = \begin{pmatrix}\dot{\mathbf x_0}\\\dot{\mathbf x_1}\\\dot{\mathbf x_2}\end{pmatrix}$$

## Kinetic Energy
Let the cloth domain be $\Omega$, since the cloth is thin, we can just integrate over the triangle surface, and then multiple the thickness to get the volumetric kinetic energy, i.e. 

$$h\frac12 \int_T \rho\|v(\mathbf X)\|_2^2 dT = \frac {1}{2} \dot{\mathbf q}^T\bigg(h\int_T\rho M_0 dT\bigg)\dot{\mathbf q}$$

where 

$$M_0 = \begin{pmatrix}
\phi_0\phi_0I&\phi_0\phi_1I&\phi_0\phi_2I\\
\phi_1\phi_0I&\phi_1\phi_1I&\phi_1\phi_2I\\
\phi_2\phi_0I&\phi_2\phi_1I&\phi_2\phi_2I
\end{pmatrix}\in \mathbb R^{9\times 9}$$

and just as before, we can assemble the total kinetic energy for cloth as 

$$T = \frac12 \dot{\mathbf q}^T \big(\underset{M}{\sum_0^{m-1} E_j^TM_j E_j}\big)\dot{\mathbf q}$$

## Potential Energy
As before, we derive the potential energy from the deformation gradient.

Note that the deformation can be written as 

$$x(\mathbf X) = \mathbf x_0 + 
\begin{pmatrix}\mathbf x_0&\mathbf x_1&\mathbf x_2&\mathbf n\end{pmatrix}
\begin{pmatrix}-\vec 1^T(T^TT)^{-1}T^T\\(T^TT)^{-1}T^T\\\mathbf N^T\end{pmatrix}
\Delta \mathbf X$$

Therefore, the deformation gradient is simply 

$$F =\partial_\mathbf Xx = \begin{pmatrix}\mathbf x_0&\mathbf x_1&\mathbf x_2&\mathbf n\end{pmatrix}
\begin{pmatrix}-\vec 1^T(T^TT)^{-1}T^T\\(T^TT)^{-1}T^T\\\mathbf N^T\end{pmatrix}$$

Note that deformation gradient in this case is constant.

Then, we can apply the same potential energy function as in volumetric approach with constant thickness over the triangle area. 

$$h\int_T \varphi(F(\mathbf X))dT$$

### Energy by Principal Stretches
From volumetric approach, we have the strain represented by Right Cauchy Green Deformation 

$$\Delta \mathbf x^T\Delta \mathbf x - \Delta \mathbf X^T\Delta \mathbf X = \Delta \mathbf X^T(F^TF-I)\Delta \mathbf X$$

Apply an eigendecomposition on the deformation, we have 

$$F^TF =  V\Lambda V^T = (V\Delta \mathbf X)^T (\Lambda -I) V\Delta\mathbf X$$

where $(V\Delta\mathbf X)$ represents the rotation, and $\Lambda$ is the squared singular values of $F$. Therefore, via Principal Stretches, we have 

$$h\int_T \varphi(F(\mathbf X))dT = h\int_T \varphi(\Sigma(F))dT$$

where $\Sigma(F) = (\sigma_0(F), \sigma_1(F), \sigma_2(F))$ is the diagonal of singular value matrix from SVD of $F$.

With this, we can filter out rotations and translations, which are unwanted as they should not change the potential energy.

Then, we want our cloth to go back to undeformed shape when external forces are removed, therefore, we introduce the quadratic energy model __Co-Rotational Linear Elasticity__

$$\varphi(\sigma_0, \sigma_1, \sigma_2) = \mu \sum_0^2 (\sigma_i - 1)^2 + \frac\lambda 2(\sum_0^2 \sigma_i - 3)^2$$

Note that $\mathbf D\varphi(1, 1, 1) = 0\Rightarrow $ minimum at $(1, 1, 1)$, which is the identity transformation, this energy is minimized at undeformed shape. 

Since $F$ is constant across the triangle, now we simply have the potential energy for the triangle be 

$$h\cdot \text{area} \cdot \varphi(F)$$

and then assemble the total potential energy as

$$V = \sum_{0}^{m-1} h\cdot \text{area}_j\cdot \varphi(F_j(E_j\mathbf q))$$

## The Lagrangian
The Lagrangian and EL equation is still the same, since we only change the same of the tetrahedron. 

## Time Integration
Usually we use linearly implicit integrator for cloth due to high membrane stiffness. Therefore, we still need the generalized force and generalized stiffness. 

\begin{align*}
\mathbf f &= -\partial_{\mathbf q}V \\
&= -\sum h\cdot\text{area}_j\frac{\partial}{\partial \mathbf q }\varphi(F_j(E_j\mathbf q))\\
&= -\sum h\cdot\text{area}_j E_j^T \frac{\partial F^T}{\partial\mathbf q_j}\frac{\partial\varphi}{\partial F}\\
\frac{\partial\varphi}{\partial F} &= U\cdot diag(\frac{\partial\varphi}{\partial\sigma_0}, \frac{\partial\varphi}{\partial\sigma_1}, \frac{\partial\varphi}{\partial\sigma_2})V^T
\end{align*}

\begin{align*}
K &= -\frac{\partial^2V}{\partial \mathbf q^2}\\
&=  -\sum h\cdot\text{area}_j\frac{\partial^2}{\partial \mathbf q^2 }\varphi(F_j(E_j\mathbf q))
\end{align*}

Note that the Hessian of $\varphi$ will be extremely messy, therefore, instead of using the full Hessian to do the Newton's method, we can use an approximation of the Hessian and Quasi-Newton Method. In this case, we will have 

$$K = =  -\sum h\cdot\text{area}_j E_j^T
\frac{\partial F}{\partial\mathbf q_j}^T
\frac{\partial^2 \varphi}{\partial F^2}
\frac{\partial F}{\partial\mathbf q_j}E_j$$

Then, the problem is left with $\frac{\partial^2 \varphi}{\partial F^2}$, which involves with the SVD. 

### Derivative of SVD
For a SVD $A = U\Sigma V^T$, we can parameterized by $A$ as $U(A)\Sigma(A)V(A)^T$, hence the derivative w.r.t to entries of $A$ can be written as 

$$\frac{\partial}{\partial A_{ij}}U\Sigma V^T =\frac{\partial U}{\partial A_{ij}} \Sigma V^T U\frac{\partial\Sigma}{\partial A_{ij}}V^T + U\Sigma \frac{\partial V}{\partial A_{ij}}^T$$

Therefore, we can compute $\frac{\partial^2 \varphi}{\partial F^2}$ for each entry as

$$\frac{\partial}{\partial F_{ij}}\frac{\partial \varphi}{\partial F} =\frac{\partial U}{\partial F_{ij}} \Delta\Sigma V^T  + U\cdot diag(\Delta \sigma_{ij})\cdot V^T + U\Delta\Sigma \frac{\partial V}{\partial F_{ij}}^T$$

where 

$$\Delta \Sigma =  diag(\frac{\partial\varphi}{\partial\sigma_0}, \frac{\partial\varphi}{\partial\sigma_1}, \frac{\partial\varphi}{\partial\sigma_2})$$

$$\Delta\sigma_{ij} = \begin{pmatrix}
\frac{\partial^2\varphi}{\partial \sigma_0\sigma_0}&\frac{\partial^2\varphi}{\partial \sigma_0\sigma_1}&\frac{\partial^2\varphi}{\partial \sigma_0\sigma_2}\\
\frac{\partial^2\varphi}{\partial \sigma_1\sigma_0}&\frac{\partial^2\varphi}{\partial \sigma_1\sigma_1}&\frac{\partial^2\varphi}{\partial \sigma_1\sigma_2}\\
\frac{\partial^2\varphi}{\partial \sigma_2\sigma_0}&\frac{\partial^2\varphi}{\partial \sigma_2\sigma_1}&\frac{\partial^2\varphi}{\partial \sigma_2\sigma_2}
\end{pmatrix}
\begin{pmatrix}
\frac{\partial \sigma_0}{\partial F_{ij}}\\
\frac{\partial \sigma_1}{\partial F_{ij}}\\
\frac{\partial \sigma_2}{\partial F_{ij}}
\end{pmatrix}$$

### Vectorized Deformation Gradient
As before, we need to vectorize the deformation gradient

\begin{align*}
F &= \begin{pmatrix}
\partial_X x &\partial_Y x&\partial_Z x\\
\partial_X y &\partial_Y y&\partial_Z y\\
\partial_X z &\partial_Y z&\partial_Z z
\end{pmatrix}\\\Rightarrow 
\vec F_{9\times 1} &=
\begin{pmatrix}
\partial_X x &\partial_Y x&\partial_Z x&
\partial_X y &\partial_Y y&\partial_Z y&
\partial_X z &\partial_Y z&\partial_Z z
\end{pmatrix}^T\\
D&=\begin{pmatrix}\begin{pmatrix}-1&-1\end{pmatrix} \cdot (T^TT)^{-1}T^T\\(T^TT)^{-1}T^T\end{pmatrix}\\
\Rightarrow B_{9\times 9} &=
\begin{pmatrix}
D_{0\cdot}&\vec 0&\vec 0&D_{1\cdot}&\vec0&\vec0&D_{2\cdot}&\vec0&\vec0\\
\vec0&D_{0\cdot}&\vec 0&\vec 0&D_{1\cdot}&\vec0&\vec0&D_{2\cdot}&\vec0\\
\vec0&\vec0&D_{0\cdot}&\vec 0&\vec 0&D_{1\cdot}&\vec0&\vec0&D_{2\cdot}\\
\end{pmatrix}\\
\text{where }D_{i\cdot} &= \begin{pmatrix}D_{i0} &D_{i1}&D_{i2}\end{pmatrix}^T,\vec 0= \begin{pmatrix}0&0&0\end{pmatrix}^T\\
\vec {\mathbf x}_{9\times 1} &= \begin{pmatrix}\mathbf x_0^T&\mathbf x_1^T&\mathbf x_2^T&\mathbf x_3^T\end{pmatrix}^T\\
\vec{\mathbf N} &= \begin{pmatrix}
\mathbf N&\vec 0&\vec 0\\
\vec 0&\mathbf N&\vec 0\\
\vec 0&\vec 0&\mathbf N
\end{pmatrix}\\
\vec F &= B \vec{\mathbf x} + \vec{\mathbf N} \cdot \mathbf n
\end{align*}

Then, the gradient is 

$$\partial_{\vec {\mathbf x}}F = B + \vec{\mathbf N}\cdot \partial_{\vec{\mathbf x}}{\mathbf n}$$

then, note that the normal can be written as 

$$\mathbf n  = \frac{\Delta \mathbf x_1\times \Delta \mathbf x_2}{|\Delta \mathbf x_1\times \Delta \mathbf x_2|}$$

so that the gradient is 

$$
\partial_{\vec{\mathbf x}}{\mathbf n} = \frac{1}{|\Delta \mathbf x_1\times \Delta \mathbf x_2|} (I-\mathbf n\mathbf n^T)([\Delta X_1]_\times\begin{pmatrix}-I&0&I\end{pmatrix} - [\Delta X_2]_\times\begin{pmatrix}-I&I&0\end{pmatrix})$$

where $[\cdot]_\times$ is the skew-symmetric matrix

## Collision with Sphere

Given the query point $\mathbf x$ and a sphere of center and radius $(\mathbf c, r)$ , we need to first detect the collision and then respond. 

For the detection, simply check 

$$\|\mathbf x - \mathbf c\|^2 \leq r^2$$

For the response, we don't want the cloth to move into the sphere, hence we can just filter normal component of velocity. i.e.

$$\mathbf v_{filtered} = \mathbf v + \alpha \mathbf n$$

where the filtering component coefficient $\alpha$ satisfies

$$\mathbf n^T(v+\alpha \mathbf n) \geq 0 \Rightarrow \alpha \geq -\mathbf n^T\mathbf v$$

In addition, we want the velocity change be minimal and if velocity if away from the sphere, then we do nothing. Therefore, we have 

$$\alpha = -\min(0, \mathbf n^T\mathbf v)$$
