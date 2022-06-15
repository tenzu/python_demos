# coding:utf-8
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

np.random.seed(666)
x = np.random.uniform(-3.0, 3.0, size=100)
X = x.reshape(-1, 1)
y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, size=100)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

# 使用线性回归
lin_reg = LinearRegression()

# 线性回归 MSE
lin_reg.fit(X_train, y_train)
y_predict = lin_reg.predict(X_test)
print('The MSE of linear regression is:\n',
      mean_squared_error(y_test, y_predict))


# 使用多项式回归
def PolynomialRegression(degree):
    return Pipeline([("poly", PolynomialFeatures(degree=degree)),
                     ("std_scaler", StandardScaler()),
                     ("lin_reg", LinearRegression())])

# 2次项式回归
poly2_reg = PolynomialRegression(degree=2)
poly2_reg.fit(X_train, y_train)
y2_predict = poly2_reg.predict(X_test)
print('The MSE of degree=2 is:\n', mean_squared_error(y_test, y2_predict))
# 10次项式回归
poly10_reg = PolynomialRegression(degree=10)
poly10_reg.fit(X_train, y_train)
y10_predict = poly10_reg.predict(X_test)
print('The MSE of degree=10 is:\n', mean_squared_error(y_test, y10_predict))
# 100次项式回归
poly100_reg = PolynomialRegression(degree=100)
poly100_reg.fit(X_train, y_train)
y100_predict = poly100_reg.predict(X_test)
print('The MSE of degree=10 is:\n', mean_squared_error(y_test, y100_predict))