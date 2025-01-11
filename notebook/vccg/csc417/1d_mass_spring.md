# 1D Mass Spring System


## Generalized coordinates 
Given a particle of mass $m$ 

$$q = x(t)$$

so that the generalized velocity is 

$$\dot q = v(t)$$

### Kinetic Energy
In 1-D the kinetic energy is $\frac 12 mv^2 = \frac 12 m\dot q$

### Potential Energy
By Hooke's Law, force is linearly proportional to stretch in spring, i.e. 

$$f = -kx$$

for some stiffness coefficient $k$, then the total mechanical work is 

$$W = \int \underset{\text{force}}{-kx(t)}\underset{\text{displacement}}{v(t)} dt = \int -kx dx = -\frac12kx^2$$

and the potential energy is the negative of work

$$V = -W = \frac12 kx^2$$

### Equation of Motion
Therefore, we have 

$$L = \frac12 m\dot q^2 - \frac12 kq^2$$

By Euler Lagrange Equation

\begin{align*}
\frac{\partial L}{\partial q} &= \frac{d}{dt}\frac{\partial L}{\partial \dot q}\\
-kq &= \frac{d}{dt}(m\dot q)\\
-kq &= m\ddot q\\
\end{align*}

## Time Integration
Note that $q:\mathbb R\rightarrow \mathbb R$ is the mapping from time to the position of the particle at that time. Time integration 

 - input: A ODE $\ddot q = f(q, \dot q)$ and the initial conditions $q_0 = q(t_0), \dot q_0 = \dot q(t_0)$
 - output: the discrete update equation $q^{t+1} = f(q^t, q^{t+1},...,\dot q^t, \dot q^{t+1}, ...)$
 
### The Coupled First Order Systems
Note that we have a second-order ODE, $m\ddot q = -kq$, replaces $\dot q $ with velocity $v$, we can transform the system into a coupled first order ODE

$$m\dot v = -kq$$

rewrite into matrix form

$$\begin{pmatrix}m&0\\0&1\end{pmatrix}\frac{d}{dt}\begin{pmatrix}v\\q\end{pmatrix} = \begin{pmatrix}0&-k\\1&0\end{pmatrix}\begin{pmatrix}v\\q\end{pmatrix}$$

Denote $\mathbf y = [v, q]^T$, the equation above is further written as 

$$A  \dot{\mathbf y} = \mathbf f(\mathbf y)$$

### Phase Space
We define the phase space as the x-axis being the value of $v$ and y-axis being $q$, so that we can plot the trajectory of the position and velocity through time.

## Numerical Integration

Note that the integration above is simple, while more complex equations may not be suitable for analytical solution, so we need integrate it numerically

### Explicit and Implicit Integration
 - Explicit: Next time step can be computed entirely using the previous and current time step
 - Implicit: Next time step is computed using future values 
 
### Concerns
 - Performance: runtime / efficiency
 - Stability: We don't want the spring to "fly" out, which means we need the solution to stay "within" the bounded system of the analytical solution
 - Accuracy: the "visual" accuracy, we mostly want it looks real, even if the solution may not be mathematically correct

## Forward Euler Time Integration
Replace time derivative with finite difference

$$\dot{\mathbf y} \approx \frac{1}{\Delta t} (\mathbf y^{t+1} - \mathbf y^t)$$

so that 

\begin{align*}
A  \frac{1}{\Delta t} (\mathbf y^{t+1} - \mathbf y^t) &= \mathbf f(\mathbf y^t)\\
\mathbf y^{t+1} &= \mathbf y^t + \Delta t A^{-1}\mathbf f(\mathbf y^t)\\
v^{t+1} &= v^t - \Delta t \frac{k}{m}q^t\\
q^{t+1} &= q^t + \Delta t v^t
\end{align*}

### Problem
Because we replace the derivative with the current "slope", the trajectory is going outwards, which is unstable. 


```python 
--8<-- "csc417/scripts/1d_mass_spring.py:fe"
```

<iframe
    width="100%"
    height="480"
    src="./assets/1d_mass_spring_fe.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Runge-Kutta Time Integration

To fix the issue with Forward Euler, we can average several "slope" to pull the trajectory back. The general idea is 

$$\mathbf y^{t+1} = \mathbf y^t + \Delta t A^{-1}(\alpha \mathbf f(\mathbf y^{t+a} + \beta \mathbf f(\tilde{\mathbf y}^{t+b})))$$

where $\tilde {\mathbf y}^{t+a} = y^t + \alpha \Delta tA^{-1}\mathbf f(\mathbf y^t)$ is the Forward Euler estimate. 

Following this template, we can have Heun's Method by taking $a=0, b= 1, \alpha=\beta=\frac12$

$$\mathbf y^{t+1} = \mathbf y^t + \frac{\Delta t}{2} A^{-1}(\mathbf f(\mathbf y^t) + \mathbf f(\tilde {\mathbf y}^{t+1}))$$

The most general used method is __RK4__, The Fourth-order Runge Kutta Method. 

\begin{align*}
\kappa_1 &= A^{-1}\mathbf f(\mathbf y^t)\\
\kappa_2 &= A^{-1}\mathbf f(\mathbf y^t + \frac{\Delta t}2 \kappa_1)\\
\kappa_3 &= A^{-1}\mathbf f(\mathbf y^t + \frac{\Delta t}2 \kappa_2)\\
\kappa_4 &= A^{-1}\mathbf f(\mathbf y^t + \Delta t \kappa_3)\\
\mathbf y^{t+1} &= \mathbf y^t + \frac{\Delta t}{6}(\kappa_1 + 2\kappa_2 + 2\kappa_3 + \kappa_4)
\end{align*}


```python
--8<-- "csc417/scripts/1d_mass_spring.py:rk4"
```

<iframe
    width="100%"
    height="480"
    src="./assets/1d_mass_spring_rk4.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Backward Euler Time Integration
This is the implicit time integration. Compare to Forward Euler, instead of evaluating at the current step, we evaluate at the next time step, i.e.

$$A  \frac{1}{\Delta t} (\mathbf y^{t+1} - \mathbf y^t) = \mathbf f(\mathbf y^{t+1})$$

Note that the unknown $\mathbf y^{t+1}$ appears on both sides, which causes problem. 
However, if we look back at $\mathbf f (\mathbf y)$, note that 

$$\mathbf f (\mathbf y) = \begin{pmatrix}0&-k\\1&0\end{pmatrix}\begin{pmatrix}v\\q\end{pmatrix} = B\mathbf y$$

Since $\mathbf f$ is a linear function, we have 

\begin{align*}
A  \frac{1}{\Delta t} (\mathbf y^{t+1} - \mathbf y^t) &= B\mathbf y^{t+1}\\
(I - \Delta t A^{-1}B)\mathbf y^{t+1} &= \mathbf y^t\\
(1+\Delta t^2 \frac km) v^{t+1} &= v^t - \Delta t \frac km q^t\\
q^{t+1} &= q^t + \Delta tv^{t+1}
\end{align*}

Note that this is stable since the vector difference is the slope at $t+1$, which means it "pulls" back the trajectory to the origin. 


```python
--8<-- "csc417/scripts/1d_mass_spring.py:be"
```

<iframe
    width="100%"
    height="480"
    src="./assets/1d_mass_spring_be.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Symplectic Euler Time Integration
Note that Forward Euler causes the exploding trajectory and the Backward Euler causes damping, we can do the two integrations alternately to "cancel out" long term effect, i.e.

First take an explicit velocity step

$$v^{t+1} = v^t - \Delta t \frac km q^t$$

Then take an implicit position step

$$q^{t+1} = q^t + \Delta t v^{t+1}$$



```python
--8<-- "csc417/scripts/1d_mass_spring.py:sc"
```

<iframe
    width="100%"
    height="480"
    src="./assets/1d_mass_spring_sc.html"
    frameborder="0"
    allowfullscreen
></iframe>


???quote "Source code"

    ```python
    --8<-- "csc417/scripts/1d_mass_spring.py"
    ```
