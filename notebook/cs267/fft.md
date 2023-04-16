# Fast Fourier Transform

## Discrete Fourier Transform (DFT)
Given an 1D vector $v\in\mathbb R^m$, the 1D DFT is $\mathcal F\cdot v$ where $\mathcal F\in\mathbb R^{m\times m}$ is defined as 

$$F_{j,k} = \omega^{j\times k}, 0\leq j,k\leq m - 1$$

where $\omega$ is a complex number whose $m$'s power $\omega^m = 1$

$$\omega = e^{2\pi\frac{i}{m}} = \cos(\frac{2\pi}{m}) + i\sin(\frac{2\pi}{m})$$

2D DFT of an $m\times m$ matrix $V$ is $\mathcal F V \mathcal F$, which is equivalent to do 1D DFT on all columns independently, and then all the rows. 

### Applications 

FFT is often used in frequency filtering (convolution theorem), compressions (same idea), and interestingly, solving Poisson's equations. 

The Poisson's problems can be written as solving $L_1X + XL_1 = B$ and note that 2D FFT works similar to Eigen-decomposition, actually we have that $L_1 = F \Lambda F^{-1}$ being a eigen decomposition where 

$$F_{j,k} = \sqrt{\frac{2}{m+1}} \sin(\pi\frac{jk}{m+1}), \Lambda_j = 2(1 - \cos(\pi \frac{j}{m+1}))$$

we can substitute $L_1 = F\Lambda F^T$ and transform the RHS $B$ by $B = FB'F^T$, and then we can solve the whole thing as 

\begin{align*}
F \Lambda F^{-1} X + X F D F^T &= FB'F^T\\
F(\Lambda (F^TXF) + (F^TXF)D)F^T &= FB'F^T\\
DX' + X'D &= B' &X'_{jk} = \frac{B'_{jk}}{\Lambda_j + \Lambda_k}\\
X &= FX'F^T
\end{align*}

Thus, the total cost is 2 2D FFT , $m^2$ adds, and $m^2$ divisions. all of which in $O(m^2\log m)$

## Serial Algorithms

For each entry of FFT $F\cdot v$,  

$$(F\cdot v)_j = \sum_{k=0}^{m-1} F_{j,k} v_k = V(\omega^j), V(x) = \sum_{k=0}^{m-1} x^k v_k$$

Therefore, FFT is the same as evaluating a degree $m-1$ polynomial $V(x)$ at $m$ different points. 

### Divide and Conquer FFT

Note that we can decompose $V$ into even and odd components

\begin{align*}
V(x) &= \sum_{k=0}^{m-1} x^k v_k\\
&= (v_0 + x^2 v_2 + x^4 v_4 + \cdots) + x(v_1 + x^2 v_3 + x^4 v_5 + \cdots)\\
&= V_{even}(x^2) + V_{odd}(x^2)
\end{align*}

Each $V_{even}$ and $V_{odd}$ has degree $\frac{m}{2}-1$, and we note that $(\omega^{j+\frac{m}{2}})^2 = \omega^{2j}\omega^m = (\omega^j)^2$, hence we are only evaluating $m/2$ different points. 

Therefore, we have the algorithm

```py title="FFT_DnC"
"""
Assume that m is power of 2
"""
def FFT(v, omega, m):
    if m == 1:
        return [v[0]]
    v_even = FFT(v[0::2], omega ** 2, m / 2)
    v_odd = FFT(v[1::2], omega ** 2, m / 2)
    omega_precomp = [omega ** i for i in range(m/2)]
    return concat(
        v_even + omega_precomp * v_odd,
        v_even - omega_precomp * v_odd,
    )
```

The time complexity, by Master's theorem, is $T(m) = 2T(m/2) + O(m) \in O(m\log m)$. 

### Parallel FFT
Consider the stack tree of the recursive calls, it has $m$ leaves and $\log m$ depth. Therefore, instead of doing top-down recursion, we can do bottom-up computations, which gives a natural way for parallelizing the algorithm. 

Then, consider the recursive call, note that the divide is done by odd/even, or the last digit of the binary. Now, consider $m=2^4$, the stack tree looks like

```
XXX
XX0             XX1
X00     X10     X01     X11
000 100 010 110 001 101 011 111 
```

Note that from left to right, the leaves are ordered by reversed bit order. Therefore, what we can do is to compute FFT at each level, rewrite the elements $v_i = (F\cdot v)_{\text{bitreverse(i)}}$.

Then, for $p$ processors, the computation takes $2m\log m / p$, for communications, we need $\log(p)$ stages and $m\log(p)/p$ words. 

