# Set: Hash Tables

## Hash Table

For hash table, we take some __hash function__ $hash: \mathcal U \rightarrow\{0, 1, ..., m - 1\}$ where $\mathcal U$ is the universe that keys are chosen from, and $m$ is the number of bins pre-defined for hash table. 

Then, we use the hash function to determine which spot should we insert the (key, value) into. Thus, when we want to, we can directly find the spot by running the hash function again. 

However, in most cases $|\mathcal U| >> m$ so that there must exist $x_1 \neq x_2\neq \cdots x_k. hash(x_1) = \cdots hash(x_k)$. In this case, we call it a __collision__. The main goal for hash table is to resolve collision problem, and to choose "good" hash function. 

### Hash Functions
Some good hash function examples for natural number keys $k$ (note that any key is essentially bits, which can be seen as unsigned intergers) are 

- __division method__: $hash(k) = k\mod p$ where $p \geq m$ is a prime number.  
    - We'd like to make such the remainder by a prime number, so that it's more likely to depent on all bits of the input key instead of a fixed range of bits. For example, if we use $k\mod 2^i$, then it will only depend on the last $i$ bits of $k$. 
    - Since it only takes one division operation, it is quite fast. 

- __multiplication method__: $hash(k) = \lfloor m (k A - \lfloor kA\rfloor)\rfloor$ where $0 < A < 1$. 
    - This method fits well with binary based operations and when $m$ is set to be a power of 2. 
    - Often $A\approx (\sqrt 5 - 1)/2 = 0.6180339887$ is likely to work reasonably well. 

## Closed Addressing (Chaining)
To resolve a __collision__, the simplest way is to implement each bin as a linked list (or other list implementations, but runtime analysis will be harder), which is called __chaining__, or __closed addressing__.

Specifically,

- Object: fix-sized array of bins
- Operation:   
    - `search(H, x)`: return whether $x$ it's in `H[hash(x)]`
    - `insert(H, x)`: insert $x$ into `H[hash(x)]`
    - `delete(H, x)`: delete $x$ from `H[hash(x)]`

Assuming __simple uniform hashing__, i.e. the expected value of each bin size $a := E(b_i) = n/m$, where $n$ is the size of elements. Further assume that the hash function takes $O(1)$ time. 
#### Runtime analysis

__Claim 1.1__ `insert` takes worst case $O(1)$ time.  
_proof_. insert the new node to the head (only update 2 pointers). 

__Claim 1.2__ Under simple uniform hashing assumption, `search` takes average-case $\Theta(1+a)$ time.   
_proof_. For unsuccessful search, the time needed is 1 hash and traverse the linked list in the bin, which takes $a$ time. 

For successful search, there are $n$ cases for input $x$, i.e. $n$ keys in the table, assuming that each element in the table has $1/n$ probability being searched. Define $I_{ij}$ be the indicator random variable that the ith key and jth key being inserted to the same bin. By simple uniform hashing, the probability that $P(I_{ij} = 1) = 1/m$, thus by Bernoulli distribution, $E(I_{ij}) = 1/m$. Then, to find some node $i$, we need to compare the searched key with all nodes before $i$, and by our `insert`, those are nodes inserted after $i$; and then $i$. Therefore, for some node $i$, the number of elements compared is 
$1 + \sum_{j=i+1}^n I_{ij}$. We can write the average case time as 

\begin{align*}
E(T(n)) &= E(\sum_{i=1}^n \frac{1}{n} (1 + \sum_{j=i+1}^n I_{ij}))\\
&= \frac{1}{n} \sum_{i=1}^n (1 + \sum_{j=i+1}^n E(I_{ij}))\\
&= \frac{1}{n} \sum_{i=1}^n (1 + \sum_{j=i+1}^n \frac{1}{m})\\
&= 1 + \frac{1}{nm}(n^2 - \frac{n(n+1)}{2})\\
&= 1 + \frac{a}{2} - \frac{a}{2n}\\
&\in \Theta(1+a)
\end{align*}

__Claim 1.3__ Under simple uniform hashing assumption, `delete` takes average-case $\Theta(1+a)$ time.   
_proof_. search, and then constant time to update pointers. 

Note that, if $n/m$ is proportional, then $a\in O(1)$. Thus, all operations take constant worst case expected time. 

## Open Addressing
For __open addressing__, we have 

- Object: fix-sized array (key, value) of size $M$
- Operation:
  - `search(H, x)`: seach for each of `H[h(x, 0)], H[h(x, 1)], ...` until find or encountered `None`
  - `insert(H, x)`: try `H[h(x, 0)], H[h(x, 1)], ...` until we find `None` or `DEL` at `i`, then insert into `H[h(x, 1)]`. 
  - `delete(H, x)`: search for $x$, say at `H[h(x, 0)]`, then make `H[h(x, 0)] = DEL`

The successively examining of `H[h(x, 0)], H[h(x, 1)], ...` is called __probing__. 

First, note that our array eventually have size $M \geq n$, otherwise we are unable to store all wanted key, value pairs, since the table can be filled up. 

Then, Note that in this case, $h(x, i)$ take a key $x$ and a counter $i$. We define this as a parameterized hash function

$$h: \mathcal U \times \{0, ..., M - 1\} \rightarrow \{0, ..., M - 1\}$$

Consider the sequence $(h(x, i))_{i=0}^{M-1}$, calling it the __probe sequence__ of key $x$. It must be a permutation of $\{0, 1, \cdots, M-1\}$ so that the sequence performs like the insertion order for $x$. 
We want to make the __uniform hashing__ assumption, i.e. $h$ generates probe sequence for each key being equally likely to be any of $M!$ permutaions of $\{0, ..., M-1\}$. Unfortunately, such assumption is hard to implement. 

The following techniques guarentee that the probe sequence for each key $x\in\mathcal U$ is valid. However, the mast number of probe sequences that they can generate is $m^2$. Thus none of them satisfy the uniform hashing assumption. 

All methods uses the ordinary hash function $hash$ we defined above, refers to as __auxiliary hash function__. We know that $hash$ will collide, so that we want to avoid collision by the additional $i$. 

### Linear Probing

$$h(x, i) = (hash(x) + c_0i) \mod M. \quad c_0\in\mathbb N^+$$

Consider the example of $c_0=1$, then the probe sequence is simply $(hash(k), hash(k) + 1, ...,M-1, 0, 1, ...)$.  
However, linear probing suffers from __primary clustering__. Clusters arise because an empty slot preceded by i full slots gets filled next with probability $(i+1)/M$. Thus, the longer it runs, the occupied slots tend to get longer. Also, if $hash(x) = hash(y)$, then their probe sequences are the same. 

### Quadratic Probling

$$h(x, i) = (hash(x) + c_0i + c_1i^2) \mod M.\quad c_0, c_1\in\mathbb N^+$$

The same issue that if if $hash(x) = hash(y)$, then their probe sequences are the same. Also, it still suffers clustering problem, but milder than linear probing.

### Double Hashing

$$h(x, i) = (hash_1(x) + i \cdot hash_2(x)) \mod M$$

It is "double" as we use two different hash functions. Thus, the chance that $hash_1, hash_2$ both collide is much reduced. In practice, this tends to give the best results. 

## Universal Hashing

With a fixed hash function, then a malicious adversary can choose $n$ keys that all collide with each other. The only efficient way to improve the situation is to randomly sample hash functions in a way that is independent of the keys that are actually going to be stored. 

The approach is called __universal hashing__, at the beginning of hashtable construction, we randomly pick a hash function from a class of functions. Therefore, given a fixed sequence of input and opeartions, each execution will have different results, and guarentees a good average case time. 

Let $\mathcal H$ be a finite collection of hash functions $h: \mathcal U \rightarrow \{0, 1,..., m-1\}, \mathcal H = \{h_1,...,h_n\}$. $\mathcal H$ is __universal__ if for each pair of distinct keys $k_1, k_2\in\mathcal U$. There are at most $|\mathcal H|/m$ hash functions $h\in\mathcal H$ s.t. $h(k_1) = h(k_2)$. 

In other words, with a hash function randomly chosen from $\mathcal H$, for any pair of distinct keys $k_1, k_2$,

$$P(h(k_1) = h(k_2))\leq 1/m$$

### Universal Hashing Theorem

__Claim__ Using universal hasing and chaining. The worst case expected running time for `search` is $1 + \frac{n}{m}$. 

_proof_. The settings are very much similar to the average case running time for chaining, but note that we are now considering expected running time instead of average running time.  

Let $h\in\mathcal H$ be chosen randomly, let $n$ be the size of data in the table $T$, define $a = n/m$ be the load factor. $I_{ij} =\mathbb I(h(k_i) = h(k_j))$. Since $h\in\mathcal H$, $I_{ij} = P(h(k_i) = h(k_j))\leq 1/m$. 

Define the random variable $Y_i$ be the number of keys other than $k_i$ that is in the same bin as $k_i$. Then, 

$$E(Y_i) = E[\sum_{k_j\in T, i\neq j} I_{ij}] \leq \sum_{k_j\in T, i\neq j} \frac{1}{m}$$

Thus, for unsuccessful search, $k_i\not\in T, E(Y_i) \leq  \sum_{k_j\in T} \frac{1}{m} = \frac{n}{m}$.    
for successul search, $E(Y_i) \sum_{k_j\in T, i\neq j} \frac{1}{m} = \frac{n-1}{m}$.

Let the random variable $n_{h(k)}$ be the number of linked list nodes traversed in bin $h(k)$,   
for unsuccessful search, it traverses all nodes, $E(n_{h(k_i)}) = E(Y_i) \leq n/m$;  
for successful search, it traverses all nodes plus $k_i$ itself, $E(n_{h(k_i)}) = E(Y_i)  + 1\leq \frac{n-1}{m} +1 < \frac{n}{m}+1$;  

### Universal Class of Hash Functions

For $\mathcal U = \{0, 1, ..., 2^{w} - 1\}$, for a hash table with $m=2^M$ bins, the following family of hash functions is universal

$$\mathcal H_{M, w} = \{h_{ab} = ((ak + b)\mod 2^w) // 2^{w-M} : 0 < a < 2^w, a\text{ is odd}, 0\leq b < 2^{w-M}\}$$

This family is very natural for binary based computers. Note that $\mathcal U$ represent is the set of binary representations of unsigned intergers with $w$ bits, typically we have $w = 16, 32, 64$. Then, $ak+b$ is unsigned integer arithmetic, $\mod 2^w$ is simply taking the last $w$ bits, and $// 2^{w-M}$ is a bit shift, taking the $M$ left most bits. 

For a hash table with $m$ bins, let $p > m$ be prime, define $\mathbb Z_{p} = \{0, 1, ..., p-1\}, \mathbb Z_p^* =  \{1, ..., p-1\}$. The following family of hash functions is universal

$$\mathcal H_{p, m} = \{h_{ab} = ((ak + b)\mod p)\mod m : a\in Z_p^*, b\in Z_p\}$$


## Implementation

???quote "Header for hashset"

    ```c title="hash.h"
    --8<-- "csc265/assets/hash.h"
    ```

[More about the dynamic list](./amortized.md)
