# Shader Pipeline


## Viewing Transformations

<figure markdown>
  ![](./assets/view_transformation.png){width="720"}
</figure>


The viewing transformations inputs a canonical coordinate $(x, y, z)$ to some $(x, y)$ on the 2D image space. One common system is a sequence of 3 transformations
 - __camera transformation__ $(x, y, z)\rightarrow (x_c, y_c, z_c)$ given $eye$ and orientation $u, v, w$
 - __projection transformation__ $(x_c, y_c, z_c) \rightarrow (x_v, y_v)$, $x_v, y_v\in [-1, 1]$ all the points that  are visible in the camera space given the type of projection desired
 - __viewport transformation__ $(x_v, y_v)\rightarrow (I_x, I_y)$ maps the unit image rectangle to desired rectangle in pixel coordinates

### [Perspective Projections](http://www.songho.ca/opengl/gl_projectionmatrix.html)

## [Shader Pipeline (OpenGL)](https://www.khronos.org/opengl/wiki/Rendering_Pipeline_Overview)

__Vertex specification__  
Set up Vertex Array Object (VAO), which contains one or more Vertex BUffer Objects (VBO), each VBO stores some information about each vertex. For example, if we load a .obj file, then VAO (the object) may end up having several VBOs, for example, one VBO stores vertex positions, one VBO stores vertex colors, and another one stores vertex normals.

__Vertex shader__  
Performs operation on every vertex, doing all the homogeneous transformations, i.e.

 - $M$: modeling transformation: to move object into world space, doing all the translations, rotations, scaling, etc. 
 - $V$ viewing transformation/camera transformation: transforms from world coordinates to camera coordinates. 
 - $P$ perspective projection matrix, so that we only consider vertex in the window space (visible within the camera), and normalize $(x, y, z)$ by $w$.


__Tessellation__  
patches of vertex data are subdivided into smaller Primitives. Tessellation control shader (TCS) determines how much tessellation to do and 
tessellation evaluation shader (TES) takes the tessellated patch and computes vertex values for each generated vertex.  
For example Catmull–Clark subdivision can be a TCS/TES algorithm.

__Rasterization__  
Given the tessellated primitives, filled in the primitive with pixels. 

__Fragment shader__  
Given a sample-sized segment of a rasterized Primitive, fragment shader computes a set of colors and a single depth value. In our cases, it will be pixel-wise coloring.

Note that the shader pipeline is only for `OpenGL`. In other frameworks (`WebGL`, `DirectX`, etc.) the abstractions are different. For example, `WebGL` does not have support for tessellation and you have to do it in `js` (likely on CPU). 

```glsl title="vertex shader example"
--8<-- "csc418/assets/shaders.js:108:116"
```

```glsl title="fragment shader example"
// fragment shader using Blinn Phong shading
--8<-- "csc418/assets/shaders.js:2:5"

--8<-- "csc418/assets/shaders.js:141:154"
```

## Value Noise and Procedural Patterns
Other than a texture mapping, we can also generate patterns, i.e. procedural patterns. For example, if we want to make a ocean texture, we can generate some waves mesh and color it by some algorithm, instead of map a 2D image onto it. 

### Noise
Note that in reality, lots of patterns need some sort of "randomness", s.t. the volume of a cloud on the sky, the waves of the water, etc. 

#### Properties of Ideal Noise
 - __pseudo random__ Given the same input, it should always return the same value. 
 - __dimension__ The noise function is some $N:\mathbb R^d\rightarrow \mathbb R$, which is a $d$-dim noise function. 
 - __band limited__ One of the frequencies dominates all others. 
 - __continuity / differentiability__ We want the change in local is small, but change in global is large

### [Perlin Noise](https://en.wikipedia.org/wiki/Perlin_noise#Algorithm_detail)
Perlin noise is a example of value noise, it's pseudo random, and continuous, and good in producing marble like surfaces. 

#### Algorithm
__Grid Definition__  
Define an n-dim grid where each point has a random n-dim unit-length gradient vector. 

__Dot product__  
Assume $3D$ case and each box grid has side length 1. For query position $(x, y, z)$, it is located in some $d$-dim grid formed by $2^3$ grid points, $(\lfloor x\rfloor, \lceil x\rceil)\times (\lfloor y\rfloor, \lceil y\rceil)\times (\lfloor z\rfloor, \lceil z\rceil)$. Generate $2^d$ __dotGridGradient__ by dot product the offset to each grid point and gradient at that grid point. 

__Interpolation__  
Note that we have $2^3$ scale values, and we will have a trilinear interpolation so that we can get the value at that point.  
Note that we take a smooth step $s:\mathbb R^d\rightarrow \mathbb R^d$ as the coefficient of interpolation. $s$ must have the property $s(0) = s(1) = s'(0) = s'(1) = 0$, one good smooth step function is 

$$s(t) = 3t^2 - 2t^3$$

### Improved Perlin Noise
Note that $s''(t) = 6 - 12t$ is not continuous,  if the derivative of the function used to compute the normal of the displaced mesh is not continuous then it will introduce a discontinuity in these normals wherever $x=0, 1$, so that we use improved smooth step

$$6t^5 - 15t^4 + 10t^3$$

Also, note that when random directions (gradient direction) is close to standard direction $e_i$, the noise function have very high values $\sim1$ causing a "splotchy appearance", so instead of using random directions, we use directions randomly chosen from 12 directions $(\pm 1,\pm 1,0), (\pm 1, 0, \pm 1), (0, \pm 1, \pm 1)$


```glsl title="Random sampling from sphere"
--8<-- "csc418/assets/shaders.js:27:33"
```

```glsl title="Smooth step and improved smooth step"
--8<-- "csc418/assets/shaders.js:37:39"
// The improved version
--8<-- "csc418/assets/shaders.js:43:45"
```

```glsl title="Perlin noise from 3D Seed"
--8<-- "csc418/assets/shaders.js:48:71"
```

## Bump Mapping and Normal Mapping
The real surface is often rough and bumpy, we use bump mapping algorithm to achieve the same effect. 

$$\tilde p(p):\mathbb R^3\rightarrow\mathbb R^3 := p + h(p)\hat n (p)$$

where $p$ is the original position, $\hat n$ is the normal and $h$ is the bump height function. 

Then, note that we have to calculate a new normal for the bumped point as 

$$\tilde n(p) = \partial_Tp\times \partial_Bp \approx \frac{\tilde p(p +\epsilon T)-\tilde p(p)}{\epsilon} \times \frac{\tilde p(p +\epsilon B)-\tilde p(p)}{\epsilon}$$

where $T, B$ are the tangent and bitangent vector where 

$$T = \min\{\hat n \times (0, 1, 0),  \hat n \times (0, 0, 1)\}, B = T\times N$$

Note that bump mapping does not actually change the vertex position, it is used to obtain the normal mapping so that we can apply the coloring and make the surface looks "bumpy"

```glsl title="Using random bump to remap normal"
--8<-- "csc418/assets/shaders.js:217:227"
```

## Shader Demo

A demo of shaders, noise, and bump mapping

<iframe src="./assets/shaders.html" width="100%" height=480 />

???quote "Shader code"

    ```glsl
    // Shader programs are merely strings and are only 
    // loaded onto GPU
    --8<-- "csc418/assets/shaders.js"
    ```