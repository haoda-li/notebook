import plotly.graph_objects as go
import numpy as np

theta, phi = np.mgrid[0:2*np.pi:20j, 0:2*np.pi:20j]

fig = go.Figure(data=[go.Surface(
    x=(2 + np.cos(theta)) * np.cos(phi), 
    y=(2 + np.cos(theta)) * np.sin(phi), 
    z=np.sin(theta)
    )])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
with open("../assets/torus.json", "w") as f:
    f.write(fig.to_json())