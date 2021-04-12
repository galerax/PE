import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Questão 1
data_set = pd.read_csv("data/weight_chart.txt", sep="	")



plt.plot(data_set["Age"], data_set["Weight"], color="gray")

plt.title("Age X Weight")
plt.xlabel("Age (months)")
plt.ylabel("Weight (Kg)")

plt.show()