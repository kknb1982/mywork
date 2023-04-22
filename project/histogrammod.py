from variablemod import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#dataf.hist()
#plt.title("Histogram of each variable")
#plt.xlabel("Value in cm")
#plt.ylabel("Frequency")
#plt.show()

sns.histplot(data=dataf, x=sepallen, hue=species, multiple="dodge")
plt.show()

