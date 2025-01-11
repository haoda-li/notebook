# Ray Tracing and Acceleration Data Structure

## Viewing Rays

The 3D parametric line from the eye $\mathbf o\in\mathbb R^3$ to a point $\mathbf p\in\mathbb R^3$ is 

$$p(t) = \mathbf o + t(\mathbf p-\mathbf o) = \mathbf o + t \mathbf d$$

We advance from $\mathbf o$ along the vector $\mathbf d := \mathbf p-\mathbf o$ a fractional distance $t$ to find the point $\mathbf p$.  
$\mathbf e$ is the ray's origin and $\mathbf d$ is the ray's direction. 

### Basic Setup

Given a camera frame $\mathbf o$, i.e. the eye point or view point, and $\mathbf u, \mathbf v, \mathbf w$ for the basis. We specify that $-\mathbf w = view$, $\mathbf u$ points rightward from the $view$ and $\mathbf v$ points upward from the $view$. 

The viewing rays should start on the plane defined by the point $\mathbf o$ and the vectors $\mathbf u$ and $\mathbf v$; the only remaining information required is where on the plane the image is supposed to be. We'll define the image dimensions with four numbers,
for the four sides of the image: $l$ and $r$ are the positions of the left and right
edges of the image, as measured from e along the $\mathbf u$ direction; and $b$ and $t$ are the
positions of the bottom and top edges of the image, as measured from e along the
$\mathbf v$ direction. Usually $l < 0 < r$ and $b < 0 < t$.

Therefore, the pixel at $(i,j)$ in the raster image has the position 

$$u = l + (r-l)(i+0.5) / n_x; v = b + (t-b)(j + 0.5) / n_y$$

### Ray casting

For an orthographic view, the ray's origin is generated from the image and are parallel with each other. Therefore, given $u,v$

$$\mathbf d(u, v) = -\mathbf w, \mathbf o(u, v) = \mathbf o + u \mathbf u + v\mathbf v$$

For an perspective view, the ray's origin is the camera origin and rays have different directions. Therefore, given $u,v$

$$\mathbf d(u, v)= -\mathbf w + u\mathbf u + v\mathbf v, \mathbf o(u, v) = \mathbf o$$

<iframe src="./assets/camera_model.html" width="100%" height=480 />

## Ray Intersection

In general, we have the each ray as a line 

$$\mathbf r(t) = \mathbf o + t\mathbf d, t\in [0, \infty)$$

For some implicit surface represented by 0-level set $\{\mathbf p \in\mathbb R^3: f(\mathbf p) = 0\}$, we can substitute $\mathbf p = \mathbf r(t)$ and solves for real-positive roots for $t$. 

### Sphere
A sphere is represented by a center $\mathbf c= (x_c, y_c, z_c)$ and radius $r$, where 

$$f(\mathbf p) := \|\mathbf p-\mathbf c\|^2-r^2$$

so we can plug in $\mathbf p=\mathbf o+t\mathbf d$ and obtain the equation 

$$\|\mathbf o+t\mathbf d-\mathbf c\|^2-r^2 = 0$$

Note that this is a quadratic function about $t$, i.e. 

$$\mathbf d^T\mathbf d t^2 + 2\mathbf d^T(\mathbf o-\mathbf c)t + (\mathbf o-\mathbf c)^T(\mathbf o-\mathbf{c}) - r^2 = 0$$

let $A = \mathbf d^T\mathbf d, B = 2\mathbf d^T(\mathbf o-\mathbf c), C = (\mathbf o-\mathbf c)^T(\mathbf o-\mathbf{c}) - r^2$,   
Note that a ray must have two points intersect with a sphere, one point going inside and one going outside.  
Therefore, we need $B^2 - 4AC > 0$ and 

$$t = \frac{-B \pm \sqrt{B^2 - 4AC}}{2A}$$

And the normal vector and unit normal at $p$ is 

$$\mathbf n = \nabla f(\mathbf p) = 2(\mathbf p-\mathbf c), \hat{\mathbf n} = \frac{\mathbf n}{2r}$$

### Plane
A plane can be represented by an arbitrary point $\mathbf p_0$ and its normal $\mathbf n$ as 

$$f(\mathbf p) = (\mathbf p-\mathbf p_0)\cdot \mathbf n$$ 

since any vector lies on the plane should be perpendicular to the plane's normal. Therefore, we want to solve 

\begin{align*}
(\mathbf o+t\mathbf d - \mathbf p_0)\cdot \mathbf n &= 0\\
t &= \frac{(\mathbf p_0 - \mathbf o)^T \mathbf n}{\mathbf d^T\mathbf n}
\end{align*}

and the normal is just $\hat{\mathbf n} = \mathbf n/\|\mathbf n\|$

### Triangle
Triangle can be represented with 3 vertices $\mathbf a, \mathbf b, \mathbf c$, or the 3 corners.  
One way of implementing triangle intersection is to find the intersection point $\mathbf p=\mathbf o+t\mathbf d$ with the plane that the triangle lines on and then decide whether the point is within the triangle. However, we can also use barycentric coordinates where we solves 

$$\mathbf o + t\mathbf d = \mathbf a + \beta(\mathbf b-\mathbf a) + \gamma(\mathbf c-\mathbf a)$$

$$\begin{bmatrix}
x_a - x_b&x_a-x_c &x_d\\
y_a - y_b&y_a-y_c &y_d\\
z_a - z_b&z_a-z_c &z_d
\end{bmatrix}\begin{bmatrix}\beta\\\gamma\\t\end{bmatrix} = \begin{bmatrix}x_a-x_e\\y_a-y_e\\z_a-z_e\end{bmatrix}$$

if exists such $t, \beta, \gamma >0, \beta + \gamma < 1$, then there is an intersection.  
Then, the easiest way to solve such $3\times 3$ matrix is to use Cramer's rule.   
For $Ax = b$ where $A$ is $n\times n$ matrix, denote $A_i = A$ with the $i$th column being replaced by $b$, so that $x_i = \det(A_i) / \det(A)$. 

The normal is the plane's normal, i.e. can be obtained by any two vector's cross product. 

## BVH for ray intersections

[BVH implementations - AABB Tree](../csc418/bvh.md)

### Partition Heuristics 

A good partition aims to minimize the average cost of tracing a ray, which is proportional to the number of objects in the leaf node. Therefore, the average cost for ray tracing a BVH is the average cost of all triangles, weighted by the probability of hitting the object. 

If we assume uniform ray distribution with no occlusions, then the probability should be proportional to the surface area of the object. 