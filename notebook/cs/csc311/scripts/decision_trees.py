import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

plt.figure(figsize=(4, 3))
x = np.arange(0.01, 1, 0.01)
y = - 1 * x * np.log(x) - (1- x) * np.log(1- x)
plt.plot(x, y)
plt.title("Entropy of Bernoulli(0, 1)")
plt.tight_layout()
plt.savefig("../assets/decision_trees.jpg")