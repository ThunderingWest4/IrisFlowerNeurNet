from datetime import datetime
import time

starting_time = datetime.now().strftime("%H:%M:%S")
begin = time.process_time()
print("Time Started: ", starting_time)

from sklearn import datasets
import network
import random
import threading
import os
from visualize import visualize as vis

iris = datasets.load_iris()
irisdat = iris.data
#print(irisdat)
numTypes = 3
#total of 150 different things in the iris dataset
#4 attributes
#first 50 are setosa, second 50 are versicolour, last 50 are virginica
NN = network.NeuralNetwork()
NN.NeuralNetwork(len(irisdat[0]), 1, 5, numTypes)
val = []

for i in range(len(irisdat)):

    u = irisdat[i]
    if(i<=50): 
        val.append([u, 0])
    elif(50 < i and i <= 100):
        val.append([u, 1])
    elif(100 < i and i <= 150):
        val.append([u, 2])

random.shuffle(val)

training = val[0:99]
testing = val[100:]
iters = 1000
NN.train(training, iters, 0.32)
#print("Previously seen (training) example progress: ")
#NN.test(training)
#print("----------------------------------------------")
print("New and Never Before Seen (testing) example set: ")
NN.test(testing)
vis(NN.totalErr)
end_time = time.process_time()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Time Started: ", starting_time)
print("Time Finished: ", current_time)
print("Time Elapsed: ", (end_time - begin))
print("Learning Rate: " + str(NN.alpha))
print("Iterations Trained: " + str(iters))


