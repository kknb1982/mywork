import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
hist_mean = 5
hist_st_dev = 2
number_of_values = 1000

normal_data = np.random.normal(loc = hist_mean, scale = hist_st_dev, size = number_of_values)

plt.hist (normal_data)
plt.show()