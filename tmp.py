# coding:utf-8
# 特征降维模拟
import numpy as np
import matplotlib.pyplot as plt

X = np.empty((100, 2))
X[:, 0] = np.random.uniform(0., 100., size=100)
# 两个特征之间存在线性关系，降维效果明显
X[:, 1] = 0.75 * X[:, 0] + 3 + np.random.normal(0, 10., size=100)
plt.scatter(X[:, 0], X[:, 1])
plt.show()


def demean(X):
    return X - np.mean(X, axis=0)  # 已经向量化，无需 for 循环


X_demean = demean(X)
print('第一特征减去平均值后的均值:\n', np.mean(X_demean[:, 0]))
print('第二特征减去平均值后的均值:\n', np.mean(X_demean[:, 1]))
plt.scatter(X_demean[:, 0], X_demean[:, 1])
plt.show()  # 注意坐标轴原点位置和坐标轴上下限
