# Image Features - Harris Corner Detector


```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.signal import convolve2d

def imshow(img, ax=None, title="", bgr=True):
    # since plt and cv2 have different RGB sorting
    if bgr:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    if ax == None:
        plt.imshow(img.astype(np.uint8))
        plt.axis("off")
        plt.title(title)
    else:
        ax.imshow(img.astype(np.uint8))
        ax.set_axis_off()
        ax.set_title(title)
        
plt.rcParams["figure.figsize"] = (12,6)
```

## Image Stitching

When matching to images, and even to merge into one.  
__Detection__ identify the interest points  
__Description__ extract __feature vector__ around each interest point  
__Matching__ determine correspondence between descriptors in two views

The goal is to detect the same points in both images, the number of points must be generated in each image independently, and must have a sufficient number for comparison, while at the same time not too many, which makes the algorithm slow. 

### What are good characteristics for a interest point
Must have somewhat unique texture in the local sense  
Large contrast changes, i.e. gradients  
Edge is less useful since line segments can be localized on any place with the same orientation (aperture problem)  
Therefore, we need at least two different orientations, which can be reliably matched

## Corner Detection
"Corner like" patch can be reliably matched

We should easily recognize the corner "point" by looking through a small window, where there should have a large change in intensity in all directions. 

### Weighed summed square difference

$$E_{WSSD}(u,v) = \sum_x \sum_y w(x,y)[I(x+u, u+v) - I(x,y)]^2$$

where $w: \mathbb N^2 \rightarrow \mathbb R$ is the weighted function, for example indicator $\mathbb I((x,y) \text{ in window})$, or 2-D Gaussian. 

Them, fit $I(x+u, y+v)$ by a first-order Taylor series expansion about $x,y$: 

$$I(x+u, y+v)\approx I(x,y) + u\cdot \frac{\partial I}{\partial x}(x,y) + v\cdot \frac{\partial l}{\partial y}(x,y)$$

Then, we can approximate $I$ by a series of polynomials, so that we can plugging in for $E_{WSSD}$

$$\begin{align*}
E_{WSSD}(u,v) &= \sum_x \sum_y w(x,y)[I(x+u, u+v) - I(x,y)]^2\\
&\approx \sum_x\sum_y w(x,y)(I(x,y) + u\cdot I_x + v\cdot I_y - I(x,y))^2\\
&= \sum_x\sum_y w(x,y)(u^2I_x^2 + 2u\cdot v\cdot I_x\cdot I_y + v^2I_y^2)\\
&= \sum_x \sum_y w(x,y) \cdot \begin{bmatrix}u&v\end{bmatrix}
\begin{bmatrix}I_x^2&I_x\cdot I_y\\I_x\cdot I_y &I_y^2\end{bmatrix}
\begin{bmatrix}u\\v\end{bmatrix}\\
\text{Let }M &:= \sum_x\sum_y w(x,y)\begin{bmatrix}I_x^2&I_x\cdot I_y\\I_x\cdot I_y &I_y^2\end{bmatrix}\\
&= \begin{bmatrix}u&v\end{bmatrix}
M
\begin{bmatrix}u\\v\end{bmatrix}
\end{align*}$$


​<figure markdown>
![png](assets/harris_corner_1.jpg){width="720"}
</figure>

The images are $I, I_x, I_y, I_{x}I_y, I_{x}I_x, I_{y}I_y$

Note that $M$ is independent of $u,v$.

Consider using an indicator weight function, then $M = \begin{bmatrix}\sum_{x,y} I_x^2 &\sum_{x,y} I_x\cdot I_y\\\sum_{x,y} I_x\cdot I_y &\sum_{x,y} I_y^2\end{bmatrix}$ defines the shape. Generally, $E_{WSSD}(u,v)$ will be a ellipse

```plotly
{"file_path": "csc420/assets/harris_corner_wssd.json"}
```
    


Note that $M$ is symmetric $2\times 2$ matrix and is diagonalizable, i.e. $M = V diag(\lambda_1, \lambda_2), V^{-1}$, and $\lambda_{\min}^{-1/2}, \lambda_{max}^{-1/2} \propto$ length of the radii of the ellipse and indicate the direction of of slowest change and fastest change, respectively. 

Then, a perpendicular corner will have large lambdas and $\lambda_1 \approx \lambda_2$, for edges, $\lambda_a >> \lambda_b$, for "flat" region, lambdas are small.

## Harris Corner Detector
Given such characteristics of lambda, we can propose a rotationally invariant criteria 

$$R := \lambda_1\lambda_2 - \alpha(\lambda_1+\lambda_2)^2 = det(M) - \alpha \cdot trace(M)^2$$

Where $\alpha \in (0.04, 0.06)$ is a constant coefficient

$R<0$ then edge  
$R > 0$ then corner  
$|R| < \epsilon$ for some small threshold then flat region

    
​<figure markdown>
![png](assets/harris_corner.jpg){width="720"}
</figure>
    


### General Procedure
- compute vertical and horizontal gradients $I_x,I_y$
- compute $I_x^2, I_y^2, I_x\cdot I_y$  
- compute Gaussian weighted $M$ for each pixel
- compute $R = det(M) - \alpha trace(M)^2$ for each image window, as corner score
- Find points above threshold $R > S$  
- Non-maximum suppression to keep only the local maxima

### Properties
- Rotation and Shift invariant (for Harris corner detector)
- NOT scale invariant (if an image is enlarged, then we cannot find the corner with the same window size)


???quote "Source code"

    ```python
    --8<-- "csc420/scripts/harris_corner.py"
    ```