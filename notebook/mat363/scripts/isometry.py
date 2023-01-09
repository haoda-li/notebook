import plotly.graph_objects as go
import numpy as np

u, v = np.mgrid[-2 : 2 :50j, -2: 2:50j]
S = go.Surface(
    x=u - u**3 / 3 + u * v * v,
    y = v - v**3/3 + v*u*u,
    z=u*u-v*v
)
fig = go.Figure(data=[S])

fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.write_html("../assets/isometry.html",full_html=False, 
               auto_open=False, include_plotlyjs="cdn", auto_play=False)