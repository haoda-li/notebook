import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-6, 10, 0.01)
y = np.arange(-6, 12, 0.01)
xx, yy = np.meshgrid(x, y)
f = (xx - 6) ** 2 + 5 * (yy - 7)**2

plt.figure(figsize=(6, 6))
plt.contour(xx, yy, f, levels=[3, 10, 20, 40, 80, 160, 320, 640])
an = np.linspace(0, 2 * np.pi, 100)
plt.plot(5 * np.cos(an), 5 * np.sin(an), color="red")
plt.axis("equal")
plt.xlim(-6, 8)
plt.ylim(-6, 8)
plt.savefig("../assets/ecfdoq.jpg")