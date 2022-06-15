# coding=utf-8
import arff
import numpy as np

originalData = arff.load(open('iris.arff'))

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

dataset=np.array(originalData['data'])
X = dataset[:,:4]
y = dataset[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)
standardScaler = StandardScaler()
standardScaler.fit(X_train)
print("mean value of data:\n", standardScaler.mean_)
print("standard deviation of data:\n", standardScaler.scale_)
X_train_standard = standardScaler.transform(X_train)
X_test_standard = standardScaler.transform(X_test)
kNN_classifier = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
kNN_classifier.fit(X_train_standard, y_train)
score = kNN_classifier.score(X_test_standard, y_test)
print("The score of standarized data is:\n", score)
