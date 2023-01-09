# Extra. Stone Weierstrass Theorem

## _Def'n_. Function Algebra

For $\mathcal A\subset C([a,b])$, that follows  

 - (linearity) $\forall f,g\in \mathcal A. \forall a,b\in\mathbb R. af + bg\in \mathcal A$
 - (closed under product) $\forall f,g\in\mathcal A. f\cdot g\in \mathcal A$
 
## _Thrm 1_. 
For $\mathcal A\subset C([a,b])$ be a function algebra,  
IF  

 - (vanishes nowhere) $\forall p\in [a,b]. \exists f\in \mathcal A. f(p)\neq 0$
 - (separates points) $\forall x\neq y \in [a,b]. \exists h\in\mathcal A. h(x)\neq h(y)$  
 
THEN $\mathcal A$ is dense in $C[a,b]$, i.e. $\forall f\in C[a,b]. \exists \{f_n\}\in \mathcal A. \{f_n\}\rightarrow^{u.c.} f$

## _Thrm 2_.
$\mathcal A_{trig}:= \{a_0 + \sum_{k=1}^N a_k\cos(kn) + \sum_{k=1}^N b_k \sin(kn) | a_k, b_k\in\mathbb R. N\in\mathbb N\}$ is dense in $C[-\pi, \pi]$

_proof_. Consider the assumptions of SWT  
Let $f$ have coefficients $a_k, b_k, M$, $g$ have $a'_k, a'_k, N$, let $c,d\in\mathbb R$. wlog, assume $M\geq N$, extend $a'_k, b'_k = 0. \forall k > N$

(linearity) $ca_0 + da'_0 + \sum (ca_k + da'_k)\cos(kn) + \sum(cb_k + db'_k)\sin(kn)\in \mathcal A_{trig}$  

(product) Using half angle formula $\cos(a)\cos(b) = \frac{1}{2}cos(a+b) + cos(a-b)$ and other similar ones, we can break all the products of trig functions back to a sum, hence rearrange the summation coefficients. 

(vanish nowhere) For any $a_0 + \sum a_k\cos(pn) + \sum b_k\sin(pn) = 0$, take $a_0' = a_0 + 1$ and others remain unchanged. 

(separates points) Take $a\neq b\in[-\pi,\pi]$. Using periodicity of trig functions  
If $a\neq -b. \cos(a)\neq cos(b)$, if $a = -b. \sin(a)\neq [sin(-a) = \sin(b)]$

Therefore, we can apply SWT
