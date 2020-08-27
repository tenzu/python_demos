import numpy as np
from math import exp
I = np.array([0.9, 0.1, 0.8])
W1 = np.array([[0.9, 0.3, 0.4], [0.2, 0.8, 0.2], [0.1, 0.5, 0.6]])
X1 = np.matmul(W1, I)


def sigmoid(x):
    return 1/(1+exp(-x))


for i in range(0, len(X1), 1):
    X1[i] = sigmoid(X1[i])
print(X1)
