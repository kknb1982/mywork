import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 100
low = 21
high = 65
size = number_of_entries

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint(low, high, size)

plt.scatter(ages,salaries, label = "salaries")

xpoints= np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'r', label = "x sqaured")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend()
plt.show()

plt.savefig('prettier_plt.png')