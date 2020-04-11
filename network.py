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
        self.inputBias = 1
        self.hiddenBias = 1
    
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
            for inepy in data:
                    wah = [self.inputBias]
                    for elem in inepy[0].tolist():
                        wah.append(elem)
                    inp = [wah, inepy[1]]
                    t1 = self.feedForward(inp[0])
                    HLweighted, output = t1[0], t1[1]
                    #print(output, a[1])
                    self.bProp(inp[0], inp[1], output, HLweighted, inp[0])
                
        #backprop is jury-rigged together but HOPEFULLY works        
        
    def feedForward(self, passedIn):
        ret = [0 for i in range(self.outputSize)]
        temp = [0 for i in range(self.hiddenSize)]
        #print(inp, self.ILweights, self.HLweights)

        temp = np.dot(passedIn, self.ILweights)

        for inty in range(len(temp)):
            temp[inty] = sigmoid(temp[inty])

        tx = [self.hiddenBias]
        for elemen in temp.tolist():
            tx.append(elemen)

        ret = np.dot(tx, self.HLweights)

        for minty in range(len(ret)):
            ret[minty] = sigmoid(ret[minty])

        return [temp, ret]

    def bProp(self, x, y, out, HLweighted, originp):
        #loss = (desired - actual)^2
        #RECODE THIS ENTIRE THING
        YArr = [0 for i in range(3)]; YArr[y] = 1
        #error = 0.5 * np.square(np.subtract(YArr, out))
        error =np.subtract(YArr, out)
        D_out_layer = error * sig_arr_deriv(out)

        HL_error = np.dot(D_out_layer, np.transpose(self.HLweights))
        temp = sig_arr_deriv(HLweighted)
        temp.insert(0, 1)
        D_HL = [a*HL_error for a in temp]
        #np.dot(temp, HL_error)
        #[temp[i] * HL_error for i in range(len(temp))]

        #Now to update weights
        self.HLweights += self.alpha * dot(np.transpose(HLweighted), D_out_layer)
        self.ILweights += self.alpha * dot(x, D_HL)
        self.inputBias += np.sum(D_HL) * self.alpha
        self.hiddenBias += np.sum(D_out_layer) * self.alpha
        #print(self.HLweights, self.ILweights)
        

    def test(self, testdata):
        print("-----------------------------------------------------------------")
        tests = 0
        correct = 0
        total = len(testdata)
        DoubleCheck = []
        for x in testdata:
            returned = []
            result = ""
            expected = [0 for i in range(3)]; expected[x[1]] = 1
            returned = self.feedForward(insertBias(self, x[0]))
            ans = returned[1]
            if(ans[0] == expected[0] and ans[1] == expected[1] and ans[2] == expected[2]):
                result = "correct"
                correct+=1
            else:
                result = "wrong"
            tests+=1
            DoubleCheck.append([returned[1], expected])
            print("Test Number " + str(tests) + ": The Network was " + str(result))
        print("The Network was " + str((correct/total)*100) + "% Correct")
        for element in DoubleCheck:
            print(element)        

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
    return np.sum(to_be_summed)

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

#Precondition: given is a default (vanilla i guess) python LIST and not a numpy one
def insertBias(obj, given):
    wah = [obj.inputBias]
    for elem in given:
        wah.append(elem)
    return wah
    
