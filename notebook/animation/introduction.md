# Math and Physics Background

## Position, Velocity, and Acceleration
For a particle of constant mass $m$, its position at time $t$ is $\mathbf x(t):\mathbb R\rightarrow \mathbb R^3$ (Assuming 3D space), its velocity $\mathbf v(t) = \frac{d\mathbf x}{dt}(t)$ and its acceleration $\mathbf a(t) = \frac{d\mathbf v}{dt}(t) = \frac{d^2\mathbf x}{dt^2}(t)$

## Newton's Law
1. Every object will remain at rest of in uniform motion in a straight line unless compelled to change its state by the action of an external force
2. The force acting on ab object is equal to the time rate-of-change of the momentum 
   
    $$f = \underset{\text{time rate of change}}{\frac{d}{dt}}\underset{\text{momentum}}{m\mathbf v}= m\frac{d\mathbf v}{dt} = m\mathbf a$$

3. For every action there is an equal and opposite reaction


## Variational (Analytical) Mechanics
Based on fundamental energies rather than two vectorial quantities

- __Kinetic Energy__ energy due to motion
- __Potential Energy__ energy "held within" an object due to position, internal stresses, charge, etc. 
Potential energy has the potential to become kinetic energy

### Problem Settings
Let the image of $\mathbf f(t)$ be the path of the motion, setting some functional 

$$e(\mathbf f(t), \dot{\mathbf f}(t), ...) \rightarrow \mathbb R$$

and then solve (optimize) the variational derivative to find the proper $\mathbf f$

### Generalized Coordinates
Let the generalized coordinates be $\mathbf q: \mathbb R \rightarrow \mathbb R^n$ be the actual variable parametrize the motion

$$\mathbf x(t) = \mathbf f(\mathbf q(t))$$

$$\frac{d\mathbf x}{dt}(t) = \underset{\text{Jacobian}}{\frac{d\mathbf f}{d\mathbf q}}\underset{\text{generalized velocity}}{\dot q(t)}$$

### Lagrangian
define the Lagrangian be

$$L = T - V = \text{kinetic} - \text{potential}$$

## The Principle of Least Action
Assume the end points are known, to find the path between them by finding a __stationary point__ of the __action__. 

### Action
For constant time $t_1, t_2$, the action is a functional equals the integral of the Lagrangian over 

$$S(\mathbf q(t), \dot{\mathbf q}(t)) = \int_{t_1}^{t_2} T(\mathbf q(t), \dot{\mathbf q}(t)) - V(\mathbf q(t), \dot{\mathbf q}(t)) = dt = \int_{t_1}^{t_2}L(\mathbf q(t), \dot{\mathbf q}(t))dt$$

### Stationary Point

$$S(\mathbf q + \delta\mathbf q, \dot{\mathbf q}+\delta \dot{\mathbf q}) = S(\mathbf q(t), \dot{\mathbf q}(t))$$

which means that perturbation $\delta$ of the trajectory $\mathbf q$ does not change the action.

### The Calculus of Variations (Euler Lagrange Equations)

\begin{align*}
S(\mathbf q + \delta\mathbf q, \dot{\mathbf q}+\delta \dot{\mathbf q}) &=\int_{t_1}^{t_2}L(\mathbf q + \delta\mathbf q, \dot{\mathbf q}+\delta \dot{\mathbf q})dt\\
&\approx \int_{t_1}^{t_2}L(\mathbf q, \dot{\mathbf q})dt + \int_{t_1}^{t_2}\frac{\partial L}{\partial\mathbf q}\delta\mathbf q + \frac{\partial L}{\partial\dot{\mathbf q}}\delta\dot{\mathbf q }dt\\
&= S(\mathbf q, \dot{\mathbf q}) + \underset{\text{first variation}}{\delta S(\mathbf q, \dot{\mathbf q})}
\end{align*}

Therefore, principle of least action becomes 

$$\delta S(\mathbf q, \dot{\mathbf q}) = 0$$

Then, use integration by parts (see APM462 notes for detailed steps)

$$\int_{t_1}^{t_2}\frac{\partial L}{\partial\mathbf q}\delta\mathbf q + \frac{\partial L}{\partial\dot{\mathbf q}}\delta\dot{\mathbf q }dt = \int_{t_1}^{t_2}(\frac{\partial L}{\partial \mathbf q} - \frac{d}{dt}\frac{\partial L}{\partial \dot{\mathbf q}})\delta \mathbf q dt + \underset{\text{known end points so }=0}{\frac{\partial L}{\partial \dot{\mathbf q}}\delta \mathbf q \vert_{t_1}^{t_2}}$$

Therefore, we have the Euler Lagrange equation (The lemmas are in APM462 notes)

$$\frac{\partial L}{\partial \mathbf q} = \frac{d}{dt}\frac{\partial L}{\partial \dot{\mathbf q}}$$
