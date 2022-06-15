# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(666)
x = np.random.uniform(-3.0, 3.0, size=100)
X = x.reshape(-1, 1)
y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, size=100)

# 使用线性回归
lin_reg = LinearRegression()
lin_reg.fit(X, y)
lin_reg.score(X, y)
y_predict = lin_reg.predict(X)
print('The score is:\n', lin_reg.score(X, y))
print('The MSE is:\n', mean_squared_error(y, y_predict))
plt.scatter(x, y)
plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
plt.show()
