# Radiometry and Photometry

__Radiometry__ Measurement system and units for illumination, measure the spatial properties of light.   
__Photometry__ Measure the radiometric quantities accounts for response of human visual system. 

## Units

| Physics | Radiometry | Photometry | Description |
| --- | --- | --- | --- |
| energy $Q$ | radiant energy (Joules $J$) | luminous energy ($\text{lm}\cdot\text{sec}$) |  energy of electromagnetic radiation |
| Flux (power) $\Theta = d_tQ$ | radiant Power (Watt $W$) | luminous power (lumen $\text{lm}$) | energy emitted, reflected, transmitted or received, per unit time |
| angular flux density $I$ | radiant intensity ($W/sr$) | luminous intensity (candela $\text{cd} = \text{lm}/sr$) |   power per unit solid angle emitted by a point light source |
| spatial flux density $E$ | irradiance ($W/m^2$) | illuminance ($\text{lux} = \text{lm}/m^2$) | power per unit area incident on a surface point |
| spatio-angular flux density $L$ | radiance ($W/m^2/sr$) | luminance ($\text{nit} = \text{cd}/m^2$) | power emitted, reflected, transmitted or received by a surface, per unit solid angle, per unit projected area. |


## Solid angles

A solid angle is similar to the radian on a circle, a solid angle is the ratio of subtended area on sphere to radius squared. $\Omega = A / r^2$, a sphere has $4\pi$ steradians ($sr$). 

### Differential solid angles

The surface area of the unit sphere $S^2$ is

$$\Omega = \int_{S^2} d\omega = \int_0^{2\pi}\int_0^\pi \sin\theta d\theta d\phi = 4\pi$$

where $\omega = (\phi, \theta)$ is the unit length direction. Thus, the angular flux intensity is derived from the total emitted power as 

$$\Phi = \int_{S^2} Id\omega = 4\pi I, I = \Phi / 4\pi$$

## Irradiance

### Lambert's Cosine Law
Irradiance at surface is proportional to cosine of angle between light direction and surface normal. 

$$E = \frac{\Phi}{A} \cos\theta = \frac{\Phi}{A} \mathbf l \cdot \mathbf n$$

where $\mathbf l$ is the light direction and $\mathbf n$ is the surface normal. 

### Falloff

Assume that light is emitting flux $\Phi$ in a uniform angular distribution, then the intensity falloffs by squared radius. 

$$E_1 = \frac{\Phi}{4\pi}, E_r = \frac{\Phi}{4\pi r^2}, E_r = \frac{E_1}{r^2}$$

## Radiance

__radiance / luminance__ is the power emitted, reflected, transmitted or received by a surface, per unit solid angle, per unit projected area. 

$$L(\mathbf x, \omega) = \frac{\partial^2 \Phi}{\partial\omega \partial A \cos\theta} = \frac{\partial E}{\partial \omega \cos\theta} = \frac{\partial I}{\partial A \cos\theta}$$

Consider a opaque object surface, light will absorb, reflection, and refract on the surface. Thus, the incident radiance and exitant radiance are different. 

### Environment irradiance

For a given surface, the environment irradiance is the amount of flux received is the integral over incoming light from all directions.

$$E(\mathbf x) = \int_{H^2} L_i(\mathbf x, \omega) \cos\theta d\omega$$

note that $H^2$ is the hemisphere because $\cos\theta < 0$ for the over half. 

For a uniform area light source, the light irradiance on the surface is proportional to the projected area on the unit sphere, then projected onto surface tangent plane.

$$E(\mathbf x) = \int_{H^2} L_i(\mathbf x, \omega)\cos\theta d\omega = L\int_{\Omega}\cos\theta d\omega = L\text{proj}(\Omega)$$

Thus, for a disk area light of radius $r$ and $h$ units above the surface. The projection on the unit sphere is a circle of radius $\sin(\alpha) = \sin(\tan^{-1}(r/h))$. Thus $\text{proj}(\Omega) = \pi r^2 = \pi\sin^2(\alpha)$