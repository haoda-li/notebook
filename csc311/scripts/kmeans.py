import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import scipy as sp


# --8<-- [start:kmeans]
def kMeans(x, k, step, m=None):
    
    # initialization
    if m is None:
        m = x[np.random.choice(x.shape[0], k)]
    
    # iterative step
    for i in range(step):
        # assignment step
        kd = sp.spatial.KDTree(m)
        r = kd.query(x)[1]
        
        # refitting step
        for c in range(k):
            m[c] = x[r == c].mean(axis=0)
    return r, m
# --8<-- [end:kmeans]



size = 3
centers = np.random.uniform(-5, 5, (size, 2))
sds = np.random.uniform(0.8, 1, size)

x, t = make_blobs(n_samples=500, centers=centers, n_features=2, cluster_std = sds, random_state=0)

plt.figure(figsize=(12, 18))
plt.subplot(321)
for i in range(size):
    plt.scatter(x[t==i, 0], x[t==i, 1])
plt.title("group truth")
plt.axis("off");

r, m = kMeans(x, 3, 1)
for iteration in range(4):
    plt.subplot(3, 2, 3 + iteration)
    plt.title("iteration " + str(iteration))
    plt.axis("off");
    for i in range(r.max() + 1):
        plt.scatter(x[r==i, 0], x[r==i, 1])
        r, m = kMeans(x, 3, 1, m)
plt.tight_layout()
plt.savefig("../assets/kmeans_1.jpg")



centers = np.array([[ 1.69653073,  4.85908807], [ 0.13447474,  3.7240316 ], [-2.02381919, -2.05536678]])
sds = 0.8119142178109643
m = np.array([[ 0.84192262,  4.26238333], [-1.67684624, -2.56679316], [-2.44040286, -1.48432092]])

x, t = make_blobs(n_samples=500, centers=centers, n_features=2, cluster_std = sds, random_state=0)

plt.figure(figsize=(12, 18))
plt.subplot(321)
for i in range(size):
    plt.scatter(x[t==i, 0], x[t==i, 1])
plt.title("group truth")
plt.axis("off");

r, m = kMeans(x, 3, 1, m)
for iteration in range(4):
    plt.subplot(3, 2, 3 + iteration)
    plt.title("iteration " + str(iteration))
    plt.axis("off");
    for i in range(r.max() + 1):
        plt.scatter(x[r==i, 0], x[r==i, 1])
        r, m = kMeans(x, 3, 1, m)
plt.tight_layout()
plt.savefig("../assets/kmeans_2.jpg")