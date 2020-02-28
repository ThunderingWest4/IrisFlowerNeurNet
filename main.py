from sklearn import datasets
import network

iris = datasets.load_iris()
irisdat = iris.data
#print(irisdat)
print(irisdat[0])
numTypes = 3
#total of 150 different things in the iris dataset
#4 attributes
#first 50 are setosa, second 50 are versicolour, last 50 are virginica
NN = network.NeuralNetwork(len(irisdat[0]), 2, numTypes)

