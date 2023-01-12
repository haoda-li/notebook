import plotly.graph_objects as go
import numpy as np

u, v = np.mgrid[0:4*np.pi:20j, 0:4*np.pi:20j]

fig = go.Figure(data=[go.Surface(x=v * np.cos(u), y=v * np.sin(u), z=u)])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
with open("../assets/helicoid.json", "w") as f:
    f.write(fig.to_json())