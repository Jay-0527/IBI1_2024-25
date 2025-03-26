import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
N=10000
vaccine_percentage=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for k in vaccine_percentage:
    vaccine=int(N*k)
    infected=1
    if N-infected-vaccine>0:
        susceptible=N-infected-vaccine
    else:
        susceptible=0
    
    recovered=0
    beta=0.3
    gama=0.05
    S=[susceptible]
    I=[infected]
    R=[recovered]
    
    for i in range (1000):
        infected_probability=beta*I[-1]/N
        updated_infected=np.random.choice(range(2),S[-1],p=[1-infected_probability,infected_probability]).sum()
        updated_recovery=np.random.choice(range(2),I[-1],p=[1-gama,gama]).sum()
        
        actual_susceptible=S[-1]-updated_infected
        actual_infected=I[-1]+updated_infected-updated_recovery
        actual_recovered=R[-1]+updated_recovery
        S.append(actual_susceptible)
        I.append(actual_infected)
        R.append(actual_recovered)
    color_value = int(255*k)
    plt.plot(I, label=f'{int(k*100)}% vaccinated', color=cm.viridis(color_value))
        
    
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rate')
plt.legend()
plt.show()