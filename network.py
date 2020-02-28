import math

class NeuralNetwork():

    def NeuralNetwork(self, inputN, hiddenL, outputN):
        #constructor
        self.input = inputN
        self.hidden = hiddenL
        self.output = outputN

    def fProp(self):
        pass

def activation(x):
    return (1 / (1 + (math.e ** (x*-1))))