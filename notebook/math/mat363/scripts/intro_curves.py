import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-4 * np.pi, 4 * np.pi, 0.001)
x = (1 + 2 * np.cos(t)) * np.cos(t); y = (1 + 2 * np.cos(t)) * np.sin(t)
dx1 = 3 ** 0.5 / 2 * t; dy1 = -3 / 2 * t
dx2 = -3 ** 0.5 / 2 * t; dy2 = -3 / 2 * t
plt.figure(figsize=(4, 4)); plt.xlim(-1, 4); plt.ylim(-3, 3)
plt.xticks([]); plt.yticks([])
plt.plot(x, y); plt.plot(dx1, dy1); plt.plot(dx2, dy2)
plt.savefig("../assets/intro_curves.jpg")