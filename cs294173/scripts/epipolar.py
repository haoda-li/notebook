import numpy as np
import plotly.graph_objects as go

points = np.array([
    (-2, 0, 0),
    (2, 0, 0),
    (1, 2, 2)
])

plane1 = np.array([
    (-2.5, 0.45, -.25),
    (-1.5, 0.1, -.25),
    (-1.5, 0.1, 0.25),
    (-2.5, 0.45, 0.25),
])

plane2 = np.array([
    (1.5, 0.1, -.25),
    (2.5, 0.4, -.25),
    (2.5, 0.4, 0.25),
    (1.5, 0.1, 0.25),
])

triangle = go.Scatter3d(
    x=points[:, 0], y=points[:, 1], z=points[:, 2],
    text=["Camera 1", "Camera 2", "X"], hoverinfo='none',
    mode='markers+text'
)

triangle_plane = go.Mesh3d(
    x=points[:, 0], y=points[:, 1], z=points[:, 2], opacity=0.50, hoverinfo='none'
)

plane1 = go.Mesh3d(
    x=plane1[:, 0], y=plane1[:, 1], z=plane1[:, 2],
    i=[0, 0], j=[1, 2], k=[2, 3], hoverinfo='none',
    name="image plane 1"
)

plane2 = go.Mesh3d(
    x=plane2[:, 0], y=plane2[:, 1], z=plane2[:, 2],
    i=[0, 0], j=[1, 2], k=[2, 3], hoverinfo='none',
    name="image plane 2"
)

fig = go.Figure(data=[triangle, triangle_plane, plane1, plane2])

fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
with open("../assets/epipolar.json", "w") as f:
    f.write(fig.to_json())
