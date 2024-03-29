# Mass-Spring System

## Mass and Spring
We model the physical behavior of the system as a network of point masses $P = \{(p_1, m_1),...,(p_n, m_n)\}$, where $p_1\in\mathbb R^3$ is the position and $m_i$ is the mass, and springs $E = \{(p_i, p_j)\mid 1\leq i\neq j \leq n\}$, so that the shape is a graph $G = (P, E)$.  

### Goal
Following Newton's second law, $f = ma$ where $f,a\in\mathbb R^3$. For each point mass, we need to have 

$$f_{i} = T_{i} + f^{\text{ext}}$$ 

where  
$T_{i} = \sum_{j, (p_i, p_j)\in E}f^{\text{elastic}}(p_i, p_j)$ is the sum of forces coming from any incident spring   
$f^{\text{ext}}$ is the external forces applied on the point mass

### Spring Potential Energy V(p<sub>i</sub>, p<sub>j</sub>)
For each spring $(p_i, p_j)$, define its stiffness $k > 0$ (assuming all springs have the same stiffness for now) and rest length $r_{i,j}\in\mathbb R$. The __potential energy__ $V(p_i, p_j)$ is defined as 

$$V(p_i, p_j):\mathbb R^{3\times 2}\rightarrow \mathbb R:= \frac k2(\|p_i-p_j\|-r_{ij})^2$$

Note that $\frac12$ is because the force is attached with two vertices, hence we only calculate half on each vertex.

The force exerted by the spring on each mass is the partial derivative of the potential energy $V$ with respect to the corresponding mass position. For example, for $p_i$ we have 

$$f_{ij} = - \frac{\partial V}{\partial p_i}\in\mathbb R^3$$

### Acceleration of the point mass a<sub>i</sub><sup>t</sup>
Define $p_i^t = p_i(t):\mathbb R^{\geq 0}\rightarrow \mathbb R^3$ be the position for mass $i$ at time $t$, and velocities ${p'}_i^t = \frac{\partial p_i}{\partial t}(t)\in\mathbb R^3$.  
Given $p_i^0$ and ${p'}_i^0$, which is the initial conditions of the simulation system. Also, note that $p_i^t$ is determined only on the last know value and won't trace back, i.e. given any $t\geq 0$, we can still treat these values as the initial conditions for the remaining time.   

For the purpose of the simulation, we only need to know the position of each mass at discrete time, so we can use discrete approximation. Therefore, ${p'}_i^t$ can be approximated by finite difference 

$${p'}_i^t = \frac{p_i^t - p_i^{t-\Delta t}}{\Delta t}$$

Then, we use central finite difference to approximate the acceleration at time $t$

\begin{align*}
a_i^t = {p''}_i^t &= \frac{ {p'}_i^{t+\Delta t} - {p'}_i^{t}}{\Delta t}\\
&= \frac{1}{\Delta t}\big(\frac{p_i^{t+\Delta t} - p_i^t}{\Delta t} - \frac{p_i^{t} - p_i^{t-\Delta t}}{\Delta t}\big)\\
&= \frac{p^{t+\Delta t} - 2p_i^{t} + p^{t-\Delta t}}{(\Delta t)^2}
\end{align*}

### Time integration
Coming back to the goal, since each point mass should follow Newton's second law, we can sum them together and integrate only $p$, i.e. 

\begin{align*}
V(P) &= \frac12\sum_{i,j}k(\|p_i - p_j\|-r_{ij})^2\\
T(P) &= (\Delta t)^2 \bigg\{\sum_i m_i \big(\frac{p_i - 2p_i^t + p_i^{t-\Delta t}}{(\Delta t)^2}\big)^2\bigg\}\\
F^{\text{ext}}(P) &= \sum_i p_i^Tf_i^{\text{ext}}\\
P &= (p_1,..., p_n)\in\mathbb R^{3\times n}
\end{align*}

We want 

$$V - F^{\text{ext}} = T$$

Therefore, we can view the problem as a optimization problem, i.e. 

$$p^{t+\Delta t} = \arg\min_{P} V(P)-T(P)-F^{\text{ext}}(P)$$

## Fast Simulation of Mass-Spring System ([Paper](http://graphics.berkeley.edu/papers/Liu-FSM-2013-11/Liu-FSM-2013-11.pdf))</a>

Observe that the non linear energy  can be written as a small optimization problem

$$(\|p_i-p_j\|-r_{ij})^2 = \min_{d_{ij}\in\mathbb R^3, \|d_{ij}\|=r_{ij}}\|(p_i - p_j) - d_{ij}\|^2$$

Therefore, suppose we know the vector $d_{ij}$ corresponds to the unknown optimal solution $p^{t+\Delta t}$, then treating $d_{ij}$ as constant, we cound find the optimal solution by 

\begin{align*}
p^{t+\Delta t} &= \arg\min_p \hat E(p)\\
\hat E(P) &=\big(\frac12\sum_{ij}k\|(p_i-p_j)-d_{ij}\|^2\big) - \Delta t^2\\
&\quad - (\Delta t)^2 \bigg\{\sum_i m_i \big(\frac{p_i - 2p_i^t + p_i^{t-\Delta t}}{(\Delta t)^2}\big)^2\bigg\}\\
&\quad -\sum_i p_i^Tf_i^{\text{ext}}
\end{align*}

Which is quadratic w.r.t. $P$ and we can have the solution at 

$$d_P \hat E = 0$$

Therefore, we can define a local-global iterative algorithm.   

while condition not satisfied:

  - Given current $P$, determine $d_{ij}$ from the small optimization problem
  - Find $P$ that minimizes $\hat E$
  


### Matrices
To allow parallel computation, we need to write the equations into matrix form. 

Define $P = [p_1,...,p_n]\in \mathbb R^{n\times 3}$, and similarly $P^t, P^{t-\Delta t} \in \mathbb R^{n\times 3}$, let $M = diag(m_1,...,m_n)\in \mathbb R^{n\times n}$, we have 

\begin{align*}
T(P) &= (\Delta t)^2 \bigg\{\sum_i m_i \big(\frac{p_i - 2p_i^t + p_i^{t-\Delta t}}{(\Delta t)^2}\big)^2\bigg\}\\
&= \frac1{\Delta t^2}\bigg\{(p_i - 2p_i^t + p_i^{t-\Delta t})^Tm_i(p_i - 2p_i^t + p_i^{t-\Delta t})\bigg\}\\
&= \frac1{\Delta t^2}tr(P-2P^t + P^{t-\Delta t})^TM(P-2P^t + P^{t-\Delta t})
\end{align*}

Define $A\in\mathbb \{-1, 0, 1\}^{|E|\times |V|}$ be the matrix that represents the edges, where each row $e$ represents one edge $e = (i, j)$ as

$$A_{ek} = \begin{cases}1&k=i\\-1&k=j\\0&\text{otherwise}\end{cases}$$

Let $d = \begin{bmatrix}d_{e_1}\\...\\d_{e_m}\end{bmatrix}\in\mathbb R^{\|E\|\times 3}$ being $d_{ij}$'s stacked vertically, so that 

$$\hat V(P) = \sum_{ij}\frac{k}2 \|(p_i - p_j) -d_{ij}\|^2 = \frac{k}2\big[(AP-d)^T(AP-d)\big]$$

Finally, let $f^{\text{ext}} =\begin{bmatrix}f_1^{\text{ext}}\\...\\f_n^{\text{ext}}\end{bmatrix}$ so that 

$$F(P) = tr(P^Tf^{\text{ext}})$$

and we can combine the equations together and write it into quadratic form, with some computation, we can have 

\begin{align*}
Q &= kA^TA + \frac1{\Delta t^2}M\\
b&= kA^Td + \frac{1}{\Delta t^2}M(2P^t - P^{t-\Delta t})\\
P^{t+\Delta t} &= \arg\min_p \frac12 tr(P^TQP) - tr(P^Tb)
\end{align*}

Note this is the quadratic formula and 

$$\nabla \hat E(p) = QP - b = 0$$

solve to have $P = Q^{-1}b$
Note that $Q$ involves only $A, M, k, \Delta t$, which are all constantly defined, hence it can be precomputed and factorized into $Q = LL^T$, which $L$ is triangular, hence solve $QP = b$ ($O(n^3)$ ops) becomes solve $LL^TP = b$ ($O(n^2)$ ops)

### Sparse Matrices
Note that in most cases, $A, M$ are quite sparse, where $\frac{2}{n}$ of $A$ and $\frac1n$ of $M$ are non-zero. Instead of storing the matrix as $O(n^2)$ entries, using a sparse matrix, where takes only `n * (int, int, float)` space. Also, operations on sparse matrix are fewer $O(n^{\approx 1.5})$ for precompute $Q$ and $O(n)$ for substitution.

### Pinned Vertices
Note that if we simulate gravity $g$ within $f^{\text{ext}}$, all the mass point will be pulled down quickly, therefore, we need to fix some mass point as pinned vertices, i.e. $p_k = p_k^{rest}, \forall k$ is pinned.  
To implement this equality constraint, we use penalty method, i.e. add an extremely large penalty onto the pinned vertices, 

$$\frac w2 \sum_{k} \|p_k - p_k^{rest}\|^2$$

when $p_k$ moves away from $p^{rest}$, the potential energy is much larger than the energy in the system, hence $p_k$ will be forced to be $p_k^{rest}$.  

Therefore, we can have $C\in \mathbb R^{|pinned|\times n}, C_{ki} = \mathbb I(p_i\text{ is the kth pinned vertex})$
and the penalty term becomes 

$$\frac w2 tr((CP-CP^{rest})^T(CP-CP^{rest}))$$

so that we have 

$$Q_{C} = wC^TC, b_C = wC^TCP^{rest}$$

And we need to solve $(Q+Q_C)P = (b+b_C)$
Note that $Q+Q_C$ is still constant, hence prefactorization still works.
