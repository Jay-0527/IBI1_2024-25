import os  
import pandas as pd  
import matplotlib.pyplot as plt 
import numpy as np 

os.chdir(r"C:/Users/71588/Desktop/IBI1_2024-25/Resit/Practical10") #change the directory to the current working directory

# Task 1: Read the csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") #read the csv file into a pandas dataframe

# Task 2: Show columns 3-4 for first 10 rows
print(dalys_data.iloc[0:10, [2, 3]]) # Columns are 0-indexed
# The DALYs recorded in Afghanistan in 1992 is 79890.55.

# Task 3: Boolean indexing for 1990
my_columns=[True,False,False,True]
print(dalys_data.loc[dalys_data.Year==1990, my_columns]) # Select rows where Year is 1990 and columns 1 and 4

# Task 4: China analysis
china_data = dalys_data.loc[dalys_data['Entity'] == 'China', ['Year', 'DALYs']] # Select China data
min_daly = china_data['DALYs'].min()
max_daly = china_data['DALYs'].max()
min_year = china_data.loc[china_data['DALYs'] == min_daly, 'Year'].values[0]
max_year = china_data.loc[china_data['DALYs'] == max_daly, 'Year'].values[0]
print(f"China minimum DALYs: {min_daly} in {min_year}")
print(f"China maximum DALYs: {max_daly} in {max_year}")
# Minimum DALYs in China is 22270.51 in 2019 and maximum DALYs in China is 41104.86 in 1990.

# Task 5: Plot China data
plt.figure(figsize=(10, 6))
plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-60)
plt.title('DALYs Over Time in China')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.show()

# Task 6: Answer custom question (question: UK vs France)
# script for question starts from the next line(line 40)
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
france_data = dalys_data[dalys_data['Entity'] == 'France']

plt.figure(figsize=(10, 6))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'r-', label='United Kingdom')
plt.plot(france_data['Year'], france_data['DALYs'], 'b-', label='France')
plt.title('DALYs Comparison: UK vs France')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.legend()
plt.show()

