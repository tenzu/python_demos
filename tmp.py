# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

X = np.arange(1, 11).reshape(-1, 2)
poly = PolynomialFeatures(degree=2)
poly.fit(X)
X2 = poly.transform(X)
print('原始数据的样本数和特征数:\n', X.shape)
print('原始特征:\n', X)

print('升维后数据的样本数和特征数:\n', X2.shape)
# 零次幂特征，原第1列特征，原第2列特征，原第1列特征平方，原第1列特征乘以第2列特征，原第2列特征平方
# 自动补全未列出的二次项特征
# degree=3 时特征为10个
print('升维后特征:\n', X2)
