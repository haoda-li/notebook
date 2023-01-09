# Finite Element Method

## Motivation
A mass spring system is just a bunch of springs and nodes, which leaves very much "empty" space in the space. For some complex animation simulations, we need to find a better representation to "fill in" the space. We are interested in the continuum mechanics (continuum: the hypothesis that the material is uniformly the same across all points). 

## Volume by Tetrahedral
A tetrahedral is a 3D object by connecting 4 vertices $x_0(t), x_1(t), x_2(t), x_3(t)$, and we can have generalized coordinates $\mathbf q=(x_0, x_1, x_2, x_3)^T$ and $\dot{\mathbf q} = (\dot{x_0}, \dot{x_1}, \dot{x_2}, \dot{x_3})^T = (v_0,v_1,v_2,v_3)^T$. 

## Finite Elements
Let $\mathbf{X_0},...,\mathbf{X_3}$ be the fixed position of the 4 vertices of a tetrahedral $T$, $f$ be some unknown function with known $f(\mathbf{X_i}), i=0,...,3$. We want to find $f$ for every point in $T$. We can have

$$f(\mathbf{X}) = \sum_{i=0}^3 f(\mathbf{X_i})\phi_i(\mathbf{X})$$

where $\phi_i$ is the weight function, or shape function, that associate with each vertices so that $f(\mathbf{X})$ is a weighted sum of values from the 4 vertices. 

Consider some wanted properties of the equation above, let $f = id$

$$\mathbf{X} = \sum^3_{i=0} \mathbf{X_i}\phi_i(\mathbf{X})$$

Note that $\mathbf{X}\in\mathbb R^3$, so that we currently have $3$ equations and $4$ unknowns $\phi_0,...,\phi_3$. However, note that we want this act as a weighted average, so we can add one more constraint $\phi_0 + ... + \phi_3 = 1$. This gives us $4$ equations, and we can simply replace $\phi_0$ with $1-\phi_1-\phi_2-\phi_3$, resulting in the final system

$$\begin{pmatrix}\Delta X\\\Delta Y\\\Delta Z\end{pmatrix} = 
\begin{pmatrix}\Delta X_1&\Delta X_2&\Delta X_3\\
\Delta Y_1&\Delta Y_2&\Delta Y_3\\
\Delta Z_1&\Delta Z_2&\Delta Z_3
\end{pmatrix} 
\begin{pmatrix}\phi_1(X)\\\phi_2(X)\\\phi_3(X)\end{pmatrix}$$

where $\Delta X = X - X_0$. We can think of shotting 3 rays from $X_0$ and use this to construct the barycentric coordinates. Finally, we have 

$$\begin{pmatrix}\phi_1(X)\\\phi_2(X)\\\phi_3(X)\end{pmatrix} = T^{-1}(\mathbf{X}-\mathbf{X_0}), \phi_0 = 1-\phi_1-\phi_2-\phi_3$$

## Deformation
Let $\mathbf{X_0}, ..., \mathbf{X_3}$ be tetrahedral in the reference (undeformed) space and $x_0(t),...,x_3(t)$ be the tetrahedral in the world (deformed) space. Therefore, with the $\phi$'s found above, we have the deformed point everywhere in the tetrahedral as 

$$x(\mathbf X) = \sum_{i=0}^3 x_i(t) \phi_i(\mathbf X) = \underset{N(\mathbf X)}{\begin{pmatrix}\phi_0I&\phi_1I&\phi_2I&\phi_3I\end{pmatrix}}\underset{q(t)}{\begin{pmatrix}x_0\\x_1\\x_2\\x_3\end{pmatrix}}$$


## Kinetic Energy

### Per tetrahedron
The kinetic energy of a tetrahedron is simply the integral of all points

$$\frac12 \int_{T}\rho\|v(\mathbf X)\|_2^2 dT = \frac12 \int_{T}\rho v^Tv dT$$

where $\rho$ is the density of the material.  

Then, since the shape function is irrelavent to $\mathbf q$, 

$$v(X) = \dot x(X) = N(X)\dot{\mathbf q}$$

Then, the integral becomes 

$$\frac12 \int_{T}\rho  \dot{\mathbf q}^TN(X)^T N(X)\dot{\mathbf q} dT = \frac 12\dot{\mathbf q}^T \bigg(\int_{T}\rho  N(X)^T N(X) dT \bigg)\dot{\mathbf q}$$

We can all this integral inside $M_0$, i.e. the mass matrix. We can expand the mass matrix as 

$$\int_T\rho \begin{bmatrix}\phi_0\phi_0I &\cdots &\phi_0\phi_3I\\\vdots&\ddots&\vdots\\\phi_3\phi_0I&\cdots&\phi_3\phi_3I\end{bmatrix}dT$$

and we can evaluate each term separately from the barycentric coordinates, for each element 

$$\rho \int_T \phi_r(\mathbf X)\phi_x(\mathbf X)dT I = 6\rho \cdot vol\cdot\int_0^1\int_0^{1-\phi_1}\int_0^{1-\phi_1-\phi_2}(\phi_r\phi_s)d\phi_3\phi_2\phi_1$$

### The Full Object
For per tetrahedron kinetic energy we have 

$$T_j = \frac12 \dot{\mathbf q_j}^TM_j\dot{\mathbf q}_j$$

And we have the generalized coordinates and velocity of the object as the stacking of all the vertices positions and velocities, i.e. $\mathbf q = (x_0,...,x_n)^T$, so that we can use the selection matrix to get each $\mathbf{q}_j$ from $\mathbf q$, and the total kinetic energy is

$$T =  \sum_0^{j-1}\frac12 \dot{\mathbf q}^TE_j^TM_jE_j\dot{\mathbf q} = \frac12 \dot{\mathbf q}^T\big(\sum_0^{j-1}E_j^TM_jE_j\big)\dot{\mathbf q} = \frac12 \dot{\mathbf q}^T M\dot{\mathbf q}$$

## Potential Energy
### Per pair points
Note that we have the reference space positions and world space, and the corresponding positions of each point. Arbitrarily pick $\mathbf X_0, \mathbf X_1$ from the reference space, let $\Delta \mathbf X = \mathbf X_1 - \mathbf X_0$. Then, its corresponding points and vector are $x(\mathbf X_0)$ and $x(\mathbf X_1)$, so that 

\begin{align*}\Delta \mathbf x &= x(\mathbf X_1) - x(\mathbf X_0) \\
&= x(\mathbf X_0 + \Delta \mathbf X) - x(\mathbf X_0)\\
&\approx x(\mathbf X_0) + \frac{\partial x}{\partial \mathbf X}\Delta \mathbf X - x(\mathbf X_0)&\text{Taylor expansion}\\
&= \frac{\partial x}{\partial \mathbf X}\Delta \mathbf X\\
&= F\Delta \mathbf X &\text{call deformation gradient }F
\end{align*}

The strain between the points is represented by $l^2 - l^2_0$,

\begin{align*}
l^2 - l^2_0 &= \Delta x^T\Delta x  - \Delta \mathbf X^T\Delta \mathbf X \\
&= \Delta \mathbf X^TF^TF\Delta \mathbf X - \Delta \mathbf X^T\Delta \mathbf X\\
&= \Delta \mathbf X^T(F^TF - I)\Delta \mathbf X
\end{align*}

We call $F^TF$ the __Right Cauchy Green Deformation__, and $(F^TF - I)$ __Green Lagrange Strain__. 

### Per tetrahedron
Like $\psi$ be a strain energy density function, which maps the strain to the potential energy. Then, we can integrate over the points as 

$$\int_T \psi(F(\mathbf X))dT$$

Then, let's consider $F(\mathbf X)$, note that 

\begin{align*}
x(\mathbf X) &= N(\mathbf X)\mathbf q(t)\\
&= \mathbf x_0 + \begin{pmatrix}\mathbf x_0&\mathbf x_1&\mathbf x_2&\mathbf x_3\end{pmatrix}
\begin{pmatrix}\begin{pmatrix}-1&-1&-1\end{pmatrix} \cdot T^{-1}\\T{-1}\end{pmatrix}
(\mathbf X - \mathbf X_0)\\
F = \frac{\partial x}{\partial \mathbf X} &= \begin{pmatrix}\mathbf x_0&\mathbf x_1&\mathbf x_2&\mathbf x_3\end{pmatrix}
\begin{pmatrix}\begin{pmatrix}-1&-1&-1\end{pmatrix} \cdot T^{-1}\\T^{-1}\end{pmatrix}
\end{align*}

Note that $F$ is constant, so that the integral simply evaluate as 

$$\int_T \psi(F(\mathbf X))dT = vol \cdot \psi(F_0)$$

### The Full Object
Then, simply summing over all tetrahedrons with the usage of selection matrix

$$V = \sum_{j=0}^{m-1}vol_j \cdot \psi(F_j(E_j\mathbf q))$$

## The Lagrangian
Then, plug in $L = T - V$ and apply Euler-Lagrange Equation $\frac{d}{dt}\frac{\partial L}{\partial \dot{\mathbf q}} = - \frac{\partial V}{\partial \mathbf q}$, we finally arrives 

$$M\ddot{\mathbf q} = -\frac{\partial V}{\partial \mathbf q}$$

Then consider $ -\frac{\partial V}{\partial \mathbf q} = -\sum_{j=0}^{m-1}vol_j \cdot \frac{\partial}{\partial \mathbf q}\psi(F_j(E_j\mathbf q))$, this differentiation is tricky due to $F$ being a matrix. We can flatten $F$ to a vectorized deformation gradient. For example, a row-wise flatten will have

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
D&=\begin{pmatrix}\begin{pmatrix}-1&-1&-1\end{pmatrix} \cdot T^{-1}\\T{-1}\end{pmatrix}\\
\Rightarrow B_{9\times 12} &=
\begin{pmatrix}
D_{0\cdot}&\vec 0&\vec 0&D_{1\cdot}&\vec0&\vec0&D_{2\cdot}&\vec0&\vec0&D_{3\cdot}&\vec0&\vec0\\
\vec0&D_{0\cdot}&\vec 0&\vec 0&D_{1\cdot}&\vec0&\vec0&D_{2\cdot}&\vec0&\vec0&D_{3\cdot}&\vec0\\
\vec0&\vec0&D_{0\cdot}&\vec 0&\vec 0&D_{1\cdot}&\vec0&\vec0&D_{2\cdot}&\vec0&\vec0&D_{3\cdot}\\
\end{pmatrix}\\
\text{where }D_{i\cdot} &= \begin{pmatrix}D_{i0} &D_{i1}&D_{i2}\end{pmatrix}^T,\vec 0= \begin{pmatrix}0&0&0\end{pmatrix}^T\\
\vec {\mathbf x}_{12\times 1} &= \begin{pmatrix}\mathbf x_0^T&\mathbf x_1^T&\mathbf x_2^T&\mathbf x_3^T\end{pmatrix}^T\\
\vec F &= B \vec{\mathbf x}
\end{align*}

Then, we can put the new dirivatives back, we have 

\begin{align*} 
-\frac{\partial V}{\partial \mathbf q} &=  -\sum_{j=0}^{m-1}vol_j \cdot \frac{\partial}{\partial \mathbf q}\psi(F_j(E_j\mathbf q))\\
&= -\sum_{j=0}^{m-1}vol_j \cdot \frac{\partial}{\partial \mathbf q}\psi(B_jE_j\mathbf q))\\
&= -\sum_{j=0}^{m-1}vol_j \cdot E_j^TB_j^T\frac{\partial \psi(F_j)}{\partial F}\\
\mathbf f_j&= -vol_j \cdot B_j^T\frac{\partial \psi(F_j)}{\partial F}\\
\mathbf f &= \sum_0^{m-1}E_j^T\mathbf f_j
\end{align*}

## Time Integration Using Backward Euler
Although we can still use linear implicit time integration, it's quite unstable in this case. Instead we will use backward Euler

$$M\dot{\mathbf q}^{t+1} = M\dot{\mathbf q}^t + \Delta t \mathbf f(\mathbf q^{t+1})$$

$$\mathbf q^{t+1} = \mathbf q^t + \Delta \dot{\mathbf q}^{t+1}$$

Which is solving the equation 

$$M\dot{\mathbf q}^{t+1} - M\dot{\mathbf q}^t - \Delta t \mathbf f(\mathbf q^t + \Delta \dot{\mathbf q}^{t+1}) = 0$$

However, this equation is non-linear and we need to do non-linear optimization. Define

$$E(\mathbf v) = \frac 12 (\mathbf v - \dot{\mathbf q}^t)^TM(\mathbf v - \mathbf q^t) + V(\mathbf q^t + \Delta t \mathbf v)$$

Note that $\partial_{\mathbf v} E = M\dot{\mathbf q}^{t+1} - M\dot{\mathbf q}^t - \Delta t \mathbf f(\mathbf q^t + \Delta \dot{\mathbf q}^{t+1})$, so that when $E$ is at minimum, we can have $\partial E = 0$. 

### Newton's Method
(More derivations in APM462 or CSC336 notes)

Newton's Method is an iterative algorithm as follows

```python
def netwon_method(v0):
    v = v0
    while grad(E(v)).norm() < tolerance:
        solve Hessian(E(v)) d = - grad(E(v))
        a = [choose a]
        v = v + a * d
    return v
```
with

$$grad = \frac{\partial E}{\partial \mathbf v} = M(\mathbf v - \dot{\mathbf q}^t) + \Delta t \frac{\partial V}{\partial \mathbf q}\mid_{\mathbf q^t + \Delta t \mathbf v}$$

$$Hessian = \frac{\partial^2 E}{\partial \mathbf v^2} = M + \Delta t^2 \frac{\partial^2 V}{\partial \mathbf q^2}\mid_{\mathbf q^t + \Delta t \mathbf v}$$

### Line Search
Note the `[choose a]` part in Newton's Method, how do we know a $\alpha$ is appropriate, which means not to small for a update and not to large that gets out of the decreasing gradient. Therefore, we can set a target value as $E(v) + c d^T g$, by MVT, this will be larger than the optimum we want but smaller than $E(v)$. Then, if we can find some update that's smaller than this, then we made sufficient progress. Therefore, the algorithm is

``` python
def line_search(v, d, g):
    a = a_max #an initial guess
    while E(v + ad) > E(v) + c * d.T.dot(g) and a >= tolerance:
        a = p * a #choose some p < 1, so that a is reduced
    return a
```

## Skinning
Note that tetrahedral mesh for the simulation is much more computation expensive. We cannot use a very fine mesh for the simulation. Instead, we will use a "skinning" triangle mesh. 

We start with the precondition that each vertex of the skinning mesh will be contained in the simulation mesh. Then, note that for each vertex in the skinning mesh, it is within some tetrahedron, which we can map it to the 4 vertices with barycentric coordinates. For example, for triangle $X_A, X_B, X_C$ in the reference space, its position in the reformed space is 

$$\begin{pmatrix}x(X_A)\\x(X_B)\\x(X_C)\end{pmatrix} = 
\begin{pmatrix}
\phi_0(X_A)I &\phi_1(X_A)I &\phi_2(X_A)I &\phi_3(X_A)I \\
\phi_0(X_B)I &\phi_1(X_B)I &\phi_2(X_B)I &\phi_3(X_B)I \\
\phi_0(X_C)I &\phi_1(X_C)I &\phi_2(X_C)I &\phi_3(X_C)I 
\end{pmatrix}\begin{pmatrix}x_0\\x_1\\x_2\\x_3\end{pmatrix}
$$

With the generalized coordinates $q$, we can then construct the skinning weights $W$ or dimension $\|V_{\text{skin}} \|\times \|V_{\text{sim}}|$ so that $\mathbf x_{\text{surface}} = W \mathbf q$
