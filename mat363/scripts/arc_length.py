import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-20 * np.pi, 20 * np.pi, 0.1)
def log_spiral(t, k):
    plt.gca().set_aspect('equal')
    plt.plot(np.exp(k * t) * np.cos(t), np.exp(k * t) * np.sin(t))
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.title(rf"k={k}")
plt.figure(figsize=(12, 4))
plt.subplot(131); log_spiral(t, 0.01)
plt.subplot(132); log_spiral(t, 0.02)
plt.subplot(133); log_spiral(t, -0.05)
plt.savefig("../assets/arc_length.jpg")