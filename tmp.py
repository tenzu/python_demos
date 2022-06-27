# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

iris = datasets.load_iris()
X = iris.data
y = iris.target
# 只选取两个特征作为示例
X = X[y < 2, :2]
y = y[y < 2]
# 不进行预测，因此不分成训练集和数据集
standardScaler = StandardScaler()
standardScaler.fit(X)
X_standard = standardScaler.transform(X)

# C 为 soft margin 参数，取值越大越接近 hard margin，容错空间越小
# C = 0.01 时可看到出现数据分类错误
svc = LinearSVC(C=1e9)
svc.fit(X_standard, y)


def plot_svc_decision_boundary(model, axis):

    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int(
            (axis[1] - axis[0]) * 100)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int(
            (axis[3] - axis[2]) * 100)).reshape(-1, 1),
    )
    X_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])

    plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)

    w = model.coef_[0]
    b = model.intercept_[0]

    # w0*x0 + w1*x1 + b = 0
    # => x1 = -w0/w1 * x0 - b/w1
    plot_x = np.linspace(axis[0], axis[1], 200)
    up_y = -w[0] / w[1] * plot_x - b / w[1] + 1 / w[1]
    down_y = -w[0] / w[1] * plot_x - b / w[1] - 1 / w[1]

    up_index = (up_y >= axis[2]) & (up_y <= axis[3])
    down_index = (down_y >= axis[2]) & (down_y <= axis[3])
    plt.plot(plot_x[up_index], up_y[up_index], color='black')
    plt.plot(plot_x[down_index], down_y[down_index], color='black')


plot_svc_decision_boundary(svc, axis=[-3, 3, -3, 3])
plt.scatter(X_standard[y == 0, 0], X_standard[y == 0, 1])
plt.scatter(X_standard[y == 1, 0], X_standard[y == 1, 1])
plt.show()

# 两个特征对应两个系数，sklearn 中的 SVM 支持多分类
print('SVM 截距:', svc.intercept_)
print('SVM 系数:', svc.coef_)