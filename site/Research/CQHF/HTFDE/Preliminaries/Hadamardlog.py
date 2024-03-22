import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 10)
f = np.log(x)

plt.plot(x, f, 'o-')
plt.plot(np.log(x), f, 'o-')

plt.legend([r'$g(x)$', r'$f(t)$'])

import os

file_dir = os.path.dirname(__file__)
print(file_dir)
# 保存
plt.savefig(os.path.join(file_dir, 'Hadamardlog.png'))

plt.show()