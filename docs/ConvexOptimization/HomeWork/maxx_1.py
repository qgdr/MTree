import plotly.graph_objects as go
import numpy as np

x = np.linspace(-1, 1, 1000)
y = np.linspace(-1, 1, 1000)

x, y = np.meshgrid(x, y)
z = np.maximum(np.abs(x), np.abs(y))

fig = go.Figure(data=go.Surface(x=x, y=y, z=z, opacity=0.8, showlegend=False))

fig.update_coloraxes(showscale=False)
fig.update_layout(
    xaxis_range=[-1, 1],
    yaxis_range=[-1, 1],
    # zaxis_range=[-1, 1],
    coloraxis_showscale=False,
    showlegend=False
)

# fig.show()


import os

file_dir = os.path.dirname(__file__)
print(file_dir)
# 保存
fig.write_html(os.path.join(file_dir, 'maxx_1.html'))
fig.show()