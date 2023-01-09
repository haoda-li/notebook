# Pivoting

## Permutation Matrices
Has exactly one $1$ in each row and all others are $0$ and the same for each column. i.e. a permutation of rows/columns of $I$. 

If we want to interchange column 1 and column J, then let $E_{ij}$ denote the zero matrix with the $ij$'s entry be $1$. 

\begin{align*}
P &= I - (e_i - e_j)(e_i-e_j)^T\\
&= I - (e_ie_i^T - e_ie_j^T - e_je_i^T + e_je_j^T)\\
&= I - E_{11} + E_{1j} + E_{j1} - E_{jj}
\end{align*}

Is a identity matrix that interchange rows $i,j$. 

So that $PA$ interchanges row of $A$ and $AP$ interchanges column of $A$ 

A permutation matrix is non-singular and $P^{-1} = P^T$

$P$ is closed under multiplications:  
By definition, there is only one $1$ on each row and column of $P_1$, so that consider $P_2$, which only interchanges rows, and the resulted matrix will still have only one $1$ on each row, and since columns are not interchanged, the property of permutation is maintained. 

## Pivoting (Row partial pivoting)
### Intuition
Consider $A =\begin{bmatrix}\epsilon&1\\1&1\end{bmatrix}, \epsilon$ is small, $b = \begin{bmatrix}1\\2\end{bmatrix}$. Then the multiplier $m_{21} = \epsilon^{-1}$.  
The decomposition $L = \begin{bmatrix}1&0\\\epsilon^{-1}&1\end{bmatrix}, U = \begin{bmatrix}\epsilon&1\\0&1-\epsilon^{-1}\end{bmatrix}$.   
However, if $\epsilon$ is very small, $\epsilon^{-1}$ is extremely large and $U\rightarrow \tilde U =\begin{bmatrix}\epsilon&1\\0&-\epsilon^{-1}\end{bmatrix}$, and $L\tilde U = \begin{bmatrix}\epsilon&1\\1&0\end{bmatrix}$

Note that $A^{-1} = (-1+\epsilon)^{-1} \begin{bmatrix}1&-1\\-1&\epsilon\end{bmatrix}, \tilde A = L\tilde U = -1\begin{bmatrix}0&-1\\-1&\epsilon\end{bmatrix}$. If we want to solve  
$Ax = [1,2]^T, x = A^{-1}b\approx [1,1]^T, \tilde x = \tilde A^{-1}b \approx [2, 1]^T$

However, if $A = 
\begin{bmatrix}
1&1\\
\epsilon&1
\end{bmatrix}, b = \begin{bmatrix}2\\1\end{bmatrix}\Rightarrow m_{21} =\epsilon, M_1 = \begin{bmatrix}
1&0\\
-\epsilon&1
\end{bmatrix} \rightarrow U = \begin{bmatrix}
1&1\\
0&1
\end{bmatrix}, M_1 b = \begin{bmatrix}
2\\1
\end{bmatrix}, x = [1,1]^{-1}$

### Algorithm
Searching first column for element of largest magnitude

$$A_{J\cdot}, J = arg\max_{1\leq j \leq n}\{|a_{j1}|\}$$

Then use a permutation matrix $P_1$ to interchange $A_J\cdot$ with $A_1\cdot$ and calculate $M_1$ so that $|m_{i1}|\leq 1$  
So that we can do such recursively on $A_{1:n\times 1:n}$ and so on

Therefore, we have $M_{n-1}P_{n-1}...M_1P_1A$

### Decompose pivoted matrix
Consider $MPA = U\Rightarrow PA = M^{-1}U$, since the pivot, all $m_{ij}\leq 1$ so that $L$ has all the lower triangular entries be $|L_{ij}|\leq 1$

### Solving linear systems
Given $Ax =b$, since $P$ is non-singular $PAx = Pb$, Let $\hat b = Pb, LU x = \hat b$, and we solve it as before. 

### Example 

$$A = \begin{bmatrix}-2&10&1\\1&-4&2\\4&-8&4\end{bmatrix}, b = \begin{bmatrix}4\\3\\1\end{bmatrix}$$

Let $P_1 = \begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}, P_1A = \begin{bmatrix}4&-8&4\\1&-4&2\\-2&10&1\end{bmatrix}, M_1 = \begin{bmatrix}1&0&0\\-1/4&1&0\\1/2&0&1\end{bmatrix}, M_1P_1A = \begin{bmatrix}4&-8&4\\0&-2&1\\0&6&3\end{bmatrix}$  
$P_2 = \begin{bmatrix}0&1\\1&0\end{bmatrix}, M_2=\begin{bmatrix}1&0\\1/3&1\end{bmatrix}, M_2P_2M_1P_1A = \begin{bmatrix}4&-8&4\\0&6&3\\0&0&2\end{bmatrix} = U$

## Finding PA = LU
Noting that $P_{k+1}M_k \neq M_kP_{k+1}$, but suppose we have $P_{k+1}M_k = \hat M_k P_{k+1}$, then we can have 

$$M_nP_n...M_1P_1A = b \Rightarrow P_n...P_1A = \hat M_1^{-1}...\hat M^{-1}_n b$$

Since $P^T = P^{-1}, P_2M_1P_2^T = \hat M_1 P_2P_2^T = \hat M_1P_2P_2^{-1} = \hat M_1$  

$$\hat M_1 = P_2(I-m_1e_1^T)P_2^T = P_2P_2^T - P_2m_1e_1^TP_2^T = I - (P_2m_1)(P_2e_1)^T$$

By the design of the algorithm, $P_2$ will not interchange the first columns, hence $P_2e_1 = e_1$, but $P_2m_1$ will interchange the multipliers, let $\hat m_1 = P_2m_1$.  

Also, consider the intuition behind: $M_1P_2^T$ only change $[2:n]$ columns, which does not touch the first column ($m$'s), $P_2M_1$ cannot change the first row, but the order of $m$'s. Then consider $M_1[2:n, 2:n] = I_{(n-1)\times (n-1)}$, there's only $1$ on the diagonal,  interchanging $i,j$ row plus interchanging $i,j$ column will just swap them back. Therefore, the only change thing is the order of $m$'s, i.e. $m_i, m_j$ are swapped. 

Therefore, because $m_1e_1^Tm_2e_2^T = 0$ (see notes on LU decomposition)

$$\hat M_1^{-1} = I + \hat m_1e_1^T, M_1^{-1}M_2^{-1} = (I + \hat m_1e_1^T)(I + \hat m_2e_2^T) = I + \hat m_1e_1^T + \hat m_2e_2^T$$

Therefore, $L = I + \sum \hat m_k e_k^T, P = \prod P_k$

### Solving system of linear equations
Let $\hat b = Pb$, since we have computed $PA=LU, PAx = Pb\Rightarrow LUx = \hat b\Rightarrow Ly = \hat b$

You can just store $P$ as a vector form, and we know we only need to interchange $(n-1)$ times. 

## Find Determinant
Note that $P_k$ is either identity or interchange two rows, $\det(I)=1$, but if we interchange two rows $\det(P_k)=-1$.   Considered the matrix where the interchanged 1's are on the corner, for such matrix, determinant is $-1$ and for the other parts, it's $1$. 

\begin{align*}
\det(PA) &= \det(LU)\\
\det(P)\det(A)&=\det(L)\det(U)\\
\det(A) &= \det(P)^{-1}{\det(L)\det(U)}\\
&=\det(P)^{-1}[1][\prod_i^n u_{kk}]\\
&= \prod_i^n u_{kk} * (-1)^{\text{number of interchanges} \% 2}
\end{align*}

## Computation Time
Consider $A_{n\times n}$  

- Find the largest magnitude in the first column takes $n$ comparisons  
- Swap the two rows takes $n$ swaps. 
- Then we are doing the normal Gaussian elimination steps, which takes $n-1$ divisions and $(n-1)^2$ addition and multiplications. 

Notice that the next stage will just work recursively on $A_{n-1\times n-1}$. 
Therefore, the total comparisons and swaps will be $\frac{n(n-1)}{2}$, Gaussian elimination takes $\frac{n^3}{3} + O(n^2)$

### Solving x
Then consider $Ux = Lb$
 - Since $P$ matrix only swaps, each $P_i$ takes 1 swap
 - $M_i$ takes $(n-i)$ adds and multiplications

Therefore, the total computation takes $\frac{n^2 - n}{2}$ adds and multiplications and $(n-1)$ swaps. 
