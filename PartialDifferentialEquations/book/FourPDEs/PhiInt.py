import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)

x, y = np.meshgrid(x, y)
phi = 1/(3*4/3*np.pi*np.sqrt(x**2+y**2))

u, v = np.mgrid[0:2*np.pi:20j, 0:2*np.pi:20j]
x1 = 0.3*np.cos(u)*np.sin(v)
y1 = 0.3*np.sin(u)*np.sin(v)
z1 = 0.01*np.cos(v)

x2 = x1 + 0.2
y2 = y1 + 0.3
z2 = 0.01*np.cos(v)

fig = plt.figure(figsize=(16, 8))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, phi, label='phi', alpha=0.5)

ax1.plot_surface(x1, y1, z1, color='r')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, phi, label='phi', alpha=0.5)
ax2.plot_surface(x2, y2, z2, color='r')

plt.savefig('./PhiInt.jpg')
plt.show()
