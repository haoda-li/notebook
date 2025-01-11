# 3D Transformations

## Properties of Transformations
Transformations such as translation, rotation, and scaling are represented as matrices using homogeneous coordinates. 

Applying transformation is equivalent to left multiply the matrix. 

Since matrix multiplication is a linear transformation. Applying a sequence of transformation is equivalent to left multiply them in the transformation order, hence transformations are associative and transformations can be composed. 

$$T_n T_{n-1} ... T_{1}x = (T_n T_{n-1} ... T_{1})x$$ 

Multiply its inverse will reverse the transformation (since $T^{-1}Tx = (T^{-1}T)$). 

Transformation order matters, since matrix multiplications are not communitive. 

### Common 2D Transformations

$T$ translation, $R$ rotation ==counterclockwise==, $S$ scale / reflection (when $s_x=-1$ or $s_y = -1$)

$$T(x, y) = \begin{bmatrix}
1&0&x\\0&1&y\\0&0&1
\end{bmatrix},
R(\theta) = \begin{bmatrix}
\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1
\end{bmatrix},
S(s_x, s_y) = \begin{bmatrix}
s_x&0&0\\0&s_y&0\\0&0&1
\end{bmatrix}$$

### Decomposing Transformations 

Since multiple transformations can be composed into one transformation, we can then decompose the matrix. 

- Eigen decomposition: $A = V \Lambda V^{-1}$ where $\Lambda$ is diagonal. Used to decompose scaling (as $\Lambda$).
- Singular value decomposition: $A = USV^T$ where $S$ is diagonal, $U, V$ are orthonormal. Used to decompose rotation (as $UV^T$) and scaling (as $S$).
- Polar decomposition $A = PRSR^T, PR = Q$ is a further decomposition of SVD. $P, R$ are orthonormal. Used to decompose rotation (as $P$ and scaling as $S$). 

## 3D Affine Transformations

An 3D affine transformation is of the form 

$$A = \begin{bmatrix}a&b&c&t_x\\e&f&g&t_y\\h&i&j&t_z\\0&0&0&1\end{bmatrix}$$ 

__translation__ is of the form 

$$T = \begin{bmatrix}1&0&0&t_x\\0&1&0&t_y\\0&0&1&t_z\\0&0&0&1\end{bmatrix}$$ 

__rotation__ is of the form 

$$R =\begin{bmatrix}\mathbf R&\mathbf 0\\\mathbf 0&1\end{bmatrix}, \mathbf R\in SO(3)$$

__scaling__ is of the form 

$$S = \begin{bmatrix}s_x&0&0&0\\0&s_y&0&0\\0&0&s_z&0\\0&0&0&1\end{bmatrix}$$

3D points is represented as $[x, y, z, 1]$ and vectors as $[x, y, z, 0]$.

For reverse transformation (inverse matrices). 
## Coordinate Systems

In general, a 3D coordinate system is defined by three ==normalized== vectors $\mathbf u, \mathbf v, \mathbf w$ and one origin point $\mathbf o$. Any transformation can be understood as transform a point/vector relative to the coordinate system. Alternatively, a transformation can be seen as a reverse transformation of the coordinate system relative to the point. 

The frame to world transformation is written as $\begin{bmatrix}\mathbf u & \mathbf v & \mathbf w & \mathbf o\\0&0&0&1\end{bmatrix}$ which transforms objects from the world coordinate system $[\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \mathbf 0]$ to the defined coordinate system.

## Representations of 3D Rotations

Geometrically, a 3D rotation rotates along a 3D-axis $(x, y, z)$ by $\theta$ degrees. 

### Euler Angle Rotation
Rotation around standard axes are 

$$R_x(a) = \begin{bmatrix}
1&0&0&0\\
0&\cos a&-\sin a &0\\
0&\sin a &\cos a&0\\
0&0&0&1
\end{bmatrix}, R_y(a) = \begin{bmatrix}
\cos a&0&\sin a&0\\
0&1&0&0\\
\sin a&0 &\cos a&0\\
0&0&0&1
\end{bmatrix}, R_z(a) = \begin{bmatrix}
\cos a&-\sin a&0&0\\
\sin a&\cos a&0 &0\\
0&0&1&0\\
0&0&0&1
\end{bmatrix}$$

Then, any rotation can be represented by $R = R_z(c)R_y(b)R_x(a)$, which is called __Euler angle__. ==The rotation order matters==. 

Euler angle is not a good representation because the same rotation cannot be uniquely defined. Also, there's gimbal lock problem, in which we lose degree of free when two rotation axis align. Also, the manifold is very ugly. 


### Rotation Around an Axis

Suppose we are rotating around $\mathbf w$. The first problem is that how we define the degree of rotation $\theta$, or what is $R_{\mathbf w}(0)$. 

The idea is to have $\mathbf w$ aligned to $\mathbf x$ and we can do $R_x$. Specifically, 

1. Rotate about $\mathbf x$-axis to put $\mathbf w$ into xy plane. 
2. Rotate about $\mathbf z$ to align $\mathbf w$ with $\mathbf x$.
3. Apply $R_x(\theta)$.
4. Reverse step 2 and 1 by matrix inverse (both are rotation so transpose).

### Rodrigues' Rotation Formula
The rotation around axis $\mathbf n$ by angle $\theta$ can be written into $3\times 3$ rotation matrix as

$$\mathbf R(\mathbf n, \theta) = \cos \theta \mathbf I + (1-\cos\theta)(\mathbf n\cdot \mathbf n) + \sin \theta [\mathbf n]_{\times}$$

$[\mathbf n]_{\times}$ is the cross product matrix. 

We can show that 

- $\mathbf R \cdot \mathbf n = \mathbf n$
- $\mathbf R e_1 = \cos \theta e_1 + \sin\theta e_2$
- $\mathbf R e_2 = -\sin\theta e_1 + \cos\theta e_2$

### Exponential Map

"Exponential" because of the matrix exponential form from Rodrigues' rotation formula. [More on rotation time derivatives](../csc419/../csc417/rotations.md)

Note that we can combine $\theta$ into the rotation axis as the scale $|\mathbf r\| = \theta$ so that the rotation can be compactly written as a 3D vector. Thus, it can be a "map". 

### Quaternions 

A more popular way derived from Rodrigues' is the quaternion, represented in 4 numbers. 

$$\mathbf q = (z_1, z_2, z_3, s) = iz_1 + jz_2 + kz_3 + s = (\mathbf z, s)$$

where $i,j,k$ are complex variables $i^2 = j^2 = k^2 = -1$ and $ij=k, jk=i, ki=j,ji=-k,kj=-i,ik=-j$

Following regular complex arithmetic, we define 

- dot product 

$$\mathbf q\cdot \mathbf p = (\mathbf z_q s_p + \mathbf z_p s_q + \mathbf z_p \times \mathbf z_q, s_ps_q - \mathbf z_p \cdot\mathbf z_q)$$

- conjugate: $\mathbf q^* = (-\mathbf z, s)$
- magnitude: $\|\mathbf q\|^2 = \mathbf q\cdot \mathbf q^* = \mathbf z\cdot \mathbf z + s^2$
- any real number vectors $\mathbf v_q = (\mathbf v, 0)$
- rotation as quaternions $\mathbf r =(\mathbf w\sin\frac{\theta}{2}, \cos\frac{\theta}{2})$
- rotating a vector $r^*\cdot \mathbf v_q\cdot \mathbf r^*$
- __composing rotations__ $\mathbf r = \mathbf r_1\cdot\mathbf r_2$

The reason behind quaternions is the great properties, it is "double unique" ($(\mathbf r, \theta) = (-\mathbf r, -\theta)$), the surface is a 3-sphere in 4D and its nice for interpolation. 

Note that these good properties are shared by exponential map, but compositing quaternions is easier. 

## Camera Model

We define camera as a coordinate system located at origin, the up direction is $+y$-axis, view direction is $-z$ axis, and right is $+x$-axis. Note that this definition is just by convention, the camera coordinates are defined differently depending on implementations. 

### Look at Transformation (c2w and w2c)

Like any 3D object, a camera are positioned into the world space by a rigid transformation 

$$K = \begin{bmatrix}\mathbf R&\mathbf t\\\mathbf 0&1\end{bmatrix} = \begin{bmatrix}
u_x&r_x&-v_x&e_x\\
u_y&r_y&-v_y&e_y\\
u_z&r_z&-v_z&e_z\\
0&0&0&1
\end{bmatrix}$$

where $\mathbf R = \mathbf u, \mathbf r, -\mathbf v$ rotates the camera coordinates right, up, view from $(\mathbf x, \mathbf y, -\mathbf z)$ to $(\mathbf u, \mathbf r, -\mathbf v)$ and $\mathbf t = \mathbf e$ translates camera from origin to $\mathbf e$. 

"look at" matrix transforms objects in the world coordinates to the camera coordinates, thus is the inverse of $K$, i.e. 

$$K^{-1} = \mathbf R^T(-T) = \begin{bmatrix}\mathbf R^T&\mathbf -R^Tt\\\mathbf 0&1\end{bmatrix}$$

### Perspective Projection

Consider the simple pinhole camera model, where camera is a point and we place the image plane in front of the camera with distance $d$. Every 3D point $(x,y,z)$ is projected onto the image plane as $(\frac{d}{z}x, \frac{d}{z}y, d)$. Which can be written in homogenous transformation 

$$M = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&d^{-1}&0\end{bmatrix}, M\begin{pmatrix}x\\y\\z\\1\end{pmatrix} = \begin{pmatrix}x\\y\\z\\\frac{z}{d}\end{pmatrix}\iff \begin{pmatrix}\frac{d}{z}x\\\frac{d}{z}y\\d\\1\end{pmatrix}$$

Then, note that the image plane cannot be infinitely large. In practice, we fix the size of the image plane and change $d$, or equivalently the focal length. When $d$ is small, we get a larger viewing angle. Also, we can define near $n$ and far $f$, which are two planes to clip the 3D space, we only render objects that falls within the range of $[n, f]$. 

To summarize, we have additional parameters for camera (rather camera models in graphics pipeline instead of the real camera). 

- $\text{FOV}_y$ the vertical angular field of view
- $w/h$ aspect ratio as width and height of the image plane / field of view
- $n, f$ the depth of near clipping and far clipping plane

From this we can derive the corners of the near clipping plane as top-left corner $(x_0, y_0, n)$ and bottom-right corner $(x_1, y_1, n)$ where 

$$y_0 = n \tan(\text{FOV}_y), y_1 = -y_0, x_1 = \frac{wy}{h}, x_0 = -x_1$$
  
### Normalized Device Coordinates (NDC)
Note that we can warp the volume in between near and far to a unit box, called __normalized device coordinates (NDC)__. This transformation will preserve the depth order and is defined as 

$$P = \begin{bmatrix}
n / x_1&0&0&0\\0&n / y_00&0&0\\0&0&\frac{f+n}{f-n}&\frac{2nf}{f-n}\\0&0&-1&0
\end{bmatrix}$$