#Set a dictionary to record data and print it.
#Set a variable that can be changed to output the value.
#Import matplotlib to draw chart. Set languages and their corresponding values.
#Make colours different in different bars and define ylabel and the title. Show the exact value on top of each bar.
dict1={"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}
print(dict1)
chosent=input("Enter the language you want to see the percentage of users: ") #Ask user to input the language they want to see the percentage of users.``
print(chosent,"percentage of users: ",dict1[chosent])
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
languages = ['JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript']
counts = [62.3, 52.9, 51, 51, 38.5] #Set languages and their corresponding values.
bar_colors = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange', 'tab:green'] #Set different colours in different bars.
bars=ax.bar(languages, counts, color=bar_colors)
ax.set_ylabel('percentage')
ax.set_title('percentage of users')
ax.bar_label(bars, labels=counts)#Show the exact value on top of bar
plt.show()
