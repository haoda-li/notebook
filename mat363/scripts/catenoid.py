import plotly.graph_objects as go
import numpy as np

t, theta = np.mgrid[-1:1:10j, 0:1.5 * np.pi:50j]

fig = go.Figure(data=[go.Surface(
    x=np.cosh(t) * np.cos(theta), 
    y=np.cosh(t) * np.sin(theta), 
    z=t)])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
with open("../assets/catenoid.json", "w") as f:
    f.write(fig.to_json())