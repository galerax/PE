import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Questão 2
data_set = pd.read_csv("data/feature_counts.txt", sep="	")

fig, ax = plt.subplots()
ax.set_title("Features in Genoma (GRCm38)")
ax.set_xlabel("Count")
ax.set_ylabel("Features")

eixo_y = range((len(data_set)))

ax.set_yticks(eixo_y)
ax.set_yticklabels(data_set["Feature"])

ax.barh(eixo_y, data_set["Count"], color="gray")

plt.show()