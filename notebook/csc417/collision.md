# Rigid body Collisions

## Problem Setup
For two rigid bodies $A, B$. A collision happens when two rigid bodies have contact, i.e. some point on $A$ has $0$ distance to some point on $B$. For the simulation, a collision is divided into two parts, detection and response. 

### Collision Detection
We want to find whether two rigid bodies collide (whether $y_A, y_B$ contact) and often want to have the contact normals $\hat n$. The detection for different types of objects are quite different. For simplicity, we only consider the collision between a moving rigid body $A$ and a static plane $P$. In this case, we can detect on each vertex of the rigid body and have the contact normal be defined as the outward facing normal $\hat n_P$ as contact normal. 

### Collision Response
Note that a rigid body is moved by the rigid transformation $R, p$, so that we cannot update/response based on vertices. 

### Signorini Conditions (3 Rules of of Contact Mechanics)
Given the two points $y_A, y_B$ be the contact point on $A, B$. Consider the contact mechanics, we want our collision resolution to satisfy
 1. No inter-penetration between two objects: $d(y_A, y_B) \geq 0$ where $d$ is the signed distance. 
 2. Contact forces "push" objects apart: $f_{contact} = a\hat n, a\in\mathbb R^{\geq 0}$
 3. Contact forces can only be applied when objects are in contact, or __complementarity__ $d(y_A, y_B)\perp a$

## Equations of Motions

Consider each contact point, record them as $\mathbf y_A, \mathbf y_B$ (since the equations of motion computes on reference space, this can reverse the world space points back to $\bar X_A, \bar X_B$) and have the contact normal $\mathbf n$ towards object $B$. Therefore, we have $\mathbf f_B = a\mathbf n$ and by Newton's Third law, $\mathbf f_A = -a\mathbf n$

Consider the equations of motions, 

\begin{align*}
m\dot{\mathbf p}^{t+1} &= m\dot{\mathbf p}^t + \Delta t \mathbf f_{ext}\\
\mathbf p^{t+1} &= \mathbf p^t + \Delta t\dot{\mathbf p}^t\\
(R\mathcal I R^T)\omega^{t+1} &= (R\mathcal I R^T)\omega^t + \Delta t \omega^t\times ((R\mathcal I R^T)\omega^t)+\Delta t\tau^t_{ext}\\
R^{t+1} &= \exp([\omega]_\times^t\Delta t)R^t
\end{align*}

Note that each collision will give an external force in the world space $\mathbf x$, i.e. updates on $\mathbf f_{ext}, \tau_{ext}$. The external torques and forces are computed (see rigid bodies notes)

$$\begin{pmatrix}\tau_{ext}\\\mathbf f_{ext}\end{pmatrix} = J(\bar X)^T\mathbf f(\bar X)$$

and replace the force with $\mathbf f_A(\bar X_A) = -a\mathbf n, \mathbf f_B(\bar X_A) = a\mathbf n$, we can have 

$$M\dot{\mathbf q}^{t+1} = M \dot{\mathbf q}^t + \Delta t \mathbf f^t + \Delta t \sum_{j=0}^{n_c-1} a_j J(\mathbf y_j)^T \hat {\mathbf n}_j$$

where 
$M = \begin{bmatrix}R\mathcal I R^T & \mathbf 0\\\mathbf 0 &mI\end{bmatrix}, \dot{\mathbf q} = \begin{bmatrix}\omega\\\dot{\mathbf p}\end{bmatrix}$, $\mathbf f$ is the external forces and torques other than the contact forces, and $\hat{\mathbf n} = \begin{cases}-\mathbf n &\text{Object A}\\\mathbf n &\text{Object B}\end{cases}$. 

### Constraints
Then, to find each $a_j$, we constraint it with Signorini conditions, since rule 2 has been satisfied and we know that at time $t$ the conditions must be satisfied, we can add constraints that $\forall j$

\begin{align*}
a_j&\geq 0\\
d(\mathbf y_{jA}^t + \Delta t \dot{\mathbf y}_{jA}^{t+1}, \mathbf y_{jB}^t + \Delta t \dot{\mathbf y}_{jB}^{t+1}) &\geq 0\\
d(\mathbf y_{jA}^t + \Delta t \dot{\mathbf y}_{jA}^{t+1}, \mathbf y_{jB}^t + \Delta t \dot{\mathbf y}_{jB}^{t+1}) &\perp a\\
\end{align*}

Then, the issue is that the signed distance is non-linear. However, note that the contact point can be viewed as infinitesimally small plane with normal $\mathbf n$, so that we can project the closest distance from $\mathbf y_A$ to the plane on $B$ as $-\Delta t \mathbf n^T\dot{\mathbf y}_A^{t+1}$ and similarly for $B$ we have $\Delta t \mathbf n^T\dot{\mathbf y}_A^{t+1}$ 

$$d(\mathbf y_{jA}^t + \Delta t \dot{\mathbf y}_{jA}^{t+1}, \mathbf y_{jB}^t + \Delta t \dot{\mathbf y}_{jB}^{t+1}) = \Delta t\mathbf n^T( \dot{\mathbf y}_{jB}^{t+1} -  \dot{\mathbf y}_{jA}^{t+1})$$

and we can take away that $\Delta t$ since it won't impact the constraint. 



## Multiple Collisions on Multiple Rigid Bodies

For a scene of multiple rigid bodies and multiple contacts, record the object ID $A, B$, the contact point $\mathbf y$ and contact normal $\mathbf n$ (always points toward $B$), 

Note that for this collision, it will have impact on object $A, B$ as 

\begin{align*}
M_A\dot{\mathbf q}^{t+1}_A &= M_A \dot{\mathbf q}^t_A + \Delta t \mathbf f^t_A + \Delta t \sum_{j\neq i}^{n_{Ac}-1} a_j J(\mathbf y_j)^T \hat {\mathbf n}_j - \Delta t a_iJ(\mathbf y_i)^T{\mathbf n}_i\\
M_B\dot{\mathbf q}^{t+1}_B &= M_B \dot{\mathbf q}^t_B + \Delta t \mathbf f^t_B + \Delta t \sum_{j\neq i}^{n_{Bc}-1} a_j J(\mathbf y_j)^T \hat {\mathbf n}_j + \Delta t a_iJ(\mathbf y_i)^T{\mathbf n}_i
\end{align*}

Then, we simplify the notation by taking $\mathbf f_i^A =\sum_{j\neq i}^{n_{Ac}-1} a_j J(\mathbf y_j)^T \hat {\mathbf n}_j$ so that the equations above becomes

\begin{align*}
\dot{\mathbf q}^{t+1}_A &= \dot{\mathbf q}^t_A + \Delta t M_A^{-1}\mathbf f^t_A + \Delta t M_A^{-1}\mathbf f_i^A - \Delta t a_iJ(\mathbf y_i)^T{\mathbf n}_i\\
\dot{\mathbf q}^{t+1}_A &= \dot{\mathbf q}_A^{t+1*} + \Delta t M_A^{-1}\mathbf f_i^A - \Delta t a_iJ(\mathbf y_i)^T{\mathbf n}_i\\
\dot{\mathbf q}^{t+1}_B &= \dot{\mathbf q}_B^{t+1*} + \Delta t M_B^{-1}\mathbf f_i^B + \Delta t a_iJ(\mathbf y_i)^T{\mathbf n}_i
\end{align*}

where $\dot{\mathbf q}_A^{t+1*}$ is the unconstrained velocity as computed from rigid bodies mechanics, without any collisions. 

Then, since $\dot{\mathbf y}_A$ is the world space velocity,  $\dot{\mathbf y}_{Ai} = J_A(\mathbf y_i)\dot{\mathbf q}_A^{t+1}$
and the constraints becomes 

\begin{align*}
a_j&\geq 0\\
\mathbf n_i^T(J_B(\mathbf y_i)\dot{\mathbf q}_B^{t+1} - J_A(\mathbf y_i)\dot{\mathbf q}_A^{t+1}) &\geq 0\\
\mathbf n_i^T(J_B(\mathbf y_i)\dot{\mathbf q}_B^{t+1} - J_A(\mathbf y_i)\dot{\mathbf q}_A^{t+1}) &\perp a_i
\end{align*}

We can then substitute $\dot{\mathbf q}_B^{t+1}, \dot{\mathbf q}_A^{t+1}$ with the equations above. 

Write $\mathbf g_i^A = -J(\mathbf y_i)^T\mathbf n_i, \mathbf g_i^B = J(\mathbf y_i)^T\mathbf n_i$, the substitution yields 

\begin{align*}
\delta_i &= \Delta t\big((\mathbf g_i^B)^T M_B^{-1} \mathbf g_i^B + (\mathbf g_i^A)^T M_A^{-1} \mathbf g_i^A\big)\\
\gamma_i &= (\mathbf g_i^B)^T(\dot{\mathbf q}^{t+1*}_B+ \Delta t M_B^{-1} \mathbf f_i^B) + (\mathbf g_i^A)^T(\dot{\mathbf q}^{t+1*}_A+ \Delta t M_A^{-1} \mathbf f_i^A)\\
\delta_i a_i + \gamma_i &= \mathbf n_i^T(J_B(\mathbf y_i)\dot{\mathbf q}_B^{t+1} - J_A(\mathbf y_i)\dot{\mathbf q}_A^{t+1})
\end{align*}

and finally the problem becomes

\begin{align*}
\forall i \in \{0,...,n_c-1\}\\
a_i\geq 0\\
\delta_i a_i + \gamma_i \geq 0\\
\delta_i a_i + \gamma_i \perp a_i
\end{align*}

which yields $a_i = \max(-\gamma_i/\delta_i, 0)$.

### Projected Gauss-Seidel

Note that each $\gamma_i$ involves $a_j$ for $j\neq i$, hence solving all equations in parallel is hard. Instead, we use an iterative algorithm. 

``` python title="Projected Gauss-Seidel"
qdot = compute() # qdot for each rigid bodies without collisions

k = 0 # iteration counter
a = [0, 0, ..., 0] # array of length n for each a_i
constraints = False
while k < MAX_ITER or not constraints:
    k += 1
    for i in range(n):
        delta, gamma = equations above
        a[i] = max(-gamma / delta, 0)
    constraints = check_constraints(a)
    
qdot += dt * sum([a[j] * Jacobian(y[j]) @ n_hat[j] for j in range(n)])
q = compute() # from new qdot
```

## Static Objects
Sometimes we have static objects in the scene, for example the static ground which should not move. In this case, we can have its mass being infinitely large. Hence, its inverse mass is 0. Then, starting with 0 velocity, the object cannot move and contribute to any part of the collision response. 
