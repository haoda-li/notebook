# Physics based Animation

## Mass spring system

Given a set of mass points (vertices) and springs (edges). For each spring connecting two mass points $(\mathbf a, \mathbf b)$, the stretch  force from $\mathbf a$ to $\mathbf b$ as $\mathbf f_{a\rightarrow b} = k_s(\mathbf b - \mathbf a)$ where $k_s$ is the stiffness of the spring. The reverse force $\mathbf f_{b\rightarrow a} = -\mathbf f_{a\rightarrow b} = k_s(\mathbf a - \mathbf b)$.

For non-zero length spring, let $l_0$ be its length as rest pose, we can expand the equation to 

### Potential force

$$\mathbf f_{a\rightarrow b} = k_s \frac{\mathbf b -\mathbf a}{\|\mathbf b -\mathbf a\|}(\|\mathbf b -\mathbf a\| - l_0)$$

The potential energy of the spring is the integral over the displacement length $x = (\|\mathbf b -\mathbf a\| - l_0)$ and the potential energy is 

$$V = k_s (\|\mathbf b - \mathbf a\| - l_0)^2$$

Note that $k_s$ defines the "stiffness" of a spring, while the value of $k_s$ has different effect on springs of different resolution. Therefore, we need to normalize each $k_s$ by spring length, so that the stiffness is defined on the change in length as a fraction of the original length.

### Damping force
Behaves like viscous drag on motion, slow down motion in the direction of motion. However, we should only drag on change in spring length so that the damping force is only on internal, spring-driven motion instead of the whole system. 

$$\mathbf f_a = -k_d \frac{\mathbf b - \mathbf a}{\|\mathbf b - \mathbf a\|}(\dot{\mathbf b} - \dot{\mathbf a}) \cdot \frac{\mathbf b - \mathbf a}{\|\mathbf b - \mathbf a\|}$$


### Standard Form
The standard form of motion describes the external forces as 

\begin{align*}
&\mathbf f = &\mathcal K(\mathbf x) &+\mathcal D(\mathbf x, \dot{\mathbf x}) &+\mathcal M(\mathbf x, \dot{\mathbf x}, \ddot{\mathbf x})\\
&\text{external force} = &\text{internal elasticity} &+ \text{damping} &+\text{momentum}
\end{align*}

where $\mathcal{K}, \mathcal{D}, \mathcal{M}$ can be linearized as matrices. Also, zero-length springs can result in constant $K, D$ and typically we use a pre-computed constant $M$ and keep it diagonal by lumping. 


## Euler's Method (Forward Euler)

\begin{align*}
\mathbf x^{t+dt} &= \mathbf x^t + dt \dot{\mathbf x}^t\\
\dot{\mathbf x}^{t+dt} &= \dot{\mathbf x}^t + dt \ddot{\mathbf x}^t
\end{align*}

__Forward Euler__ is simple but only first order accurate, and often goes unstable. In a mass spring system, the velocity is always estimated from the last timestamp. Thus, energy is always increasing exponentially. 

### Modified Euler

To prevent the error growing too quick, average velocity at start and end of step. 

\begin{align*}
\dot{\mathbf x}^{t+dt} &= \dot{\mathbf x}^t + dt \ddot{\mathbf x}^t\\
\mathbf x^{t+dt} &= \mathbf x^t + \frac{dt}{2} (\dot{\mathbf x}^t + \dot{\mathbf x}^{t+dt})\\
&= \mathbf x^t  + dt \dot{\mathbf x}^t + \frac{(dt)^2}{2}\ddot{\mathbf x}^t
\end{align*}

This accumulates less error and is OK for stiff systems, while still instable when $k_s$ is large. 

## Implicit Euler (Backward Euler)
Instead of computing the force by 

$$\mathbf f^t = \mathcal K(\mathbf x^t) +\mathcal D(\mathbf x^t, \dot{\mathbf x}^t) +M\ddot{\mathbf x}$$

using the future derivatives for the current step as 

$$\mathbf f^t = \mathcal K(\mathbf x^{t+dt}) +\mathcal D(\mathbf x^{t+dt}, \dot{\mathbf x}^{t+dt}) +M\ddot{\mathbf x}$$

To be able to solve the unknown, we the system is linear so that 

\begin{align*}
\mathbf f^t &=  K(\mathbf x^t + \Delta \mathbf x) + D(\dot{\mathbf x}^t + \Delta \dot{\mathbf x}) +M\ddot{\mathbf x}\\
            &=  K(\mathbf x^t +  dt\dot{\mathbf x}^{t+dt}) + D(\dot{\mathbf x}^t + dt \ddot{\mathbf x}) +M\ddot{\mathbf x}
\end{align*}

Implicit Euler can be made unconditionally stable, while we need to solve a nonlinear problem for the unknown acceleration, which often involves optimization based solver, such as Newton's method. Therefore, implicit Euler takes longer than explicit method. 


## Position-based / Verlet Integration

Note that forward Euler is unstable because error is growing exponentially. Masses will move increasingly faster and eventually diverge. Therefore, the idea is to constrain mass positions after each forward step so that it cannot diverge. The constraints will dissipate the increased energy hence stabilize the system. 

Generally, the constraints are expressed as "stiffness" of the springs. For example, limit the spring max lengths by 

$$\forall \mathbf a,\mathbf b \in V. \|\mathbf a - \mathbf b\| \leq l_{\max}$$

At each update, do the forward step as normally, then enforce the stiff constraints by adjusting the velocities. 