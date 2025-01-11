# Problem Formulations for 3D Vision

## Fundamentals 

### World to image projection
For 3D to 2D images, we go through 

$$[\mathbf X_w = (x_w, y_w, z_w)]\iff [\mathbf X_c = (x_c, y_c, z_c)] \implies [\mathbf x_i (x_i, y_i)]$$

where $\mathbf X_w$ is the world coordinates, $\mathbf X_c$ is the camera coordinates, and $\mathbf x_i$ is the image coordinates. The transformation from $\mathbf X_w$ to $\mathbf X_c$ is the world to camera (w2c) transformation, and the inverse if camera to world (extrinsic, camera poses) transformation. The transformation from $\mathbf X_c$ to $\mathbf x_i$ is the projection, which is not invertible (loss $z$ in this process). Often time we use perspective projection, described by the camera intrinsic. 

### Representing rotations

[Representations of 3D Rotations notes](../cs284/transforms.md#representations-of-3d-rotations)

For neural networks, we need continuous space so that we can "learn". One effective way is to predict some $3\times 3$ matrix $A$ and use SVD to decompose $A$ s.t. $A = USV^T$, $R = UV^T$. 

### 3 Key Components

In a big picture, there are 3 key components for 3D from images. 

- __Camera__ the relative motion among camera poses
- __Correspondences__ which pixel on the images correspond to the same point in 3D
- __Structure__ the 3D points / objects

## Photometric Stereo

Given fixed camera, fixed objects, a light source (point light of directional) s.t. the light source changes its position in each image. We want to recover the 3D shape.

From BRDF, suppose that we are using directional light and the object has uniform material, then we have the specular light 

$$B_i = \rho \mathbf n_i \mathbf l$$

where $B_i$ is the __observed__ pixel value, $\rho$ is the coefficient for BRDF, light color, material, etc., $\mathbf n_i$ is the __unknown__ surface model and $\mathbf l$ is the light direction. 

If we know the light direction in each image, then we can recover the normal from a system of equations, which facilitates high-fidelity 3D scans. 


## Camera calibration, stereo, and epipolar geometry

### Camera calibration
First, consider camera calibration from $s\mathbf x = K \cdot [R|\mathbf t] \cdot \mathbf X$ where $P:=K\cdot [R|\mathbf t]$ is the $3\times 4$ projective matrix. Therefore, if we know the the position of some image pixels $\mathbf x$, 3D point $\mathbf X$, and the correspondence between them, we can solve a linear system of equations with 12 unknowns. In practice, since errors exist, we use linear least squares to optimize the system of equations.

Note that we can recover intrinsic $K$ and extrinc $[R|\mathbf t]$ from $P$ using QR decomposition, since $K$ is a upper-triangular matrix and $R\in SO3$.  

### Stereo
If two cameras are calibrated and we know their relative poses to each other. We then have a stereo camera. For simplicity, we assume that the cameras have parallel optical axis. We want to recover the relative depth from camera to the seen object. 

If we know pixels in two image planes $(u_1, v_1), (u_2, v_2)$ corresponds to the same pixel $\mathbf X = (X,Y,Z)$ in 3D. In addition, we know the extrinsic as eyes $\mathbf O_1, \mathbf O_2$ and optical axis $\mathbf d$ (assuming parallel) for each camera, and the intrinsic $K$ (assume identical intrinsic). 

We can compute 
- 3D world space position $\mathbf I_1 = (x_1, y_1, z_1), \mathbf I_2 = (x_2, y_2, z_2)$ for the pixels on the image plane. 
- $B = \mathbf O_1 - \mathbf O_2$, the difference between two camera positions
- $d_1, d_2$ the disparity of $(u_1, v_1), (u_2, v_2)$ to $\mathbf d$

Then, $\mathbf X\mathbf I_1\mathbf I_2$ forms a similar triangle to $\mathbf X\mathbf O_1\mathbf O_2$, and we have a angle-side-angle problem for the triangle $\mathbf X\mathbf O_1\mathbf O_2$.

If we have two images taken from the same camera at different poses, we can also do stereo just as fine. However, __translation is required for stereo__. Consider the rotation case, where $B = \mathbf O_1 - \mathbf O_2 = 0$, then we don't have the similar triangle and cannot perceive depth. 

### Epipolar geometry

Consider the projection of the line $\mathbf O_1\mathbf X$ onto the image plane of camera 2, the projection will form a line $\mathbf l_2$, and similarly on plane 1 we have $\mathbf l_1$ projected from $\mathbf O_2\mathbf{X}$

```plotly
{"file_path": "cs294173/assets/epipolar.json"}
```

Therefore, we have the __epipolar constraint__ that vectors $\mathbf x_1 = \mathbf{I}_1 - \mathbf{O}_1,\mathbf x_2 = \mathbf{I}_2 - \mathbf{O}_2, \mathbf t = \mathbf{O}_2 - \mathbf O_1$ are colinear. 

If we know the camera poses between stereo cameras, and we have feature point on camera 1, then we only need to search for points on the epipolar line $\mathbf l_2$. 

## Multi-view Stereo (MVS)

Now, expand stereo from 2 cameras to multiple camera. The input is calibrated images. In ideal case, MVS should give exactly the same depth as stereo. However, in practice they are different due to mismatching, errors in calibration, etc. The basic idea for MVS is that for each image, do stereo for each of its neighboring images and get depth from each pair. Finally, optimize all depth information so that the disagreement among images is minimalized. With more images, it gives a stronger match signal and more freedom for choosing a best subset of images to match. 

Depth fusion is a common problem for MVS, which given per image depth map, either dense depth map directly from RGBD, or sparse depth map from photometric stereo. The goal is to fuse the depth into a 3D model by maximizing the depth consistency. 


## Structure from Motion (SfM) and Visual SLAM

The all-in-one paper [COLMAP: SfM Revisited](https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf)

The hardest type of problem in 3D vision is SfM, in which we only have unstructured images. What we can get from images is the correspondence (through feature extraction and patch match). 

The output is a sparse 3D location $\mathbf x_i$ for each matched pixel, and camera parameters ($R, \mathbf t$ and sometimes even $K$ if the images are taken by different cameras) for each image. 

The objective is to minimizing re-projective error: given the set of cameras and the structure (sparse point cloud), how many pixels are the same as in the images. 

Common pipeline involves
- Feature extraction and matching: SIFT feature extraction and its derivatives, matching involves RANSAC to estimate fundamental matrix (epipolar constraint)
- Image connectivity graph: which clusters of images are neighbors
- Correspondence estimation: linkup pairwise matches in the connectivity graph to form connected components of matches across more images
- Camera parameter estimation and sparse cloud reconstruction

### Bundle adjustment

We could write the reprojection errors over $m$ reconstructed points and $n$ images as 

$$g(\mathbf X, \mathbf R, \mathbf T) = \sum_{i=1}^m \sum_{j=1}^n w_{ij} \|P(\mathbf x_i, R_j, \mathbf t_j) - (u_{ij}, v_{ij})\|$$

where $w_{ij}$ is an indicator that point $i4 is visible in image $j$, $\mathbf x_i$ and $P$ is the projection from 3D space to the camera's image plane, and $(u_{ij}, v_{ij})$ is the pixel value corresponds to point $i$ in image $j$. 

__Bundle adjustment__ aims to minimize the error. 


### Visual SLAM

Instead of giving a set of image, V-SLAM has continuous input stream from camera and additional sensors (IMU for motion acceleration, LIDAR for depth). Also, the localization often requires to be real-time (for robot exploration). 

In general, the algorithm is similar to SfM, but image connectivity and correspondence is given by nature (the robot cannot teleport). Bundle adjustment is often done periodically on a cluster of images collected. Also, V-SLAM introduces the problems such as loop closure so that more constraints are presented. 