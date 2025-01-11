# Defining Surfaces

## Topology Refresher

A subset $U$ of $\mathbb R^n$ is __open__ if $\forall a\in U. \exists \epsilon > 0. \forall u \in \mathbb R^n. \|u-a\|<\epsilon\implies u\in U$. 

A map $f: (X\subset \mathbb R^m)\rightarrow (Y\subset\mathbb R^n)$ if __continuous__ at $a\in X$ if 

$$\forall \epsilon > 0.\exists \delta > 0. \forall u\in X. \|u-a\| < \delta \implies \|f(u)-f(a)\| < \epsilon$$  

Equivalently, $f$ is continuous IFF for all open set $V\subset\mathbb R^n$, exists open set $U\subset\mathbb R^m$  s.t. $U\cap X = \{x\in X: f(x)\in V\}$.

$f$ is a __homeomorphism__ is it is continuous, bijective, and its inverse is also continuous, and $X,Y$ are homeomorphic. 

## Defining Surfaces

Suppose that we are trying to parameterize the surface of a unit sphere $\{x\in\mathbb R^3: \|x\| = 1\}$ with the xy-plane. Intuitively, if we pick the south pole on the sphere, map it to the origin, and then wrap the plane on the surface. Then, we will have one circle on the plane being map to the north pole ([Stereographic Projection](../mat334/functions.md#stereographic-projection)). However, we will lose regularity in this case as the derivative will be all 0. 

This is a very simple case, but from this we can see that a plane is not enough to parameterize all kinds of surfaces. Instead, we will locally parameterize surfaces by subsets of $\mathbb R^2$. i.e. for some surface $\Sigma$, for some open subset $V\subset \Sigma$, we are interested in some homeomorphism $f$ to map $U\subset\mathbb R^2$ to $V$. 


A subset $\Sigma\subset\mathbb R^3$ if a __surface__ if $\forall p\in \Sigma$, exists open subset $U\subset \mathbb R^2$ and open $V\in\mathbb R^3$ s.t. $p\in V$ and $V\cap \Sigma$ is homeomorphic to $U$.   
A __open subset__ of surface $\Sigma$ is defined as $\Sigma\cap V$ where $V\subset\mathbb R^3$ and open.  
A __surface patch__ of the open subset is a homeomorphism $\sigma: U\rightarrow \Sigma\cap V$.  
A __atlas__ is a finite collection of surface patches whose images $\cup_{i=1}^N(\Sigma\cap V_i) = \Sigma$

## Regular Surfaces
A surface is __regular__ if all of its surface patches in atlas is regular.  
A surface patch is regular if $\sigma$ is smooth and regular. i.e. For 
$\sigma(u, v) = (x(u,v), y(u,v), z(u,v))^T$, its Jacobian 

$$D\sigma = \begin{bmatrix}\partial_u x&\partial_vx\\\partial_uy&\partial_vy\\\partial_u z&\partial_vz\end{bmatrix}$$ 

has linearly independent columns (equivalently, rank = 2, $D\sigma$ is injective, exists 2 rows where the formed $2\times 2$ matrix is invertible). 

If a surface path $\sigma$ is regular. Then $\{\partial_u\sigma, \partial_v\sigma\}$ are linearly independent, hence can span a plane. For some fixed $(u_0, v_0)$, we have that 

$$D\sigma(u_0, v_0)\begin{bmatrix}a\\b\end{bmatrix} = a\frac{\partial\sigma}{\partial u}(u_0) + b\frac{\partial\sigma}{\partial v}(v_0)$$

is the tangent plane at $(u_0, v_0)$. Otherwise, we cannot span such plane, hence not regular. 

### Example: Image of 2D functions
A plane can be defined as $f(u,v) = \mathbf a+ u  \mathbf b+ v  \mathbf c$ where $\mathbf b, \mathbf c$ are linearly independent. Then, note that if we define $\sigma := f$ to be the surface patch from $U=\mathbb R^2$ to $V=\Sigma$, note that $\sigma = f$ is obviously bijective. In addition, $Df = [\mathbf b,\mathbf c]$ is linearly independent. Therefore, plane is a regular surface. 

Moreover, if we consider image of some differentiable function $f: U\subset\mathbb R^2\rightarrow V\subset\mathbb R$. Define $\sigma(u,v) = (u, v, f(u, v))$, given that $f$ is differentiable, $\sigma$ is obviously continuous and bijective, and 

$$D\sigma = \begin{bmatrix}1&0\\0&1\\\partial_uf&\partial_vf\end{bmatrix}$$

is obviously linearly independent. 

__Corollary.__ If $\Sigma$ is a surface, then $\forall p\in \Sigma, \exists V\subset \Sigma$ s.t. $p\in V, V$ is open and $V$ is the graph of anyone of $z = \psi(x,y), y = \varphi(x,z), x = \tau(x,y)$ where the mapping is smooth. Then, $\Sigma$ is regular. 

### Example: Sphere

Consider the unit sphere $\{(x,y,z) : x^2 + y^2 + z^2 = 1\}$. 

First, try $z = \pm\sqrt{1 - x^2 - y^2}$, and map from 2 circles to the upper and lower hemisphere. 

$$\sigma^z_1(u, v) = (u, v, \sqrt{1-u^2-y^2}), \sigma^z_2 = (u, v) = (u, v, -\sqrt{1-u^2-y^2})$$

However, since that square root is defined on $\mathbb R^{\geq 0}$ and we need that the domain of $\sigma$ be open, we have that 

$$U_1 = U_2 = \{(u, v): u^2 + v^2 < 1\}$$

Then, note that the circle $\{(x, y, 0): x^2 + y^2 = 1\}$ is not covered.   
Similarly, we can take 

$$\sigma^x_1(u, v) = ( \sqrt{1-u^2-y^2}, u, v), \sigma^x_2 = (u, v) = ( -\sqrt{1-u^2-y^2}, u, v)$$


$$\sigma^y_1(u, v) = (u,  \sqrt{1-u^2-y^2}, v), \sigma^y_2 = (u, v) = (u,  -\sqrt{1-u^2-y^2}, v)$$

Note that each pair alone is unable to cover the sphere.  
However, the six patches together can cover the sphere surface. 

However, if we consider the example at the very beginning, although one patch is not enough, it looks like that the plane should be able to cover the sphere with one circular open subset uncovered. If we have another patch to cover that subset, then the sphere can be covered with two patches. 

Consider some point $\mathbf a = (x, y, z)$ on the surface, and let $\mathbf b = (x, y, 0)$ be its projection on the xy-plane. Then, let 

$$\theta = \arccos(\mathbf a \cdot \mathbf b), \psi = \arccos(\mathbf b\cdot \mathbf e_1)$$

Therefore, we can have that 

$$\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}
\cos\theta\cos\psi\\
\cos\theta\sin\psi\\
\sin\theta
\end{pmatrix}, \theta\in[-\pi/2, \pi/2], \psi\in[0, 2\pi]$$

Then, since $U$ must be open, we can only take 

$$U_1 = \{(\theta, \psi): \theta\in(-\pi/2, \pi/2), \psi\in(0, 2\pi)\}$$

In this case, consider the uncovered parts: 

$$\psi = 0 = 2\pi\implies \begin{pmatrix}
\cos\theta\cos 0\\
\cos\theta\sin 0\\
\sin\theta
\end{pmatrix} = \begin{pmatrix}
\cos\theta\\
0\\
\sin\theta
\end{pmatrix}$$

$$\theta = \pm\pi/2 \implies \begin{pmatrix}
0\\
0\\
\pm\sin\psi
\end{pmatrix}$$

Therefore, the uncovered part is the upper semicircle $\{(x, 0, z): x \geq 0\}$ on the xz-plane.  
However, we can easily obtain another patch, where the uncovered part is the lower semicircle $\{(x, y, 0): x\leq 0\}$ by rotating $\sigma$ by $\pi$ along z-axis, and $\pi/2$ along x-axis. 

$$\sigma_2 = R_x(\pi/2)R_z(\pi)\sigma_1 = \begin{pmatrix}
\cos\theta\cos \psi\\
\cos\theta\sin \psi\\
\sin\theta
\end{pmatrix} = R_x(\pi/2)\begin{pmatrix}
-\cos\theta\cos \psi\\
-\cos\theta\sin \psi\\
\sin\theta
\end{pmatrix} = \begin{pmatrix}
-\cos\theta\cos \psi\\
-\sin\theta\\
-\cos\theta\sin \psi\\
\end{pmatrix}$$

### Example: Circular Cone (Not a Surface)
Note that each surface patch $\sigma$ maps from an open set of a plane to an open subset, and the map is invertible and continuous. Therefore, we can apply continuous mapping theorem. For any point $p\in \Sigma$ on the surface and some surface patch $\sigma$, the neighborhood of $p$ (or an open disk containing $p$) should be mapped to the neighborhood of its pre-image (an open disk containing $\sigma^{-1}(p)$). 

Consider the circular cone 

$$S = \{(x,y,z)\in\mathbb R^3: x^2 + y^2 = z^2\}$$

Let $\sigma: U\rightarrow V \cap S$ be a surface patch containing $p = (0, 0, 0)\in S$, $a = \sigma^{-1}(p)\in U$. Take $p_+,p_-$ in $p$'s neighborhood and $p_+$ in the upper cone $(z>0)$ and $p_-$ in the lower cone $(z<0)$, and $a_+, a_- \in U$ be the pre-image, respectively. 

Then, consider a continuous path $\gamma:[0, 1]\rightarrow V$ from $p_- = \gamma(0)$ to $p_+ = \gamma(1)$, we claim that $\gamma$ must pass through $p$. 

Let $\pi: \mathbb R^3\rightarrow\mathbb R, \pi(x,y,z) =z$, then $\pi\circ\gamma: [0, 1]\rightarrow\mathbb R$. Then we have $[\pi\circ\gamma](0) < 0, [\pi\circ\gamma](1) > 0$. By IVT, there exists some $[\pi\circ\gamma](t) = 0$, and since $\gamma([0, 1]) \subseteq S$, the only possible point with $z=0$ is $\gamma(t) = (0,0,0)$.

Therefore, by continuous mapping theorem, any path from $a_-$ to $a_+$ must pass through $a$, which violates the assumption that $U$ is an open set. 

Another similar example is two planes intersecting together. 

The takeaway here is that if we remove the point, the set has at least 2 connected components, then the set is not a surface. 
