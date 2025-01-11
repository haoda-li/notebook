# Pose Parameterization and Optimization

Note based on [A tutorial on SE(3) transformation parameterizations and on-manifold optimization](https://arxiv.org/abs/2103.15980)[@blancoclaraco2022tutorial] and [SE(3) Geometry and Kinematics](https://natanaso.github.io/ece276a2019/ref/ECE276A_12_SE3.pdf)



In this note, unless specified, we are only interested in transformations in 3D. 


## Parametrize Rotations

The parameterization conventions are based on [`three.js`](https://threejs.org/docs) implementations. 

<iframe src="./assets/rotations.html" height=480 width="100%" />
A pose is just a rotation $\mathbf R$ and a translation $\mathbf t = (x, y, z)$, but the rotation can be parameterized in multiple ways with different pros and cons. 

### Euler Angles [:simple-threedotjs:](https://threejs.org/docs/?q=euler#api/en/math/Euler)

The rotation is parameterized by 3 Euler angles $\mathbf r = (r_x, r_y, r_z)$ and the rotation axis order (e.x. `xyz`, `roll-pitch-yaw`). Which means rotate around the first axis, and then the modified second axis, and finally the modified third axis. 

However, euler angle degenerates, a.k.a. one possible rotation can be represented by two different set of Euler angles. In practice, optimizations directly on Euler angle representation is not a good idea due to the rotation order and the degeneration problem. However, euler angle representation is easy to interpret, hence used as user input.

### Quaternions [:simple-threedotjs:](https://threejs.org/docs/?q=euler#api/en/math/Quaternion)


The rotation is parameterized by __normalized__ 4D vector $(q_x, q_y, q_z, q_r)$. A geometric interpretation is that of a rotation of $\theta$ radians around the axis $\mathbf v \propto (q_x, q_y, q_z)$, where the angle $\theta$ is $q_r = \cos(\frac{\theta}{2})$. 

Note that quaternions expects to be normalized, hence it also has only 3 degree of freedom despite of being 4D. 

### Rotation Matrices [:simple-threedotjs:](https://threejs.org/docs/?q=euler#api/en/math/Matrix4.extractRotation)

The __speicial orthogonal group__ $SO(3)$ is the set of all matrices $\mathbf{R}$ that is orthogonal ($\mathbf{R}^T\mathbf{R} = \mathbf{RR}^T = I$ or $\mathbf{R}^{-1}=\mathbf{R}$, orthogonal also implies invertible) and $\det(R)= 1$. Matrices in $SO(3)$ are __rotation matrices__, which are isometric (the transformation preserves distance).

The __special Euclidean group__ $SE(3)$ is the set of all __rigid transformation matrix__ in the form 

$$\mathbf{T} = \begin{pmatrix}&&&t_x\\&\mathbf{R}&&t_y\\&&&t_z\\0&0&0&1\end{pmatrix}$$

which is the homogeneous transformation of $\mathbf{R}\mathbf x + \mathbf t$.

## Conversions 



### Euler Angles to Quaternions

Given Euler angle $(r_x, r_y, r_z)$ and the order `XYZ`, the quaternion is 

\begin{align*}
q_x &= \sin(r_x/2) \sin(r_y/2) \sin(r_z/2) + \cos(r_x/2) \sin(r_y/2) \sin(r_z/2)\\
q_y &= \cos(r_x/2) \sin(r_y/2) \cos(r_z/2) - \sin(r_x/2) \cos(r_y/2) \sin(r_z/2)\\
q_z &= \cos(r_x/2) \cos(r_y/2) \sin(r_z/2) + \sin(r_x/2) \sin(r_y/2) \cos(r_z/2)\\
q_r &= \cos(r_x/2) \cos(r_y/2) \cos(r_z/2) - \sin(r_x/2) \sin(r_y/2) \sin(r_z/2)\\
\end{align*}

???quote "Quaternion.setFromEuler"
    ```js
    setFromEuler(euler) {
      const cos = Math.cos;
      const sin = Math.sin;

      const c1 = cos( x / 2 );
      const c2 = cos( y / 2 );
      const c3 = cos( z / 2 );

      const s1 = sin( x / 2 );
      const s2 = sin( y / 2 );
      const s3 = sin( z / 2 );

      switch ( order ) {

        case 'XYZ':
          this._x = s1 * c2 * c3 + c1 * s2 * s3;
          this._y = c1 * s2 * c3 - s1 * c2 * s3;
          this._z = c1 * c2 * s3 + s1 * s2 * c3;
          this._w = c1 * c2 * c3 - s1 * s2 * s3;
          break;

        // Other order see original code
        ...
      }
      return this;
    }
    ```

### Euler Angles to Matrix

Since applying a rotation transformation is equivalent to right-side multiplication of a rotation matrix, as of the Euler angle rotation definition, it can be composed of 3 matrices. 

$$
\mathbf{R}_X(\theta) = \begin{bmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{bmatrix}
\mathbf{R}_Y(\theta) = \begin{bmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{bmatrix}
\mathbf{R}_Z(\theta) = \begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}
$$

$$\mathbf R(r_x, r_y, r_z) = \mathbf{R}_Z(r_z)\mathbf{R}_Y(r_y)\mathbf{R}_X(r_x)$$

???quote "Matrix4.makeRotationFromEuler"
    ```js
    makeRotationFromEuler(euler) {

      const te = this.elements;

      const x = euler.x, y = euler.y, z = euler.z;
      const a = Math.cos(x), b = Math.sin(x);
      const c = Math.cos(y), d = Math.sin(y);
      const e = Math.cos(z), f = Math.sin(z);

      switch ( order ) {

        case 'XYZ':

          const ae = a * e, af = a * f, be = b * e, bf = b * f;

          te[0] = c * e;
          te[4] = - c * f;
          te[8] = d;

          te[1] = af + be * d;
          te[5] = ae - bf * d;
          te[9] = - b * c;

          te[2] = bf - ae * d;
          te[6] = be + af * d;
          te[10] = a * c;

          break;

        // Other order see original code
        ...
      } 

      return this;
    }
    ```

### Quaternion to Matrix

$$R(q_x, q_y, q_z, q_r) = \begin{bmatrix}
q_r^2 + q_x^2 - q_y^2 - q_z^2 & 2(q_xqy - q_r q_z) & 2(q_zq_x + q_rq_y)\\
2(q_xq_y + q_rq_z) & q_r^2 - q_x^2 + q_y^2 - q_z^2 & 2(q_yq_z - q_rq_x)\\
2(q_zq_x - q_rq_y) & 2(q_yq_z + q_rq_x) & q_r^2 - q_x^2 - q_y^2 + q_z^2
\end{bmatrix}$$

???quote "Matrix4.makeRotationFromQuaternion"
    ```js
    makeRotationFromQuaternion(q) {
      const te = this.elements;

      const x = q.x, y = q.y, z = q.z, w = q.w;
      const x2 = x + x,	y2 = y + y, z2 = z + z;

      // careful that xx = 2 * x * x instead of x * x
      const xx = x * x2, xy = x * y2, xz = x * z2;
      const yy = y * y2, yz = y * z2, zz = z * z2;
      const wx = w * x2, wy = w * y2, wz = w * z2;

      // q is normalized x*x+y*y+z*z+r*r = 1
      te[ 0 ] = ( 1 - ( yy + zz ) );
      te[ 1 ] = ( xy + wz );
      te[ 2 ] = ( xz - wy );

      te[ 4 ] = ( xy - wz );
      te[ 5 ] = ( 1 - ( xx + zz ) );
      te[ 6 ] = ( yz + wx );

      te[ 8 ] = ( xz + wy );
      te[ 9 ] = ( yz - wx );
      te[ 10 ] = ( 1 - ( xx + yy ) );
    }
    ```

### Matrix to Quaternion

In general, the matrix can be converted into quaternion as 

\begin{align*}
q_x &= \frac{R_{32}-R_{23}}{4q_r}\\
q_y &= \frac{R_{13}-R_{31}}{4q_r}\\
q_z &= \frac{R_{21}-R_{12}}{4q_r}\\
q_r &= \frac{\sqrt{1 + R_{11} +R_{22} + R_{33}}}{2}
\end{align*}

Notice that if $tr(R) = R_{11} +R_{22} + R_{33} < -1$ then the formulas is invalid. Therefore, we need to identify which major diagonal element has the greatest value. 

Therefore, it's divided into 4 cases. 

- The trace is good. Then we use the formula above
- $R_{11}$ is the largest, then

\begin{align*}
    q_x &= \frac{\sqrt{1 + R_{11} - R_{22} - R_{33}}}{2} \\
    q_y &= \frac{R_{12} + R_{21}}{4q_x}\\
    q_z &= \frac{R_{13} + R_{31}}{4q_x}\\
    q_r &= \frac{R_{32} - R_{23}}{4q_x}
\end{align*}

- $R_{22}$ is the largest, then

\begin{align*}
    q_x &= \frac{R_{12} + R_{21}}{4q_y} \\
    q_y &= \frac{\sqrt{1 + R_{11} - R_{22} - R_{33}}}{2} \\
    q_z &= \frac{R_{23} + R_{32}}{4q_y}\\
    q_r &= \frac{R_{13} - R_{31}}{4q_y}
\end{align*}

- $R_{33}$ is the largest, then

\begin{align*}
    q_x &= \frac{R_{13} + R_{31}}{4q_z}\\
    q_y &= \frac{R_{23} + R_{32}}{4q_z}\\
    q_z &= \frac{\sqrt{1 + R_{11} - R_{22} - R_{33}}}{2} \\
    q_r &= \frac{R_{21} - R_{12}}{4q_z}
\end{align*}


???quote "Quaternion.setFromRotationMatrix"
    ```js
    setFromRotationMatrix( m: Matrix4 ) {
      // Assume m is 4x4 transformation matrix and
      // the upper 3x3 of m is a pure rotation matrix (i.e, unscaled)
      
      const te = m.elements,
        m11 = te[ 0 ], m12 = te[ 4 ], m13 = te[ 8 ],
        m21 = te[ 1 ], m22 = te[ 5 ], m23 = te[ 9 ],
        m31 = te[ 2 ], m32 = te[ 6 ], m33 = te[ 10 ],
        trace = m11 + m22 + m33;

      if ( trace > 0 ) {

        const s = 0.5 / Math.sqrt( trace + 1.0 );

        this._w = 0.25 / s;
        this._x = ( m32 - m23 ) * s;
        this._y = ( m13 - m31 ) * s;
        this._z = ( m21 - m12 ) * s;

      } else if ( m11 > m22 && m11 > m33 ) {

        const s = 2.0 * Math.sqrt( 1.0 + m11 - m22 - m33 );

        this._w = ( m32 - m23 ) / s;
        this._x = 0.25 * s;
        this._y = ( m12 + m21 ) / s;
        this._z = ( m13 + m31 ) / s;

      } else if ( m22 > m33 ) {

        const s = 2.0 * Math.sqrt( 1.0 + m22 - m11 - m33 );

        this._w = ( m13 - m31 ) / s;
        this._x = ( m12 + m21 ) / s;
        this._y = 0.25 * s;
        this._z = ( m23 + m32 ) / s;

      } else {

        const s = 2.0 * Math.sqrt( 1.0 + m33 - m11 - m22 );

        this._w = ( m21 - m12 ) / s;
        this._x = ( m13 + m31 ) / s;
        this._y = ( m23 + m32 ) / s;
        this._z = 0.25 * s;

      }

      return this;

    }
    ```

## Operations on Rotations

For most operations, again we only consider quaternions and matrices. 

### Pose Composition

For compositing two transformation matrices, it's simply right-side multiplication $T_2 T_1$. 

For quaternions, applying a rotation on a 3D point can be effectively applied by first converting to a matrix, and then matrix multiplication. Therefore, the only useful operation is to composing two quaternions rotations. 

For quaternions $\mathbf{q}_1, \mathbf{q}_2$, its multiplication is defined as 

$$\mathbf{q}_1 \cdot \mathbf{q}_2 = \begin{pmatrix}
q_x = q_{r1}q_{x2} + q_{r2}q_{x1} + q_{y1}q_{z2} - q_{y2}q_{z1}\\
q_y = q_{r1}q_{y2} + q_{r2}q_{y1} + q_{z1}q_{x2} - q_{z2}q_{x1}\\
q_z = q_{r1}q_{z2} + q_{r2}q_{z1} + q_{x1}q_{y2} - q_{x2}q_{y1}\\
q_r = q_{r1}q_{r2} - q_{x1}q_{x2} - q_{y1}q_{y2} - q_{z1}q_{z2}
\end{pmatrix}$$

???quote "Quaternion.multiplyQuaternions"
    ```
    multiplyQuaternions( a, b ) {

      // from http://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/code/index.htm

      const qax = a._x, qay = a._y, qaz = a._z, qaw = a._w;
      const qbx = b._x, qby = b._y, qbz = b._z, qbw = b._w;

      this._x = qax * qbw + qaw * qbx + qay * qbz - qaz * qby;
      this._y = qay * qbw + qaw * qby + qaz * qbx - qax * qbz;
      this._z = qaz * qbw + qaw * qbz + qax * qby - qay * qbx;
      this._w = qaw * qbw - qax * qbx - qay * qby - qaz * qbz;

      return this;

    }
    ```

### Inverse
For transformation matrix, the inverse is simply the inverse of the matrix, and we know that rotation matrices are orthogonal, hence the inverse is the transpose.

For quaternions, thinks about the geometric interpretation. We can rotate the object along the opposite axis the same radians. Therefore, define the __conjugate__ of the quaternion as $\mathbf q^* = (-q_x, -q_y, -q_z, q_r)$, and the conjugate is the inverse rotation. 

## Pose Optimizations 

The key problem for pose optimization is essentially find a smooth path s.t. the source camera pose $P_{s}$ can be moved to the goal pose $P_d$. 

Geometrically speaking, the path is a sequence of infinitely small delta transformation $T_0, T_1, T_2, ... \in SE(3)$, where each transformation $P_i = T_i T_{i-1}...T_0P_s$ moves closer to and eventually become $P_d$. 

### Lie Groups

Let $G$ be a set of elements and consider a binary operation (often understood as multiplication). For any two elements $A,B\in G$, denote the result of the multiplication as $AB$. Then, $G$ plus the operation is a __group__ if the following properties are satisfied

- __Closure__ $\forall A, B\in G. AB\in G$
- __Associativity__ $\forall A,B,C\in G. (AB)C=A(BC)$
- __Identity__ $\exists I\in G. \forall A\in G. IA=AI=A$
- __Inverse__ $\forall A\in G. \exists A^{-1}\in G. AA^{-1} = A^{-1} A = I$

A __manifold__ $M$ is a topological space s.t. $\forall p\in M$, its neighborhood is a homeomorphism. Intuitively, it means that for any point on the manifold, there's an infinitely small neighborhood that is "flat". 
  
Consider a paper, the paper is a 2D manifold embedded in 3D space. However, if we fold the paper to form a "sharp" edge, it's no longer a manifold. 

Denote the __tangent space__ of manifold $M$ at point $p$ as $T_pM$ can be intuitively defined as the vector space of the derivatives at $p$ of all possible smooth curves on $M$ that pass through $p$. 

Finally, a __Lie group__ $G\subset \mathbb R^n$ is 
- a group 
- a manifold
- the multiplication operation and inverse operation are both smooth. 

### SE(3) and SO(3) as Lie Groups

For our purpose, we notice that SE(3) is a 6D manifold (3 degree of freedom for rotation and 3 for translation) since 

- The product of 2 SE(3) matrices is still in SE(3). 
- The products of SE(3), a.k.a. matrix multiplications, are associative
- Exists the identity matrix $I:=[\mathbf I_3 \mid \mathbf 0_3]$
- Exists inverse transformation $[\mathbf R\mid \mathbf t]^{-1} = [\mathbf R^T\mid -\mathbf R^T \mathbf t]$
- The product and the inverse are continuous w.r.t. each of the element.

Similarly, $SO(3)$ is also a 3D manifold and another Lie group. 

Intuitively, we confirm that the pose optimization problem is an optimization over a smooth manifold. 

### Lie Algebra 

A __Lie algebra__ is a vector space $V$ over some field $F$ with a binary operation $[\cdot, \cdot]$ (called a __Lie bracket__) associated with every Lie group. The Lie bracket satisfies that $\forall X, Y, Z \in V, \forall a, b\in F$

- __Closure__ $[X, Y] \in V$
- __Bi-linearity__ $[aX+bY, z] = a[X,Z] + b[Y,Z], [Z,aX+bY] = a[Z,X]+b[Z,Y]$
- __Alternating__ $[X, X] = 0$
- __Jacobi identity__ $[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0$

An __exponential map__ maps elements from the Lie algebra to the Lie group (manifold) and determines the local structure of the manifold, and a __logarithm map__ maps elements from the manifold to the algebra. 

### Lie Algebra of SO(3)

Note that for rotations, local changes can be well-represented by the Euler angles. Therefore, let the Lie algebra of SO(3) be the space of 

$$so(3) := \{\mathbf{r}_{\times} \in\mathbb R^{3\times 3} | \mathbf r\in\mathbb R^{3}\}$$

the exponential map is 

$$\mathbf R = \exp(\mathbf r_{\times}) = \sum_{k=0}^\infty \frac{1}{k!}\mathbf r_{\times}^k = I + \mathbf r_{\times} + \frac{1}{2!} \mathbf r_{\times}^2 +  \frac{1}{3!}\mathbf r_{\times}^3 + \cdots$$

__Rodrigues Formula__ gives the closed-form expression

$$\mathbf R = \mathbf I_3 + \frac{\sin \|\mathbf r\|}{\|\mathbf r\|}\mathbf r_{\times} + \frac{1 - \cos \|\mathbf r\|}{\|\mathbf r\|^2}\mathbf r_{\times}^2$$

Therefore, any local linear change to $\mathbf r$ can be mapped to rotation matrices $\mathbf R$. Practically, we can parameterize the delta transformation as 6D vector $(\mathbf r, \mathbf t)$ and optimize them separately.

??? quote "exp_map_SO3"
    ```python
    def skew_sym_mat(r):
      """ take a 3D vector, return its skew symmetric matrix 
      """
      r_x, r_y, r_z = r
      return torch.tensor([
        [   0, -r_z,  r_y],
        [ r_z,    0, -r_x],
        [-r_y,  r_x,   0]
      ])

    def exp_map_SO3(r):
      """ take a so(3) tangent vector r, return SO(3) rotation matrix R
      """
      
      r_skew = skew_sym_mat(r)
      r_norm = torch.norm(r)
      r_norm_inv = 1.0 / r_norm

      R = torch.eye(3)
      R += r_norm_inv * r_norm.sin() * r_skew
      R += r_norm_inv * r_norm_inv * (1.0 - r_norm.cos()) * (r_skew @ r_skew)
      return R
    ```

### Lie Algebra of SE(3)

Alternatively, we jointly optimize 6 parameters over the 6D manifold. 

$$se(3) := \big\{\xi_{\times} = \begin{bmatrix}\mathbf{r}_{\times} &\mathbf t\\\mathbf 0&0\end{bmatrix} \in\mathbb R^{4\times 4} | \xi = (\mathbf r,\mathbf t)\in\mathbb R^{6}\big\}$$

The exponential map and Rodrigues formula is given as 

$$T = \exp(\xi_{\times}) = \sum_{k=0}^\infty \frac{1}{k!} \xi_{\times}^k = \mathbf I_4 + \xi_{\times} + \frac{1-\cos(\|\mathbf r\|)}{\|\mathbf r\|^2}\xi_{\times}^2 + \frac{\|\mathbf r\|-\sin(\|\mathbf r\|)}{\|\mathbf r\|^3}\xi_{\times}^3$$

Note that the exponential map is consisted of the rotational exponential map and a translation

\begin{align*}\exp(\xi_{\times}) &= \begin{bmatrix} \exp(\mathbf r_{\times}) & J_L(\mathbf r) \mathbf t \\\mathbf 0 & 1\end{bmatrix}\\
J_L(\mathbf r) &= \sum_{k=0}^\infty \frac{1}{(k+1)!}\mathbf r_{\times}^k = \mathbf I_3 + \frac{1 - \cos(\|\mathbf r\|)}{\|\mathbf r\|^2}\mathbf r_{\times} + \frac{\|\mathbf r\| - \sin(\|\mathbf r\|)}{\|\mathbf r\|^3} \mathbf r_{\times}^2
\end{align*}

??? quote "exp_map_SE3"
    ```python
    def left_jacobian(r):
      """ take a so(3) tangent vector r, return 
      the left jacobian matrix
      """
      J = torch.eye(3)
      r_norm = torch.norm(r)
      r_norm_inv = 1.0 / r_norm
      r_skew = skew_sym_mat(r)

      J += r_norm_inv ** 2 * (1.0 - r_norm.cos()) * r_skew
      J += r_norm_inv ** 3 * (r_norm - r_norm.sin()) * (r_skew @ r_skew)
      return J


    def exp_map_SE3(xi):
      """ take a se(3) tangent vector xi = (r, t), return SE(3) transformation matrix T
      """
      r = xi[:3]
      t = xi[3:]
      T = torch.eye(4)
      T[:3, :3] = exp_map_SO3(r)
      J = left_jacobian(r)
      T[:3, 3] = J @ t
      return T
    ```