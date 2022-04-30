#importing the required packages 
import numpy as np
import random as rn
import matplotlib.pyplot as plt 
import math as m
#definition for calculating the number of decay
def zeros(q):
    n=0
    for i in range(len(q)):
            if q[i]==0:
                n += 1
    return(n)
nl =[1000,5000, 10000, 50000, 100000] #set of number of particles 
p = 0.001 #probability

#N = (zeros(q))

itera = 0
for n in nl:
    L = []
    q = np.ones(n)
    for j in range(1000):
        q = np.ones(n) 
        for i in range(n):
            if q[i]!=0:
                if rn.uniform(0,1)< p:
                    q[i] = 0
        N = zeros(q)
        L.append(N) 

plt.figure()
plt.hist(L, density = True) 
plt.title(n)
plt.show()