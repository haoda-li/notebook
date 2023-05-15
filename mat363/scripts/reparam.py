import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-0.999, 1., 0.001)
plt.plot(t*t, t*t*t / (1 - t*t)**0.5)
plt.savefig("../assets/reparam.jpg")