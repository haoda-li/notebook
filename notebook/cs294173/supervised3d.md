# Single View 3D with Supervision

In general, 3D learning focus on 2D images input (along with other sensor data) and output a 3D representation that describe the scene. 

## Depth Prediction on Monocular Images
Given 2D RGB images, the goal is to give a depth map that describes the ray distance at each pixel position.

A very initial idea is to directly predict the depth loss as the sum of distance between prediction and GT

$$\mathcal L_d(y, y^*) = \sum_{i\in I} \|y_i - y_i^*\|^2$$

### Scale invariant depth loss

[Depth Map Prediction from a Single Image using a Multi-Scale Deep Network](https://arxiv.org/abs/1406.2283) 

However, the problem arises due to scale ambiguity. Smaller but closer object will appears the same size as larger but far object. Therefore, we only want to consider the relative depth of each set of values, which means $\mathcal L(y, y^*) = \mathcal L(ay, y^*)$. This leads to the __scale invariant depth loss__

$$\mathcal L(y, y^*) = \sum_{i\in I} \|\log y_i - \log y_i^* + \frac{1}{n}\sum_{i\in I}(\log y_i^* - \log y_i)\|^2$$

The architecture adapts a coarse to fine structure to capture information from distant pixels. 

### Scale and shift invariant disparity loss

[Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer](https://arxiv.org/abs/1907.01341)

scale and shift invariant loss considers the shift of the camera and the scale ambiguity at the same time. Let $\mathbf d$ be the predicted disparity (inverse depth) and $\mathbf d^*$ be the ground truth. We first align the two disparity by computing predictors 

$$(s, t) = \arg\min \sum_{i\in I}(s\mathbf d_i + t - \mathbf d_I^*)^2$$

so that we can align our predicted disparity with the ground truth as $\hat{\mathbf d} = s\mathbf d + t$. Note that $s,t$ has a closed form solution 

$$t(\mathbf d) = \text{median}(\mathbf d), s(\mathbf d) = \frac{1}{N} \sum_{i\in I} | \mathbf d - t(\mathbf d)|$$

We can align both the prediction and the ground truth to have zero translation and unit scale

$$\hat{\mathbf d} = \frac{\mathbf d - t(\mathbf d)}{s(\mathbf d)}, \hat{\mathbf d}^* = \frac{\mathbf d^* - t(\mathbf d^*)}{s(\mathbf d^*)}$$

and the SSI loss is defined as 

$$\mathcal L_{SSI}(\hat{\mathbf d}, \hat{\mathbf d}^*) = \frac{1}{2N} \sum_{i\in I} \|\hat{\mathbf d}_i - \hat{\mathbf d}_i^*\|$$

An additional regularization term (multiscale gradient matching introduced by [MegaDepth](https://arxiv.org/abs/1804.00607)) is also adapted.

## Depth Estimation on Videos

[Robust Consistent Video Depth Estimation](https://robust-cvd.github.io/)

Compared to single images, video data makes the assumption that the adjacent frames have consistent camera poses (single image depth estimation fails) and the object in the scene have consistent movement (dynamic scenes, hence SfM fails). The task can be modelled by several components

- The objects in the scene, as a depth map
- The camera poses, as extrinsic and intrinsic $R, t, K$
- The deformation of the object

Given an image sequence, RCVD computes the optical flow for frame $i$ and $i+k$ for every $k$ frames, a mask for dynamic pixels, and per-image depth map (mapped to camera coordinates, so that projected as a 3D point cloud). If we know some other image's pose, then we can reproject the point cloud into the other image, and see if such point is the same as the projected pixel from optical flow. This is the __reprojection loss__ from frame $i$ to frame $j$

$$\mathcal L_{reproject}^{i,j}(x) = \mathcal L_j(\mathbf c_{i\rightarrow j}(x), \mathbf c_j(f_{i\rightarrow j}(x)))$$

where $x$ is the 3D point in frame $i$, $\mathbf c_{i\rightarrow j}$ is the feature of the reprojection in frame $j$, and $f$ is the optical flow from $i$ to $j$. 

The reprojection mentioned above requires camera poses. However, direct optimization of the camera pose is hard for CNN. Instead, RCVD uses a depth deformation model to align the depth. Instead of given full 6D freedom, RCVD replaces the depth scale coefficient with a spatially varying bilinear spline so that the optimization can be smoothed. 

## 3D Representations 

Similar to depth scale ambiguity issue, we need to consider which coordinate system to use for learning 3D. Camera coordinate system is not generally a good choice since the same object can be seen from infinitely many camera coordinates. Instead, we use a "canonical" coordinate system, centered at the object. Generally, we assume that for objects in the same category, they should have a similar shape structure, hence similar distribution of directions (canonical coordinates) and similar distribution of the volume (center of the object). 

Therefore, for the learning, the supervision will be ==3D object representations in the canonical coordinate system==. For image-based input, we need to recover the transformations (from camera space to the object space) and the object representation.

### Voxels
Voxel representation is a uniform 3D grid $V(x,y,z)\in \in \{0, 1\}$. In general, it can be seen as a 3D mask hence we can seen the problem as a voxel-wise classification problem. The 3D supervision will be another voxel volume representation, and the supervision loss is simply cross entropy loss at each voxel location. 

Earlier attempts ([Learning a Predictable and Generative
Vector Representation for Objects](https://arxiv.org/abs/1603.08637), [Pix2vox](https://arxiv.org/abs/1901.11153)) uses an encoder-decoder structure to encode 2D images and decode to 3D voxel volumes. Following works uses octrees to allow hierarchical approach to save computations. 

### Implicit Volumetric Representations
Accounting for the resolution bottleneck on voxel grid, another set of works represents the 3D space as a implicit filed that maps 3D location $\mathbf x$ to a scalar output. The output can be 

- Signed distance ([DeepSDF](https://arxiv.org/abs/1901.05103)), the closest distance to the surface. positive distance means outside of the surface and negative means inside. Surface at 0-level..
- Occupancy function or Inside/outside score ([Occupancy Networks](https://arxiv.org/abs/1812.03828), [Learning Implicit Fields for Generative Shape Modeling](https://arxiv.org/abs/1812.02822)), $0$ if outside the shape, $1$ is inside. Surface at $\frac{1}{2}$-level. 

The core idea is similar, encode 2D images to a latent code, and then add position $(x,y,z)$ (possibly with a positional encoding) to the latent code, and final decode them into the scalar value. Given a 3D scalar field, the surface is represented by the level-set. Marching-cubes algorithm is an effective way to extract meshes from 3D scalar field, given the actual level. 

### Parametric surface

[AtlasNet: A Papier-Mache Approach to Learning 3D Surface Generation](https://arxiv.org/abs/1802.05384)

Suppose that a 3D surface can be represented by multiple pieces of manifold surfaces. Each manifold surface is a manifold mapping from $(u,v)$ to $(x,y,z)$ and the 3D surface can be represented by $n$ pieces of manifold with overlapping. 

To allow learning of such manifold, the latent code is padded with randomly sampled point cloud from $[0,1]\times [0, 1]$ sheet and decoded into corresponding point cloud location. Since the point cloud is uniformly sampled from a 2D square, we can increase the resolution by increase the number of samples. If the whole object can be represented by deforming a sphere, then we can also sample from a unit sphere. Note that in this case, the supervision is point cloud sampled from 3D mesh, and the loss is the Chamfer distance loss. 

??? note "Chamfer distance"

    given two point cloud $\mathcal P$ and $\mathcal Q$, the Chamfer distance loss is

    $$L_C(\mathcal P,\mathcal Q) = \sum_{p\in \mathcal P} \min\{d(p, q) | q\in\mathcal Q\} + \sum_{p\in \mathcal P} \min\{d(p, q) | p\in\mathcal P\}$$

    Note that there's no correspondence between point cloud and the points are orderless. In addition, the number of points in two point cloud can be different. 