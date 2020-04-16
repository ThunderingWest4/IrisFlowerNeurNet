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
            info = []
            for inepy in data:
                wah = [self.inputBias]
                for elem in inepy[0].tolist():
                    wah.append(elem)
                tY = [0 for i in range(3)]; tY[inepy[1]] = 1
                inp = [wah, tY]
                t1 = self.feedForward(inp[0])

                HLweighted, output = t1[0], t1[1]
                info.append([inp, HLweighted, output])
                #print(output, a[1])
                self.backprop(HLweighted, output, inp[0], inp[1], len(data))
            #now all examples have been ff'd
            #info[0] = input of ex, info[1] = HLweighted, info[2] = predicted output
            """errors = (-1/len(info)) * np.sum([np.multiply(info[i][0][1], arrLog(info[i][2])) + 
                     arrMult(
                     np.subtract(1, info[i][0][1]), 
                     arrLog(
                         np.subtract(1, info[i][2])) 
                     ) for i in range(len(info))])"""
            
            #errors = (-1/len(info)) * np.sum(np.subtract(info[i][0][1], info[i][2]) for i in range(len(info)))
            #self.bProp(errors, info)
            #random.shuffle(data)
            #print(i)
    def backprop(self, HLw, pred, x, y, totalEx):
        print(pred, y)
        error = 2*np.subtract(y, pred)
        print(error)
        
        t = [self.hiddenBias]
        for thing in HLw:
            t.append(thing)
        HLw = t

        DHL = dot(HLw, np.multiply(error, sig_arr_deriv(pred)))
        DIL = np.dot(x, (np.dot(np.multiply(error, sig_arr_deriv(pred)), np.transpose(self.HLweights))*sig_arr_deriv(HLw))[1:])
        
        self.HLweights += np.multiply(self.alpha, DHL)
        self.ILweights += np.multiply(self.alpha, DIL)
        #self.hiddenBias += np.sum(DHL)*self.alpha
        #self.inputBias += np.sum(DIL)*self.alpha

    def feedForward(self, passedIn):
        ret = [0 for i in range(self.outputSize)]
        temp = [0 for i in range(self.hiddenSize)]
        #print(inp, self.ILweights, self.HLweights)

        temp = np.dot(self.ILweights, passedIn)

        for inty in range(len(temp)):
            temp[inty] = sigmoid(temp[inty])

        
        tx = [self.hiddenBias]
        for elemen in temp.tolist():
            tx.append(elemen)
       
        ret = np.dot(tx, self.HLweights)
        
        for minty in range(len(ret)):
            ret[minty] = sigmoid(ret[minty])
        print(passedIn, tx, ret)
        return [temp, ret]
        #return [temp, ret]

    def bProp(self, yErrs, inform):

        for i in range(len(inform)): 
            YArr = inform[i][0][1]
            HLweighted = inform[i][1]
            currOutErr = yErrs
            x = inform[i][0]
            #error = 0.5 * np.square(np.subtract(YArr, out))

            HL_error = np.dot(currOutErr, np.transpose(self.HLweights))
            temp = sig_arr_deriv(inform[i][1])
            temp.insert(0, self.hiddenBias)
            D_HL = [a*HL_error for a in temp]
            #np.dot(temp, HL_error)
            #[temp[i] * HL_error for i in range(len(temp))]

            #Adding two 0's to make dimensions match that of HLweighted
            #Dout = currOutErr.tolist()
            #D_out_layer.append(0)
            #D_out_layer.append(0)            
            #Now to update weights
            D_out_layer = currOutErr.tolist()
            #D_out_layer = [self.hiddenBias]
            #print(Dout)
            #for tjing in Dout:
            #    D_out_layer.append(tjing)
            tHL = HLweighted.tolist()
            tHL.insert(0, self.hiddenBias)
            print(self.unDottedRet)
            #self.HLweights += (self.alpha * np.dot(D_out_layer, (self.unDottedRet)))
            #i think we need not the summed and weighted layer but the full on every weighted value
            #self.ILweights += self.alpha * np.dot(x[0], np.transpose(self.rawTemp))
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
    if(type(x) == int or type(x) == float or type(x) == np.float64):
        return (1 / (1 + np.exp(-1*x)))
    else:
        return(sigList(x))

def sig_arr(x):
    return [sigmoid(a) for a in x]

def maxIndex(arr):
    ind = 0
    prevmax = 0
    for i in range(len(arr)):
        if(arr[i] > prevmax):
            ind = i
            prevmax = arr[i]
    return ind

def sig_deriv(x):
    return sigmoid(x)*(np.subtract(1, sigmoid(x)))

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
    rety = []
    for x in arr1:
        rettemp = []
        for y in arr2:
            rettemp.append(x*y)
        rety.append(rettemp)
    return rety

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
    
def arrLog(arr):
    return [math.log(abs(x)) for x in arr]

def arrMult(a1, a2):
    while(len(a1) < len(a2)):
        a1.append(1)
    while(len(a2) < len(a1)):
        a2.append(1)
    return np.multiply(a1, a2)