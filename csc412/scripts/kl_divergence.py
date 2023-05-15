import numpy as np
import matplotlib.pyplot as plt

# --8<-- [start:kl]
def KL_divergence(p, q):
    p = p.flatten()
    q = q.flatten()
    idx = (p != 0) & (q != 0)
    p = p[idx]
    q = q[idx]
    return np.sum(p * np.log(p / q))
# --8<-- [end:kl]


from scipy.stats import multivariate_normal


x, y = np.meshgrid(np.linspace(-2, 4, 100), np.linspace(-2, 4, 100))
pos= np.dstack((x, y))
Normal_01 = multivariate_normal([0, 0], np.identity(2))
Normal_21 = multivariate_normal([2, 2], np.identity(2))
Normal_12 = multivariate_normal([1, 1], [[1, .5], [.5, 1]])

pi = Normal_01.pdf(pos) + Normal_21.pdf(pos); 
qi = Normal_12.pdf(pos); 
pi /= pi.sum() # p ~ N([0, 0], I) + N([2, 2], I)
qi /= qi.sum() # q ~ N([1, 1], [[1, 0.5], [0.5, 1]])
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.contour(x, y, pi, cmap="Reds"); plt.contour(x, y, qi, cmap="Blues");
plt.title(f"KL(q, p) = {KL_divergence(qi, pi):.4f}\n" + 
          f"KL(p, q) = {KL_divergence(pi, qi):.4f}")
plt.axis("off")
plt.gca().set_aspect("equal")
plt.tight_layout()

pi = Normal_01.pdf(pos) + Normal_21.pdf(pos);
qi = Normal_21.pdf(pos);
pi /= pi.sum() # p ~ N([0, 0], I) + N([2, 2], I)
qi /= qi.sum() # q ~ N([2, 2], I)
plt.subplot(122)
plt.contour(x, y, pi, cmap="Reds"); plt.contour(x, y, qi, cmap="Blues");
plt.title(f"KL(q, p) = {KL_divergence(qi, pi):.4f}\n" + 
          f"KL(p, q) = {KL_divergence(pi, qi):.4f}")
plt.axis("off")
plt.gca().set_aspect("equal")
plt.tight_layout()
plt.savefig("../assets/vi_1.jpg")
