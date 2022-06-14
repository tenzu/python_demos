# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 生成样本特征和标签（非线性关系）
x = np.random.uniform(-3, 3, size=100)
X = x.reshape(-1, 1)
print('原始矩阵特征:\n', X.shape)
y = 2 + x + 0.5 * x**2 + np.random.normal(0, 1, 100)

poly = PolynomialFeatures(degree=2)  # 最高次为2
poly.fit(X)
X2 = poly.transform(X)
print('现有矩阵特征:\n', X2.shape)  # X 的 0,1,2 次方特征
lin_reg2 = LinearRegression()
lin_reg2.fit(X2, y)
y_predict2 = lin_reg2.predict(X2)
print('节距:\n', lin_reg2.intercept_)  # y 中指定为 2
print('多项式系数:', lin_reg2.coef_)    # y 中指定为 0, 1, 0.5
plt.scatter(x, y)
plt.plot(np.sort(x), y_predict2[np.argsort(x)], color='r')
plt.show()