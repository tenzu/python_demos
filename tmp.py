# coding:utf-8
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)

# 使用 OOB 后无需 train_test_split，仅对样本数量进行随机取样
bagging_clf = BaggingClassifier(DecisionTreeClassifier(),
                                n_estimators=500,
                                max_samples=100,
                                bootstrap=True,
                                oob_score=True,
                                n_jobs=-1)
bagging_clf.fit(X, y)
print('决策树放回取样随机选择样本数量时的准确度:\n', bagging_clf.oob_score_)

# 仅针对特征进行随机取样
random_subspaces_clf = BaggingClassifier(DecisionTreeClassifier(),
                                         n_estimators=500,
                                         max_samples=500,
                                         bootstrap=True,
                                         oob_score=True,
                                         max_features=1,
                                         bootstrap_features=True)
random_subspaces_clf.fit(X, y)
print('决策树放回取样随机选择特征时的准确度:\n', random_subspaces_clf.oob_score_)

# 针对样本数量和特征都进行随机取样
random_patches_clf = BaggingClassifier(DecisionTreeClassifier(),
                                       n_estimators=500,
                                       max_samples=100,
                                       bootstrap=True,
                                       oob_score=True,
                                       max_features=1,
                                       bootstrap_features=True)
random_patches_clf.fit(X, y)
print('决策树放回取样随机选择样本数量和随机特征时的准确度:\n', random_patches_clf.oob_score_)