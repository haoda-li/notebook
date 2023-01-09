import plotly.graph_objects as go
import numpy as np

t = np.arange(0, 2*np.pi, 0.05)
p = np.array((np.cos(t), np.sin(t), np.zeros_like(t)))
orient = np.array((np.sin(t/2), np.zeros_like(t), np.cos(t/2))) / 2.
top = p + orient
bot = p - orient
surface = np.empty((3, top.shape[1] * 2))
surface[:, ::2] = top
surface[:, 1::2] = bot

fig = go.Figure(
    data=[
        go.Scatter3d(x=top[0], y=top[1], z=top[2], mode="lines", name="'top'"),
        go.Scatter3d(x=bot[0], y=bot[1], z=bot[2], mode="lines", name="'bottom'"),
        go.Scatter3d(x=surface[0, ::3], y=surface[1, ::3], z=surface[2, ::3], mode="lines", name="normal")
    ],
    )
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.write_html("../assets/mobius.html",full_html=False, auto_open=False, include_plotlyjs="cdn", auto_play=False)