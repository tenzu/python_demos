# coding:utf-8
# 获得前 n 个主成分
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


X = demean(X)


def f(w, X):
    return np.sum((X.dot(w)**2)) / len(X)


# 根据数学公式求梯度
def df(w, X):
    return X.T.dot(X.dot(w)) * 2. / len(X)


def direction(w):
    return w / np.linalg.norm(w)


def first_component(X, initial_w, eta, n_iters=1e4, epsilon=1e-8):
    w = direction(initial_w)
    cur_iter = 0
    while cur_iter < n_iters:
        gradient = df(w, X)
        last_w = w
        w = w + eta * gradient
        w = direction(w)
        if (abs(f(w, X) - f(last_w, X)) < epsilon):
            break
        cur_iter += 1
    return w


initial_w = np.random.random(X.shape[1])
eta = 0.001
w = first_component(X, initial_w, eta)
# 去掉第一主成分的分量
X2 = X - X.dot(w).reshape(-1, 1) * w
plt.scatter(X2[:, 0], X2[:, 1])
plt.show()


def first_n_components(n, X, eta=0.01, n_iters=1e4, epsilon=1e-8):
    X_pca = X.copy()
    X_pca = demean(X_pca)
    res = []
    for i in range(n):
        initial_w = np.random.random(X_pca.shape[1])
        w = first_component(X_pca, initial_w, eta)
        res.append(w)
        X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w
    return res


# 第二主成分
print('The 2 principal components are:\n', first_n_components(2, X))
