# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

boston = datasets.load_boston()
X = boston.data
y = boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X_train, y_train)

# 训练集准确度很好但测试集很差，说明过拟合，模型泛化能力差
print('Decison tree regressor score on test data:\n', dt_reg.score(X_test, y_test))
print('Decison tree regressor score on train data:\n', dt_reg.score(X_train, y_train))