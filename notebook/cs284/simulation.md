# Physics based Animation

## Mass spring system

Given a set of mass points (vertices) and springs (edges). For each spring connecting two mass points $(\mathbf a, \mathbf b)$, the stretch  force from $\mathbf a$ to $\mathbf b$ as $\mathbf f_{a\rightarrow b} = k_s(\mathbf b - \mathbf a)$ where $k_s$ is the stiffness of the spring. The reverse force $\mathbf f_{b\rightarrow a} = -\mathbf f_{a\rightarrow b} = k_s(\mathbf a - \mathbf b)$.

For non-zero length spring, let $l_0$ be its length as rest pose, we can expand the equation to 

### Potential force

$$\mathbf f_{a\rightarrow b} = k_s \frac{\mathbf b -\mathbf a}{\|\mathbf b -\mathbf a\|}(\|\mathbf b -\mathbf a\| - l_0)$$

The potential energy of the spring is the integral over the displacement length $x = (\|\mathbf b -\mathbf a\| - l_0)$ and the potential energy is 

$$V = k_s (\|\mathbf b - \mathbf a\| - l_0)^2$$

### Damping force
