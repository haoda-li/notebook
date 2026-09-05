# Linear Regression

## Modular approach of a question
- Choose a __model__ describing the relationships between variables of interest
- __loss function__ quantifying how bad is the fit
- __regularizer__ saying how much we prefer different candidate explanations
- fit the model using an __optimization algorithm__

For supervised learning  
Given: target $t\in\mathcal T$ (response, outcome, output, class)  
features $x\in\mathcal X$ (inputs, covariates, design)  
Objective to learn a function $f:\mathcal X \rightarrow \mathcal T$ .s.t. $t\approx y = f(x)$

## Linear Regression

### Model

$$y = f(\vec x) = \sum_{j} w_j x_j +b$$ 

where $\vec x$ is the input, $y$ is __prediction__, $\vec w$ is __wights__, $b$ is the __bias__  
$\vec w, b$ are the __parameters__ 

In matrix form  
$y = XW$ where 

$$ X=
\begin{bmatrix}  
1&[x^{(1)}]^T\\
...&...\\
1&[x^{(D)}]^T
\end{bmatrix}, W = \begin{bmatrix}b&w_1&w_2&...&w_D\end{bmatrix}^T$$

### Loss Function (Squared error)
$\mathcal L(y, t) = \frac{(y-t)^2}{2}$ where $y-t$ is the residual and $\frac{1}{2}$ is just to make the calculations convenient. 


Therefore, define __cost function__ to be the average over all training examples  

$$\mathcal J(\vec w, b) = \frac{\sum^N (y^{(i)}- t^{(i)})^2}{2} = \frac{1}{2} \sum^N (\vec w^T \vec x^{(i)} + b - t^{(i)})^2$$

To minimize the loss/cost, calculate $\partial_{w_j} \mathcal J := 0, \forall j \in \{0,1,2,.., N\}, w_0 = b$   
The resulted 

$$\vec w^{L.S.} = (X^TX)^{-1}X^Tt$$

### Improving model: Polynomial curve fitting 
Consider __feature mapping__ $\psi(x):\mathbb R^D\rightarrow \mathbb R^M$, for example $x\in\mathbb R, \psi(x) = [1, x, x^2]^T$, so that we get a new $\vec x'$ and can be used into fit

#### Underfit and Overfit
Underfit: model is too simple to fit the data  
Overfit: too complex so that fit the data perfectly

### Improving model: L<sup>2</sup> Regularization
A function that quantifies how much we prefer one hypothesis vs. another

We encourage the weights to be small by choosing as our regularizer the $L^2$ penalty $\mathcal R(\vec w) := \frac{\|\vec w\|^2_2}{2}$  
The regularized cost function makes a trade-off between fit to the data and the norm of the weights  

$$\mathcal J_{reg}(\vec w) = \mathcal J(\vec w) + \lambda \mathcal R(\vec w)$$

Hence $\lambda$ is a hyperparameter that we can tune with a validation set and allows to vary penalty on dimensionality. 

When measuring the validation rate, we still measure $\mathcal J(\vec w)$, but for training we will use $\mathcal J_{reg}(\vec w)$ for determining $M$

__Probelms__ need to make sure $x_i$'s have approximately the same unit so that $\mathcal R(\vec w)$ is not dominated by some feature weights

For LS, regularized cost gives 

$$\vec w_\lambda^{Ridge} = arg\min_{\vec w} \mathcal J_{reg}(\vec w)= (X^T X+\lambda I)^{-1}X^T t$$

### L<sup>1</sup> Regularization  
$\mathcal R_{L^1} = \sum |w_i|$ encourages weights to be exactly zero, we can design regularizers based on whatever property we'd like to encourage. 

## Conclusion
- Choose a model and a loss function
- Formulate an optimization problem
- Solve the minimization problem using either direct solution (set derivative to zero) or gradient descent (move $\vec w$, start with a guess, slowly changes to minimize cost, when direct solution is unavailable)
- __vectorize__ 
- use __features__ to get a more powerful linear model
- improve the generalization by adding a __regularizer__

