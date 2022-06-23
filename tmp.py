# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

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
print('F1 score:\n', f1_score(y_test, y_predict))
print('Confusion matrix:\n', confusion_matrix(y_test, y_predict))
print('Precision score:\n', precision_score(y_test, y_predict))
print('Recall score:\n', recall_score(y_test, y_predict))

# 更改 threshold 值
decision_scores = log_reg.decision_function(X_test)
y_predict_2 = np.array(decision_scores >= 5, dtype='int')
print('The threshold = 5.0')
print('Confusion matrix changes to:\n', confusion_matrix(y_test, y_predict_2))
print('Precision score changes to:\n', precision_score(y_test, y_predict_2))
print('Recall score changes to:\n', recall_score(y_test, y_predict_2))