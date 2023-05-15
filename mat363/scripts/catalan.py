import plotly.graph_objects as go
from numpy import sin, cos, sinh, cosh, pi, mgrid

u, v = mgrid[-2 * pi: 2 * pi:20j, -0.5*pi:0.5*pi:10j]

fig = go.Figure(data=[go.Surface(
    x=u - sin(u) * cosh(v), 
    y=1 - cos(u) * cosh(v), 
    z=-4*sin(u/2) * sinh(v/2)
    )])
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

with open("../assets/catalan.json", "w") as f:
    f.write(fig.to_json())