from sklearn import datasets
import network
import random

iris = datasets.load_iris()
irisdat = iris.data
#print(irisdat)
print(irisdat[0])
numTypes = 3
#total of 150 different things in the iris dataset
#4 attributes
#first 50 are setosa, second 50 are versicolour, last 50 are virginica
NN = network.NeuralNetwork()
NN.NeuralNetwork(len(irisdat[0]), 2, numTypes)
val = []

for i in range(len(irisdat)):
    x = irisdat[i]
    "print(x)"
    u = [1]
    for el in x:
        u.append(el)
    if(i<=50): 
        val.append([u, 1])
    elif(50 < i and i <= 100):
        val.append([u, 2])
    elif(100 < i and i <= 150):
        val.append([u, 3])

random.shuffle(val)

"print(val)"

training = val[0:124]
testing = val[125:]

NN.train(training, 2000)

NN.test(testing)
