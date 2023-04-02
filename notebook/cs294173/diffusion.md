real image, add noise step by step to random images. and learn to come back step by step (each step goes through the diffusion model), and the model can be directed by other prompt (often text). 

Diffuse => process to add noise  
denoise => reverse process of the diffuse.
    during the denoise, each step the denoise will take to the real image manifold, but the algorithm will corrupt it again (add next step of noise).


write diffuse / corruption operator as $C(x, t)$, for example $C(x,t) = x + \sigma(t)\eta$ and denoiser $D(x,t)$ such as $x - \sigma_{\theta}(x,t)$

so that the diffusion training goal is 

$$L = \|x - D(C(x,t))\|^2$$

in the example above, that will be just $\|\sigma(t)\eta - \sigma_{\theta}(x,t)\|^2$ if we can perfectly predict the added noise, then we are in the manifold. 


# Learning from 2D diffusion models

score distillation sampling 

perturb image with random amount of noise and estimate update direction. Freeze diffusion model, update direction following score function. 

shading from light model instead of baked in NeRF. 

# Score Jacobian Chaining

sample multiple random noise and average the update directions.

sparsity losses prevent blurry 3D models, view dependent prompting