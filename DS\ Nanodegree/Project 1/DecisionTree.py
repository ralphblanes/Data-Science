import scipy
import csv as csv
import numpy as np
import pandas
from sklearn.ensemble import RandomForestClassifier

data = pandas.read_csv(('./Data/Titanic/train.csv'),header = 0)

data[data['Sex'] == 'male'] = 1.0
data[data['Sex'] == 'female'] = 0.0
data[data['Sex'].isnull()] = -1.0
#1 for male, 0 for female, -1 for null

data[data['Embarked'] == 'C'] = 0.0
data[data['Embarked'] == 'S'] = 1.0
data[data['Embarked'] == 'Q'] = 2.0
#a different number for each port


data[data['Age'].isnull()] = data['Age'].median()
#Munging Age numbers
data.drop('PassengerId',1)
data = data.as_matrix()

forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit(data[0::,1::],data[0::,0])
output = forest.predict(data)
print output



