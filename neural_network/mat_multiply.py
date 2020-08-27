import numpy as np
from math import exp
I = np.array([0.9, 0.1, 0.8])
W1 = np.array([[0.9, 0.3, 0.4], [0.2, 0.8, 0.2], [0.1, 0.5, 0.6]])
X1 = np.matmul(W1, I)
print(X1)
print(type(X1))
for i in range(len(X1)):
    X1[i] = 1 / (1 + exp(-X1[i]))
print(X1)