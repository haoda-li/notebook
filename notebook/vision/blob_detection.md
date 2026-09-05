# Image Features - Blob Detection


### Goal
Independently scale interest points in each image, such that the detections are repeatable across different scales. 

### General Idea
Extract features as a variety of scales, e.g., by multiple resolutions in a image pyramid, and then matching features at the "corresponding" level

With the Harris corner detector we can find a maxima in a spatial search window, then find scale that gives local maxima of a function $f$ in both position and scale. 

## "Blob" Detection - Laplacian of Gaussian

$$\nabla^2g(x,y,\sigma)=-(\pi\sigma^4)^{-1}(1-\frac{x^2+y^2}{2\sigma^2})\exp(-\frac{x^2+y^2}{2\sigma^2})$$

Define the __characteristic scale__ as the scale that produced peak of the Laplacian response, so that such interest points are local maxima in both position and scale


```python exec="on"
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import scipy.ndimage as scim

fig = make_subplots(3, 2, shared_xaxes=True)

N = 50
x = np.zeros(N)
x[N//3:N//3*2] = 1
sigma = 0
for i in range(3):
    for j in range(2):
        fig.add_trace(
            go.Scatter(
                x=np.arange(N), 
                y=scim.gaussian_laplace(x, sigma),
                name=f"sigma={sigma}"
            ),
            row=i+1, col=j+1
        )
        sigma += 1.5
fig.update_layout(margin={'t': 0, 'l': 0, 'b': 0, 'r': 0})
print(fig.to_html(full_html=False, include_plotlyjs="cdn"))
```


### Difference of Gaussian
__Problem with LoG__: LoG is not separable, and larger the $\sigma$, larger the filter is. 

Consider the approximation by finite differencing of Gaussian

$$DoG := G(x,y,k\sigma) - G(x,y,\sigma)$$

where $G$ is the Gaussian function
DoG is separable since Gaussian is separable, hence its difference. 


```python exec="on"
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
N = 50
x = np.linspace(-10, 10, N)
sigmas, ks = [1, 2, 3], [0.5, 0.7, 0.95]

fig = make_subplots(3, 3, shared_xaxes=True, shared_yaxes=True)

for i in range(9):
    sigma = sigmas[i % 3]
    k = ks[i // 3]
    g = 1 / sigma * np.exp(-(x ** 2) / (2 * (sigma ** 2)))
    g2 = 1 / (sigma * k) * np.exp(-(x ** 2) / (2 * ((sigma*k) ** 2)))
    fig.add_trace(
        go.Scatter(
            x=x,y=g-g2,name=f"k={k}, sigma={sigma}"
        ),
        row=i%3+1, col=i//3+1
    )
fig.update_layout(margin={'t': 0, 'l': 0, 'b': 0, 'r': 0})
print(fig.to_html(full_html=False, include_plotlyjs="cdn"))
```

???quote "Source code"

    ```python
    --8<-- "vision/scripts/blob_detection.py"
    ```