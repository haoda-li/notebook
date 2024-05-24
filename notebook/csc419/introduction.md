# Introduction


## Curves
### Parametric Equation
Represent the curve as the image of some function $\vec p:\mathbb R\rightarrow \mathbb R^2$. For example $\vec p(t) = (\cos(t), \sin(t))$ is the curve of a circle of radius 1

### Implicit Equation
Represent the curve as the level set of some function, i.e. for some $C\in\mathbb R. g:\mathbb R^2\rightarrow\mathbb R^1$, the curve is $\{(x, y) \mid g(x, y) = C\}$. For example $\{(x, y)\mid x^2 + y^2 - 1= 0\}$ be the curve of a circle  of radius 1.

## Surfaces

### Functional Surface
Consider a function $f:\mathbb R^2\rightarrow \mathbb R$, the surface is the image of $f$. of a __height field__. However, in this case, we cannot represent a perpendicular surfaces parallel to the z-axis. 

### Parametric Equation
Similar to a parametric curve, we can represent a surface as the image of $S:\mathbb R^2 \rightarrow \mathbb R^3$. If we can draw a map from parametric domain to 3D on the small neighborhood of each point (other than the boundary), we call it a __manifold__ (not very topologically definition of the manifold).

### Implicit Equation
Define $g:\mathbb R^3\rightarrow \mathbb R$, then the curve is the level set of $g$, i.e. $\{(x, y, z) \mid g(x, y, z) = C\}$

## Tangent and normal

### For Curves
For a parametric curve, the tangent $\frac{\partial \vec p}{\partial t} = \vec t$ and unit tangent $\hat t = \frac{\vec t}{ \|\vec t\|}$ represents the direction to which stay as on a curve.  

For an implicit curve, the normal $\nabla g$ and the unit normal $\hat n = \frac{\nabla g}{\|\nabla g\|}$ represents the direction to get off the curve.  
Note that $\hat n \cdot \hat t = 0$, i.e. the tangent and normal are perpendicular.

### For Surfaces
The normal is  still $\nabla g$ and the unit normal $\hat n = \frac{\nabla g}{\|\nabla g\|}$.  

However, the tangent is now a space or a plane in 2D, $\{\hat t \mid \hat t\cdot \hat n = 0\}$, For a parametric curve, the two easy tangent line is $\hat t_1 = \frac{\partial S}{\partial u}$ and $\hat t_2 = \frac{\partial S}{\partial v}$, and the tangent plane is then spanned by $\hat t_1, \hat t_2$, if we have $\hat t_1\cdot \hat t_2 = \pm 1$, i.e. $\partial_uS = c\:\partial_vS$, then it is a __degenerate__ point, i.e. at that point, it is a curve instead of a surface. 

## Geometry + Topology
A surface is then defined by geometry and topology. 

Some properties that defines geometry and topology

| Geometry | Topology |
| --- | --- |
| position | closed-ness|
| tangent / normals | orientable |
| dimension |number of boundaries <br> (ex. calendar has 2 boundaries)|
| "curvature" | number of (topological) holes <br> (ex. a donut has one hole) |
| self-intersection |


## Discrete Topology
Note that in computer science world, there is no actual "continuous" space, so we need some discrete methods. 
