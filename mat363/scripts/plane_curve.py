import matplotlib.pyplot as plt 
import numpy as np

t = np.arange(0, np.pi, 0.01)
t0_idx = len(t) // 3

arc1 = np.array((np.cos(t), np.sin(t)))
tangent1 = np.array((-np.sin(t), np.cos(t)))
d2gamma1 = np.array((-np.cos(t), -np.sin(t)))
arc2 = np.array((np.cos(t), -np.sin(t)))
tangent2 = np.array((-np.sin(t), -np.cos(t)))
d2gamma2 = np.array((-np.cos(t), np.sin(t)))

def plot_curve(t0, gamma, dgamma, d2gamma, ax):
    t0 = t[t0_idx] # 30 degree
    p = np.array((gamma[0, t0_idx], gamma[1, t0_idx]))
    tangent = dgamma[:, t0_idx]
    normal = np.array(((0, -1), (1, 0))) @ tangent
    kappa_s = (d2gamma[:, t0_idx] / normal)[0]
    ax.plot(gamma[0], gamma[1])
    ax.arrow(p[0], p[1], tangent[0] / 30, tangent[1]/30,  head_width=.05, color="b")
    ax.arrow(p[0], p[1], tangent[0], tangent[1], shape='full', head_width=.05, color="r")
    ax.arrow(p[0], p[1],  normal[0], normal[1], shape='full', head_width=.05, color="g")
    ax.set_title(rf"$\kappa_s = {kappa_s}$");
    
plt.figure(figsize=(8, 4))
ax = plt.subplot(121); ax.set_aspect('equal'); ax.axis("off")
plot_curve(t, arc1, tangent1, d2gamma1, ax)
ax = plt.subplot(122); ax.set_aspect('equal'); ax.axis("off")
plot_curve(t, arc2, tangent2, d2gamma2, ax)

plt.savefig("../assets/plane_curve.jpg")