dict1={"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}
print(dict1)
percentage=dict1["HTML"]
print(percentage)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

languages = ['JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript']
counts = [62.3, 52.9, 51, 51, 38.5]
bar_colors = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange', 'tab:green']
bars=ax.bar(languages, counts, color=bar_colors)
ax.set_ylabel('percentage')
ax.set_title('percentage of users')
ax.bar_label(bars, labels=counts)
plt.show()