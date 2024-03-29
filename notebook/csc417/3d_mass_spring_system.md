# 3D Mass Spring System

## Two Particles and One String
Let the particles be $x_1(t), x_2(t)\in\mathbb R^3$ and define the strings to have a rest length $l_0\in\mathbb R^+$, then we define the generalized coordinates and generalized velocity being 

$$\mathbf q = \begin{pmatrix}\mathbf x_0\\ \mathbf x_1\end{pmatrix}, \dot{\mathbf q} = \begin{pmatrix}\mathbf v_0\\ \mathbf v_1\end{pmatrix}$$

### Kinetic Energy
Then, the kinetic energy for each particle in the system is $\frac 12 m_i\|v_i\|_2^2 = \frac12 v_i^T\underset{M_i}{(m_iI)}v_i$ and the total kinetic energy is the sum of all the kinetic energy, i.e.

$$T = \sum_{i=0}^1 \frac 12 \mathbf v_i^TM_i v_i = \frac{1}{2}\dot{\mathbf q}^TM\dot{\mathbf q}, M = \begin{pmatrix}M_0&0\\0&M_1\end{pmatrix}$$

### Potential Energy
The properties we want

 - Spring should go back to original length when all external forces are removed
 - Rigid motion should not change the energy'
 - Energy should depend only on particle positions

Therefore, we define __Strain__ being $l - l_0$ which is the difference of the deformed length from the rest length, 

$$l = \sqrt{(x_1 - x_0)^T(x_1 - x_0)} = \sqrt{\big[\begin{pmatrix}-I &I\end{pmatrix}\begin{pmatrix}\mathbf x_0 \\\mathbf x_1\end{pmatrix}\big]^T\big[\underset{B}{\begin{pmatrix}-I &I\end{pmatrix}}\underset{\mathbf q}{\begin{pmatrix}\mathbf x_0 \\\mathbf x_1\end{pmatrix}}\big]} = \sqrt{\mathbf q^T B^TB\mathbf q}$$

then the potential energy is 

$$V = \frac12 k(l-l_0)^2 = \frac12 k(\sqrt{\mathbf q^TB^TB\mathbf q} - l_0)^2$$

### Euler-Lagrange Equation
Consider the Lagrangian $L = T - V$, note that $T$ is only related to $\dot{\mathbf q}$, hence

$$\frac{\partial L}{\partial \mathbf q} = \frac{\partial T}{\partial \mathbf q} - \frac{\partial V}{\partial \mathbf q} = -\frac{\partial V}{\partial \mathbf q}$$

and the Euler-Lagrange Equation is simplified a bit as 

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{\mathbf q}} = - \frac{\partial V}{\partial \mathbf q}$$

Further more, we have

\begin{align*}
\frac{d}{dt}\frac{\partial L}{\partial \dot{\mathbf q}} &= \frac{d}{dt}\frac{\partial}{\partial \dot{\mathbf q}}(\frac12 \dot{\mathbf q}^TM\dot{\mathbf q})\\ 
&=\frac{d}{dt}M\dot{\mathbf q}\\
&= M\ddot{\mathbf q}
\end{align*}

So that the Euler-Lagrange equation is derived to be 

$$M\ddot{\mathbf q} = - \frac{\partial V}{\partial \mathbf q}$$

## N Particles
The generalized coordinates and generalized velocity will be 

$$\mathbf q = \begin{pmatrix}\mathbf x_0\\\vdots\\ \mathbf x_n\end{pmatrix}, \dot{\mathbf q} = \begin{pmatrix}\mathbf v_0\\\vdots\\ \mathbf v_n\end{pmatrix}$$

### Kinetic Energy

$$T = \sum_{i=0}^1 \frac 12 \mathbf v_i^TM_i v_i = \frac{1}{2}\dot{\mathbf q}^TM\dot{\mathbf q}, M = \begin{pmatrix}M_0&\cdots&0\\\vdots&\ddots&\vdots\\0&\cdots&M_n\end{pmatrix}\in\mathbb R^{3n\times 3n}$$

### Potential Energy
Define the potential energy for each spring $j$ being $V_j:\mathbb R^{6}\rightarrow \mathbb R$ so that 

$$V = \sum_{j=0}^{m-1}V_j(\mathbf x_A, \mathbf x_B)$$

To vectorize this operation, consider a selection $3\times 3n$ matrix 

$$S_{i} = \begin{pmatrix}\mathbf 0_{3\times 3}\cdots I_{3\times3}\cdots &\mathbf 0\end{pmatrix}, S_i\mathbf q = \mathbf x_i$$

therefore, we can have 

$$\mathbf q_j = \begin{pmatrix}x_A\\x_B\end{pmatrix} = \begin{pmatrix}S_A\\S_B\end{pmatrix}\mathbf q = E_j \mathbf q$$

So that 

$$V = \sum_{j=0}^{m-1}V_j(E_j q)$$

### Euler-Lagrange Equation
Note that the derivation in EL equation still holds, 

$$M\ddot{\mathbf q} = - \frac{\partial V}{\partial \mathbf q}$$

Then, consider 

\begin{align*}
-\frac{\partial V}{\partial \mathbf q} &= - \frac{\partial }{\partial \mathbf q}\sum_{j=0}^{m-1}V_j(E_j q)\\
&= - \sum_{j=0}^{m-1}\frac{\partial }{\partial \mathbf q}V_j(E_j q)\\
&= - \sum_{j=0}^{m-1} E_j^T  \frac{\partial V_j}{\partial \mathbf q_j}(\mathbf q_j)\\
&= \sum_{j=0}^{m-1} E_j^T  \mathbf f_j(\mathbf q_j)
\end{align*}

## Linearly-Implicit Time Integration
From backward Euler, we have 

$$M\dot{\mathbf q}^{t+1} = M\dot{\mathbf q}^t + \Delta t \mathbf f(\mathbf q^{t+1})$$

$$\mathbf q^{t+1} = \mathbf q^t + \Delta t \dot{\mathbf q}^{t+1}$$

We substitute $\mathbf f(\mathbf q^{t+1})$ with our position update so that 

$$M\dot{\mathbf q}^{t+1} = M\dot{\mathbf q}^t + \Delta t \mathbf f(\mathbf q^t + \Delta t \dot{\mathbf q}^{t+1})$$

Then we use Taylor first order approximation

$$M\dot{\mathbf q}^{t+1} = M\dot{\mathbf q}^t + \Delta t \mathbf f(\mathbf q^t) + \Delta t^2 \frac{\partial \mathbf f}{\partial \mathbf q}\dot{\mathbf q}^{t+1}$$

Rearrange equations, we have 

$$(M - \Delta t^2 K)\dot{\mathbf q}^{t+1} = M\dot{\mathbf q}^t + \Delta t  \mathbf f(\mathbf q^t)$$

where $K = \frac{\partial \mathbf f}{\partial \mathbf q}$ is the stiffness matrix, since $\mathbf f = -\frac{\partial}{\partial \mathbf q}\sum^{m-1} V_j(E_j\mathbf q)$

\begin{align*}
K &= \frac{\partial \mathbf f}{\partial \mathbf q}\\
 &= -\frac{\partial^2}{\partial \mathbf q^2}\sum^{m-1} V_j(E_j\mathbf q)\\
 &= -\sum^{m-1} \frac{\partial^2}{\partial \mathbf q^2} V_j(E_j\mathbf q)\\
 &= \sum^{m-1} -E_j^T \frac{\partial^2V_j}{\partial \mathbf q^2} E_j^T\\
 &= \sum_{j=0}^{m-1} E_j^TK_jE_j&K_j = - \frac{\partial^2  V_j}{\partial\mathbf q^2}
\end{align*}

## Fixed Boundary Conditions
We want some $x_i$ being fixed to fixed coordinate $b_i$, 
let $\hat{\mathbf q} = P\mathbf q$ being all the non fixed points, where $P$ is the selection matrix that selects non fixed points, therefore $P^T\hat q + \mathbf b$, where $\mathbf b$ have all the fixed coordinates, then we can have 

$$\mathbf q = P^T\hat q + \mathbf b, \dot{\mathbf q} = P^T \dot{\hat{\mathbf q}}$$

So that the updates is 

$$P(M - \Delta t^2 K)P^T\dot{\hat{\mathbf q}}^{t+1} = PM\dot{\mathbf q}^t + \Delta t  P\mathbf f(\mathbf q^t)$$

$$\mathbf q^{t+1} = \mathbf q^t + \Delta t P^T \dot{\hat{\mathbf {q}^{t+1}}}$$
