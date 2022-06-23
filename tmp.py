# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix

digits = datasets.load_digits()
X = digits.data
y = digits.target.copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_predict = log_reg.predict(X_test)
decision_scores = log_reg.decision_function(X_test)

# 修改 average 参数（默认为 binary），计算多分类精准率
print('多分类精准率:\n', precision_score(y_test, y_predict, average="micro"))
# 混淆矩阵
print('Confusion Matrix:\n', confusion_matrix(y_test, y_predict))
# 绘制混淆矩阵，显示预测正确的位置
cfm = confusion_matrix(y_test, y_predict)
plt.matshow(cfm, cmap=plt.cm.gray)
plt.show()

# 绘制混淆矩阵，显示预测错误的地方
row_sums = np.sum(cfm, axis=1)
err_matrix = cfm / row_sums
np.fill_diagonal(err_matrix, 0)
plt.matshow(err_matrix, cmap=plt.cm.gray)
plt.show()