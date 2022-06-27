# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
X = iris.data
y = iris.targe
X = X[y<2,:2]
y = y[y<2]
# 不进行预测，因此不分成训练集和数据集
standardScaler = StandardScaler()
standardScaler.fit(X)
X_standard = standardScaler.transform(X)
