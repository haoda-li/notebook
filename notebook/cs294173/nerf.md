# Neural Radiance Fields

volumetric rendering, fields(3d representation) and sampling

plenoptic function

explain what's the set of all things that we can ever see? 

what people see what be seen as a function

$\theta, \phi$ viewing direction
$\lambda$ wavelength
$t$ time
$V_{x,y,z}$ position of the eye

total 7D

The objective is to recreate the visual reality (image based rendering / novel view synthesis)

remove time and wavelength, directly output RGB


## NeRF
change plenoptic function from viewing centered to object centered (object emits light instead of eye receiving light). If we discretize the space, then each grid is a sphere. 

## Lightfield / Lumigraph 1996
approach for modeling the plenoptic function. Take pictures from many views. Problem: 3D consistency, also assume that the ray shouting out from a pixel is never occluded. Thus only the plenoptic surface (You cannot flip the viewing direction).

## vs MVS
MVS wants the surface, struggles on thin, amorphous, shiny objects (pbr). 

## Analysis by Synthesis
A theory of shape by shape carving (2000) Kultulakos and Seitz

better modeling of light helps recover sharper surfaces.

## Positional encoding

since MLP is differentiable, but the image is not (edges have high frequency, sharp change), Fourier features. 

locality and smoothness

spherical functions: direction to rgb. Replace RGB branch with spherical harmonics coefficients. Analytic, simplify the learning, and make training cheap. 

One end, grid with linear interpolation and use SH to represent spherical functions at each grid location. The other end, MLP everywhere.

Takeaway, MLP is a very effective interpolator. 

## Compression on fields

sparse grid (plenvoxl), low rank (tensorRF, MN -> M + N), dictionary (instant-ngp)

## Sampling

aliasing (mipnerf) and speed (reduce #points per query by remove the empty space) problems.

many early papers sparse array, instantngp occupacy grid checking, mipnerf360 proposal network (tiny MLP that learns the weights $w_i$) 


Issues of evaluation. 