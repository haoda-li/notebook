import plotly.graph_objects as go
import numpy as np

theta, phi = np.mgrid[0:2*np.pi:50j, 0:2*np.pi:50j]

fig = go.Figure(data=[go.Surface(
    x=(2 + np.cos(theta)) * np.cos(phi), 
    y=(2 + np.cos(theta)) * np.sin(phi), 
    z=np.sin(theta)
    )])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.write_html("../assets/torus.html",full_html=False, auto_open=False, include_plotlyjs="cdn", auto_play=False)