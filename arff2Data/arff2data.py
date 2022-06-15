# coding=utf-8
import arff
import numpy as np
from sklearn.model_selection import train_test_split

originalData = arff.load(open('iris.arff'))
dataset=np.array(originalData['data'])
X = dataset[:,:-1]
y = dataset[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=666)