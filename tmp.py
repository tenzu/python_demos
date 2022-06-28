# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=666)
# 不再有 OOB，因此需要 train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

# 使用 ada boosting
ada_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),
                             n_estimators=500)
ada_clf.fit(X_train, y_train)
print('ada boosting score:\n', ada_clf.score(X_test, y_test))
