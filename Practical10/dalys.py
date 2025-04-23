import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np #import several libraries
os.chdir(r"C:/Users/71588/Desktop/IBI1_2024-25/Practical10") #change the directory to the current working directory
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") #read the csv file into a pandas dataframe
#print(dalys_data.head(5))
#print(dalys_data.info())
#print(dalys_data.describe())
#print(dalys_data.iloc[0, 3])
print(dalys_data.iloc[0:10, 2]) #print the first 10 rows and the third column. 
#The 10th year with DALYs data recorded in Afghanistan is 1999.
my_columns = [True, True, False, True] #select specific columns
print(dalys_data.iloc[0:3, my_columns]) #print the first 3 rows and the selected columns
#print(dalys_data.loc[2:4, "Year"])
dalys_1990 = dalys_data.loc[dalys_data.Year==1990, "DALYs"] #select rows where the year is 1990 and the DALYs column
print(dalys_1990)

uk = dalys_data.loc[dalys_data.Entity== "United Kingdom", ["DALYs", "Year"]] #select rows where the entity is UK and the DALYs and Year columns
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]] #select rows where the entity is France and the DALYs and Year columns
uk_mean = np.mean(uk.DALYs) #calculate the mean DALYs for UK
france_mean = np.mean(france.DALYs) #calculate the mean DALYs for France
print("UK mean DALYs:", uk_mean)
print("France mean DALYs:", france_mean)
if uk_mean > france_mean: #compare the means and print the result
    print("UK has a higher DALYs rate than France")
else:
    print("France has a higher DALYs rate than UK")
plt.plot(uk.Year, uk.DALYs, 'bo') #plot the DALYs for UK from 1990 to 2019
plt.xlabel("Year") 
plt.ylabel("DALYs") #add labels to the x and y axis
plt.title("DALYs in UK from 1990 to 2019") #add a title to the plot
plt.xticks(uk.Year,rotation=-60) #rotate the x-axis labels by -60 degrees
plt.show() #show the plot

high_dalys = dalys_data.loc[dalys_data.DALYs > 650000, ["Entity", "DALYs", "Year"]] #select rows where the DALYs are greater than 650000 and the Entity, DALYs, and Year columns
countries= high_dalys.Entity.unique() #find the unique countries with DALYs > 650000
print("Countries with DALYs > 650000:", countries) 

dalys_1990 = dalys_data.loc[dalys_data.Year==1990, "DALYs"]
plt.boxplot(dalys_1990, label="DALYs") #create a boxplot of the DALYs for 1990
plt.xlabel("1990") 
plt.ylabel("DALYs") #add labels to the x and y axis
plt.title("Boxplot of DALYs in Afghanistan in 1990") #add a title to the plot
plt.show() #show the plot   