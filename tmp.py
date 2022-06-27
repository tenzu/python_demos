# coding:utf-8
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

boston = datasets.load_boston()
X = boston.data
y = boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

# epsilon 与 margin 意义相同
def StandardLinearSVR(epsilon=0.1):
    return Pipeline([('std_scaler', StandardScaler()),
                     ('linearSVR', LinearSVR(epsilon=epsilon))])

svr = StandardLinearSVR()
svr.fit(X_train, y_train)

print('Standard linear SVR score:\n', svr.score(X_test, y_test))