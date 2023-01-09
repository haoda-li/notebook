# Rotation Matrix Time Derivatives


## Problem Setup
For a point $x_0 \in\mathbb R^4$, the rotation is a transformation defined as 

$$x(\Delta t) = R(\Delta t) x_0$$

where $R(\Delta t) \in SO(3)$. 

Then, through the transformation through time $t$ will create a trajectory. We come up with the velocity of $x$ as 

$$\dot x (\Delta t) = \dot R(\Delta t) x_0$$

So that the velocity is the time derivative of the rotation matrix. 

## Angular Velocity
Without loss of generality, assume $x$ is rotated along the rotation with the axis of rotation $\vec a\in\mathbb R^3$. Therefore, $x$ is travel in a circle.   
Let $\dot\theta$ be the change in angle.  
Let $v: \mathbb R\rightarrow \mathbb R^3$ be the velocity of $x$, decompose $v(t) = a(t)d(t)$ where $a$ is the magnitude and $d$ is the direction. 

Since we are rotating around $\vec a$, i.e. the plane that contains the circle is orthogonal to $\vec a$. Hence $d\perp \vec a$.  
In addition, a rotation is orthogonal matrix so that $v\perp x$, since $\vec a,v,x$ are mutually orthogonal, we can uniquely determine $d$ from 

$$d = \frac{\vec a \times x}{\|x\|}$$

Then, consider the magnitude $a$, let $y = x + \Delta tv$. The angle formed by $y$ and $x$ is $\dot\theta \Delta t$. So that we can have 

$$a\Delta t = \|x\|\tan(\dot\theta) = \|x\|\frac{\sin(\dot\theta\Delta t)}{\cos(\dot\theta\Delta t)}$$

Therefore, we can have 

$$\lim_{\Delta t\rightarrow 0} \|x\|\frac{\sin(\dot\theta\Delta t)}{\cos(\dot\theta\Delta t)} = \|x\|\frac{\dot\theta\Delta t}{1} = \|x\|\dot\theta\Delta t$$

so that 

$$a = \|x\|\dot\theta$$

and then

$$v = ad=\dot\theta\|x\|\frac{\vec a\times x}{\|x\|} = (\dot\theta \vec a) \times x = \omega \times x$$

Therefore, we obtain the angular velocity $\omega$, which includes the velocity of angle and the rotation direction.


<iframe
    width="100%"
    height="480"
    src="./assets/rotation.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Rotation Matrix
Since cross product can be written into cross matrix form as matrix multiplication, $v=\omega\times x $ can then be understood as 

$$\frac{dx}{dt} = [\omega]_\times x$$

which is a linear ODE, and has analytical solution

$$x(t) = \exp([\omega]_\times t) x$$

where $\exp(M)$ is the matrix exponential. 

### Matrix Exponential
For an invertible matrix $A\in\mathbb R^{n\times n}$. the matrix exponential $\exp(A)$ is given as 

$$\exp(A) = V\begin{bmatrix}e^{\lambda_1}&\cdots&0\\\vdots&\ddots&\vdots\\0&\cdots&e^{\lambda_n}\end{bmatrix}V^{-1}$$

Where $A=V\Lambda A^{-1}$ is the Eigen decomposition. However, as we did the decomposition, it is not very efficient. 

For our problem, since $[\omega]_{\times}$ is a cross product matrix, hence $3\times 3$ skew-symmetric, we can use __Rodrigues' Rotation Formula__. First, we can break $\omega t$ into the axis of rotation and angle of rotation, as $\vec a$ and $\theta$

$$\omega t = \frac{\omega}{\|\omega\|}{\|\omega\|t} = \vec a \theta$$

then Rodrigues' Rotation Formula gives 

$$R(t) = I + \sin(\theta)[\vec a]_\times + (1-\cos(\theta)) {[\vec a]_\times}^2$$

### Relationship between R and w
Note that we have $\dot x(t) = \dot R(t)x_0$ and the equation above gives $\dot x(t) = [\omega]_\times x$, therefore, we have found the relation that 

$$\dot R = [\omega]_\times$$

## General Equation
Consider the explicit equation with a fixed $t_0$

$$x(t_0+\Delta t) = \Delta R(\Delta t) R(t_0)x_0$$

and its time derivative is 

$$v = \frac{dx}{d\Delta t} = \Delta \dot R(\Delta t) R(t_0)x_0$$

Note that from the derivations above, since $R(t_0)x_0$ is a fixed point, $v$ is just the time derivative of rotation at time $t_0$ so that 

$$v = [\omega]_\times Rx_0$$

Another form of this equation is

\begin{align*}
v &= \omega \times Rx_0\\
&= -(Rx_0)\times \omega\\
&= R{[x_0]_\times}^TR^T \omega
\end{align*}

then this form gives that $v$ is linear in $\omega$.


???quote "Source code"

    ```python
    --8<-- "csc417/scripts/rotations.py"
    ```
