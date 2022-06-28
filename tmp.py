# coding:utf-8
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 逻辑回归
log_clf = LogisticRegression()
log_clf.fit(X_train, y_train)
print('Logistic regression score:\n', log_clf.score(X_test, y_test))

# 支撑向量机
svm_clf = SVC()
svm_clf.fit(X_train, y_train)
print('SVM score:\n', svm_clf.score(X_test, y_test))

# 决策树分类
dt_clf = DecisionTreeClassifier(random_state=666)
dt_clf.fit(X_train, y_train)
print('Decision tree score:\n', dt_clf.score(X_test, y_test))

# 三种算法的预测值
y_predict1 = log_clf.predict(X_test)
y_predict2 = svm_clf.predict(X_test)
y_predict3 = dt_clf.predict(X_test)

y_predict = np.array((y_predict1 + y_predict2 + y_predict3) >= 2, dtype='int')
print('手动集成学习准确率:\n', accuracy_score(y_test, y_predict))

# 使用 sklearn voting classifier
voting_clf = VotingClassifier(estimators=[
    ('log_clf', LogisticRegression()), ('svm_clf', SVC()),
    ('dt_clf', DecisionTreeClassifier(random_state=666))
],
                              voting='hard')

voting_clf.fit(X_train, y_train)
print('sklearn voting score:\n', voting_clf.score(X_test, y_test))