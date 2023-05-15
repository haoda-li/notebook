import plotly.graph_objects as go
import numpy as np
t = np.arange(-1, 1, 0.1)
d1 = go.Scatter3d(
        x=0.333333 * (1 + t)**1.5, y=0.333333 * (1 - t)**1.5, z=2**(-0.5) * t,
        mode='lines', name='(1)'
    )
d3 = go.Scatter3d(
        x=t, y=np.cosh(t), z=np.zeros(t.shape),
        mode='lines', name='(3)'
    )
t = np.arange(-1.5 * np.pi, 1.5 * np.pi, 0.01)
d2 = go.Scatter3d(
        x=0.8 * np.cos(t), y=1 - np.sin(t), z=-0.6 * np.cos(t),
        mode='lines', name='(2)'
    )
d4 = go.Scatter3d(
        x = np.cos(t)**3, y=np.sin(t)**3, z=np.zeros(t.shape),
        mode='lines', name='(4)'
    )
fig = go.Figure(data=[d1, d2, d3, d4])
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
with open("../assets/curvature.json", "w") as f:
    f.write(fig.to_json())