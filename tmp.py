# coding:utf-8
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 使用 hard voting
voting_clf = VotingClassifier(estimators=[
    ('log_clf', LogisticRegression()), ('svm_clf', SVC()),
    ('dt_clf', DecisionTreeClassifier(random_state=666))
],
                              voting='hard')

voting_clf.fit(X_train, y_train)
print('hard voting score:\n', voting_clf.score(X_test, y_test))

# 使用 soft voting
voting_clf2 = VotingClassifier(estimators=[
    ('log_clf', LogisticRegression()), ('svm_clf', SVC(probability=True)),
    ('dt_clf', DecisionTreeClassifier(random_state=666))
],
                               voting='soft')

voting_clf2.fit(X_train, y_train)
print('soft voting score:\n', voting_clf2.score(X_test, y_test))