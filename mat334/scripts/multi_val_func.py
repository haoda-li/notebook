import matplotlib.pyplot as plt
import numpy as np

def angle(z):
    # since np.angle uses y-axis as branch cut, 
    # we need to change it to x-axis
    theta_pos = np.angle(z) * (z.imag > 0)
    theta_neg = (np.angle(z) + 2 * np.pi) * (z.imag < 0)
    return theta_pos + theta_neg
def sqrt(z):
    # define our sqrt function with branch cut y=0
    return np.abs(z)**.5 * np.exp(1j * (angle(z)/2))

t = np.arange(0, 2 * np.pi, np.pi/100)
c = np.array([
    1.2 * np.exp(1j * t[:, np.newaxis]),
    1.1 + np.exp(1j * t[:, np.newaxis]),
    1.1j + np.exp(1j * t[:, np.newaxis]),
    1.1 + 1.1j + np.exp(1j * t[:, np.newaxis]),
])
c_func = [
    '$c(t) = 1.2e^{it}$',
    '$c(t) = 1.1 + e^{it}$',
    '$c(t) = 1.1i + e^{it}$',
    '$c(t) = 1.1 + 1.1i + e^{it}$'
]
fc = sqrt(c)
fig = plt.figure(figsize=(16, 4))
fig.suptitle(r"f defined as $\sqrt{r} e^{i\theta/2}$", y=0)
for i in range(c.shape[0]):
    plt.subplot(1, 4, 1+i)
    plt.xlim(-3, 3); plt.ylim(-3, 3)
    plt.gca().set_aspect('equal')
    plt.axhline(c="grey", ls="--"); plt.axvline(c="grey", ls="--"); 
    plt.scatter(c[i].real, c[i].imag, s=.5); plt.scatter(fc[i].real, fc[i].imag, s=.5)
    plt.title(f"fig{i}. " + c_func[i])
plt.savefig("../assets/multi_val_func_01.jpg")