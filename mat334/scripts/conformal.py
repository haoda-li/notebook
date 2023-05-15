import numpy as np
import matplotlib.pyplot as plt

def point_mapping(f, f_str, z, zb):
    plt.axis("equal")
    plt.scatter(z.real, z.imag, s=1)
    plt.plot(zb.real, zb.imag)
    plt.scatter(f(z).real, f(z).imag, s=1)
    plt.plot(f(zb).real, f(zb).imag)
    plt.axhline(0, c="gray", ls=":")
    plt.axvline(0, c="gray", ls=":")
    plt.title(f_str)

x = np.linspace(0, 1, 20)
z = x.repeat(20) + 1j * np.tile(x, 20)

plt.figure(figsize=(12, 4))
plt.subplot(131)
z1 = z[z.real + z.imag >= 1]
zb1 = np.concatenate((1+1j* x, x[::-1] + 1j))
f1 = lambda x: (x * x)
point_mapping(f1, r"$f(z) = z^2$", z1, zb1)

plt.subplot(132)
z2 = z[z.real + (1 - z.imag) >= 1]
zb2 = np.concatenate((x, x + 1j * x))
f2 = lambda x: (x ** 3)
point_mapping(f2, r"$f(z) = z^3$", z2, zb2)

plt.subplot(133)
z3 = 2 * z.real + np.pi * 2j * z.imag  
zb3 = np.concatenate((2 * x, np.pi * 1j * x))
f3 = lambda x: (np.exp(x))
point_mapping(f3, r"$f(z) = e^z$", z3, zb3)
plt.savefig("../assets/conformal.jpg")