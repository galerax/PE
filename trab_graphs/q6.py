import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Questão 6
data_set = pd.read_csv("data/chromosome_position_data.txt", sep="	")


mut1 = data_set[["Position", "Mut1"]]
mut2 = data_set[["Position", "Mut2"]]
wt = data_set[["Position", "WT"]]

line1, = plt.plot(mut1["Position"], mut1["Mut1"], color="red")
line2, = plt.plot(mut2["Position"], mut2["Mut2"], color="blue")
line3, = plt.plot(wt["Position"], wt["WT"], color="green")

plt.title("Graph Distribution")
plt.xlabel("Position within chromosome")
plt.ylabel("Value")
plt.legend([line1, line2, line3], ["Mut1", "Mut2", "WT"])

plt.show()