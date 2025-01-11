# Rigid Body Simulation


## Defining the Transformation
Reviewing cloth simulation and deformable objects, we simulate a deformation from reference $X$ to world space $x$ as 

$$\Delta x\approx \underset{F}{\frac{\partial x}{\partial X}}\Delta X$$

so that we can have the strain 

\begin{align*}
\Delta x^T\Delta x - \Delta X^T\Delta X &= \Delta X F^TF\Delta X - \Delta X^T\Delta X\\
&= \Delta X^T(F^TF-I)\Delta X
\end{align*}

where $F^TF-I$ is the Green Lagrange Strain. 

For a rigid object, the object cannot be deformed so that $F^TF-I = 0\Rightarrow F^TF=I\Rightarrow F\in O(3)$, i.e. $F$ is an orthogonal matrix.  
For common 3D transformations, rotation matrices and reflection matrices are both orthogonal. However, reflection will have the object's topology passing through itself, which is not rigid.

Therefore, we limit $F\in SO(3)$, i.e. rigid bodies can only rotate, and $SO(3)$ is called the special orthogonal Group, 

$$\forall R\in SO(3). R^T = R^{-1}\land \det(R) > 0$$

In addition, rigid bodies can translate. Therefore, we have the rigid transformation from reference to world space as 

$$\mathbf x(\mathbf X, t) = R(t)\mathbf X + \mathbf p(t)$$

$\mathbf x, \mathbf X \in \mathbb R^3$, $R\in SO(3)$ is the rotation and $\mathbf p\in \mathbb R^3$ is the translation (often written in $\mathbf t$ but we don't want this to be confused with time $t$). 

## Generalized Coordinates
Consider the mapping 

$$\mathbf x(\mathbf X, t) = R(t)\mathbf X + \mathbf p(t)$$

clearly, only $R, \mathbf p$ is about time, so that our generalized coordinates is 

$$\mathbf q = \{R, \mathbf p\}$$

Note that $\mathbf q$ is a set instead of a unified stacked vector. 

## Generalized Velocity
Consider the time derivative of the transformation on a single point

\begin{align*}
\mathbf v(\mathbf X,t ) &= \dot{\mathbf x}(\mathbf X, t) \\
&= \frac{d}{dt}R(t)\mathbf X + \frac{d}{dt}\mathbf p(t)\\
&= \dot{R(t)}\mathbf X + \dot{\mathbf p(t)}
\end{align*}

$\dot{\mathbf p(t)}$ is called the __linear velocity__ since it's just the velocity of the origin of the object moves,  
$\dot{R(t)}$ is the __time derivative of rotation matrix__, and it's more complex, we can represent it with 

$$\dot{R(t)} = R{[X]_{\times}}^TR^T\omega$$

where $[\cdot]_\times$ is the cross product matrix, 

$$X\in\mathbb R^3. [X]_{\times} = \begin{bmatrix}0&-X_z& X_y\\X_z&0&-X_z\\-X_y&X_x&0\end{bmatrix}, a\times b = [a]_\times b$$

$\omega\in\mathbb R^3$ is the __angular velocity__, $\|\omega\|$ (magnitude) encodes the speed or rotation and angle encodes the axis of rotation. 

\begin{align*}
\mathbf v(\mathbf X,t ) &= \dot{R(t)}\mathbf X + \dot{\mathbf p(t)}\\
&= R{[X]_{\times}}^TR^T\omega + \dot{\mathbf p(t)}\\
&= R \begin{bmatrix}{[X]_{\times}}^T&I\end{bmatrix}\begin{bmatrix}R^T&0\\0&R^T\end{bmatrix}\begin{bmatrix}\omega\\\dot{\mathbf p}\end{bmatrix}\\
&= R \begin{bmatrix}{[X]_{\times}}^T&I\end{bmatrix}A\dot{\mathbf q}
\end{align*}

Since $R, \mathbf X$ is constant about $t$, we can define our generalized velocity $\dot{\mathbf q}\in\mathbb R^6 = [\omega, \dot{\mathbf p}]^T$. and we define $A = \begin{bmatrix}R^T&0\\0&R^T\end{bmatrix}$ to simplify the expression.

## Kinetic Energy
As usual, we can find kinetic energy as

\begin{align*}
\frac12\int_\Omega\rho\|\mathbf v(\mathbf X )\|_2^2 d\Omega &= \frac12\int_\Omega \rho \mathbf v^T\mathbf v d\Omega\\
&= \frac12\dot{\mathbf q}^TA^T \big(\rho\int_\Omega 
\begin{bmatrix}[\mathbf X]_\times {[\mathbf X]_\times}^T &[\mathbf X]_\times \\ [\mathbf X]_\times&I\end{bmatrix}
d\Omega\big)A\dot{\mathbf q}\\
&= \frac12\dot{\mathbf q}^TM\dot{\mathbf q}
\end{align*}

where $M$ is the mass matrix, $M = A^T \big(M_0\big)A$ and $M_0 \in \mathbb R^{6\times 6}$ is a constant matrix integrating over the whole volume. 

## Center of Mass
The center of mass is defined as the weighted average of points of the volume,

$$\mathbf C = \frac1m \int_\Omega\rho\mathbf X d\Omega, m = \int_\Omega \rho d\Omega$$

With the center of Mass, we can transfer our reference space to the center-of-mass coordinates system

$$\bar{\mathbf X} = \mathbf X - \mathbf C$$

This is convenient for the computation of $M_0$, 

$$M_0 =\rho\int_\Omega \begin{bmatrix}[\mathbf X]_\times {[\mathbf X]_\times}^T &[\mathbf X]_\times \\ [\mathbf X]_\times&I\end{bmatrix}
d\Omega  = \rho\int_\Omega 
\begin{bmatrix}[\bar{\mathbf X}]_\times {[\bar{\mathbf X}]_\times}^T &[\bar{\mathbf X}]_\times \\ [\bar{\mathbf X}]_\times&I\end{bmatrix}
d\Omega$$

Consider the off-diagonal entries, 

\begin{align*}
\int_\Omega [\bar{\mathbf X}]_\times d\Omega &= \int_\Omega [\mathbf X -\mathbf C]_\times d\Omega\\
&= \int_\Omega [\mathbf X]_\times d\Omega - \int_\Omega [\mathbf C]_\times d\Omega\\
&= \int_\Omega [\mathbf X]_\times d\Omega - \int_\Omega 1d\Omega \cdot [\mathbf C]_\times\\
&= 0
\end{align*}

So that we only need to compute the diagonal


### Surface Integral via Divergence Theorem
Note that $M_0$ is an integral over the volume, naturally, we can use tetrahedral mesh so that we can do this integral. However, a more efficient method will use only the surface mesh. 

Divergence Theorem states that 

$$\int_V \nabla \mathbf f (\mathbf X) dV = \int_A \mathbf f(\mathbf X) \cdot \mathbf ndA$$

so that we can turn a volume integral to a surface integral 
Therefore, consider the entries of $M_0$

\begin{align*}
M_0 &= \rho \int_\Omega 
\begin{bmatrix}[\bar{\mathbf X}]_\times {[\bar{\mathbf X}]_\times}^T &0\\0&I\end{bmatrix}d\Omega \\
 [\bar{\mathbf X}]_\times {[\bar{\mathbf X}]_\times}^T &= 
\begin{bmatrix}
\bar{X_y}^2 + \bar{X_z}^2 & -\bar{X_x}\bar{X_y}&-\bar{X_x}\bar{X_z} \\
-\bar{X_x}\bar{X_y} &\bar{X_x}^2 + \bar{X_z}^2&-\bar{X_y}\bar{X_z}\\
-\bar{X_x}\bar{X_z}&-\bar{X_y}\bar{X_z}&\bar{X_x}^2 + \bar{X_y}^2\end{bmatrix}
\end{align*}

$\mathcal I$ is called the inertia matrix and we can integrate $M_0$ over each entry. 

Since each entry is simple enough, we can pick some integral of it and then apply divergence theorem. 
For example

\begin{align*}
\int_\Omega \bar{X_y}^2 + \bar{X_z}^2d\Omega &= \int_T\frac13\begin{pmatrix}0\\\bar{X_y}^3\\\bar{X_z}^3\end{pmatrix}\cdot \mathbf N dT \\
\int_\Omega \bar{X_y}\bar{X_z}d\Omega &= \int_T\begin{pmatrix}\bar{X_x}\bar{X_y}\bar{X_z}\\0\\0\end{pmatrix}\cdot \mathbf N dT \\
\int_\Omega 1d\Omega &= \int_T\frac13\begin{pmatrix}\bar{X_x}\\\bar{X_y}\\\bar{X_z}\end{pmatrix}\cdot \mathbf N dT 
\end{align*}

Then, because we are using triangle meshes, we can integrate over $T$ through the barycentric coordinates via

$$\bar{\mathbf X} = \bar{\mathbf X}_0 \phi_0 + \bar{\mathbf X}_1 \phi_1+\bar{\mathbf X}_2 \phi_2$$

Then, define $h: (\phi_0, \phi_1, \phi_2)\rightarrow \mathbb R$ and integrate as 

$$2\text{Area}\int_0^1\int_0^{1-\phi}h(1-\phi_1-\phi_2, \phi_1, \phi_2)d\phi_2d\phi_1$$

Therefore, we can obtain 

$$M_0 =   
\begin{bmatrix}\rho \int_\Omega[\bar{\mathbf X}]_\times {[\bar{\mathbf X}]_\times}^Td\Omega &0\\0&mI\end{bmatrix} = \begin{bmatrix}\mathcal I&0\\0&mI\end{bmatrix}$$

where $\mathcal I$ is the <a href="https://en.wikipedia.org/wiki/Inertia">inertia</a> matrix

## Final Form of Kinetic Energy
Put every thing together 

\begin{align*}
T &= \frac12 \dot{\mathbf q}^TA^T M_0 A\dot{\mathbf q}\\
&= \frac 12\dot{\mathbf q}^T
\begin{bmatrix}R^T&0\\0&R^T\end{bmatrix}^T
\begin{bmatrix}\mathcal I&0\\0&mI\end{bmatrix}
\begin{bmatrix}R^T&0\\0&R^T\end{bmatrix}\dot{\mathbf q} \\
&= \frac 12\dot{\mathbf q}^T
\begin{bmatrix}R\mathcal I R^T&0\\0&mI\end{bmatrix}\dot{\mathbf q}
\end{align*}

## Potential Energy
Since the object is rigid and cannot deform, 

$$V = 0$$

## Newton-Euler Equations (The Lagrangian)
Since $V = 0$, we have $L = T$ so that the Euler-Lagrange Equation gives __Newton-Euler Equations__ 

1. __Conservation of Angular Momentum__
   
    $$(R\mathcal I R^T)\dot\omega = \omega \times ((R\mathcal IR^T)\omega) + \tau_{ext}$$

    Where $\dot\omega$ is the angular acceleration, $\tau_{ext}$ is the external torque and $\omega \times ((R\mathcal IR^T)\omega)$ is the quadratic velocity vector
2. __Conservation of Linear Momentum__ 
   
    $$mI\ddot{\mathbf p} = \mathbf f_{ext}$$
    
    where $\ddot{\mathbf p}$ is the acceleration and $\mathbf f_{ext}$ is the external force.

### External Torques and Forces
For a force applied to some position $\mathbf x$ as $\mathbf f(\mathbf x)$, this will result in a rotation as well as a translation. Note that 

$$\mathbf v(\bar{\mathbf X}, t) = R 
\begin{bmatrix}{[X]_{\times}}^T&I\end{bmatrix}
\begin{bmatrix}R^T&0\\0&R^T\end{bmatrix}
\begin{bmatrix}\omega\\\dot{\mathbf p}\end{bmatrix}$$

Let $J \in\mathbb R^{3\times 6} = R \begin{bmatrix}{[X]_{\times}}^T&I\end{bmatrix}\begin{bmatrix}R^T&0\\0&R^T\end{bmatrix}$ be the rigid body __Jacobian matrix__, which converts the generalized velocity to the velocity on some point

$$\mathbf v(\bar{\mathbf X}, t) = J \dot{\mathbf q}$$

Therefore, given $\mathbf x$ in the world space, we first inverse it back to reference space w.r.t. the center-of-mass

$$\bar{\mathbf X} = R^T(\mathbf x - p)-\mathbf C$$

and then we can compute $f(\bar{\mathbf X})$ and $J(\bar{\mathbf X})$ so that 

$$\begin{pmatrix}\tau_{ext}\\\mathbf f_{ext}\end{pmatrix} = J(\bar{\mathbf X})^T\mathbf f(\bar{\mathbf X})$$

## Time Integration
The NE Equations are 2 second order ODEs, and they are not inter-related. Therefore, we can derive update equations independently. 

### Update on Translation
The update for linear momentum is simple. Note that this is just the translation of the center of mass, we can think this as the update of the point mass, the rule is simply 

\begin{align*}
m\dot{\mathbf p}^{t+1} &= m\dot{\mathbf p}^t + \Delta t \mathbf f_{ext}\\
\mathbf p^{t+1} &= \mathbf p^t + \Delta t\dot{\mathbf p}^t
\end{align*}

### Update on Rotation
For the angular velocity update, we can simply using the Forward Euler, i.e. approximate 

$$\dot\omega = \Delta t^{-1}(\omega^{t+1}-\omega^t)$$ 

so that the update is 

$$(R\mathcal I R^T)\omega^{t+1} = (R\mathcal I R^T)\omega^t + \Delta t \omega^t\times ((R\mathcal I R^T)\omega^t)+\Delta t\tau^t_{ext}$$

However, when we update the rotation, we cannot simply use the $x^{t+1} = x^t + \Delta t v^T$, since this will destroy the orthogonality.   
Alternatively, we can view this as solving an __initial value problem__. 

$$d_t\mathbf x = \mathbf v^t, \mathbf x(t_0) = \mathbf x^t$$

integrating yields that 

\begin{align*}
d_t\mathbf x &= \mathbf v^t\\
\int_{t0}^{t1}d\mathbf x &= \int_{t0}^{t1}\mathbf v^t dt\\
\mathbf x(t) &= \mathbf v^t \Delta t + \mathbf x^t
\end{align*}

With this, we can view $\mathbf v^t$ as the velocity of rotation around $\mathbf p$ so that 

\begin{align*}
\mathbf v^t &= \omega^t \times (R\bar{\mathbf X} - \mathbf p -\mathbf p)\\
\mathbf y&:= R\bar{\mathbf X}\\
\mathbf v^t &= d_t\mathbf y = \omega^t\times \mathbf y\\
\mathbf y(t_0) &= \mathbf y^t
\mathbf y(t_1) = \exp([\omega]_\times^t\Delta t)\mathbf y(t_0)\\
R^{t+1} &= \exp([\omega]_\times^t\Delta t)R^t
\end{align*}
