# coding:utf-8
# 特征降维模拟
from xml.dom import INVALID_MODIFICATION_ERR
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

# 目标函数
def f(w, X):
    return np.sum((X.dot(w)**2)) / len(X)

# 根据数学公式求梯度
def df_math(w, X):
    return X.T.dot(X.dot(w)) * 2. / len(X)

def direction(w):
    return w / np.linalg.norm(w)

def gradient_ascent(df, X, initial_w, eta, n_iters=1e4, epsilon=1e-8):

    w = direction(initial_w)
    cur_iter = 0

    while cur_iter < n_iters:
        gradient = df(w, X)
        last_w = w
        w = w + eta * gradient
        w = direction(w)  # 注意1：每次求一个单位方向
        if (abs(f(w, X) - f(last_w, X)) < epsilon):
            break

        cur_iter += 1

    return w

initial_w = np.random.random(X.shape[1])  # 注意2：不能用 0 向量开始
print('w 初始值:\n', initial_w)
eta = 0.001
w = gradient_ascent(df_math, X_demean, initial_w, eta)

plt.scatter(X_demean[:, 0], X_demean[:, 1])
plt.plot([0, w[0] * 30], [0, w[1] * 30], color='r')
plt.show()