import matplotlib.pyplot
import numpy
# neural network class defination


class neuralNetwork:
    # initialize the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # learning rate
        self.lr = learningrate
        pass

    # train the neural network
    def train():
        pass

    # query the neural network
    def query():
        pass


input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.5
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
print(numpy.random.rand(3, 3) - 0.5)
