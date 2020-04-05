import math
import random
import numpy as np

class NeuralNetwork():

    def NeuralNetwork(self, inputN, hiddenL, outputN):
        #constructor
        self.input = inputN
        self.hidden = hiddenL
        self.output = outputN
        self.totalL = self.input + self.hidden + self.output

    def fProp(self):
        pass
    
    def train(self, data, iters):
        self.ILweights = [[random.randint(-1000, 1000) for k in range(5)] for q in range(5)]
        #5 branches from each node
        #4 input nodes + 1 bias node
        #5 nodes in the hidden layer + 1 bias
        #3 nodes in output layer, 3 choices
        self.HLweights = [[random.randint(-1000, 1000) for k in range(3)] for q in range(6)]
        #range(3) because 3 branches off
        #q in range(5) because 5 nodes
        #weightedVals1 = []
        #weightedVals2 = []
        """for i in range(iters):
            for a in data:
                LInput = a[0]
                y = a[1]
                for f in range(len(LInput)):
                    weightedVals.append([LInput[f]*self.ILweights[f][w] for w in range(len(self.ILweights))])
        """
        for a in data:
                """LInput = a[0]
                #already has a bias
                y = a[1]
                #y is the expected output/index of solution. 
                #the output of nn will be a len3 array and the inds are 0, 1, 2
                #y is the expected index of solution
                almost = []
                for f in range(len(LInput)):
                    "print(self.ILweights, LInput)"
                    tem = self.ILweights[f]
                    almost.append(sigmoid(sum([tem[i]*LInput[f] for i in range(len(tem))])))

                weightedVals1.append(almost)
                
                #we now have the nodes of the first hidden layer
                #now to find what value they output when multiplied by the new weights
                #3 connections per node, including the bias

                for t in weightedVals1:
                        node = bias(t)                        
                        #add bias
                        print(node, LInput)
                        temp2 = []
                        for f in range(len(node)):
                            temp2.append(sigmoid(sum(np.dot(LInput, self.HLweights))))
                        weightedVals2.append(temp2)

                print("---------------------------------")
                print(weightedVals1)
                print(weightedVals2)"""
                output = self.feedForward(a[0])
                ans = a[1]
                print(output)
                
        
        #we almost have the fprop part down, next we need to work on backprop
        
    def feedForward(self, inp):
        ret = []
        temp = []
        #print(inp, self.ILweights, self.HLweights)
        for x in inp:
            t1 = []
            for chain in self.ILweights:
                #print(x, chain)
                t1.append(sigmoid(sum([j*x for j in chain])))
            temp.append(t1)
        for i in temp:
            t2 = []
            for chain in self.ILweights:
                #print(x, chain)
                t2.append(sigmoid(sum([j*x for j in chain])))
            ret.append(t2)
        return ret

    def test(self, testdata):
        pass

    def bProp(self):
        pass

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))


def maxIndex(arr):
    ind = 0
    prevmax = 0
    for i in range(len(arr)):
        if(arr[i] > prevmax):
            ind = i
            prevmax = arr[i]
    return ind

def bias(arr):
    temp = [1]
    for el in arr:
        temp.append(el)
    return temp

def sig_deriv():
    


    return 4