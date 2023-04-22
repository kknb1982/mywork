import pandas as pd

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"
datafields = sepallen, sepalwid, petallen, petalwid, species

dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)
dataf2 = dataf[sepallen]
#print (dataf)

print (dataf2)
meanvalues = dataf2.groupby(species).mean()
stringmean = meanvalues.to_string(header=True, index =True)
print(stringmean)