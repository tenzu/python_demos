import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# all data for training
def kNNTrain1():
    raw_data_X1 = [[3.393533211, 2.331273381], [3.110073483, 1.781539638],
                   [1.343808831, 3.368360954], [3.582294042, 4.679179110],
                   [2.280362439, 2.866990263], [7.423436942, 4.696522875],
                   [5.745051997, 3.533989803], [9.172168622, 2.511101045],
                   [7.792783481, 3.424088941], [7.939820817, 0.791637231]]
    raw_data_y1 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    X_train = np.array(raw_data_X1)
    y_train = np.array(raw_data_y1)
    x = np.array([2.343808831, 3.368360954])
    kNN_classifier = KNeighborsClassifier(n_neighbors=6, n_jobs=-1)
    kNN_classifier.fit(X_train, y_train)
    X_predict = x.reshape(1, -1)
    y_predict = kNN_classifier.predict(X_predict)
#    plt.scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], color='b')
#    plt.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], color='r')
#    plt.scatter(X_predict[0, 0], X_predict[0, 1], color='g', marker='*')
#    plt.show()
    return y_predict[0]


# data for training and testing
def kNNTrain2():
    iris = datasets.load_iris()
    iris.keys()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.93,
                                                        random_state=666)
    #    x = np.array([5.1, 3.5, 1.4, 0.2])
    #    x = np.array([7.0, 3.2, 4.7, 1.4])
    x = np.array([6.3, 3.3, 6.0, 2.5])
    kNN_classifier = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
    kNN_classifier.fit(X_train, y_train)
    X_predict = x.reshape(1, -1)
    y_predict = kNN_classifier.predict(X_predict)
    y_predict2 = kNN_classifier.predict(X_test)
    print("The score for prediction is:", accuracy_score(y_test, y_predict2))
    return y_predict[0]


print("Below is the prediction from kNNTrain1")
print("The prediction is:", kNNTrain1())
print("Below is the prediction from kNNTrain2")
print("The prediction is:", kNNTrain2())