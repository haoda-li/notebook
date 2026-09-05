# Amortized Analysis

## Amortized Complexity

Let $\sigma = (\sigma_i)_1^m$ be a sequence of operations on data structure $D$, and $t_i$ be the time to execute $\sigma_i$. Let $S$ be the set of all valid sequence of operations on $D$ so that $\sigma\in S$. 

__Sequence complexity__   $C(m) = \max\{\sum_1^m t_i: \sigma \in S\}$.   
__Amortized complexity__  $A(m) = \frac{C(m)}{m}$ time each operation takes in average. 

### Aggregate Analysis
In aggregate analysis, we show that for all $n$, a sequence of $n$ operations takes
worst-case time $T(n)$ in total. In the worst case, the average cost, or amortized
cost, per operation is therefore $T(n)/n$.

### Accounting Method
We assign differing charges to different operations, with some operations charged more or less than they actually cost. The amount charged on each operation is called __amortized cost__. When an operation's amortized cost exceeds its actual cost, the differnt is assigned to specific objects in the data structure as __credit__. 

In the worst case analysis, we have to make such that the the amortized cost provides an upper bound on the actual cost. Which mean that for all sequences of $n$ operations. $\sum^n \hat c_i \geq \sum^n c_i$ where $\hat c_i$ is the amortized cost for ith operation, $c_i$ is the actual cost. Then, the total credit stored is $\sum^n \hat c_i - \sum^n c_i \geq 0$ all the time. 

### [+] Potential Method
As an extension to accounting method, we represents the prepaid work (credit in accounting method) as "__potential__". We associate the potential with the data structure instead of specific objects within the data structure. 

Let the state of an initial data structure as $D_0$, and $D_i$ be the state of the data structre after applying the ith operation to $D_{i-1}$. Define a __potential function__

$$\Phi: \{D_0, ..., D_{n-1}\}\rightarrow \mathbb R$$ 

to be the potential associated with data structure $D_i$. Then, the amortized cost $\hat c_i$ of the ith operation w.r.t. potential function $\Phi$ is defined by 

$$\hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$$

and the total amortized cost of the n operations is 

$$\sum_{i=1}^n \hat c_i = \sum_{i=1}^n (c_i + \Phi(D_i) - \Phi(D_{i-1})) = \sum_{i=1}^n c_i + \Phi(D_n) - \Phi(D_0)$$



## Example: Binary Counter
Consider a binary counter increment, which keeps a number $x\mod 2^k$ be increament. The data structure used is a sequence $A:=(b_0, ..., b_{k-1}), b_i \in \{0, 1\}. x = \sum_{i=0}^{k-1} a_i 2^i$. 

```py title="increment(A)" linenums="1"
j = 0
while j < A.k and A[j] == 1:
    A[j] = 0
    j += 1
if j == k:
    A[j] = 0
A[j] = 1
```

### Aggregate Analysis
Consider the number of bits flipped in each increment be the actual cost, we know that $A[i]$ flipped every $2^i$ time. 
Thus, let $N_j$ be the number of jth bit flips. we have the total cost

$$C(m) = \sum_{j=0}^{k-1} N_j = \sum_{j=0}^{k-1} \lfloor \frac{m}{2_i}\rfloor \leq m\sum_{j=0}^{k-1} 2^{-i} = 2m$$

$$A(m) = C(m)/m = 2\in O(1)$$

### Accounting Method
charge an amortized cost of 2 dollars to set a bit to $1$. When a bit is set we use 1 dollar, and the other 1 dollar as credit to be used later when we flip the bit back to 0. Therefore, every 1 in the counter has a dollar of credit, so that we charge nothing to reset a bit to $0$. Since there will always be 1 in $A$, the amount of credits is always positive. Thus, the total amortized cost is $C(n)\in O(n)$ and  $A(n)\in O(1)$

### [+] Potential Method
Suppose that ith operation set $t_i$ bits from 1 to 0. Then $c_i \leq t_i + 1$.  
Define $\Phi(A_i) := \sum_{j=0}^{k-1}\mathbb I(b_j = 1)$, i.e. the number of 1's in $A_i$. 
Then, $\Phi(A_i) - \Phi(A_{i-1}) \leq -t_i + 1$ since at least $t_i$ number of 1's in $A_{i-1}$ so that they can be reset by ith operation, and at most one 0-bit can be flipped to $1$ in each operation. 
Therefore

$$\hat c_i = c_i +\Phi(A_i) - \Phi(A_{i-1}) \leq t_i + 1 -t_i + 1  = 2$$

We know that $\Phi(D_0) = 0, \Phi(D_n) \leq k$ so that 

$$C(n) = 2n -k \in O(n), A(n) \leq 2 \in O(1)$$

## Example: Dynamic Table

Instead of using linked list in chaining implementation, we instead us a dynamic sized table. For each bin, we store a pointer to an array `arr`, a number `size` to be the number of elements stored, and `maxsize` to be the array length. Then, insert is implemented as 

```py title="insert(T, x)" linenums="1"
if T.size == T.maxsize:
    allocate new_arr of size 2 * T.maxsize
    T.maxsize *= 2
    copy T.arr into new_arr # T.size ops
    T.arr = new_arr
T.arr[T.size] = x # 1 op
T.size += 1
```

Let $d(T) := \text{size}/\text{maxsize}$ be the load factor, assuming that we start with $\text{maxsize} = 1$. After each `insert`, we have that $0.5 < d(T) \leq 1$ since we only double `maxsize` when `size == maxsize`. 

### [+] Potential Method
Define $\Phi(T_i) = 2 \times$ number of occupied slot in the second half of `arr`. 

$$\Phi(T_i) = 2 (\text{size} - \text{maxsize}/2) = 2\text{size} - \text{maxsize}$$

Then, we have two cases to consider 

If $T_i.\text{size} = T_i.\text{maxsize}$, then we have the cost 

$$c_i = T_i.\text{size} + 1$$

Also we know that $T_{i-1}.\text{size} = T_i.\text{size} - 1, T_{i-1}.\text{maxsize} = T_i.\text{maxsize} / 2$. Thus

\begin{align*}
\phi_i - \phi_{i-1} &= 2T_i.\text{size} -  T_i.\text{maxsize} - 2(T_i.\text{size} - 1) + T_i.\text{maxsize} / 2\\
&= 2 - T_i.\text{maxsize}/2
\end{align*}

From the `if` condition, we also have that $ T_i.\text{maxsize}/2 =  T_i.\text{size} - 1$

$$c_i + \phi_i - \phi_{i-1} = T_i.\text{size} + 1 + 2 - T_i.\text{size} + 1 = 4\in O(1)$$

If $T_i.\text{size} < T_i.\text{maxsize}$, then we have the cost 

$$c_i + \phi_i - \phi_{i-1} = 1 + 2 = 3 \in O(1)$$

### Accounting Method

For each `insert`, we charge $3$ dollars. 1 dollar for setting $x$, and 2 dollar as credit. When the if branch runs, for each index $i$, it pays for the cost of copying itself and the slot $i - T.\text{maxsize} / 4$. Consider one iteration before the `if` branch runs. Known that `T.size == T.maxsize` then the second half have 2 credits since they have never been copied. Thus, they have enough credit to pay for the cost of the first half. 

### Aggregate Analysis
After $n$ insert, the `maxsize` of the table will be $2^{\lceil \lg n\rceil}$, thus we have doubled the table size $\lceil \lg n\rceil - 1$ times. Each time copies $2^0, 2^1, ..., 2^{\lceil \lg n\rceil - 1}$ elements. Thus, the total costs will be 

$$C(n) = n + \sum_{i=0}^{\lceil \lg n\rceil - 1} 2^i = n + 2^{\lceil \lg n\rceil} - 1 \leq n + 2^{\lg n + 1} = 3n$$
