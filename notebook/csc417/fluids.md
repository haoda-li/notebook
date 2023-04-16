# Fluid Simulation using SPH and FLIP

## Introduction
Fluid, such as gas and water, plays an important role in animations. Although its flows look simple, simulation of fluid is much more complex than that of solid. The motion of fluid is governed by the incompressible Navier-Stokes equations, and various methods have been developed to simplify and solve the system.  

Two approaches are often taken to measure the motion of fluid. Lagragian approach treats the fluid as a set of particles, while Eulerian approach treats the fluid space as a grid field and measures quantities at each fixed point. 

In this report, we will present the particle based SPH method and particle-grid hybrid FLIP method. In SPH method, we view each particle as a blob of fluid with constant mass and varying volume. Similar to the finite element approach, for each particle position, we accumulate its density and forces by a weighted sum of particles within a radius, where the weights comes from smoothing kernels. We would then use the accumulated force to update the velocity of the particle. In FLIP method, we view each particle as a blob of fluid with constant mass and volume. We would evenly divide the space into fixed-size volumes using a staggered-grid system, and project particles' velocities onto velocity-grids of that staggered-grid system. We will then use the projected velocities of particles to calculate the pressure within each cell of the pressure-grid, and use that pressure to update each particle's own velocities. In both methods, we would use updated velocities of particles to update particles' positions.

## Related Work
Due to the complexity of fluid simulation, many works aim to build an efficient, stable, and visually appealing system for fluid simulation. For example, Stam's Stable Fluids [@stam1999stable] is one of the pioneer work for real-time fluid simulation. In addition, many works focus on specific phenomenon, such as ocean waves [@hinsinger2002interactive] and  lava drops [@stora1999animating]. 

## Problem Setup
For an arbitrary fluid, the incompressible Navier-Stokes equation describes the motion [@bridson2007fluid] as 

\begin{align*}
\rho \frac{\partial \mathbf{v}}{\partial t} + \rho \nabla \mathbf{v}\cdot \mathbf{v} &= -\nabla p + \rho \mathbf{g} + \mu\nabla^2\mathbf{v}\\
\text{subjected to }\nabla \cdot \mathbf{v} &= 0
\end{align*}

where $\rho$ is the density, $\mathbf{v}$ is the velocity, $\mathbf{g}$ is an external force, $p$ is the pressure, and $\mu$ is the viscosity coefficient of the fluid.

For a system of fluid, we represent it with a finite number of particles $\mathcal P = \{P_1,..., P_n\}$. For each particle $P_i$, we store its quantities such as velocity $\mathbf{v}_i$ and  position $\mathbf{p}_i$.  

## SPH Method
Instead of the incompressible condition as equation (2), SPH method assures conservation of mass 

$$\frac{\partial{\rho}}{\partial{t}}  + \nabla\dot(\rho t) = 0$$

by assigning constant mass $m$ to each particle.  Then, we can split the forces in equation (1) into pressure $-\nabla p$, external forces $\rho \mathbf{g}$, and viscosity $\mu\nabla^2\mathbf{v}$. Finally, as particles are moving with the fluid, we can update the particle's velocity via self-advection. For each particle, we have

$$\frac{D \mathbf v_i}{D t} = \frac{1}{\rho_i} (-\nabla p_i + \rho_i\mathbf{g} + \mu\nabla^2\mathbf v_i)$$

To update density of each particle and forces acting on each particle, we use Smoothed-Particle Hydrodynamics, which interpolates the quantities of $A$ at some location $\mathbf p$ as a weighted sum of all particles 

$$A(\mathbf{ p}) = \sum_{j=1}^n m_j\frac{A_j}{\rho_j}W(\mathbf p - \mathbf{p}_j) = m\sum_{j=1}^n\frac{A_j}{\rho_j}W(\mathbf p - \mathbf{p}_j)$$

where $W$ is called the smoothing kernel, and the desired properties for $W$ are being even ($W(\mathbf{r}) = W(-\mathbf r)$) and normalized ($\int W(\mathbf r)d\mathbf{r} = 1$). An appealing property for SPH is that the quantities are functions of the position, hence taking derivative is simply taking derivative on the smoothing kernel. In addition, to reduce the computation, we may only weigh the neighborhood of the target location, which means $W(\mathbf p - \mathbf p_j) = 0$ if $\|\mathbf p - \mathbf p_j\| > h$ for some support radius $h$. In this paper, 3 smoothing kernels are proposed for density, pressure, and viscosity. 

### Density
Using equation (5), the density update is 

$$\rho_i = m\sum_{j}\frac{\rho_j}{\rho_j}W(\mathbf p_i - \mathbf p_j) = m\sum_{j}W_{\text{poly6}}(\mathbf p_i - \mathbf p_j)$$

with the density smoothing kernel

$$W_{\text{poly6}}(\mathbf r) = \frac{315}{64\pi h^9}(h^2-\|\mathbf r\|^2)^3$$

### Pressure
Instead of directly using equation (5), the pressure update is

$$-\nabla p_i = -m\sum_j \frac{p_i +  p_j}{2\rho_j}\nabla W_{\text{spikey}}(\mathbf p_i-\mathbf p_j)$$

we use the mean pressure of two particles to keep it symmetric. Consider two particles interacting with each other, this equation makes sure they get the same amount of pressure. The smoothing kernel is 

$$W_{\text{spikey}}(\mathbf r) = \frac{15}{\pi h^6}(h-\|\mathbf r\|)^3$$

Because the pressure is not carried on each particle, we compute it using modified ideal gas state equation

$$p_i = k(\rho_i - \rho_0)$$

where $k$ is the gas constant, $\rho_0$ is the rest density for the fluid. Since we only care about the offset of pressure from each direction, removing the constant rest density from all directions have no effect on the simulation and improves numerical stability.

### Viscosity
Since viscosity only depends on velocity differences, the update is 

$$\mu\nabla^2 \mathbf v_i = \mu m \sum_j \frac{\mathbf v_j - \mathbf v_i}{\rho_i}\nabla^2W_{\text{visco}}(\mathbf p_i-\mathbf p_j)$$

with smoothing kernel

$$W_{\text{visco}}(\mathbf r) = \frac{15}{2\pi h^3}(-\frac{\|r\|^3}{h^3} + \frac{\|r\|^2}{h^2} + \frac{h}{2\|r\|} - 1)$$

### Surface Tension
For simulating liquid, we often model air as void. Then, surface tension, or the attractive forces pulling liquid molecules to each other, creates the imbalance on the liquid's surface. To model such force, we add a smooth color field as

$$c_i = m\sum_j \rho_j^{-1}W(\mathbf{p}_i - \mathbf{p}_j)$$

so that we can define its gradient field $\mathbf n = \nabla c$ and curvature as $\kappa = \frac{\nabla^2 c}{\|\mathbf n\|}$, and the surface tension is 

$$\sigma\kappa\mathbf{n} = \sigma \frac{\nabla^2 c \cdot \nabla c}{\|\nabla c\|}$$

### External forces
For external forces such as gravity and collision forces, we consider each particle as a mass and directly apply the forces onto them. For the collision response, we simply push them away from the object and reflect its velocity around the collision normal.


### Neighboring Search
Note that we only need to sum up the neighboring particles within a certain radius $h$, a natural optimization will be dividing the space into grid of $h$, then for each particle, we only need to search for the 27 cubes. 

## FLIP Method

We would first simplify the incompressible Navier-Stokes equation by removing the viscosity term, and the simplified equation looks like this:

$$\rho \frac{\partial \mathbf{v}}{\partial t} + \rho \nabla \mathbf{v}\cdot \mathbf{v} = -\nabla p + \rho \mathbf{g} \text{ subjected to }\nabla \cdot \mathbf{v} = 0$$

FLIP method be divided into three parts in general to handle three different effects: advection, external forces, and pressure.

The first two steps of the FLIP method are very simple. At each time step, we would first update each particle's position based on its current velocity, and then we would update each particle's velocity by considering the how external force, such as the gravitational force, influences particles. 

The first step takes care of the effect of advection, which states that:

$$\frac{\partial \mathbf{v}}{\partial t} + \nabla \mathbf{v}\cdot \mathbf{v} = 0$$

The second step takes care of the effect of external forces, which states that:

$$\rho \frac{\partial \mathbf{v}}{\partial t} = \rho \mathbf{g}$$

The third and the most important step is to calculate pressure and use pressure to further update each particle's velocity, and this step takes care of the effect of pressure, which strates that: 

$$\rho \frac{\partial \mathbf{v}}{\partial t} = -\nabla p \text{ subjected to }\nabla \cdot \mathbf{v} = 0$$

We will break this step down into multiple parts and explain each part in detail.

### Velocity projection
The first part is to build a three-dimensional staggered-grid system. This staggered-grid system consists of four separate three-dimensional grids. Three velocity-grids of the staggered-grid system are used to handle $x$, $y$, and $z$ component of velocity individually, and the remaining pressure-grid is used to handle the pressure. For each of the particles and for each of the three components of the velocity, we would first find the cell of the velocity-grid that contains that particle based on that particle's position, and then project that particle’s corresponding velocity component onto eight corners of that cell using trilinear interpolation.
### Solving pressure
We would discretize equation (17) to solve for pressure, and the resulting equation for calculating pressure looks like this: 

$$\nabla\cdot\nabla p = \frac{\rho}{\Delta t}\nabla\cdot \mathbf{v}^t$$

Combining with the staggered-grid system and finite difference derivative technique, we could solve for pressure $p$ and obtain the pressure-grid.
### Updating velocity using pressure
After obtaining pressure-grid, we could use this equation to update velocity-grids:

$$\mathbf{v}^{t+1} = \mathbf{v}^{t} -  \frac{\Delta t}{\rho}\nabla p$$

We would project the change in velocity, which is $-\frac{\Delta t}{\rho}\nabla p$ back onto particles.

### Solid boundary conditions
There are two more boundary conditions we need to consider. The first one is the solid boundary condition, which means that the fluid could not flow through the solid wall. It is very simple for this constraint to hold: we just need to the change the velocities on the velocity-grids that are on the solid wall to zero. We would use those changed velocity-grids to calculate the pressure-grid, and use pressure-grid to update velocities on the velocity-grids that are __inside__ the solid wall. The velocities on the velocity-grids that are on the solid wall have already been updated to 0, and the changes in velocities on the velocity-grids that are on the solid wall would be the negative projected particle velocity. After implementing the above parts, we could simulate smoke. However, to simulate fluid like water, we still have one more constraint to implement.

### Free surface boundary conditions
One important fact is that the air would not exert pressure on the water. To simulate water, we need to make sure that the pressure is zero on the water surface. To keep track of the water surface, we would mark each cell of the pressure-grid as fluid cell or air cell. We would initialize cells containing particles to $-1$ and empty cells to $+1$. Note that this would result in stair-step artifacts in fluid surface, so we then applied three-dimensional Gaussian convolution to smooth that scalar filed containing $-1$ and $+1$. After smoothing, the cells containing positive values become air cells, and the cells containing negative values become fluid cells. We would only calculate the pressure inside the fluid cell. When the fluid cell is adjacent to an air cell, we would first find the fluid surface by applying linear interpolation to the value inside the fluid cell and value inside the adjacent air cell to find the position of zero, which represents the fluid surface, we would then modify the pressure inside the fluid cell with ghost pressure to make sure that the pressure on the fluid surface is zero. In that way, the free surface boundary conditions would be satisfied, and we could simulate water.

## Results
We implemented these methods using Eigen [@eigenweb] and libigl [@libigl] on CPU with single threading. We simulated the scene of pouring water into a box with 5625 particles. For both methods, we can animate the scene in real time. The frame rate is quite steady for FLIP method, while in SPH method the frame rate had significant drops when particles are crowded together. In both cases, the scene successfully simulates the water flows and waves. 

## Conclusion
In this paper, we introduce two particle-based methods for simulating fluids. SPH method uses a purely particle based approach, and use smoothing kernels to interpolate force components from neighboring particles. FLIP method uses particles to represent fluid blobs, and a staggered-grid system to directly solve pressure. By taking different approaches, the two methods have quite different characteristics. SPH, due to its purely particle based design, is easier to implement, SPH also provides more physical coefficients, hence can model a wide class of fluids. However, SPH method is not incompressible. On the other hand, FLIP simplifies the model by assuming incompressible, inviscid conditions. FLIP has better performance on simulating water. Computational complexity is also different for each of the two methods. For SPH method, there would be more computations if the particles are compressed within a small portion of the entire space, since we need to consider more particles to compute forces for each of the particles. However, for FLIP method, there would be more computations if particles are evenly spread across the entire space since in that case, we would have more fluid cells to consider when constructing the pressure grid.
