import numpy as np
import matplotlib.pyplot as plt #import certain libraries to complete the task.
N=10000
infected=1
susceptible=9999
recovered=0
beta=0.3
gama=0.05 #Set variables for every given information
S=[susceptible]
I=[infected]
R=[recovered] #Create lists to record the number of people who are susceptible, infected or recovered.
for i in range (1000): #set a 1000 times loops
    infected_probability=beta*I[-1]/N
    updated_infected=np.random.choice(range(2),S[-1],p=[1-infected_probability,infected_probability]).sum()
    updated_recovery=np.random.choice(range(2),I[-1],p=[1-gama,gama]).sum() #calculate the number of people who are infected right now or recovered right now
    actual_susceptible=S[-1]-updated_infected
    actual_infected=I[-1]+updated_infected-updated_recovery
    actual_recovered=R[-1]+updated_recovery #calculate the actual number of people who are susceptible, infected, recovered for now.
    S.append(actual_susceptible)
    I.append(actual_infected)
    R.append(actual_recovered) #add the actual number to the list

plt.plot(S,label="susceptible",color="red")
plt.plot(I,label="infected",color="blue")
plt.plot(R,label="recovered",color="green") #draw three plots for three conditions and set different colours
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend(loc='upper right') #Set x,y label, title and legend for the chart.
plt.show()