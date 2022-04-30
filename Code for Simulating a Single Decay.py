#for importing the required packages 
import numpy as np
import random as rn
import matplotlib.pyplot as plt 
import math as m
#definition to count the number of zeros
def zeros(q):
    n=0
    for i in range(len(q)):
            if q[i]==0:
                n += 1
    return(n)
n = 100000 #number of particles
p = 0.001 #probability of each decay
q = np.ones(n) #particles given each matrix location 
L = [] #to find the number of decay number
itera = 0
N = zeros(q) 

while N < 0.9*n: #going over all the particles until 90% decay is obtained 
    itera += 1
    for i in range(n): #going through each particles
        if q[i]!=0:    #checking if the particle has already decayed
            if rn.uniform(0,1)< p: #checking if the probability is statisfied 
                q[i] = 0 #if yes then it decays (indicated by zero)
    N = zeros(q)  #calculating the number of zeros (decays)
    L.append(n-N) #storing them 
    
print(itera)

T = np.arange(itera)
plt.plot(T, L, label = "Monte carlo method")
plt.title(n, 'particles')
plt.plot(T,n * np.exp (-T*p),linestyle = '--', label = 'Ideal') 
print(np.log(2)/p)
plt.legend(loc='upper right')
plt.show()
