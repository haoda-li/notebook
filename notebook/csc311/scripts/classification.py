import matplotlib.pyplot as plt
import numpy as np

z = np.arange(-10, 10, 0.01)
loss = (np.exp(-z) + 1) ** -1
plt.figure(figsize=(4, 3))
plt.plot(z, loss)
plt.title("logistic function")
plt.tight_layout()
plt.savefig("../assets/classification_logistic.jpg")


plt.figure(figsize=(4, 3))
plt.plot(z, -1 * np.log(loss), label="t = 1")
plt.plot(z, -1 * np.log(1 - loss), label="t = 0")
plt.legend()
plt.tight_layout()
plt.savefig("../assets/classification_loss.jpg")


