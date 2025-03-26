import numpy as np
import matplotlib . pyplot as plt #import certain libraries
population = np.zeros((100, 100)) #make array of all susceptible population
outbreak = np.random. choice(range(100) ,2)
population[outbreak[0], outbreak[1]] = 1 #choose one random point in our 100 100 array for where the outbreak happens
plt.figure (figsize =(6,4),dpi=150) 
beta=0.3
gama=0.05 #set variables for given information
snapshot_times = [0, 10, 50, 99] #make a list to record the four time for drawing picture
for t in range(100): #make a 100 times loop
    infected_area=np.where(population==1) # return a tuple for the coordinates of infected areas
    infected_points = list(zip(infected_area[0], infected_area[1])) #change the tuple to the list that record every eligible coordinates.
    for (i, j) in infected_points: # Check all 8 neighbors
            for x in [i-1, i, i+1]:
                for y in [j-1, j, j+1]: 
                    if (x == i and y == j) or x < 0 or y < 0 or x >= 100 or y >= 100:
                        continue # jump the loop to make sure the eight neighbours are in the field
                    
                    if population[x, y] == 0 and np.random.random() < beta:
                        population[x, y] = 1 #Infect susceptible neighbors according to probability beta
    for (i, j) in infected_points:
            if np.random.random() < gama:
                population[i, j] = 2 #make the infected person recovered according to gama
    if t in snapshot_times:
        plt.subplot(2, 2, snapshot_times.index(t) + 1) #make four subplots and present them according to their sequential order.
        plt.imshow(population , cmap='viridis', interpolation='nearest') #Show the plots and set colours
        plt.title(f'Time = {t}', fontsize=12) #Set titles for each plot.
plt.show()
    