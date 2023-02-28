# Neural Radiance Fields

## Plenoptic Function
Consider some function to describe the set of all things that we can ever see (i.e. all the necessary inputs that will impact the seen color). The parameters are 

- $\theta, \phi$ the viewing directions
- $x_v, y_v, z_v$ the eye position
- $\lambda$ wavelength
- $t$ time

The estimation of the function is the image based rendering / novel view synthesis problem. One classical approach for modeling plenoptic function is Lightfield (1996), which take pictures from many views. The problems are 3D consistency and also assume that the ray shouting out from a pixel is never occluded. Thus only the plenoptic surface.

## NeRF

[Non-conceptual details and formulations](../research/nerf.md)

Change plenoptic function from viewing centered to object centered (object emits light instead of eye receiving light) and simplify the problem to 5D (remove wavelength and time). Intuitively, a NeRF can be discretized as a 3D grid, and at each grid location, we have a sphere of colors.  

Relations with some other works

 - MVS: multi-view stereo aims to recover the surface mesh based on physics based rendering, hence struggle on thin, amorphous, and shiny objects. 
 - analysis by synthesis: [A Theory of Shape by Space Carving (2000) by Kutulakos](https://www.cs.toronto.edu/~kyros/pubs/00.ijcv.carve.pdf) use calibrated images to "carve" the volume and form the final shape. However, the non-differentiable and handmade way are limited. 

## Components of NeRF

A NeRF can be seen as 3 parts. 
- Volumetric rendering equations
- Fields (Embedders): how to represent the 3D space
- Sampling function: how to sample points along the ray. 

### Encodings

Intuitively, MLPs are differentiable and "over-smooths" high frequency features. Images typically have high frequency details and are not differentiable in local patches (edges). The idea is to transform the features into another space so that it can learn faster and preserves high frequency details. Existing approaches includes

- [Fourier features, positional encoding](https://bmild.github.io/fourfeat/index.html) The positional encoding used in original NeRF, also useful for other 2D/3D regression tasks. 
- [Hash encoding, instant-ngp](https://nvlabs.github.io/instant-ngp/) A multi-res hash encoding. An image is "continuous" in non-edge spaces. If we hash the image pixels, then the image becomes continuous in the neighboring spaces. The hash value will be learned by an MLP at the same time. Also, "multi-res" means that we store the features at different resolution and do trilinear interpolations when retrieve them. This provides faster training and inference. 
- [Spherical harmonics](https://alexyu.net/plenoctrees/) RGB is not continuous, but SH coefficients are. The MLP can predict SH coefficients instead RGB. Also, we benefits from SH as the function is analytic, simple to compute, and simplify the learning. 

### Fields Compression

In NeRF, the field is parameterized by a large MLP, which is expensive for inference. However, the space is not filled by object volume in most cases. Indeed, many space are often empty. The idea is to shrink the 3D space by different representations of fields. 

- Sparse voxel grid, works such as [NSVF](https://lingjie0206.github.io/papers/NSVF/) and [Plenoxels](https://alexyu.net/plenoxels/). The idea is to construct voxel grid on the space, the grid is "sparse" because we can skip empty voxels. 
- Lower rank representations such as [TensorRF](https://apchenstu.github.io/TensoRF/). Decompose the 4D tensor volume into lower-rank matrices and vectors. 
- A dictionary, or multi-res hash grid. [instant-ngp](https://nvlabs.github.io/instant-ngp/). Hashing with the hash key learned by the neural network. Multi-res allows to store features in different frequency. 


### Sampling

The considerations for sampling are 

 - __Aliasing__ Do we have enough samplings in some space, do we "skip" the important surfaces. 
 - __Speed__ Do we have redundant samplings in the empty space

In the original NeRF, the idea is to do coarse-to-fine sampling. Starting with uniform sampling, and then do another fine sampling by importance (via volume density $\sigma$). The problem is that it requires a very large number of point, hence very slow inference. 

Following up works start to use different field representations so that empty space are skipped (sparse voxels, occupancy grid checking in instant-ngp). 

Surface-based methods predict surface and only sample near the surfaces. 

For aliasing, [MipNeRF](https://jonbarron.info/mipnerf360/) samples from a cone instead of the original ray. Note that the sampling function is the same in MipNeRF, the idea is to use a integrated positional encoding so that features further away will have different sampling rate (mip as of mipmap). 

[MipNeRF-360](https://arxiv.org/pdf/2111.12077.pdf) further uses a proposal network (a tiny MLP) to learn (distilled model) the weights $w_i$. 