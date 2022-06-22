# coding:utf-8
# coding:utf-8
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

digits = datasets.load_digits()
X = digits.data
y = digits.target.copy()
# 手动生成有偏数据
y[digits.target == 9] = 1
y[digits.target != 9] = 0
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
print('逻辑回归准确度:\n', log_reg.score(X_test, y_test))
y_log_predict = log_reg.predict(X_test)
print('混淆矩阵:\n', confusion_matrix(y_test, y_log_predict))
print('精准率:\n', precision_score(y_test, y_log_predict))
print('召回率:\n', recall_score(y_test, y_log_predict))
print('F1 score:\n', f1_score(y_test, y_log_predict))
