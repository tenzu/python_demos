# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

digits = datasets.load_digits()
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

knn_clf1 = KNeighborsClassifier(n_jobs=-1)
knn_clf1.fit(X_train, y_train)
print('The kNN score is:\n', knn_clf1.score(X_test, y_test))

# 64个主成分
pca = PCA(n_components=X_train.shape[1])
pca.fit(X_train)
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)
knn_clf2 = KNeighborsClassifier(n_jobs=-1)
knn_clf2.fit(X_train_reduction, y_train)
print('The PCA score is:\n', knn_clf2.score(X_test_reduction, y_test))
# 主成分所解释的方差
print('主成分所解释的方差:\n', pca.explained_variance_ratio_)
# 前 i 个主成分保留下来的方差信息比例曲线
plt.plot([i for i in range(X_train.shape[1])], [
    np.sum(pca.explained_variance_ratio_[:i + 1])
    for i in range(X_train.shape[1])
])
plt.show()
# 指定保留 95% 的方差信息
pca = PCA(0.95)
pca.fit(X_train)
print('保留 95% 方差信息时对应的主成分个数:\n', pca.n_components_)
# score 低于选取64个主成分的情况，但效率会高很多
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)
knn_clf2 = KNeighborsClassifier(n_jobs=-1)
knn_clf2.fit(X_train_reduction, y_train)
print('The PCA score is:\n', knn_clf2.score(X_test_reduction, y_test))

pca = PCA(n_components=2)
pca.fit(X)
X_reduction = pca.transform(X)
for i in range(10):
    plt.scatter(X_reduction[y == i, 0], X_reduction[y == i, 1], alpha=0.8)
plt.show()