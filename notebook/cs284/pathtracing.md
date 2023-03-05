# Global Illumination and Path Tracing

## Radiometry and Photometry

__Radiometry__ Measurement system and units for illumination, measure the spatial properties of light.   
__Photometry__ Measure the radiometric quantities accounts for response of human visual system. 

| Physics | Radiometry | Photometry | Description |
| --- | --- | --- | --- |
| energy $Q$ | radiant energy (Joules $J$) | luminous energy ($\text{lm}\cdot\text{sec}$) |  energy of electromagnetic radiation |
| Flux (power) $\Theta = d_tQ$ | radiant Power (Watt $W$) | luminous power (lumen $\text{lm}$) | energy emitted, reflected, transmitted or received, per unit time |
| angular flux density $I$ | radiant intensity ($W/sr$) | luminous intensity (candela $\text{cd} = \text{lm}/sr$) |   power per unit solid angle emitted by a point light source |
| spatial flux density $E$ | irradiance ($W/m^2$) | illuminance ($\text{lux} = \text{lm}/m^2$) | power per unit area incident on a surface point |
| spatio-angular flux density $L$ | radiance ($W/m^2/sr$) | luminance ($\text{nit} = \text{cd}/m^2$) | power emitted, reflected, transmitted or received by a surface, per unit solid angle, per unit projected area. |


### Solid angles

A solid angle is similar to the radian on a circle, a solid angle is the ratio of subtended area on sphere to radius squared. $\Omega = A / r^2$, a sphere has $4\pi$ steradians ($sr$). 

The surface area of the unit sphere $S^2$ is

$$\Omega = \int_{S^2} d\omega = \int_0^{2\pi}\int_0^\pi \sin\theta d\theta d\phi = 4\pi$$

where $\omega = (\phi, \theta)$ is the unit length direction. Thus, the angular flux intensity is derived from the total emitted power as 

$$\Phi = \int_{S^2} Id\omega = 4\pi I, I = \Phi / 4\pi$$

### Irradiance

__Lambert's Cosine Law__ Irradiance at surface is proportional to cosine of angle between light direction and surface normal. 

$$E = \frac{\Phi}{A} \cos\theta = \frac{\Phi}{A} \mathbf l \cdot \mathbf n$$

where $\mathbf l$ is the light direction and $\mathbf n$ is the surface normal. 

__Falloff__ Assume that light is emitting flux $\Phi$ in a uniform angular distribution, then the intensity falloffs by squared radius. 

$$E_1 = \frac{\Phi}{4\pi}, E_r = \frac{\Phi}{4\pi r^2}, E_r = \frac{E_1}{r^2}$$

### Radiance

__radiance / luminance__ is the power emitted, reflected, transmitted or received by a surface, per unit solid angle, per unit projected area. 

$$L(\mathbf x, \omega) = \frac{\partial^2 \Phi}{\partial\omega \partial A \cos\theta} = \frac{\partial E}{\partial \omega \cos\theta} = \frac{\partial I}{\partial A \cos\theta}$$

Consider a opaque object surface, light will absorb, reflection, and refract on the surface. Thus, the incident radiance and exitant radiance are different. 

### Environment irradiance

For a given surface point $\mathbf x$, the environment irradiance is the amount of flux received is the integral over incoming light from all directions.

$$E(\mathbf x) = \int_{H^2} L_i(\mathbf x, \omega) \cos\theta d\omega$$

where $\theta = \omega_i \cdot \mathbf n_x$ is the angle between the incoming light and the surface normal at $\mathbf x$, note that $H^2$ is the hemisphere because $\cos\theta < 0$ for the over half. 

For a uniform area light source, the light irradiance on the surface is proportional to the projected area on the unit sphere, then projected onto surface tangent plane.

$$E(\mathbf x) = \int_{H^2} L_i(\mathbf x, \omega)\cos\theta d\omega = L\int_{\Omega}\cos\theta d\omega = L\text{proj}(\Omega)$$

Thus, for a disk area light of radius $r$ and $h$ units above the surface. The projection on the unit sphere is a circle of radius $\sin(\alpha) = \sin(\tan^{-1}(r/h))$. Thus $\text{proj}(\Omega) = \pi r^2 = \pi\sin^2(\alpha)$

### Material reflectance (BRDF)

For a material surface point $\mathbf x$, the incoming irradiance from angle $\omega_i$ is a differential of the total irradiance.

$$\partial_{\omega}E(\omega_i) = L_i(\mathbf x, \omega_i)\cos\theta_i d\omega_i$$

and outgoing radiance, or the reflectance, at direction $\omega_r$, is proportional to the incoming irradiance, and we define the __bidirectional reflectance distribution function (BRDF)__ as

$$f_{\mathbf x}(\omega_i, \omega_r) = \frac{\partial_{\omega} L_r (\omega_r)}{\partial_{\omega} E_i (\omega_i)} = \frac{\partial_{\omega} L_r (\omega_r)}{L_i(\mathbf x, \omega_i)\cos\theta_i d\omega_i}$$

so that the outgoing reflectance at position $\mathbf x$ and viewing direction $\omega_r$ is

$$L_r(\mathbf x, \omega_r) = \int_{H^2} f_{\mathbf x}(\omega_i, \omega_r) L_i(\mathbf x, \omega_i) \cos\theta_i d\omega_i$$


## Global illumination and path tracing

Note that the outgoing irradiance $L_r$ can intersect other surfaces and become $L_i$ on other surfaces, thus the integral is recursive (and probably infinitely recursive if the light is bouncing within a closed environment). Which means

$$L_i(\mathbf x, \omega_i) = L_o(T(\mathbf x, \omega_i), -\omega_i)$$

where $T(\mathbf x, \omega_i)$ is the first intersection in the scene along ray $\mathbf x, \omega_i$.

Therefore, we rewrite the reflection equation at surface position $\mathbf x$ and outgoing angle $\omega_o$ as

$$L_o(\mathbf x, \omega_o) = L_e(\mathbf x, \omega_o) + \int_{H^2} f_{\mathbf x}(\omega_i, \omega_o) L_o(T(\mathbf x, \omega_i), -\omega_i)\cos\theta_i d\omega_i$$

We simplify the notation by using higher order operator as 

- $R(L_i) = L_o$ the reflection operator, the outgoing radiance resulting from the incoming radiance
- $T(L_o) = L_i$ the transport operator, the incoming radiance that is the light transport of the other outgoing irradiance. 

Together, we simplify the notation as 

$$L_o = L_e + (R\circ T)(L_o) := L_e + K(L_o)$$

the outgoing light is the sum of self-emitting light, plus all the lights bouncing around the scene and reflected on the surface. 

Intuitively, the amount of the light on the surface will converge since we lose some light at each bounce. In fact, we can make sure that $L_o$ converges if the BRDF is correctly defined. Therefore, we have that 

$$L = \sum_{i=0}^{\infty} K^i(L_e)$$

where $L_e$ is the emitted light and $K^0(L_e) = L_e$. In other words, the total amount of light of a surface is the sum of its own emitted light $K^0$, all emitted light that reflected by the surface $K^1$, all emitted light that bounced once and reflected by the surface $K^2$, all emitted light bounced twice, and so on. 

### Monte Carlo estimate

Given a distribution $p(\omega_i)$ on the incoming light direction, the Monte Carlo estimate of the outgoing reflectance is 

$$\tilde{L_r}(\mathbf x, \omega_r) = \frac{1}{N}\sum_{j=1}^N \frac{1}{p(\omega_j)} f_{\mathbf x}(\omega_j, \omega_r)L_i(\mathbf x, \omega_j)\cos \theta_j$$

some choice of $p$ can be the [uniform distribution of hemisphere directions](./mcintegral.md#uniform-direction-sampling-from-hemispheres) with $p(\omega_i) = \frac{1}{2\pi}$, importance sampling of the BRDF function, or importance sampling of the lights (uniformly sample positions on the light)

We can implement the operator as a recursion, i.e.

```py
# eye: the viewing position
# dir: the viewing angle
def Lout(eye, dir, recursion_depth=0):
    x = scene.intersect(eye, dir) # the object surface
    w_out = -dir # the outgoing direction of x
    L = x.emission(w_out) # emitted light

    # avoid infinite recursion
    if recursion_depth == MAX_RECURSION_DEPTH:
        return L

    # importance sampling a incoming direction based on brdf
    w_in, pdf = x.brdf.sample(w_out) 
    L += Lout(x, w_in, recursion_depth + 1) * x.brdf.f(w_in, w_out) * dot(x.normal, w_in) / pdf
    return L
```

Although higher `MAX_RECURSION_DEPTH` will give better estimation, since light contributions from higher bounces decrease exponentially and will eventually become small enough. The above implementation is biased, especially when `MAX_RECURSION_DEPTH` is small, since we can never observe any bounced lights for `MAX_RECURSION_DEPTH + 1` bounces. 

### Russian Roulette 

Russian Roulette is a Monte Carlo estimate of infinite integrals. For some random variable $X$, let $Y \sim \text{Uniform}(0, 1)$ and define 

$$X_{rr} = \frac{X}{p_{rr}} \mathbb I(Y < p_{rr})$$

so that the expected value for $X_{rr}$ is 

$$E(X_{rr}) = p_{rr}E(\frac{X}{p_{rr}}) + (1-p_{rr})0 = E(X)$$

which means that we stop the recursion if we fail a Bernoulli trial with probability $p_{rr}$. 

### Path tracing

We further decompose `Lout` into two parts. The direct illumination given by light sources ($K^1(L_o)$) and indirect illumination given by reflected light from other surfaces ($K^{>1}(L_o)$). Summarize all things together, we have

```py
def L0(x, w_out):
    return x.emission(w_out)

def L1(x, w_out):
    L = 0
    for _ in raneg(NUM_SAMPLES):
        # randomly choose light i from multiple lights in the scene
        # with probability pi
        light, pi = scene.sample_light_source()
        # importance sampling of light position with probability pl
        light_pos, pl = light.sample_dir()
        w_in = normalized(light_pos - x)
        # if the light arrives the object, not blocked by others
        if not scene.intersect(x, w_in):
            l = light.emission(light_pos, -w_in)
            L += l * x.brdf(w_in, w_out) * dot(w_in, x.normal) / pi / pl
    return L



def L1_and_more(x, w_out, recursion_depth=0):
    L = L1(x, w_out)
    w_in, pdf = x.brdf.sample(w_out) 
    cpdf = continue_probability(x.brdf, w_in, w_out) \
        if recursion_depth > MAX_RECURSION_DEPTH \
        else 1
    # start Russian Roulette when we already enough bounces
    if random() > cpdf:
        return L
    # importance sampling a incoming direction based on brdf
    x_reflected = scene.intersect(x, w_out)
    w_in_reflected = -w_out
    L += L1_and_more(x_reflected, w_in_reflected, recursion_depth + 1) \ 
        * x.brdf.f(w_in, w_out) \ 
        * dot(x.normal, w_in) \ 
        / pdf / cpdf
    return L

# eye: the viewing position
# dir: the viewing angle
def Lout(eye, dir):
    x = scene.intersect(eye, dir) # the object surface
    w_out = -dir # the outgoing direction of x
    return L0(x, w_out) + L1_and_more(x, w_out)
```