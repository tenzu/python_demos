# coding:utf-8
# 岭回归
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)
x = np.random.uniform(-3.0, 3.0, size=100)
X = x.reshape(-1, 1)
y = 0.5 * x + 3 + np.random.normal(0, 1, size=100)

def PolynomialRegression(degree):
    return Pipeline([("poly", PolynomialFeatures(degree=degree)),
                     ("std_scaler", StandardScaler()),
                     ("lin_reg", LinearRegression())])

X_train, X_test, y_train, y_test = train_test_split(X, y)
# 使用多项式回归
poly_reg = PolynomialRegression(degree=20)
poly_reg.fit(X_train, y_train)
y_poly_predict = poly_reg.predict(X_test)
# MSE 较大，出现过拟合
print('The MSE of 20th regression is:\n', mean_squared_error(y_test, y_poly_predict))


def plot_model(model):
    X_plot = np.linspace(-3, 3, 100).reshape(100, 1)
    y_plot = model.predict(X_plot)

    plt.scatter(x, y)
    plt.plot(X_plot[:, 0], y_plot, color='r')
    plt.axis([-3, 3, 0, 6])
    plt.show()


plot_model(poly_reg)

# 使用 sklearn 自带的岭回归
from sklearn.linear_model import Ridge

def RidgeRegression(degree, alpha):
    return Pipeline([("poly", PolynomialFeatures(degree=degree)),
                     ("std_scaler", StandardScaler()),
                     ("ridge_reg", Ridge(alpha=alpha))])

ridge1_reg = RidgeRegression(degree=20, alpha=0.0001)   # alpha 参见公式
ridge1_reg.fit(X_train, y_train)
y1_predict = ridge1_reg.predict(X_test)
print('The MSE after ridge is:\n', mean_squared_error(y_test, y1_predict))
plot_model(ridge1_reg)