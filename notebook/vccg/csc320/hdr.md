# High Dynamic Range

## Dynamic Range
$DR := \frac{L_{max}}{L_{min}}$ where $L$ is the the brightness of the visible in the photo  
Measured in $EV := \lg(DR)$

### Problem with DR
Human perception can detect $\sim 14 EV$ stops, while 8-bit image can only represent $\sim 6$ stops (due to the $\gamma$-function), even the best sensor can capture $14$ bits.pixel, and TV can only display $6-10$ stops

On the images, bright pixels will saturate the sensor, while the dark pixels are below the the threshold required to be represented

### General Ideas of HDR
__Capturing__ taking photos at multiple EV to capture more  
__Display__ find a mapping function that can display more tones from HDR images in 8-bit LDR display

## Inverse Camera Response Function

Let $\Phi$ represent the scene irradiance, $Z(x,y)$ be the camera recorded value on $(x,y)$. 
Consider $\Delta t$ be he different exposure time. Then, 

$$Z = f_{camera}(\Phi\Delta_t)$$

where $f_{camera}$ is all the remapping from RAW (i.e. gamma function). 
Then if we know how to approximate the inverse of $f_{camera}$, then we can know the original $\Phi\Delta_t$, then the algorithm is to

```python title="Inverse Camere Response"
for (x, y) in all image pixel:
    for j in photos with exposure time delta_t(j):
        estimate Phi_ij by Z(x,y) and delta_t(j)
estimate Phi_i by Phi_ij's
output Phi_i with image response function
```

## Log-inverse Response Function

$$g(Z) = log(f^{-1}(Z)) = \log\Phi + \log\Delta_t$$

i.e. the log of inverse response function  
Also, note $Z\in \mathbb N. Z \leq 255$, thus we only need to approximate $256$ values

Then, note that we have $N$ pixels and $P$ images, i.e. $NP$ equations and $N + 256$ unknowns. i.e.  

$$g(Z_{ij}) - \log \Phi_i = \log \Delta t_{j}$$ 

where $Z_{ij}, \log\Delta t_j$ are known, $g, \log\Phi_i$ are unknown
Then, denote $g_{ij} = g(Z_{ij}), \phi_i = \log \Phi_i, \delta_j = \log \Delta t_j$  
Let 

$$\vec x = [g(0), g(1), ..., g(255), \phi_1,...,\phi_N]^T$$  

$$\vec b = [\underset{j\text{ times}}{\delta_1,...,\delta_1},...,\underset{j\text{ times}}{\delta_i,...,\delta_i}]$$

$$A_{NP\times 256+N}$$

where for the $ij$th row, $A[Z_{ij}+1] = 1, A[256+i] = -1$

## Smoothness Constraints
Since we know that $g$ is a smoothly increasing function, i.e. 

$$g_{z+1} - g_z \approx g_{z} - g_{z-i}\Rightarrow 2g_z - g_{z+1} - g_{z-1}\approx 0$$ 

so we add the $254$ equations, i.e. $254$ columns to $A, x$. Where

$$A_{NP + k, k-1} = -1, A_{NP+k,k}=2, A_{NP+k, k+1}= -1, b_{NP+1 : NP+254} = 0$$


## Final Equation

$$\Phi_i = \exp(\frac{\sum^P w(Z_{ij} \log \phi_{ij})}{\sum^P w(Z_{ij})})$$

$w$ is a weighting factor that depends on the pixel value, i.e. the integer approximation of $g$. $w$ should be lower at $0/255$ for the compensation of black level and saturation. 
