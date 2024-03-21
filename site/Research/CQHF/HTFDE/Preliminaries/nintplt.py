import plotly.graph_objects as go
import numpy as np

x = np.array([0, 0, 0])
y = np.array([0, 1, 0])
z = np.array([1, 0, 0])
points = np.array([x, y, z])

i = np.array([0])
j = np.array([1])
k = np.array([2])


fig = go.Figure()
fig.add_trace(go.Mesh3d(x=points[:,0], y=points[:,1], z=points[:,2], alphahull=5, opacity=0.4, color='red', i=i, j=j, k=k, name='Hull'))

x = np.array([0, 0, 1])
y = np.array([0, 1, 0])
z = np.array([1, 0, 0])
points = np.array([x, y, z])

fig.add_trace(go.Mesh3d(x=points[:,0], y=points[:,1], z=points[:,2], alphahull=5, opacity=0.4, color='green', i=i, j=j, k=k, name='Hull'))

N = 5
points = np.zeros([N, 5])
points[:, 0] = np.linspace(0, 1, N)
points[:, 3] = np.array([10, 13, 15, 10, 8])

fig.add_scatter3d(x=points[:,0], y=points[:,1], z=points[:,2], mode='lines', line=dict(color='Black', width=50))

for i in range(N):
    for j in range(N-i):
        fig.add_scatter3d(x=points[:N-(i+j), 0], y=points[:,1]+points[j, 0], z=points[:, 2]+points[i, 0], mode='markers', marker=dict(size=points[:, 3], color=points[:, 3], colorscale='Viridis', opacity=0.8), showlegend=False)




fig.update_coloraxes(showscale=False)
fig.update_layout(
    scene = dict(
        xaxis_title=r'∫',
        yaxis_title=r'∬',
        zaxis_title=r"∭",
        xaxis = dict(nticks=5, range=[0,1],),
        yaxis = dict(nticks=5, range=[0,1],),
        zaxis = dict(nticks=5, range=[0,1],),
        aspectratio=dict(x=1, y=1, z=1),
        
    ),
    coloraxis_showscale=False,
    showlegend=False
)

import os

file_dir = os.path.dirname(__file__)
print(file_dir)
# 保存
fig.write_html(os.path.join(file_dir, 'nintplt.html'))
fig.show()