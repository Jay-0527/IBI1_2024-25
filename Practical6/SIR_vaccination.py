import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm #import certain libraries
N=10000
vaccine_percentage=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #make a list for vaccine percentage.
for k in vaccine_percentage: #use for loop to traverse every value in the list
    vaccine=int(N*k)
    infected=1
    if N-infected-vaccine>0:
        susceptible=N-infected-vaccine
    else:
        susceptible=0 # Make sure that the value is positive for every k
    
    recovered=0
    beta=0.3
    gama=0.05 # set variables for given information
    S=[susceptible]
    I=[infected]
    R=[recovered] # Create lists to record the number of people who are susceptible, infected or recovered.
    
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
    color_value = int(255*k) #Set gradients colour when k increases
    plt.plot(I, label=f'{int(k*100)}% vaccinated', color=cm.viridis(color_value)) #draw the plot and add the label corresponding to the k value at present
        
    
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rate')
plt.legend() #Set x,y label, title and legend for the chart.
plt.show()
