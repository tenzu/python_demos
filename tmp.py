# coding:utf-8
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)

# 使用 OOB 后无需 train_test_split
bagging_clf = BaggingClassifier(DecisionTreeClassifier(),
                                n_estimators=500,
                                max_samples=100,
                                bootstrap=True,
                                oob_score=True)
bagging_clf.fit(X, y)
print('决策树放回取样 OOB 准确度:\n', bagging_clf.oob_score_)