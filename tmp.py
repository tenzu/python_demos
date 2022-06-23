# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

digits = datasets.load_digits()
X = digits.data
y = digits.target.copy()
# 手动形成有偏数据
y[digits.target == 9] = 1
y[digits.target != 9] = 0
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_predict = log_reg.predict(X_test)
decision_scores = log_reg.decision_function(X_test)

precisions, recalls, thresholds = precision_recall_curve(
    y_test, decision_scores)
plt.plot(thresholds, precisions[:-1], c='r')
plt.plot(thresholds, recalls[:-1], c='b')
plt.show()

# 精准率-召回率曲线，自动选择坐标值上下限，召回率急剧下降前精确率的值（横坐标）对应平衡点
plt.plot(precisions, recalls)
plt.show()

# 绘制 ROC 曲线
fprs, tprs, thresholds = roc_curve(y_test, decision_scores)
plt.plot(fprs, tprs)
plt.show()
# 求出 ROC 曲线下的面积
# AUC = area under curve
print('ROC AUC score:\n', roc_auc_score(y_test, decision_scores))