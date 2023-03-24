import matplotlib.pyplot as plt
import numpy as np
min_salary = 20000
max_salary = 80000
number_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(min_salary,max_salary,number_of_entries)

plt.hist(salaries)
plt.show()