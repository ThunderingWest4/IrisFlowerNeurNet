import numpy as np

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[0],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        print(self.layer1, self.output)

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(np.transpose(self.layer1), (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(np.transpose(self.input), ((np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), np.transpose(self.weights2.T)) * sigmoid_derivative(self.layer1))))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

def sigmoid(arr):
    return [(1 / (1 + np.exp(-1*x))) for x in arr]

def sigmoid_derivative(arr):
    return np.multiply(sigmoid(arr), np.subtract(1, sigmoid(arr)))