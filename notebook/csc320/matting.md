# Image Matting

## Alpha Channel 
Alpha channel is pixel "transparency" $\alpha\in [0, 1]$  

When representing RGBA pixel as RGB, we calculate the alpha composite   

$$C = \alpha_F C_F + (1-\alpha_F)C_B$$ 

where $F:=$ foreground, $B:=$background

## Matting Problem
We want to extract all the foreground pixels $F = [F_r, F_g, F_b]$ and matte $\alpha$, Given $B=[B_r, B_g, B_n], C=[C_r, C_g, C_b]$  
Therefore, for each pixel, the equation is 

$$C_{r,g,b}=\alpha F_{r,g,b} + (1-\alpha)B_{r,g,b}$$ 

Which are 3 equations and 7 unknowns

## Methods to solve Matting equation

### Known Background
If $B$ is known, and given there is no semi-transparency, i.e. $\alpha = \mathbb I(C=B)$
Therefore, we reduce $4$ unknowns

#### Problems 
Background must be known accurately, and constant  
Foreground subject cannot be similar to the background  
$\alpha$ is either 0 or 1, hence no semi-transparency

### Blue Screen Matting
Assume background contains only blue, i.e. $B = [0, 0, B_b]$, then  

$$C_r = aF_r, C_g = aF_g, C_b = (1-a)B_b$$

#### Problems
You cannot have any blue channel in the foreground, which is almost impossible. Also, "blue/green spilling" will have blue light reflected, make components blue

### Gray or Skin Colored Foreground
Constant, one-channel color background, and assume foreground color is proportional, such as gray $F:= [d, d, d]$, flesh$F:=[d, d/2, d/2]$. Then, 

$$C_r = aF, C_g = aF, C_b = aF + (1-a)B_v$$

The assumption is too strong

### Triangulation Matting
If there are two different background, with the same lighting and position, let the two backgrounds be $B_0, B_1$, then  

$$C_0 = aF + (1-a)B_0, C_1 = aF + (1-a)B_1$$

We have 6 equations, 4 unknowns

Then, to solve such system of equations, we can use a sparse matrix 

$$\begin{bmatrix}C_{0,r}\\C_{0,g}\\C_{0,b}\\C_{1,r}\\C_{1,g}\\C_{1,b}\end{bmatrix}
 = \begin{bmatrix}1&0&0&B_{0,r}\\0&1&0&B_{0,g}\\0&0&1&B_{0,b}\\1&0&0&B_{1,r}\\0&1&0&B_{1,g}\\0&0&1&B_{1,b}
\end{bmatrix}\begin{bmatrix}F_r\\F_g\\R_b\\\alpha\end{bmatrix}$$

$$b = Ax$$

So that we can approximate using psurdo-inverse, $x = (A^TA)^{-1}A^Tb$
