#importing the required packages 
import numpy as np
import random as rn
import matplotlib.pyplot as plt 
import math as m
#definition to calculate number of decays
def zero(q, s):
    n=0
    for i in range(len(q)):
            if q[i]==s:
                n += 1
    return(n)

#defintion to find an element in a matrix
def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)
t_half_a = 14.9 #half life of Radium 
t_half_b = 9.92 #half lifeof Ac 
timepoint = 50 #number of time steps 
t1 = 200 #total time
dt = t1 / timepoint #time step
n = 10000 #number of particles
pa = 1 - np.exp(-dt / t_half_a * np.log(2)) #Calculating the decay probabilities 
pb = 1 - np.exp(-dt / t_half_b * np.log(2))
qa = np.zeros(timepoint) #number of Ra decay in each time step
qb = np.zeros(timepoint) #number of Ac decay in each time step
dqa = np.zeros(timepoint) #Change in number of Ra decay in each time step
dqb = np.zeros(timepoint) #Change in number of Ac decay in each time step
q = np.ones((n)) #matrix of each particle
#iterating till the time reaches
for j in range(timepoint):
    qa[j] = zero(q, 1) #to find the number of decays
    qb[j] = zero(q, 2)
    if j> 1:
        dqa[j] = qa[j] - qa[j-1] #calculating the change
        dqb[j] = qb[j]-qb[j-1] 
    #going through each particle 
    for i in range(n):
        #checking if a particles has not decayed at all
        if q[i]==1:
            if rn.uniform(0,1)< pa: #checking if the probability is statisfied 
                q[i] = 2 #then decay to Ac
            else:
                q[i] = 1 #else will it wont
        elif q[i] == 2: #checking if Ra has decayed to Ac
            if rn.uniform(0,1)< pb: #checking if the probability is satisfied
                q[i] = 3  #then decay
            else:
                q[i] = 2 #else not
                
timebase = np.arange(0, t1, t1/timepoint)
plt.plot(timebase, qa,label = 'Radium')
plt.plot(timebase, qb,label = 'Acitinium') 
print(pa) 
plt.figure() 
plt.plot(timebase,dqa) 
plt.plot(timebase,dqb) 
val =max(dqb) 
print(dqb.index(val))

