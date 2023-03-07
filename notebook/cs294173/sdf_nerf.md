# Surface based Volume Rendering

[SDF Studio Github Repo](https://github.com/autonomousvision/sdfstudio) is a unified framework for SDF-based volume rendering. 

## SDF based Volume Rendering

The works are aiming to solve the problem that given a set of images $\{I_k\}$ of a 3D object, aim to output the surface $S$ as a level-set of some field $f: \mathbb R^3\rightarrow \mathbb R$. $f$ can be SDF field which maps position $\mathbf x$ to signed distance to the closest surface, or an occupancy field that maps $\mathbf x$ to a probability $[0,1]$ s.t. $\mathbf x$ is inside of outside of the volume. 


### NeuS

[NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction](https://lingjie0206.github.io/papers/NeuS/)

Represents a scene as SDF field $f_\theta(\mathbf x)$ and radiance field $c(\mathbf x, \mathbf d)$. Both approximated by separate MLPs.

Note that volume rendering is modelled by 

$$C(\mathbf r) = \int_{t_n}^{t_f} T(t)\sigma(\mathbf r(t)) \mathbf c(\mathbf r(t), \mathbf d)dt$$

where $T$ is the accumulated transmittance and $\sigma: \mathbb R^3 \rightarrow [0,1]$ is the volume density (estimated from MLP in NeRF). Then, the issue is that how do we get $\sigma$ from SDF. The idea is to uses a logistic density distribution to map the signed distance $\mathbb R\rightarrow [0, 1]$, i.e.

$$\sigma(\mathbf x) = \phi_s(f_\theta(\mathbf x)) = \phi_s(x) = \frac{se^{-sx}}{(1+e^{-sx})^2}$$

However, in this case $T(\mathbf x)\sigma(\mathbf x)$ is biased to positive SDF value instead of the zero-level set, thus we should re-design the density $\rho(t)$ s.t. 

$$T(t) = \exp(-\int_0^t \rho(u)du), T(t)\rho(t)$$

With some derivation (see the paper), we have that 

$$\rho(t) = \max(\frac{-d_t\Phi_s(f(\mathbf r(t)))}{\Phi_s(f(\mathbf r(t)))}, 0)$$

where $\Phi_s$ is the cdf of logistic distribution. 

### VolSDF
[Volume Rendering of Neural Implicit Surfaces](https://lioryariv.github.io/volsdf/)

In VolSDF, the volume density is represented from SDF as 

$$\sigma(\mathbf x) = \alpha \Psi_\beta(f(\mathbf x)), \Psi_\beta(s) = \begin{cases}\frac{\exp(s/\beta)}{2}&s\leq 0\\1-\frac{\exp(-s/\beta)}{2}&s>0\end{cases}$$

where $\Psi_\beta$ is the CDF of Laplace distribution with $0$ mean and $\beta$ scale. and $\alpha > 0, \beta > 0$ __are learnable parameters__.

VolSDF proposes a novel sampling method based on SDF, that requires significantly smaller sampling points for each ray. 



Given $\beta$ and a wanted error bound $\epsilon$ (typically $\epsilon = 0.1$) on the opacity. The algorithm aims to get a set of sample from $[0, M]$ (near, far) such that the opacity approximation error is bounded by $\epsilon$. The detailed algorithm and proofs are provided in the paper. 

### UniSurf

[UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction](https://moechsle.github.io/unisurf/)

UniSurf uses occupancy field $o$ s.t. $o(\mathbf x)=0$ when outside of the volume and $o(\mathbf x)=1$ when inside of the volume. Note that the surface normal $\mathbf n(\mathbf x) = \nabla_{\mathbf x} o / \|\nabla_{\mathbf x} o\|$. Then, we replace volume density $\sigma$ with occupancy and estimate color $\mathbf c$ from $\mathbf x, \mathbf d, \mathbf n(\mathbf x)$ and an additional feature vector $\mathbf h(\mathbf x)$. 

UniSurf also gives a surface consistency regularization

$$\mathcal L_{reg} = \sum_{\mathbf x_x \in\mathcal S} = \|\mathbf n(\mathbf x_s) - \mathbf n(\mathbf x_s + \epsilon)\|_2$$

## Additional Supervisions

With SDF, the level set is more concentrated onto a surface, which is beneficial for estimating normal and depth. Therefore, many methods have looked at additional supervision terms designated for various purposes. 

The most commonly used losses for SDF based NeRF are

The L1 RGB reconstruction loss, directly supervised by the actual pixel color in the image

$$\mathcal L_{rgb} = \sum_{\mathbf r} \|\hat C(\mathbf r) - C(\mathbf r)\|_1$$

The Eikonal Loss for SDF values of near-surface sampled points

$$\mathcal L_{eik} = \sum_{\mathbf x\in\mathcal X}(\|\nabla f_\theta(\mathbf x)\|_2 - 1)^2$$

### MonoSDF

[MonoSDF: Exploring Monocular Geometric Cues for Neural Implicit Surface Reconstruction](https://niujinshuchong.github.io/monosdf/)

MonoSDF incorporates deep learning based 2D depth and normal estimation. 2D monocular depth/normal estimation provides dense depth map and is continuous within the image. However, any photometric approach suffers from inconsistency across images. In other words, multiple images of the same scene from different angles cannot be well aligned by projecting the depth. 

MonoSDF proposes two losses to solve this problem. 

The __depth consistency loss__

$$\mathcal L_d = \sum_{\mathbf r} \|(w\hat D(\mathbf r) + q) - \bar D(\mathbf r)\|^2$$

where $\hat D(\mathbf r) = \sum_{i} T_ia_i t_i$ (similar to $\hat C$, replace sampled point radiance directly with ray depth). $\bar D$ is the 2D depth. and $w, q$ are scale and translation term for alignment. $w,q$ is estimated per image (ray batch) using least-squares. 

The __normal consistency loss__

$$\mathcal L_{\mathbf n} = \sum_{\mathbf r} \|\hat N(\mathbf r) - \bar N(\mathbf r)\|_1 + \|1-\hat N(\mathbf r)\cdot \bar N(\mathbf r)\|_1$$

where $\hat N(\mathbf r) = \sum_{i} T_ia_i \mathbf n_i$ ($\mathbf n_i$ is given by the gradient of SDF at $t_i$), $\bar N$ is the 2D normal. The later term is used to transform the 2D normal to the same coordinate system of the 3D construction. 

### Manhattan SDF

[Neural 3D Scene Reconstruction with the Manhattan-world Assumption](https://zju3dv.github.io/manhattan_sdf/)

Instead of using normal consistency loss, ManhattanSDF specifically targets at indoor scenes with the Manhattan world assumption. i.e. the floor will always have $\mathbf n_f = (0,0,1)$ and the room will always rectangular so that the walls are perpendicular to the floor, and parallel or perpendicular to other walls. 

Therefore, the loss can be written as 

$$\mathcal L_{\text{floor}}(t_i) = \|1-\mathbf n_i \cdot \mathbf n_f\|_1, \mathcal L_{\text{wall}}(t_i) = \min_{i\in\{-1, 0, 1\}}\|i-\mathbf n_i \mathbf n_w\|_1$$

However, not pixel in the scene is wall or floor, and we only want to apply the geometric loss to certain pixels. The first idea is to use a 2D segmentation network to segment out walls and floors, and use it as a mask for the loss. Then, the problem is that 2D segmentation can have errors. Therefore, ManhattanSDF uses another MLP to predict the semantic logits, similar to the radiance MLP, and the pixel logits is $\hat S(\mathbf r) = \sum_i T_ia_i s_i$ and softmax the logits to probabilities $(\hat p_{\text{floor}}, \hat p_{\text{wall}}, \hat p_{\text{other}})$. Then the joint geometric loss is defined as 

$$\mathcal L_{joint} = \sum_{\mathbf r} \hat p_{\text{floor}} \mathcal L_{\text{floor}} + \hat p_{\text{wall}} \mathcal L_{\text{wall}}$$

To make sure the probabilities not vanish, adding a cross entropy loss to supervise the semantic MLP

$$\mathcal L_{s} = \sum_{\mathbf r} \bar p_k(\mathbf r) \log \hat p_k(\mathbf r)$$

where $\bar p_k$ is the 2D segmentation logits.