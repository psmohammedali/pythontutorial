#IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#IMPORT DATA SET (Make sure the availability of data set in the same folder)
dataset = pd.read_csv('Malware.csv')
dataset2 = dataset.copy()
dataset2 = dataset.drop(['classification'], axis=1)
X = dataset2.iloc[:,1:].values
y = dataset.iloc[:, 2].values


#LABEL ENCODING
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

#SPLIT THE DATA SET
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
print(X_train)
print(y_train)
print(X_test)
print(y_test)


#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)
print(X_test)

#TRAINING THE MODEL
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 50, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
accuracy_score(y_test, y_pred)


print(cm)
temp = accuracy_score(y_test, y_pred)
