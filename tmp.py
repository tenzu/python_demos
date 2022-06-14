# coding:utf-8
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

# 该数据集共有70000个样本，arff 文件约 125 MB，可能下载较慢
# to-do：补充读入本地 arff 文件的方法
mnist = fetch_openml('mnist_784')
X, y = mnist['data'], mnist['target']
# 手动分割数据集，取前60000个样本为训练集，后10000个为测试集
X_train = np.array(X[:60000], dtype=float)
y_train = np.array(y[:60000], dtype=float)
X_test = np.array(X[60000:], dtype=float)
y_test = np.array(y[60000:], dtype=float)

# 使用 kNN 算法进行分类（未进行归一化），很耗时
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_train)
print('原数据集包含特征数:\n', X_train.shape)  # 包含 784 个特征
print('降维前的准确率:\n', knn_clf.score(X_test, y_test))

# 使用 PCA 降维后再使用 kNN 算法
pca = PCA(0.90)  # 仅保留 90% 的特征信息
pca.fit(X_train)
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_reduction, y_train)
print('降维后包含特征数:\n', X_train_reduction.shape)
print('降维后的准确率:\n', knn_clf.score(X_test_reduction, y_test))
print('降维去除了噪音，可能准确率更高！')