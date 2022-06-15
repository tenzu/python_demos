# coding=utf-8
import os
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# cd to txt2Data folder first
currentPath = os.getcwd()
workingPath = os.chdir(currentPath)


def loadTxt(fileName):
    data = np.loadtxt(fileName, dtype=np.float32, delimiter='\t')
    return data


originalData = loadTxt('data.txt')
X = originalData[:, :-1]
y = originalData[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=666)

print('Shapes of X_train, X_test, y_train, y_test are:\n', np.shape(X_train),
      np.shape(X_test), np.shape(y_train), np.shape(y_test))
plt.figure(1)
plt.subplot(1, 2, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], c='b', marker='+')
plt.axis([0, 100, 0, 100])
plt.xlabel('Feature i')
plt.ylabel('Feature j')
# plt.legend()
plt.title('Features')
plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c='r', marker='1')
plt.axis([0, 100, 0, 100])
plt.xlabel('Feature i')
# plt.ylabel('Feature j')
# plt.legend()
plt.title('Features')
plt.show()