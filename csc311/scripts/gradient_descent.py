import autograd.numpy as np
import autograd
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)
np.random.seed(1)

# helper function yielding a random positive semi-definite matrix
def random_psd_matrix(seed=None):
    """return random positive semi-definite matrix with norm one"""
    np.random.seed(seed)
    A = np.random.randn(2,2)
    A = np.dot(A.T,A)
    A = np.dot(A.T,A)
    A = A / np.linalg.norm(A, ord=2)
    return A

# define forward function
def f(x, a):
    """f(x) = x^T A x"""
    y = 0.5*np.dot(x.T, np.dot(a, x))
    return y

# helper function for isocontour plotting
def plot_isocontours(one_d_grid, g, ax):
    """
    first makes a 2d grid from the 1d grid
    then plots isocontours using the function g
    """
    X,Y = np.meshgrid(one_d_grid, one_d_grid)  # build 2d grid
    Z = np.zeros_like(X)
    # numpy bonus exercise: can you think of a way to vectorize the following for-loop?
    for i in range(len(X)):
        for j in range(len(X.T)):
            Z[i, j] = g(np.array((X[i, j], Y[i, j])))  # compute function values
    ax.set_aspect("equal")
    ax.contour(X, Y, Z, 100)

matrices = [np.ones((2, 2)), random_psd_matrix(0), random_psd_matrix(1), random_psd_matrix(11)]
fig, axes = plt.subplots(2, 2, figsize=(8, 9))
fig.tight_layout()
for i, A in enumerate(matrices):
    ax = axes[i//2][i%2]
    plot_isocontours(np.linspace(-0.5, 0.5, 200), lambda x: f(x, A), ax)
    ax.set_title(rf"{A}")
fig.savefig(f"../assets/gradient_descent_1.jpg")


df_dx = autograd.grad(f, 0)

A = random_psd_matrix(0)  # argument specifies the random seed
fig, ax = plt.subplots(figsize=(4, 4))
plot_isocontours(np.linspace(-5, 5, 100), lambda x: f(x, A), ax)  # plot function isocontours

# hyperparameters
LEARNING_RATE = 2.0 
INITIAL_VAL = np.array([4., -4.])  # initialize

x = np.copy(INITIAL_VAL)
ax.plot(*x, marker='.', color='r', ms=25)  # plot initial values

# --8<-- [start:grad]
for i in range(32):
    x_old = np.copy(x)
    delta = -LEARNING_RATE*df_dx(x, A)  # compute gradient times learning rate
    x += delta  # update params
# --8<-- [end:grad]
    # plot
    # plot a line connecting old and new param values
    ax.plot([x_old[0], x[0]], [x_old[1], x[1]], linestyle='-', color='k',lw=2)  
    fig.canvas.draw()
    ax.set_title('i={}, x={} | f(x)={}'.format(i, x, f(x, A)))
fig.tight_layout()
fig.savefig(f"../assets/gradient_descent_2.jpg")


fig, ax = plt.subplots(figsize=(4, 4))
plot_isocontours(np.linspace(-5, 5, 100), lambda x: f(x, A), ax)  # plot function isocontours

# initialize
x = np.copy(INITIAL_VAL)
delta = np.zeros(2) 
ax.plot(*x, marker='.', color='r', ms=25)  # plot initial values

# hyperparameters
LEARNING_RATE = 2.0
ALPHA = 0.5

# --8<-- [start:momentum]
for i in range(32):
    x_old = np.copy(x)
    delta_old = np.copy(delta)

    g = df_dx(x, A)  # compute standard gradient
    delta = -LEARNING_RATE*g + ALPHA*delta_old  # update momentum term
    x += delta  # update params
# --8<-- [end:momentum]
    # plot
    ax.plot([x_old[0], x[0]], [x_old[1], x[1]],'-k',lw=2)  # plot a line connecting old and new param values
    fig.canvas.draw()
    ax.set_title('i={}, x={} | f(x)={}'.format(i, x, f(x, A)))

fig.tight_layout()
fig.savefig(f"../assets/gradient_descent_3.jpg")


