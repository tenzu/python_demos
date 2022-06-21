# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

np.random.seed(666)
X = np.random.normal(0, 1, size=(200, 2))
y = np.array((X[:, 0]**2 + X[:, 1]) < 1.5, dtype='int')
for _ in range(20):
    y[np.random.randint(200)] = 1
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.show()