import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-6, 10, 0.01)
y = np.arange(-6, 12, 0.01)
xx, yy = np.meshgrid(x, y)
c1 = plt.Circle((0, 0), 5, color="red", alpha=.5)
c2 = plt.Circle((0, 0), 3, color="white")
fig, axs = plt.subplots(1, 3, figsize=(16, 5))
axs[0].add_artist(c1);axs[0].add_artist(c2)
axs[0].contour(xx, yy, (xx) ** 2 + (yy - 6)**2, 
               levels=[0.01, 3, 10, 20, 40, 80, 120], cmap="rainbow")
axs[0].axis("equal");axs[0].set_xlim(-5, 7);axs[0].set_ylim(-5, 7);

c1 = plt.Circle((0, 0), 5, color="red", alpha=.5)
c2 = plt.Circle((0, 0), 3, color="white")
axs[1].add_artist(c1);axs[1].add_artist(c2)
axs[1].contour(xx, yy, (xx) ** 2 + (yy - 2)**2, 
               levels=[0.01, 3, 10, 20, 40, 80, 120], cmap="rainbow")
axs[1].axis("equal");axs[1].set_xlim(-5, 7);axs[1].set_ylim(-5, 7);

c1 = plt.Circle((0, 0), 5, color="red", alpha=.5)
c2 = plt.Circle((0, 0), 3, color="white")
axs[2].add_artist(c1);axs[2].add_artist(c2)
axs[2].contour(xx, yy, (xx-2) ** 2 + (yy - 3)**2, 
               levels=[0.01, 3, 10, 20, 40, 80, 120], cmap="rainbow")
axs[2].axis("equal");axs[2].set_xlim(-5, 7);axs[2].set_ylim(-5, 7)

fig.savefig("../assets/icfdoq.jpg")