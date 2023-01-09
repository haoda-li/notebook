import numpy as np
import plotly.graph_objs as go

def stereographic_proj(z):
    x, y = z[0], z[1]
    z_len_sq = x*x + y*y
    X = 4 * x / (z_len_sq + 4)
    Y = 4 * y / (z_len_sq + 4)
    Z = 2 * z_len_sq / (z_len_sq + 4)
    return np.array([X, Y, Z])

n = 50

#just a sphere
theta = np.linspace(0,2*np.pi,n)
phi = np.linspace(0,np.pi,n)

sphere = go.Surface(
    x=np.outer(np.cos(theta), np.sin(phi)), 
    y=np.outer(np.sin(theta), np.sin(phi)), 
    z=np.outer(np.ones(n), np.cos(phi)) + 1,
    colorscale="greens",
    opacity=0.5,
    showscale=False,
    hoverinfo="skip"
)

z = (2, 1)
points = np.array([
    [0, 0, 2],
    stereographic_proj(z),
    [z[0], z[1], 0]
])
line = go.Scatter3d(
    x=points[:, 0], y=points[:, 1], z=points[:, 2])

data = [sphere, line]
layout = go.Layout(
    title='stereographic projection',
    scene = dict(
        zaxis = dict(
            backgroundcolor="rgb(213, 232, 212)",
            gridcolor="white",
            showbackground=True,
            zerolinecolor="white"
        )
    )
)
fig = go.Figure(data=data, layout=layout)
fig.write_html("../assets/stere_proj.html", full_html=False, auto_open=False, include_plotlyjs="cdn", auto_play=False)


values = np.hstack((-np.exp(np.linspace(-10, 10, n//2)), 0, np.exp(np.linspace(-10, 10, n//2 - 1))))
z1 = np.stack((np.zeros(n), values, np.zeros(n)))
z2 = np.stack((values, np.zeros(n), np.zeros(n)))
P1 = stereographic_proj(z1)
P2 = stereographic_proj(z2)
line1 = np.empty((3, 3*n))
line2 = np.empty((3, 3*n))
line1[:, 1::3] = z1
line1[:, ::3] = P1
line1[:, 2::3] = P1
line2[:, 1::3] = z2
line2[:, ::3] = P2
line2[:, 2::3] = P2
scatter1 = go.Scatter3d(
    x=line1[0], y=line1[1], z=line1[2], 
    mode='markers+lines', marker=dict(size=4), name="x=0"
)
scatter2 = go.Scatter3d(
    x=line2[0], y=line2[1], z=line2[2], 
    mode='markers+lines', marker=dict(size=4), name="y=0"
)

data = [sphere, scatter1, scatter2]
layout = go.Layout(
    title='stereographic projection',
    scene = dict(
        xaxis={'range': [-3, 3]},
        yaxis={'range': [-3, 3]},
        zaxis = dict(
            backgroundcolor="rgb(213, 232, 212)",
            gridcolor="white",
            showbackground=True,
            zerolinecolor="white",
            range=[0, 6]
        )
    )
)
fig = go.Figure(data=data, layout=layout)
fig.update_layout(scene_aspectmode='manual',
                  scene_aspectratio=dict(x=1, y=1, z=1))
fig.write_html("../assets/stere_proj_2.html", full_html=False, auto_open=False, include_plotlyjs="cdn", auto_play=False)