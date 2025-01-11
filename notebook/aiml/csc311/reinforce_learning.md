# Reinforcement Learning

## Reinforcement Learning Problem
An agent continually interacts with the environment. How should it choose its actions so that its long-term rewards are maximized. 

Reinforcement Learning is challenging in 

 - continuous stream of input information, and we have to choose actions
 - effects of an action depend on the state of the agent in the world 
 - obtain reward that depends on the state and actions 
 - You know only the reward for your action, not other possible actions. 
 - Could be a delay between action and reward. 

### Markov Decision Process (MDP)
MDP is the mathematical framework to describe RL problems.

A discounted MDP is defined by a tuple $(S, A, P, R, \gamma)$ where 
 
 - $S$ state space, discrete or continuous (most cases discrete)
 - $A$ action space. we only consider finite action apace, i.e. $A = \{a_1,...,a_M\}$
 - $P$ transition probability
 - $R$ immediate reward distribution
 - $\gamma$ discount factor $0\leq \gamma \leq 1$
 
The agent has a __state__ $s\in S$ in the environment. 

At every time step $t = 0, 1,...$ the agent is at state $S_t$. 

 - Takes an __action__ $A_t$
 - Moves into a new state $S_{t+1}$, according to the dynamics of the environment and the selected action, i.e., $S_{t+1}\sim P(\cdot|S_t, A_t)$
 - Receives some __reward__ $R_t \sim R(\cdot|S_t, A_t, S_{t+1})$
 - Alternatively, $R_t \sim R(\cdot|S_t, A_t)$ or $R_t\sim R(\cdot |S_t)$

The action selection mechanism is described by a __policy__ $\pi$, which is a mapping from states to actions, i.e., $A_t = \pi(S_t)$ (deterministic policy) or $A_t\sim \pi(\cdot|S_t)$ (stochastic policy). 

The goal is to find a policy $\pi$ s.t. __long term rewards__ of the agent is maximized. 

Different notions of long-term reward: 

 - Cumulative/total reward: $R_0 + R_1 + R_2 + ...$
 - Discounted (cumulative) reward: $R_0 + \gamma R_1 + \gamma^2 R_2 + ...$ 
    - The discount factor $0\leq \gamma \leq 1$ determines how myopic the agent is. 
    - When $\gamma >> 0\Rightarrow $ more myopic, $\gamma >> 1\Rightarrow $ less myopic. 

#### Transition Probability (or Dynamics)
The transition probability describes the changes in the state of the agent when it chooses actions 

$$P(S_{t+1} = s'|S_t = s, A_t = a)$$

This model has __Markov property__; the future depends on the past only through the current state. 

A __policy__ is the action-selection mechanism of the agent, and describes its behavior. Policy can be deterministic or stochastic. 

## Value Function based Reinforcement Learning
The expected future reward, and is used to evaluate the desirability of states.  
State-value function $V^\pi$ for policy $pi$ is a function defined as 

$$V^\pi(s):= E_\pi \bigg[\sum_{t\geq 0}\gamma^t R_t\mid S_0 = s], R_t\sim R(\cdot |S_t, A_t, S_{t+1})\bigg]$$

describes the expected discounted reward if the agent starts from state $s$ following policy $\pi$. 

Action-value function $Q^\pi$ for policy $\pi$ is 

$$Q^\pi(s,a) := E_\pi\bigg[\sum_{t\geq 0}\gamma^t R_t\mid S_0 = s, A_0 = a\bigg]$$

describes the expected discounted reward if the agent starts from state $s$, takes action $a$, and afterwards follows policy $\pi$. 

The goal is to find a policy $\pi$ that maximizes the value function, i.e. the optimal value function 

$$Q^*(s,a)=\sup_\pi Q^\pi(s,a)$$

Given $Q^*$, the optimal policy can be obtained as 

$$\pi^*(s) = \arg\max_a Q^* (s,a)$$

The goal of an RL agent is to find a policy $\pi$ that is close to optimal, $Q^\pi \approx Q^*$
