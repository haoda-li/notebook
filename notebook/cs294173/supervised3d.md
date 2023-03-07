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
