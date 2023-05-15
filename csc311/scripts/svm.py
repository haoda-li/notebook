import numpy as np
import matplotlib.pyplot as plt

z = np.arange(-3, 3, 0.01)
plt.figure(figsize=(6, 4))
plt.plot(z, np.maximum(0, 1 - z), label="y=1")
plt.plot(z, np.maximum(0, 1 + z), label="y=-1")
plt.title("Hinge Loss")
plt.xlabel("z")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("../assets/svm_hinge_loss.jpg")

err = np.arange(0.001, 0.999, 0.001)
a = np.log((1 - err) / err) / 2
plt.figure(figsize=(6, 4))
plt.plot(err, a)
plt.xlabel("err, weighted error")
plt.ylabel("classifier coefficient")
plt.tight_layout()
plt.savefig("../assets/svm_error.jpg")


z = np.arange(-2, 3, 0.01)
plt.figure(figsize=(6, 4))
plt.plot(z, np.maximum(0, 1-z), label="Hinge")
plt.plot(z, np.exp(-z), label="exponential")
plt.title("Hinge Loss vs. Exponential Loss")
plt.xlabel("z")
plt.ylabel("Loss")
plt.ylim(0, 3)
plt.tight_layout()
plt.savefig("../assets/svm_vs.jpg")