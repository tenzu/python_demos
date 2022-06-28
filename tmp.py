# coding:utf-8
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=666)

# 随机森林拥有决策树和 bagging classifier 的所有参数
rf_clf = RandomForestClassifier(n_estimators=500,
                                max_leaf_nodes=16,
                                oob_score=True,
                                random_state=666,
                                n_jobs=-1)
rf_clf.fit(X, y)
print('随机森林准确度:\n', rf_clf.oob_score_)