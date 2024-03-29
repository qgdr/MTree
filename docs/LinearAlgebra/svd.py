import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [3, 0],
    [1, 2],
])

t = np.linspace(0, 2*np.pi, 10000)
x = np.array([
    np.cos(t), np.sin(t)
])
plt.plot(x[0], x[1], '--')
y = A @ x
plt.plot(y[0], y[1], 'r')

l = np.sqrt(y[0]**2+y[1]**2)
i, s = np.argmin(l), np.argmax(l)
ui, us = y[:,i], y[:,s]
plt.arrow(0, 0, ui[0], ui[1], color='orange')
plt.arrow(0, 0, us[0], us[1], color='green')

vi, vs = x[:,i], x[:,s]
plt.arrow(0, 0, vi[0], vi[1], color='pink')
plt.arrow(0, 0, vs[0], vs[1], color='purple')


plt.axis("equal")
plt.grid()
plt.legend(['|x|=1', 'Ax'])

import os

file_dir = os.path.dirname(__file__)
print(file_dir)
plt.savefig(os.path.join(file_dir, 'svd.png'))

plt.show()