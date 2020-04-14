from sklearn import datasets
import network
import random
import threading
import time
import os
clear = lambda: os.system('cls') #on Windows System

start_time = time.process_time()
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

"print(val)"

def loading():
    while True:
        print("\\")
        time.sleep(0.001)
        clear()
        print(".")
        time.sleep(0.001)
        clear()
        print("/")
        time.sleep(0.001)
        clear()


training = val[0:124]
testing = val[125:]

#thread = threading.Thread(target=loading)
#thread.start()
NN.train(training, 1000, 0.1)
#thread.stop()

NN.test(testing)
end_time = time.process_time()
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Time Finished: ", current_time)
print("Time Elapsed: ", (end_time - start_time))

