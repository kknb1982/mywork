import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
#

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"

datafields = (sepallen, sepalwid, petallen, petalwid, species)

# path = "C:\Users\kirst\OneDrive - Atlantic TU\pands\mywork\project\"
filename = "summary.txt"

# Import data
dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

def printfielddata():
    with open(filename, 'a') as f:
        for name in datafields:
            if name != species:
                header = (f'The column title is {name}')
                f.write(header)
                min = str(dataf[name].min())
                max = str(dataf[name].max())
                range = (f'\nThe minimum values is: {min} \nThe maximum value is: {max}')
                f.writelines(range)
                mean = str(dataf[name].mean())
                median = str(dataf[name].median())
                mode = str(dataf[name].mode())
                averages = (f'\nMean: {mean} \nMedian: {median} \nMode: {mode}\n\n')
                f.writelines(averages)
            else:
                meanvalues = dataf.groupby(species).mean()
                stringmean = meanvalues.to_string(header=True, index =True)
                f.write(stringmean)
                f.close()

'''def getspecies():
    irisspecies = data[species].unique()
    '''
irisspecies = dataf[species].unique()

def getdatabyspecies():
    for type in irisspecies:
        speciesdata = (dataf[dataf[species] == type])
        print(speciesdata)

def gethisto():
    for name in datafields:
        if name != species:
            sns.histplot(data=dataf, x=name, hue=species, multiple="dodge")
            plt.savefig(name+ '.png')