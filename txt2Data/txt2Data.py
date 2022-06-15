# coding=utf-8
import os
import numpy as np
from sklearn.model_selection import train_test_split

# currentPath=os.getcwd()
workingPath=os.chdir('/Users/cliff/Documents/GitHub/python_demos/txtData/')

def loadTxt(fileName):
    data=np.loadtxt(fileName,dtype=np.float32,delimiter='\t')
    return data

originalData=loadTxt('temp.txt')
X=originalData[:,:-1]
y=originalData[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
