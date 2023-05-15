import numpy as np
import plotly.graph_objects as go

n_points = 8

control_points = np.random.uniform(0, 1, (n_points, 3))

# --8<-- [start:spline]
basis_catmull_rom = np.array([
    [0,      1,   0,   0],
    [-0.5,   0, 0.5,   0],
    [1,   -2.5,   2,-0.5],
    [-0.5, 1.5,-1.5, 0.5]
])

basis_cubic_bezier = np.array([
    [1, 0, 0,  0],
    [-3, 3, 0, 0],
    [3, -6, 3, 0],
    [-1, 3, -3, 1]
])

def spline(p, basis, n=20):
    u = np.linspace(0, 1, n)
    P = np.vstack([
        np.ones(n),
        u,
        u * u,
        u * u * u
    ])
    return P.T @ basis @ p
# --8<-- [end:spline]

cr_curve = []
bezier_curve = []
for i in range(len(control_points) - 3):
    cr_curve.append(spline(control_points[i:i+4], basis_catmull_rom))
for i in range(0, len(control_points) - 3, 4):
    bezier_curve.append(spline(control_points[i:i+4], basis_cubic_bezier))
cr_curve = np.concatenate(cr_curve)
bezier_curve = np.concatenate(bezier_curve)
fig = go.Figure(data=[
    go.Scatter3d(
        x=control_points[:, 0], y=control_points[:, 1], z=control_points[:, 2], 
        mode="text+lines", text=np.arange(len(control_points)), name="linear"),
    go.Scatter3d(
        x=cr_curve[:, 0], y=cr_curve[:, 1], z=cr_curve[:, 2], mode="lines", name="Catmull-Rom"),
    go.Scatter3d(
    x=bezier_curve[:, 0], y=bezier_curve[:, 1], z=bezier_curve[:, 2], mode="lines", name="Cubic Bezier")
])

fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

with open("../assets/splines.json", "w") as f:
    f.write(fig.to_json())

