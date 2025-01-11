import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

# import some data to play with
iris = datasets.load_iris()

# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = iris.data[:, :2]
y = iris.target

h = .02  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# we create an instance of Neighbours Classifier and fit the data.
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
k_set = [1, 5, 15, 50]
for i in range(4):
    clf = neighbors.KNeighborsClassifier(k_set[i], weights='distance')
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    axs[i//2][i%2].pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    axs[i//2][i%2].scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                    edgecolor='k', s=20)
    axs[i//2][i%2].set_xlim(xx.min(), xx.max())
    axs[i//2][i%2].set_ylim(yy.min(), yy.max())
    axs[i//2][i%2].set_title("(k = %i)" % k_set[i])
plt.tight_layout()
fig.savefig("../assets/knn.jpg")