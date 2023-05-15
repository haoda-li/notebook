import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

data = pd.read_csv("../assets/linss10e_1.csv", names=["wavelength", "L", "M", "S"])
data = data.fillna(0)
fig = px.scatter_3d(data.loc[data.wavelength < 650], x='L', y='M', z='S',
              color='wavelength', color_continuous_scale="rainbow")
with open("../assets/spec_locus.json", "w") as f:
    f.write(fig.to_json())