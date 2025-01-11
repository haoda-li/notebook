# Image Features - Blob Detection


### Goal
Independently scale interest points in each image, such that the detections are repeatable across different scales. 

### General Idea
Extract features as a variety of scales, e.g., by multiple resolutions in a image pyramid, and then matching features at the "corresponding" level

With the Harris corner detector we can find a maxima in a spatial search window, then find scale that gives local maxima of a function $f$ in both position and scale. 

## "Blob" Detection - Laplacian of Gaussian

$$\nabla^2g(x,y,\sigma)=-(\pi\sigma^4)^{-1}(1-\frac{x^2+y^2}{2\sigma^2})\exp(-\frac{x^2+y^2}{2\sigma^2})$$

Define the __characteristic scale__ as the scale that produced peak of the Laplacian response, so that such interest points are local maxima in both position and scale


```plotly
{"file_path": "csc420/assets/blob_detection_log.json"}
```


### Difference of Gaussian
__Problem with LoG__: LoG is not separable, and larger the $\sigma$, larger the filter is. 

Consider the approximation by finite differencing of Gaussian

$$DoG := G(x,y,k\sigma) - G(x,y,\sigma)$$

where $G$ is the Gaussian function
DoG is separable since Gaussian is separable, hence its difference. 


```plotly
{"file_path": "csc420/assets/blob_detection_dog.json"}
```

???quote "Source code"

    ```python
    --8<-- "csc420/scripts/blob_detection.py"
    ```