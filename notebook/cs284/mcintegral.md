# Monte Carlo Integration

The idea behind Monte Carlo integration is to estimate integral based on random sampling of function. 

[Notes on MC integration and importance sampling](../csc412/sampling.md)

Here we provide some common examples for the applications on MC integration in graphics

## Basic Monte Carlo Estimator 

A basic Monte Carlo estimator is a special case where $X\sim \text{Uniform}(\Omega)$ where $\Omega$ is the area that we want to integrate on. In the above case, we have that $X\sim \text{Uniform}(a, b)$ so that $F_N = \frac{b-a}{N} \sum_{i=1}^N f(X_i)$.

Extending to 3D cube, we can have 

$$F_N = (x_1-x_0)(y_1-y_0)(z_1-z_0)N^{-1} \sum_{i=1}^N f(X_i)$$

## Sampling light source area

Consider an environment where we have one area light source, and we want to find the incoming irradiance on a surface at location $\mathbf x$. 

$$E(\mathbf x) = \int_{H^2} L_i(\mathbf x, \omega) \cos\theta d\omega$$

Omitted any reflections, we know that almost all of the incoming irradiance comes from the light source. If we uniformly sample from the hemisphere, the integral will give much noise. Instead, note that the integral is equivalent to all the outgoing light at each position $\mathbf x'$ of the light source, to the direction $\omega' = \mathbf x - \mathbf x'$, multiplying the Lambert effect 

$$\mathbf l\cdot \mathbf n = \frac{\omega}{\|\omega\|}\cdot \frac{\omega'}{\|\omega'\|} = \frac{\cos\theta \cos\theta'}{\|\mathbf x - \mathbf x'\|^2}$$

Thus, the final integral is 

$$E(\mathbf x) = \int_A L_o(\mathbf x', \omega') V(\mathbf x,\mathbf x') \frac{\cos\theta \cos\theta'}{\|\mathbf x - \mathbf x'\|^2}dA'$$

where $V$ is the visibility map s.t. the surface point $\mathbf x$ is visible from light position $\mathbf x'$. 

Thus, we can use MC integration by randomly sample $N$ light beams with position $\mathbf x_i'$ and direction $\omega_i'$. 

## Inversion Method

Inversion method aims to draw samples from some PDF given its CDF (so that the PDF is unknown). For some CDF $F:\mathcal X\rightarrow [0, 1], F(x) := Pr(X < x) = u$, if we know the inverse $F^{-1}: [0, 1]\rightarrow \mathcal X$, then we can draw samples from $U\sim \text{Uniform}(0, 1)$ and draw examples from $X = F^{-1}(U)$. 

### Uniform sampling from circles

WLOG Consider a unit circle $(\cos\theta, sin\theta)$. If we independently draw $u \in [0, 1], v\in[0,2\pi)$, then $(u\cos\theta, u\sin\theta)$ is not uniform over the area of the circle. 

Note that the area of a unit sphere is 1, so that we have the CDF

$$F(r, \theta) = \frac{1}{2\pi}\int_0^r \int_0^{\theta} dv du = \frac{\theta}{2\pi} r^2$$

The marginal CDFs are 

$$F_\theta(r) = r^2, F_r(\theta) = 2\pi\theta$$

so that the inversion method gives $r = u^{1/2}, \theta = 2\pi v$ where $U,V\sim \text{Uniform}(0, 1)$.

### Uniform direction sampling from Hemispheres 
The idea is very similar, we are sampling from the sphere of a unit hemisphere. The CDF is 

$$F(\theta, \phi) = \frac{1}{2\pi}\int_0^\theta \int_0^\phi \sin\phi d\phi d\theta = \frac{(1-\cos\phi)\theta}{2\pi}$$

Marginalizing to $F(\theta) = \theta/ 2\pi, F(\phi) = 1 - \cos\phi$ and inverse $\theta = 2\pi u, \phi = \cos^{-1}(1-v) = \cos^{-1}(v')$ since $1-V \sim \text{Uniform}(0,1)$ as well.

Turning into Cartesian coordinates, we have 

$$(u,v)\rightarrow(\sqrt{1-v^2}\cos(2\pi u), \sqrt{1-v^2}\sin(2\pi u), v)$$