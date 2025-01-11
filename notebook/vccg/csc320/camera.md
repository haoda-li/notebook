# Camera

## Focus
The focal point $f = \lim_{d\rightarrow\infty} u$ where  
$f$ is the focal length  
$d$ is the distance of the object from the lens  
$u$ is the distance of the image plane

__Thin lens law__ $f^{-1} = u^{-1} + d^{-1}$

## [Depth of Field](https://en.wikipedia.org/wiki/Depth_of_field)
Range of distances where blur < 1 sensor pixel. 

$DOF \approx \frac{2u^2 NC}{f^2}$ where  
$C=$ given circle of confusion (pixel size)  
$f=$ focal length  
$N=$ f-stop  
$u=$ subject distance 

Typically, callphone camera has wider-angle lens (short focal length), hence larger DoF. Therefore, it can capture all objects in different distance, and then fake the blur by algorithm

## Camera controls
__Aperture__ expressed as $D:=f/N$,the relative size of the area in which light is collected through the lens

__Shutter speed__ $\Delta t$, the duration of the exposure, often expressed as fractions of a second


### DoF vs. Aperture and Shutter Speed
The capture photons $\propto D^2 \Delta t$  
The number of photons captured will influence the exposure. 

Also, consider DoF,   
$D = f/N\uparrow \Rightarrow DOF\downarrow$  


### ISO film speed
The sensitivity of film/sensor to light

Given exposure ($D^2\Delta t$) being constant, $ISO\uparrow\Rightarrow brightness\uparrow$

## Color image
All sensor pixels have same response curve, i.e. monochromatic and can only accepts intensity. To obtain a colored image, typically each pixel will be made to be sensitive or one of RGB by filters, typically 25% R, 25% B, 50% G. And full-color images can be obtained by __demosaicing__ each pixel with missing RGB. 

## Steps of  image formation


### Photons to Digital Numbers (Linear operations)

__radiant power from scene__ Arriving photons causes photo-electrons and the charge accumulates are more photons hits the photo-diode.

The radiant power 

$$\Phi = \int_{q} \int_\lambda H(\bar{q}, \lambda) S(\bar{q}) Q(\lambda)d\bar{q} d\lambda$$

where  
$\bar q =$ pixel footprint  
$\lambda =$ wave length     
$H=$ incidcent spectral irrandiance (the flux that can be received per/at that surface per/at that wavelength)    
$S=$ spatial response (the sensitivity of the sensor to radiation from different directions)  
$Q=$ quantum device efficiency (electrons that can be collected per incident photon at given wavelength)


__Exposure__ After exposure time, amplifier converts charge to measurable voltage  

  - With the exposure time $\Delta t$, now the total illuminance/irradiance is $\Phi\Delta t$
  - At same time, __black level__, a non-photoelextric current from photo diode, $I_0$ is added, to make the least black level. The result is $\Phi \Delta t + I_0$ 
 
  
__Sensor saturation__ The current cannot exceed __saturation current__ a set-maximum non-discarded current from photodiode  
    - $I_m = $ saturation current, adjust the voltage by $\min(\Phi\Delta t + I_0, I_m)$  

__Gain factor__ Apply an amplifier gain $g$, which is controlled by ISO (the larger $g$ the darker the darker)
    - the result will be $\frac{\min(\Phi\Delta t + I_0, I_m)}{g}$  
    - Since digital numbers is discrete, apply a flooring function $\lfloor\frac{\min(\Phi\Delta t + I_0, I_m)}{g}\rfloor$  
  
Therefore, 

$$DN = \lfloor\frac{\min(\Phi\Delta t + I_0, I_m)}{g}\rfloor$$

And for the whole process, the relationship is linear

### Gamma correction (camera response function)
Since human visual system doesn't have a linear response to light, DNs are passed through a gamma function to compensate, such function is $f(DN) := \beta(DN)^{1/\gamma}$ where $\beta, \gamma$ are constants that varies among different manufactures. 

## Image Noise

__Defocus Blur__  
when the scene points of interest are "out of focus" and not within the DoF

__Motion Blur__  
Camera moves significantly during exposure time  
More like with long exposures and long focal length (zooming in)

__Pixel noise__  
Incorrect exposure, not enough photons reaching sensor  
High ISO (gain) causes noise

__Rolling shutter__ <a href="https://en.wikipedia.org/wiki/Rolling_shutter">wiki</a>  
When captured by scanning across the scene rapidly

## Sources of Noise

_radiant power from scene_ 

__Dark Current Noise__

 - free electrons due to thermal energy, depends on temperature  
 - $\sim \text{Poisson}(\lambda = D\Delta t), D:=$thermal electron rate $(e^-/sec)$

_Exposure_

__Photon (Shot) Noise__  

- $\sim \text{Poisson}(\lambda = \Phi\Delta t )$  
$P_\lambda(\text{k events in }\Delta t) = \frac{\lambda ^k e^{-\lambda}}{k!}$, i.e. $P(\text{\#received photons}=k)= \frac{\Phi\Delta t ^k e^{-\Phi\Delta t}}{k!}$
- Largest source of noise for high exposures
- For large $\Phi\Delta t$, by LLN, we can approximate by $\text{Poisson}(\lambda)\approx N(\lambda, \sqrt \lambda)$
  
_Sensor saturation_ 

__Readout Noise__

 - $\sim N(0, \sigma_r)$, $\sigma_r$ depends on characteristics of electronics

_Gain factor_ 

__Amplifier, ADC, and Quantization Noise__ 

 - $\sim N(0, \sigma_{ADC})$  
 - The amplifier noise is dependent on $g$, i.e. gain or ISO. 
 - Largest source of noise for low exposures

## Put all Noises Together
Since all four types of noise are independent of each other, 

\begin{align*}
E(e^-) &=&\text{Black level} + &\text{dark current} + &\text{photon noise}\\
&= \min\{&I_0 + &D\Delta t + &\Phi\Delta t, I_m\}\\ 
\end{align*}

\begin{align*}
var(e^-) &= \text{dark current} &+ \text{photon noise} &+ \text{black level} &+ \text{readout noise} &+ \text{ADC noise}\\
var(e^-) &= D\Delta t &+ \phi\Delta t &+ I_0 &+ \sigma_r^2 &+ \sigma^2_{ADC} g^2
\end{align*}

Hence  
$E(DN) = \min\{\frac{I_0 + D\Delta t + \Phi\Delta t}{g}, \frac{I_m}{g}\}$  
$var(DN) = \frac{D\Delta t + \phi\Delta t + I_0 + \sigma_r^2}{g^2} + \sigma^2_{ADC} g^2$

__Signal-to-noise ratio__ $SNR = 10\log_{10} \frac{E(DN)^2}{var(DN)}$

