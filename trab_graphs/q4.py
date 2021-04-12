import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Questão 4
data_set = pd.read_csv("data/male_female_counts.txt", sep="	")

fig, ax = plt.subplots()

ax.set_title("Bar Graph")
ax.set_xlabel("Sample")
ax.set_ylabel("Count")

eixo_y = range((len(data_set)))

ax.set_xticks(eixo_y)
ax.set_xticklabels(data_set["Sample"])

ax.bar(range(len(data_set)), data_set["Count"], color="gray")
plt.show()