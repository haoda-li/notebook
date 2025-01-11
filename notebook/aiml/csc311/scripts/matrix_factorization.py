import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn


N, M, K = 6, 8, 3
U = np.random.normal(2, 1, (N, K))
U[U < 2.5] = 0
Z_T = np.random.normal(2, 1, (K, M))
Z_T[Z_T<2.5] = 0
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.title(r"$R$")
plt.imshow(U@Z_T, cmap="Greens")
plt.subplot(132)
plt.title(r"$U$")
plt.imshow(U, cmap="Greens")
plt.subplot(133)
plt.title(r"$Z^T$")
plt.imshow(Z_T, cmap="Greens")

plt.tight_layout()
plt.savefig("../assets/matrix_factorization_1.jpg")