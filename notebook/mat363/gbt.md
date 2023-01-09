# Gauss Bonnet Theorem

## GBT for simple closed curves

__Theorem__ Let $\gamma(s)$ be a unit-speed simple closed curve on a surface patch $\sigma$ of length $L$, and assume that $\gamma$ is positively orientaed. Then, 

$$\int_0^L \kappa_g ds = 2\pi - \int_{int(\gamma)}K dA_\sigma$$

where $\kappa_g$ is the geodesic curvature, $K$ is the Gaussian curvature. 

### Example

__Theorem__ Suppose that $\sigma$ has $K\leq 0$ everywhere. Prove that there are no simple closed geodesics on $\sigma$. 

_proof_. Suppose exists some simple closed geodesic $\gamma$, so that $\kappa_g = 0$, thus 

$$\int_{int(\gamma)} KdA_\sigma = 2\pi$$

If $K\leq 0$, then the integral will be negative, hence not possible. 

## GB for Curvilinear polygons
A __curvilinear polygon__ in $\mathbb R^2$ is a continuous map $\pi:\mathbb R\rightarrow\mathbb R^2$ s.t. for some real number $T$ and some points $0 = t_0 < t_1 < \cdots < t_n = T$, $\pi(t) = \pi(t')$ IFF $t'-t = kT$, $\pi$ is piece-wise smooth for each open interval $(t_i, t_{i+1})$. The one-sided derivatives exists and are non-zero and not parallel. The points are called vertices, and the intervals are edges. 

__Theorem__ Let $\gamma$ be positively oriented unit-speed curvilinear polygon with $n$ edges on a surface $\sigma$, and $a_1,..,a_n$ ne the interior angles at its vertices. Then, 

$$\int_0^L \kappa_g ds = \sum_{i=1}^n a_i - (n-2)\pi - \int_{int(\gamma)} K dA_\sigma$$


### Corollary 
If $\gamma$ is a curvilinear polygon with $n$ edges each of which is an arc of a geodesic, then the internal edges $a$'s of the polygon satisfy the equation, 

$$\sum_{i=1}^n a_i = (n-2)\pi - \int_{int(\gamma)} K dA_\sigma$$


### Example: Surface of Revolution
For $u_1 < u_2$ be constant, let $\gamma_1,\gamma_2$ be the two parallels at $u_1, u_2$ on $\sigma$, Let the region $U$ be the surface between the two parallel circles or length $L_1, L_2$. 

For surface of revolution, the normal is 

$$\mathbf N = (-g'\cos v, -g'\sin v, f')$$

Note that both $\gamma_1,\gamma_2$ are circles of radius $f(u_i)$, centered at $(0, 0, g(u_i))$, consider $\gamma_1$, 

$$\gamma_1'(v) = f(u_1)(-\sin v, \cos v, 0), \gamma_1'' = f(u_1) (-\cos v, -\sin v, 0)$$

Thus, we have the geodesic curvature

$$\kappa_g = \frac{\gamma''\cdot(\mathbf N\times \gamma')}{\|\gamma'\|^{3/2} } = \frac{f'(u_1)}{f(u_1)}$$


Then, we have 

$$\int_0^{L1} \kappa_g ds = \int_0^{2\pi f(u_1)} \frac{f'(u_1)}{f(u_1)} ds = 2\pi f'(u_1), \int_0^{L2} \kappa_g ds = 2\pi f'(u_2)$$


Then, note that the Gaussian curvature for surface of revolution is $K = -f''/f$, so that 

$$\iint_U K dA_\sigma = \int_0^{2\pi}\int_{f(u_1)}^{f(u_2)} f''/f dudv = 2\pi (f'(u_1) - f'(u_2))$$


Thus, we have that 

$$\int_0^{L1} \kappa_g ds - \int_0^{L2} \kappa_g ds = \iint_U K dA_\sigma $$


This follows GB for a curvilinear polygon with vertices $\sigma(u_1, v_0), \sigma(u_2, v_0)$

## GB for Compact Surfaces

A __triangulation__ of a surface $\Sigma$ is a collection of curvilinear polygons, each of which is contained, together with its interior, in one of the $\sigma_i(U_i)$ being a region in one of the surface patch in the atlas. Such that, 
- each point of $\Sigma$ is in at least on curvilinear polygon.
- each pair of curvilinear polygon are either disjoint, or intersection is a common edge or a common vertex. 
- each edge is an edge of exactly two polygons. 

### Euler Number
For a triangulation of a compact surface with finitely many polygons, the __Euler number__ is 

$$\chi = V-E+F$$


__Theorem__ for any triangulation of $\Sigma$, 

$$\int_\Sigma K dA = 2\pi \chi$$


__Corollary__ Euler number if independent of choice of triangulation. 

### Genus
A genus is obtained for gluing $g$ tori together, where $g$ is the number of holes. When $g=0$, we have a sphere, $g=1$ is a torus, and $g=2$ we get a "8" shaped surfaces. 

__Theorem__ $\chi(T_g) = 2 -2 g$ where $T_g$ is genus $g$.

__Corollary__ $\int_{T_g} KdA = 4\pi (1-g)$

__Theorem__ If a compact surface $\Sigma$ is diffeomorphic to the torus, then $\int_S KdA = 0$. 

_proof_. Take $g=1$ and apply the theorem. Also, since $\Sigma$ is compact, $K > 0$ for some points $p\in\Sigma$. 

__Theorem__ If $\Sigma$ is compact with $K>0$ everywhere. Then, $S$ is diffeomorphic to a sphere. 

_proof_. $\int_\Sigma KdA > 0\implies 1 - g > 0$, $g\in\mathbb N$ hence the only choice of $g$ is 0. 

Note that the converse is not necessarily true, since we can have $K=0$ for some points. 


