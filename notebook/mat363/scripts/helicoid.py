import plotly.graph_objects as go
import numpy as np

u, v = np.mgrid[0:4*np.pi:50j, 0:4*np.pi:50j]

fig = go.Figure(data=[go.Surface(x=v * np.cos(u), y=v * np.sin(u), z=u)])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.write_html("../assets/helicoid.html",full_html=False, auto_open=False, include_plotlyjs="cdn", auto_play=False)