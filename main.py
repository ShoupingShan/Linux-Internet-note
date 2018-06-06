import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import cholesky
import random
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class Perceptron(object):

    def __init__(self):
        self.learning_step = 1
        self.max_iteration = 300000

    def sign(self,x):
        if (x >= 0):
            logic=1
        else:
            logic=0
        return logic

    #  w*x+b
    def threshold(self,w,b,x):
        result = np.dot(w ,x) + b
        return result

    # train
    def train(self,x,y):

        # f,A=plt.subplots(1,2,figsize=(1,2))
        f,A=plt.subplots()
        plt.ion()
        plt.axis([-1.5, 2.5, -1.5, 2.5])
        w = np.zeros(len(x[0]))
        b = 0
        i = 0
        # A.plot(X[0:temp1 - 1, 0], X[0:temp1 - 1, 1], 'r*')
        # A.plot(X[temp1:temp1 + temp2, 0], X[temp1:temp1 + temp2, 1], 'b+')
        # A.set_xticks(());A.set_yticks(())
        while (i<self.max_iteration):
            index = len(y)
            random_number = random.randint(0,index-1)
            if (y[random_number]* self.threshold(w,b,x[random_number])<= 0):
                w = w + self.learning_step * y[random_number]*x[random_number]
                b = b + self.learning_step * y[random_number]
            i = i + 1

            if i%100==0:
                A.clear()
                y1 = (-b - w[0] * 1) / w[1]
                x2 = (-b - w[1] * 1) / w[0]
                A.plot(X[0:temp1 - 1, 0], X[0:temp1 - 1, 1], 'r*')
                A.plot(X[temp1:temp1 + temp2, 0], X[temp1:temp1 + temp2, 1], 'b+')
                A.plot([2, y1], [x2, 2], 'g')
                A.set_xticks(())
                A.set_yticks(())
            plt.draw()
            plt.pause(0.0000000001)

        return w,b


sample=50
u1=np.array([[1,1]])
u2=np.array([[0,0]])
sigma=np.array([[0.2,0],[0,0.2]])


R=cholesky(sigma)
s1=np.dot(np.random.randn(sample,2),R)+u1
s2=np.dot(np.random.randn(sample,2),R)+u2
j1=0
j2=0
max=1.0
min=1.0
for i in range(sample):
    if s1[i,0]+s1[i,1]>=max:
        j1 += 1
    if s2[i,0]+s2[i,1]<min:
        j2 += 1
X=np.zeros((j1+j2,2))
Y=np.zeros((j1+j2))
temp1 = 0
for i in range(sample):
    if s1[i,0]+s1[i,1]>=max:
        X[temp1,0] = s1[i, 0]
        X[temp1,1] = s1[i, 1]
        temp1 += 1
temp2 = 0
for i in range(sample):
    if s2[i,0]+s2[i,1]<min:
        X[temp1+temp2-1,0] = s2[i, 0]
        X[temp1+temp2-1,1] = s2[i, 1]
        temp2 += 1
# plt.plot(X[0:temp1-1,0],X[0:temp1-1,1],'r*')
# plt.plot(X[temp1:temp1+temp2,0],X[temp1:temp1+temp2,1],'b+')
for i in range(j1+j2):
    if i<j1:
        Y[i]=1
    else:
        Y[i]=-1



test = Perceptron()
w,b=test.train(X,Y)

# w*x+b=0
y1=(-b-w[0]*1)/w[1]
x2=(-b-w[1]*1)/w[0]
plt.axis([-1.5,2.5,-1.5,2.5])
plt.plot([2,y1],[x2,2],'g')
plt.show()

