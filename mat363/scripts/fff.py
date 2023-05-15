import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from numpy import sinh, cosh
from IPython.display import display, IFrame

theta, psi = np.mgrid[-.5 * np.pi:.5 * np.pi:10j, -np.pi: np.pi:10j]
u, v = np.mgrid[-.5 :.5 :10j, -1: 1:10j]
S1 = go.Surface(x=sinh(theta) * sinh(psi), y=sinh(theta) * cosh(psi), z=sinh(theta))
S2 = go.Surface(x=u - v, y=u + v, z=u * u + v * v)
S3 = go.Surface(x=cosh(theta), y=sinh(theta), z=v)
S4 = go.Surface(x=u, y=v, z=u * u + v * v)

fig = make_subplots(cols=2, rows=2, horizontal_spacing=0, vertical_spacing=0, 
                    specs=[[{"type": "scene"}, {"type": "scene"}], [{"type": "scene"}, {"type": "scene"}]])
fig.add_trace(S1, row=1, col=1)
fig.add_trace(S2, row=1, col=2)
fig.add_trace(S3, row=2, col=1)
fig.add_trace(S4, row=2, col=2)
fig.update_traces(showscale=False)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), height=720)
with open("../assets/fff.json", "w") as f:
    f.write(fig.to_json())