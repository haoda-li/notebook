import plotly.graph_objects as go
from numpy import sin, cos, sinh, cosh, pi, mgrid

u, v = mgrid[-pi:pi:50j, -pi:pi:50j]

fig = go.Figure(data=[go.Surface(
    x=u - sin(u) * cosh(v), 
    y=1 - cos(u) * cosh(v), 
    z=-4*sin(u/2) * sinh(v/2)
    )])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.write_html("../assets/catalan.html",full_html=False, auto_open=False, include_plotlyjs="cdn", auto_play=False)