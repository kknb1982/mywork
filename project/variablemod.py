# Import the libraries needed
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Create the variable names
sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"

datafields = sepallen, sepalwid, petallen, petalwid, species
print(type(datafields))
chartvariables = datafields[:4]
print(chartvariables)

# Import Fishers Iris Dataset to a DataFrame
dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

def createboxsub():
    fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
    for name in chartvariables:
        plt.suptitle("Box plots of Fisher Iris Dataset by Species")
        a = 1
        plt.subplot(2,2,a)
        sns.boxplot(data=dataf, x=species, y=name)
        plt.ylabel(f'{name} in cm')
        a += 1
               plt.show()
             
'''
g = dataf.boxplot(by=species, layout=(2,2), figsize=(10,8), return_type='axes')
plt.subplots_adjust(left=0.2,bottom=0.2, top = 0.9, right = 0.9)
ylabel
print(dataf.groupby("Species").size())

# Finds the names of the iris species
irisspecies = dataf.Species.unique()

# Defines a function to creates a text file with summary data about the variable
def printfielddata():
    # Opens a text file called summary.txt to write data to, if it does not exist it will create it
    with open('summary.txt', 'w') as f:
        # iterate through the columns of the data
        for name in datafields:
            # Ignore species at this is not numerical data
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
                for x in irisspecies:
                    f.writelines(f'\n{x} \n')
                    x = dataf[dataf["Species"] == x]
                    describex = x.describe()
                    stringx = describex.to_string(header=True, index =True)
                    f.writelines(stringx) 
                    y = dataf.groupby("Species").size())
                    f.writelines(y)
                f.close()

def createsimplehist():
    dataf.hist()
    plt.savefig('combinedhist.png')
    plt.close()

dataf.plot(kind='hist', figsize = (11,11), color=species, subplots="True", title='My Title')
plt.show()

def gethisto():
    for name in datafields:
        if name != species:
            sns.histplot(data=dataf, x=name, hue=species, binwidth=0.1)
            plt.xlabel(f'{name} in cm')
            plt.title(f'Histogram of the relevant frequency of \n{name.lower()} highlighted by iris species')
            plt.savefig(name+ '.png')
            plt.close()

g = sns.pairplot(data=dataf, hue=species,diag_kind="hist")
g.fig.subplots_adjust(left= .1, bottom=.1, top=.95)
g.fig.suptitle('Pairplot of the variables in the Fisher Iris Dataset', fontsize = 16, fontweight='bold')
g.fig.supxlabel('in cm')
g.fig.supylabel('in cm')
plt.savefig('test.png')


g = dataf.boxplot(by=species)
plt.title('Fisher xxxxx')
ax.setylabel
plt.ylabel('size in cm')
plt.show()

dataf.plot(kind='box', figsize=(8,8), subplots=True, by=species, ylabel = 'Size in cm', title='Box plot of the Fisher Iris Dataset', layout=(2,2))
plt.show()



g.fig.subplots_adjust(left= .1, bottom=.1, top=.95)

g.fig.suptitle('Pairplot of the variables in the Fisher Iris Dataset', fontsize = 16, fontweight='bold')
g.fig.supxlabel('in cm')
g.fig.supylabel('in cm')



def getviolinplots():
    for name in datafields:
        if name != species:
            sns.violinplot(data=dataf, x=species, y=name)
            plt.ylabel(name+ 'in cm')
            plt.title(f'Violin plot of {name} in cm separated by species')
            plt.savefig(name+ 'violin.png')
            plt.close()

getviolinplots()
'''
