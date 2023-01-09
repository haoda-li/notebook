# Exact Inference

## Exact Inference as Conditional Distribution

As one of the tasks on Probabilistic Models.

Consider a probabilistic models, where we are given 

 - some observed evidence $X_F$, and 
 - some unobserved random variables $X_F$ that we are interested in the distribution 
 - other variables $X_R$ that are not observed and not intersted. 

Inference is intersted in finding the conditional distribution

$$p(X_F|X_E) = \frac{p(X_F, X_E)}{\sum_{X_F}p(X_F, X_E)} = \frac{\sum_{X_R}p(X_F, X_E, X_R)}{\sum_{X_R} \sum_{X_F}p(X_F, X_E, X_R)}$$

Thus, we need to marginalize all $X_R$, and consider the conditional probability. 

## Variable Elimination

Consider the conditional distributino encountered, note that we need to do a huge number of summations. For example, consider a simple chaining of variables $A\rightarrow B\rightarrow C\rightarrow D$ and we are interested in 

$$p(D) = \sum_{A,B,C}p(A,B,C,D) = \sum_{A,B,C} p(A)p(B|A)p(C|B)p(D|C)$$

If we do the summation naively, it will be

```python
p = 0
for a in A:
    for b in B:
        for c in C:
            p += p(a) * p(b|a) * p(c|b) * p(d|c)
```

Resulting $O(k^n)$ time, where $k$ $k$ is the number of states in each variable and $n$ is the number of variables. 

On the other hand, we can use dynamic programming by decomposing the triple summations, to do __varaible elimination__. Obverse that 

\begin{align*}
p(D) &= \sum_A\sum_B\sum_C p(A)p(B|A)p(C|B)p(D|C)\\
&= \sum_C p(D|C)\sum_Bp(C|B)\sum_A p(A)p(B|A)\\
&= \sum_C p(D|C)\sum_Bp(C|B)p(B)\\
&= \sum_C p(D|C)p(C)
\end{align*}

Thus, the runtime is reduced to $O(nk^2)$

### Intermediate Factors
Consider the distribution given by 

$$P(X,A,B,C) = p(X)p(A|X)p(B|A)p(C|B,X)$$

Suppose that we'd like to marginalize over $X$, so that 

$$P(A,B,C) = \sum_X p(X)p(A|X)p(B|A)p(C|B,X) = p(B|A)\sum_X p(X)p(A|X)p(C|B,X)$$

However, $\sum_X p(X)p(A|X)p(C|B,X)$ is not a valid conditional or marginal distribution, since it is unnormalized. 

Note that the only purpose we write these intermediate distribution is to cache them in dynamic tables for the final computation results. Thus, we don't necessarily need them to be a distribution, until we finish the computations. 

Additionally, for each conditional distributions $P(A|B)$, it is a function of variables $A,B$. Thus, we introduce __factor__ $\phi$ which are not necessarily normalized distributions, but describe the local relationship between random variables.

In addition, for the summation that we want to temporarily store. We introduce another intermediate factor $\tau$, for example, we can let $\tau(A,B,C) = \sum_X p(X)p(A|X)p(C|B,X)$ so that we have $X$ eliminated. More formally, 

$$\tau(Y) = \sum_z \prod_{\phi\in \Phi}(z_{scope(\phi)\cap Z}, y_{scope(\phi)\cap Y}).\forall Y$$

where, for dag, $\Phi$ is given by 

$$\Phi = \{p(x_i | \text{parents}(x_i))\}_{i=1}^N$$

## VE Implementation

Note that the above VE algorithm is an abstraction. Where we are summing up probability functions for each state. Now, consider an implementation where each variable has finite number of states, and each state $p(X=x)$ is associated with a fixed number so that the probability functions are well-defined.

Consider a set of conditional probabilities $\phi\in\Phi$, a set of query variables $X_f \in Q$, set of evidence variables $X_e \in E$ with observed values $X_e = x_e$ and a sequence of remaining variables $X_r\in Z$. 

```python title="VE(Phi, Q, E, R)"
for each observed variable Xe in E:
    for each factor phi(..., Xe) that mentioned Xe:
        replace factor with restricted factor phi(..., Xe=xe)
for each Xr in Z:
    Phi_Xr = the set of factors in Phi that mentioned Xr
    tau = sum(prod(Phi_Xr))
    remove Phi_Xr from Phi
    add tau to Phi
# all variables are eliminated now
return normalize(prod(Phi))
```

### Factors
Each factor $\phi$ or $\tau$ is a function that takes a specific state set of scoped variables, and return a positive real number. Thus, they are implemented as a lookup table, where each line is the specific state config, and its associated value. For each table, there are $\prod_{X_i\in scope(\phi)} |X_i|$ states (table rows). 

For $\phi$'s, we directly obtain them from the conditional probability functions at initalization time. For example, we initialize $\phi(A,B) = p(A|B)$. For $\tau$, we obtain them from `prod` and `sum`. 


```python
import pandas as pd
f = pd.DataFrame({"A": [0, 0, 1, 1], "B": [0, 1, 0, 1], "value": [.9, .1, .4, .6]})
f
```

<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>




```python
g = pd.DataFrame({"B": [0, 0, 1, 1], "C": [0, 1, 0, 1], "value": [.7, .3, .8, .2]})
g
```




<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>



### Product
`prod(f,g)` takes two factors (tables) $f,g$ with a scope variable in common, and returns a new factor $h$. 

We take the inner join of the two factors, and multiply the values for each row. 


```python
def prod(f, g):
    f = f.rename(columns={"value": "value_x"})
    g = g.rename(columns={"value": "value_y"})
    h = f.merge(g)
    h['value'] = h['value_x'] * h['value_y']
    h = h.drop(['value_x', 'value_y'], axis=1)
    return h
h_prod = prod(f, g)
h_prod
```



<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.63</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0.28</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0.08</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0.48</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.12</td>
    </tr>
  </tbody>
</table>



### Sum
`sum(f, X)` takes a factor $f$ and a variable $X$, and returns a new factor by summing up $X$ from $f$. 


```python
def sum(f, X):
    f_group = f.groupby(list(set(f.columns) - {X, "value"}))[['value']].sum()
    new_f = f_group.reset_index()
    return new_f

h_sum = sum(h_prod, "C")
h_sum
```


<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>A</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>



### Restriction
`restrict(f, X, x)` takes factor $f$, an evidence variable $X$ and the evidence value $x$, and returns a new factor that only contains rows that $X=x$. 


```python
def restrict(f, X, x):
    return f.loc[f[X] == x].drop(X, axis=1)
h_r = restrict(h_prod, "C", 1)
h_r
```

<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>1</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>1</td>
      <td>0.12</td>
    </tr>
  </tbody>
</table>



### Implementation


```python title="VE(Phi, Q, E, R)"
"""Variable Elimination
Args:
    Phi: A list of factors as pd.DataFrame
    Q: A list of str, representing the query variable
    E: A list of (str, state), representing the evidence var and evidence
    R: A list of str, given the elimination ordering
"""
for evar, evidence in E:
    for i, f in enumerate(Phi):
        if evar in f.columns:
            Phi[i] = restrict(f, evar, evidence)

for var in R:
    tau = None
    to_remove = []
    for i, f in enumerate(Phi):
        if var in f.columns:
            tau = prod(f, tau) if tau is not None else f
            to_remove.append(i)
    while len(to_remove) > 0:
        del Phi[to_remove.pop()]
    if tau is not None:
        tau = sum(tau, var)
        Phi.append(tau)
p = Phi[0]
for tau in Phi[1:]:
    p = prod(p, tau)
p['value'] /= p['value'].sum()
return p   
```

## VE Ordering and Message Passing
Consider a model $T=(V,E)$ be a tree. Let $N(i)$ be the neighbors of vertex $i$. Then, the joint distribution is

$$p(x_1,...,x_n) = \frac{1}{Z}\prod_{i\in V}\phi(x_i)\prod_{(i,j)\in E} \phi_{ij}(x_i, x_j)$$

where the factors are initialized from given conditional probabilities and $Z$ is the normalizer. 

Now, define the __message passing__ as 

$$m_{j\rightarrow i}(x_i) = \sum_{X_j} \phi_j(x_j) \phi_{ij}(x_i, x_j)\prod_{k\in N(j) - \{i\}}m_{k\rightarrow j}(x_j)$$

If $x_j$ is observed with value $\bar x_j$, since we will restrict $x_j = \bar x_j$, the message passing becomes

$$m_{j\rightarrow i}(x_i) = \phi_j(\bar x_j) \phi_{ij}(x_i, \bar x_j)\prod_{k\in N(j) - \{i\}}m_{k\rightarrow j}(\bar x_j)$$

Once the message passing is complete, we can compute beliefs 

$$b(x_i)\propto \phi_i(x_i) \prod_{j\in N(i)} m_{j\rightarrow i}(x_i), p(x_i) = \frac{1}{Z}b(x_i)$$

In the case of a tree, the leaf will only have its parent being the neighbor. Therefore, if we start message passing from each leaf, and then propagate till the root, we can cache the numerical values of the message passing on each edge, without recomputing any edge. 

Thus, by the tree property, we have the message passing algorithm

1. choose any vertex be the root $r$. 
2. message passing from all leafs to $r$, and then message passing from $r$ to leafs
3. For each query variable, compute belifs and normalize it

### Message Passing for VE

Note that the time complexity of VE is  

$$O(mk^{N_{\max}})$$

where $m$ is the number of initial factors, $k$ is the number of states for each r.v. , $N_{\max}$ is the max number of random variables inside some summation. Thus, the ordering for VE is important for the running time. 

Determining the optimal ordering on a arbitrary graph is NP-hard. However, we have optimal orderings on trees, where any elimination ordering that goes from the leaves inwards towards any root will be optimal. 

If we have a DAGM that is a tree, we can directly eliminate variables from the leaf till the query variables. In this case, we will have optimal runtime and the computation of message passing is actually the same as VE.
