uk_countries=[57.11,3.13,1.91,5.45]
cn_provinces=[65.77, 41.88, 45.28, 61.27, 85.15]
sort_uk_couintries=sorted(uk_countries)
sort_cn_provinces=sorted(cn_provinces)
print(f"countries in UK:{sort_uk_couintries}")
print(f"Zhejiang neighbouring provinces:{sort_cn_provinces}")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe1 = ["57.11 billion England",
          "3.13 billion Wales",
          "1.91 billion Northern_Ireland",
          "5.45 billion Scotland"]

data = [float(x.split()[0]) for x in recipe1]
ingredients = [x.split()[-1] for x in recipe1]
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} billion)"
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))
ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Countries in UK")
plt.show()

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe2 = ["65.77 billion Zhejiang",
          "41.88 billion Fujian",
          "45.28 billion Jiangxi",
          "61.27 billion Anhui",
          "85.15 billion Jiangsu"]

data = [float(x.split()[0]) for x in recipe2]
ingredients = [x.split()[-1] for x in recipe2]

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))
ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Population distribution in Zhejiang neibouring provinces")
plt.show()


