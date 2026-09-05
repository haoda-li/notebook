import cv2
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import scipy.ndimage as scim

fig = make_subplots(3, 2, shared_xaxes=True)

N = 50
x = np.zeros(N)
x[N//3:N//3*2] = 1
sigma = 0
for i in range(3):
    for j in range(2):
        fig.add_trace(
            go.Scatter(
                x=np.arange(N), 
                y=scim.gaussian_laplace(x, sigma),
                name=f"sigma={sigma}"
            ),
            row=i+1, col=j+1
        )
        sigma += 1.5
fig.update_layout(margin={'t': 0, 'l': 0, 'b': 0, 'r': 0})
with open("../assets/blob_detection_log.json", "w") as f:
    f.write(fig.to_json())


x = np.linspace(-10, 10, N)
sigmas, ks = [1, 2, 3], [0.5, 0.7, 0.95]

fig = make_subplots(3, 3, shared_xaxes=True, shared_yaxes=True)

for i in range(9):
    sigma = sigmas[i % 3]
    k = ks[i // 3]
    g = 1 / sigma * np.exp(-(x ** 2) / (2 * (sigma ** 2)))
    g2 = 1 / (sigma * k) * np.exp(-(x ** 2) / (2 * ((sigma*k) ** 2)))
    fig.add_trace(
        go.Scatter(
            x=x,y=g-g2,name=f"k={k}, sigma={sigma}"
        ),
        row=i%3+1, col=i//3+1
    )
fig.update_layout(margin={'t': 0, 'l': 0, 'b': 0, 'r': 0})
with open("../assets/blob_detection_dog.json", "w") as f:
    f.write(fig.to_json())