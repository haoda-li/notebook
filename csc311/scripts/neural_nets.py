import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
srelu = np.log(1+np.exp(x))
logit = (1 + np.exp(-x)) ** (-1)
a, b = np.exp(x), np.exp(-x)
tanh = (a - b) / (a + b)
fig, axs = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
axs[0].plot(x, srelu); axs[0].set_title("Soft ReLU"); axs[0].set_ylim(-3, 3)
axs[1].plot(x, logit); axs[1].set_title("Logistic")
axs[2].plot(x, tanh); axs[2].set_title("tanh")
fig.tight_layout()
fig.savefig("../assets/neural_nets_activations.jpg")