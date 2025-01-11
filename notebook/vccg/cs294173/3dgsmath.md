# 3DGS Implementation Details

Based on the [3DGS paper :fontawesome-solid-link:](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)[@3Dgaussians], the [gsplat doc :fontawesome-solid-link:](https://docs.gsplat.studio/), and the [math supplement :fontawesome-solid-link:](https://arxiv.org/pdf/2312.02121.pdf)[@ye2023mathematical]

## Representation

Each splat is represented as a 3D Gaussian blob, parameterized as mean (position) $\mu \in \mathbb R^3$, covariance (isotropic shape) $\Sigma\in\mathbb R^{3\times 3}$, color $c\in\mathbb R^3$, and opacity $o\in\mathbb R$. 


The 3D covariance $\Sigma$ can be further parameterized as per-axis scale $s\in\mathbb R^3$ and rotation in quaternion $q\in\mathbb R^4 = (x,y,z,w)$. The quaternion is then converted to rotation matrix $R\in SO(3)$ as 

$$R = \begin{bmatrix}
1 - 2(y^2+z^2) & 2(xy-wz) & 2(xz+wy)\\
2(xy+wz) & 1-2(x^2-z^2) &2(yz-wx)\\
2(xz-wy) & 2(yz+wx) &1-2(x^2+y^2)
\end{bmatrix}$$

the 3D covariance $\Sigma$ is given by 

$$\Sigma = RSS^TR^T, S=diag(s)$$

The rendering camera is described by the extrinsic $R_{c2w}, t_{c2w}$ in the world coordinate space and intrinsic $f_x, f_y$ (focal length), $h, w$ (height, width), $f, n$ (far and near clipping distance).

Following the rasterization pipeline, we transform each splat into the camera space through the world to camera transformation 

$$T_{w2c} = T^{-1}_{c2w} = \begin{bmatrix}
R_{c2w} &t_{c2w}\\
\mathbf{0} & 1
\end{bmatrix}^{-1}$$

and then perspective projection 

$$P = \begin{bmatrix}
2f_x/w &0&0&0\\
0&2f_y/h&0&0\\
0&0&(f+n)/(f-n) &-2fn/(f-n)\\
0&0&1&0
\end{bmatrix}$$

to transform the camera space into normalized clip space (NDC space). 

## Gaussian projection

For the projection, the position $\mu$ is transformed into NDC space through the homogeneous transformation 

$$t =T_{w2c}\begin{pmatrix}\mu\\1\end{pmatrix},  t' = Pt$$

then into pixel coordinates 

$$\mu' = (u,v) = \begin{pmatrix}(wt_x/t_w+1)/2 + c_x\\(ht_y/t_w+1)/2+c_y\end{pmatrix}$$


the covariance $\Sigma$ is projected using the transformation from EWA Splatting paper [@zwicker2002ewa] 

$$J = \begin{bmatrix}
f_x/t_z &0& -f_xt_x/t^2_z\\
0&f_y/t_z &-f_yt_y/y^2_z
\end{bmatrix}$$

and the projection is 

$$\Sigma' = JR_{c2w}\sigma R_{c2w}^TJ^T$$

## Sorting
A naive sorting will sort all splats by the view-space depth $t_z$. Instead, notice that the size of splats is often few pixels and the frame is thus divided into $16\times 16$ pixels tiles. We find all overlapping tiles for each splat in the frame space (from 2D position $t'$ and 2D covariance $\Sigma'$, we can find the bounding box that bounds $99\%$ confidence ellipse). Note that some splats may overlap more than one tile, thus we need to duplicate them. 

To utilize parallel sorting, assign each tiled splat a key, where first 32 bits encode the tile ID (`uint32`) and the lower 32 bits encode the depth (`float32`), and we do a parallel `radix_sort` on all splats. Then, finds the start and end indices of each tile by simply compare the tile ID with the neighbors. 

In general the pseudo-code is 

??? quote "pseudo code"
    ```py
    def create_splat_keys(g_frame: ProjectedGaussians, tiled_grid):
        # the number of tiles each splat overlaps, the last index is 
        # for exclusive scan
        n_tiles_overlapped = zeros_arr(len(g_frame) + 1)

        @parallel
        for idx, splat in enumerate(g_frame):
            # integer bbox, for all tiles that overlaps the gaussian
            bbox = find_bbox(splat, tiled_grid)
            n_tiles_overlapped[idx] = bbox.area()

        tiled_splat_key_start = parallel_exclusive_scan(n_tiles_overlapped)

        tiled_splat_keys = empty_arr(tiled_splat_key_start[-1])

        @parallel
        for i, splat in enumerate(g_frame):
            bbox = find_bbox(splat, tiled_grid)
            for j, tile_id in enumerate(bbox):
                key = get_key(tile_id, splat.depth)
                tiled_splat_keys[tiled_splat_key_start[i] + j] = key
        return tiled_splat_keys

    def rasterize(cam: Camera, g: Gaussians):
        # cull gaussians outside of the camera frustum
        g_cull = cull_gaussian(g, cams) 
        # project gaussians into 2D frame space
        g_frame = project_gaussians(g, cam)
        # create tiles from the frame height and width
        tiled_grid = create_tiles(cam.w, cam.h)
        
        # create tiled splat keys
        tiled_splat_keys = create_splat_keys(g_frame, tiled_grid)

        # sort the keys
        sorted_keys = parallel_radix_sort(tiled_splat_keys)
        # find the start and end for each tile
        start_indices, end_indices = parallel_find_edges(sorted_keys)

        @parallel
        for tile in tiled_grid:
            start, end = start_indices[tile], end_indices[tile]
            @parallel
            for pixel in tile:
                pixel = rasterize(sorted_keys[start:end+1])
    ```

## Composition
Following the classic rendering equation, we need to blend the colors from front to back as 

$$C = \sum_{n} c_n a_n T_n, T_n = \prod_{m<n} (1-a_m)$$

where $a$, or the conic opacity is computed from opacity parameter $o$ multiples 2D Gaussian distribution

$$a = o (p_{\mu',\Sigma'}(\mathbf u)) = o \cdot \exp(-\frac{1}{2}(\mathbf u - \mu')^T\Sigma'^{-1}(\mathbf u - \mu'))$$

where $\mathbf u = (u,v)$ is the pixel center. 