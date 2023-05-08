import pandas as pd
import numpy as np

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"
datafields = sepallen, sepalwid, petallen, petalwid, species

dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)
dataf["Species"] = dataf["Species"].astype('category')

irisspecies = dataf.Species.unique()
speciesa = irisspecies[0]
speciesb = irisspecies[1]
speciesc = irisspecies[2]
print(speciesa, speciesb, speciesc)

for x in irisspecies:
    print (x)
    x = dataf[dataf["Species"] == x]
    print (x.describe())
    

'''
speciesadf = dataf[dataf["Species"] == speciesa]
print (speciesadf)
print (speciesadf.describe())
seplendata = dataf.pivot(columns="Species", values="Sepal Length")
print (seplendata)

print (dataf2)
meanvalues = dataf2.groupby('Species').mean()
stringmean = meanvalues.to_string(header=True, index =True)
print(stringmean)
'''