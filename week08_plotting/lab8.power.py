# h(x)=x ** 3 in the range [0, 10]

import numpy as np
import matplotlib.pyplot as plt

min = 0
max = 10

np.random.seed(1)

xpoints = np.array(range(min,max))
ypoints = xpoints ** 3

plt.plot(xpoints, ypoints, color = 'r')

plt.title('test')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()