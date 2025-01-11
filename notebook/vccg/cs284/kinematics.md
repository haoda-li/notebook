# Animation through Kinematics

[Kinematics with a concrete example](../csc418/kinematics.md)

## Data driven models (PCA)

Given a dataset of $n$ people scanning (point cloud) in the exact same pose 

$$\mathcal V = \{V_1, V_2,\cdots, V_n\}, V_i\in\mathbb R^{3\times |V_i|}$$

Reconstruct meshes based on the scanning so that they have the same topology and vertex semantics (for example, via remeshing). Then, the geometry (point positions) have the same cardinality, and all models are in $\mathbb R^{3\times |V|}$ space. Which means that we have a $n\times 3|V|$ matrix. We are interested in parameterizing human shapes via $m$ parameters, i.e. each sample $V_i$ can be represented by some basis function

$$\mathcal V \approx \bar{V} + \sum_{j=1}^m \beta_{j}\mathbf B_j$$

In other words, a mean $\bar V$ and variance components $\mathbf B_j$. Using principal component analysis, we can find a set of eigenvectors $\mathbf B_1, \mathbf B_2, ...$ and corresponding eigenvalues $\beta_1, \beta_2, ...$ s.t. the variables successively inherit the maximum possible variance from $\mathcal V$, or equivalently minimize residual errors ([Proof of equivalence](../csc311/pca.md)). 


## Forward Kinematics (Skeleton)

Skeleton is a hierarchical structure, often represented as a tree. Each bone is a line segment of length $l$ (or other shapes) with a joint and topology (connectivity). The joint defines the constraints of the local rotation and translation and the topology is represented by the edges in the skeleton tree. Joint is often of type **ball** (2 DoF rotation), **pin** (1 DoF rotation), or **prismatic** (translation). 

The transformation of each bone is the composition of the transformation of all its ancestors, i.e.

```py title="forward kinematics"
def transform(bone, skeleton):
    if bone is skeleton.root:
        return bone.Rt
    else:
        return bone.Rt @ transform(bone.parent, skeleton)
# note that we can precache the global transformation at each bone
# to prevent from repeating the computation
```

## Inverse Kinematics

Given a skeleton, a root transformation, a rest pose (initial configuration),  and some constraints on the leaf bone tips, or handles,  aim to find the interior parameter settings for all bones. 

Note that in most cases, the solution is not unique, or a solution does not exist. Therefore, the problem is often configured as an energy minimization problem. We want to write the current position as a function of joint parameters $\Theta$ and minimize the squared distance between handle positions and the bone positions, say $E(\Theta) = \|\mathbf p(\Theta) - \mathbf p^* \|^2$ under the constraints (on $\Theta$ and other terms). 

Note that there are multiple ways to formulate the objective function to achieve different constraints. For example

- __Multiple handles__ with different weights/importance 
  
    $$w_1\|\mathbf p_1(\Theta) - \mathbf p_1^*\|^2 + w_1\|\mathbf p_2(\Theta) - \mathbf p_2^*\|^2$$

- __Pointing at__ given a direction $\mathbf d$, asking the tip bone points at the direction

    $$E_{\mathbf d}(\Theta) = \|1 - \frac{\mathbf p_1(\Theta) - \mathbf p_1^*}{\|\mathbf p_1(\Theta) - \mathbf p_1^*\|}\cdot \mathbf d\|^2$$

- __Balancing__ given the mass of each bone $m_i$ and a supporting point $\mathbf s$ (either the center of the support polygon or a fixed joint on some bone), need to keep balance w.r.t. gravity. 

    $$E_{\text{balance}}(\Theta) = \|\frac{\sum_{i=1}^n m_i \mathbf c_i(\Theta)}{\sum_{i=1}^n m_i} - \mathbf s\|_{xy}^2$$

- __Keyframing__ given handle positions at some keyframes $t_1, t_2, ...$, want to find $\Theta(t)$ as a smooth function over time. To ensure smoothness, we can treat the keyframes as control points and interpolate in-between using curves, such as Bezier curve. 

$$\Theta(t) = \sum_j c_{ij}B_j(t)$$