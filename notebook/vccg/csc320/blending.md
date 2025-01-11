# Image Pyramids and Blending

## Smoothing Filter
Assume the smoothing weights $\hat w$ is $1\times 5$. To make such weights a proper smoothing filters. $\hat w$ is symmetric, sum to $1$, and have equal contribution 

$$\hat w = [c, b, a, b, c], b = 1/4, c = \frac{1-2a}{4}$$

$$a+2b+2c = 1$$

$$a+2c = 2b=1/2$$

then the convolution filter is $W = \hat w\hat w^T$ is a $5\times 5$ filter. 

## Reduce Function
Define $Reduce: g_l\Rightarrow g_{l+1}$ where 

$$g_{l+1}(i,j) = \sum_{-2}^2 \sum_{-2}^2 W(m,n)g_i(2i-m,2j-n)$$

$$D_l = \begin{bmatrix}
1&0&0&...&0\\
0&0&1&...&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&...&1
\end{bmatrix},
C_l = \begin{bmatrix}
c&b&a&b&c&0&...&0\\
0&c&b&a&b&c&...&0\\
\vdots&\ddots&\ddots&\ddots&\ddots&\ddots&\ddots&\vdots\\
0&0&0&0&0&0&...&c
\end{bmatrix}$$

so that $g_{l+1} = D_L \cdot C_l\cdot g_l$ where $g$ is vectorized image. 

## Laplacian Pyramid
Let $L_i = g_i - expand(g_{i+1})$ be the difference between levels $g_l, g_{l+1}$, since $g_{l+1}$ has different size. We need to expand.

### Expand Function

$$expand(g_l) = 4\sum^2_{-2}\sum^2_{-2} W(m,n)g_l(\frac{i-m}{2}, \frac{j-n}{2})$$

## Blending
Given source images $A,B$ and binary matte $M$, compute Laplacian Pyramids for $A, B$ i.e. $AL_0, ..., AL_{N-1}, Ag_N, BL_0, ..., BL_{N-1}, Bg_N$, Gaussian pyramid for $M$, i.e. $Mg_0, ..., Mg_N$. Then, using matting equation, using $M$ as alpha channel. 

$$SL_i = Mg_l AL_l + (1-Mg_l)BL_l$$

Finally, reconstruct Laplacian pyramid $SL$, which is desired. 
