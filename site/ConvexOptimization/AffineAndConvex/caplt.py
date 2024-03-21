import plotly.graph_objects as go
import numpy as np

x = np.array([0.7, 0.2, 0.2])
y = np.array([0.1, 0.6, 0.2])
z = np.array([0.3, 0.1, 0.8])

i = np.array([0])
j = np.array([1])
k = np.array([2])

points = np.array([x, y, z])


fig = go.Figure()
fig.add_trace(go.Mesh3d(x=points[:,0], y=points[:,1], z=points[:,2], alphahull=5, opacity=0.4, color='red', i=i, j=j, k=k, name='Hull'))


fig.add_scatter3d(x=points[:,0], y=points[:,1], z=points[:,2], mode='markers', marker=dict(size=10, color=[1, 1, 1], colorscale='Viridis', opacity=0.8))


s, t = np.meshgrid(np.linspace(-5, 5, 2), np.linspace(-5, 5, 2))
surf = np.array([s * (points[1, i] - points[0, i]) + t * (points[2, i] - points[0, i]) + points[0, i] for i in  range(3)])

fig.add_surface(x=surf[0], y=surf[1], z=surf[2], opacity=0.2, showscale=False)
fig.update_coloraxes(showscale=False)
fig.update_layout(
    scene = dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        xaxis = dict(nticks=5, range=[0,1],),
        yaxis = dict(nticks=5, range=[0,1],),
        zaxis = dict(nticks=5, range=[0,1],),
        aspectratio=dict(x=1, y=1, z=1),
        
    ),
    coloraxis_showscale=False
)

import os

file_dir = os.path.dirname(__file__)
print(file_dir)
# 保存
# fig.write_html(os.path.join(file_dir, 'caplt.html'))
fig.show()