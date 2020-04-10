import math
import random
import numpy as np

class NeuralNetwork():

    def NeuralNetwork(self, inputN, hiddenL, hiddenS, outputN):
        #constructor
        self.input = inputN
        self.hidden = hiddenL
        self.hiddenSize = hiddenS
        self.outputSize = outputN

    def fProp(self):
        pass
    
    def train(self, data, iters, learningRate):
        self.alpha = learningRate
        self.ILweights = [[random.random() for k in range(5)] for q in range(5)]
        #5 branches from each node
        #4 input nodes + 1 bias node
        #5 nodes in the hidden layer + 1 bias
        #3 nodes in output layer, 3 choices
        self.HLweights = [[random.random() for k in range(3)] for q in range(6)]
        #range(3) because 3 branches off
        for i in range(iters):
            for inp in data:
                    t1 = self.feedForward(inp[0])
                    HLweighted, output = t1[0], t1[1]
                    #print(output, a[1])
                    self.bProp(inp[0], inp[1], output, HLweighted, inp[0])
                
        #backprop is jury-rigged together but HOPEFULLY works        
        
    def feedForward(self, inp):
        ret = [0 for i in range(self.outputSize)]
        temp = [0 for i in range(self.hiddenSize)]
        #print(inp, self.ILweights, self.HLweights)

        for x in range(len(inp)):
            for i in range(self.hiddenSize):
                temp[i] += self.ILweights[x][i]*sigmoid(inp[x])
                #temp[i] += self.ILweights[x][i]*(inp[x])
        #for inty in range(len(temp)):
        #    temp[inty] = sigmoid(temp[inty])

        for i in range(len(temp)):
            for i in range(self.outputSize):
                ret[i] += self.HLweights[x][i]*sigmoid(temp[x])
                #ret[i] += self.HLweights[x][i]*(temp[x])
        #for minty in range(len(ret)):
        #    ret[minty] = sigmoid(ret[minty])
        return [temp, ret]

    def bProp(self, x, y, out, HLweighted, originp):
        #loss = (desired - actual)^2
        #RECODE THIS ENTIRE THING
        YArr = [0 for i in range(3)]; YArr[y] = 1
        error = np.subtract(YArr, out)
        D_out_layer = error * sig_arr_deriv(out)

        HL_error = dot(D_out_layer, np.transpose(self.HLweights))
        temp = sig_arr_deriv(HLweighted)
        temp.insert(0, 1)
        D_HL = mult(HL_error, temp)

        #Now to update weights
        self.HLweights += self.alpha * dot(np.transpose(HLweighted), D_out_layer)
        self.ILweights += self.alpha * dot(x, D_HL)

    def test(self, testdata):
        print("-----------------------------------------------------------------")
        tests = 0
        correct = 0
        total = len(testdata)
        for x in testdata:
            result = ""
            returned = self.feedForward(x[0])
            ans = returned[1]
            if(maxIndex(ans) == x[1]):
                result = "correct"
                correct+=1
            else:
                result = "wrong"
            tests+=1
            print("Test Number " + str(tests) + ": The Network was " + str(result))
        print("The Network was " + str((correct/total)*100) + "% Correct")
        

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

def sig_deriv(x):
    return sigmoid(x)*(1-sigmoid(x))

def sig_arr_deriv(inarr):
    a = []
    for x in inarr:
        a.append(sig_deriv(x))
    return a

def roundint(x):
    return 1 if (x>=0.5) else 0

def rounder(givArr):
    ret = []
    for x in givArr:
        ret.append(roundint(x))
    return ret

def dot(arr1, arr2):
    to_be_summed = []
    for x in arr1:
        for y in arr2:
            to_be_summed.append(x*y)
    return sum(to_be_summed)

def add(arr, num):
    ret = []
    for mini in arr:
        temp = []
        for x in mini:
            temp.append(x+num)
        ret.append(temp)
    return ret

def mult(arr1, arr2):
    if(len(arr1) == len(arr2)):
        return [arr1[i]*arr2[i] for i in range(len(arr1))]
    else:
        raise Exception("Inequal shapes {} and {}", len(arr1), len(arr2))

    
