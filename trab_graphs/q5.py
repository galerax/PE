import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Questão 5
data_set = pd.read_csv("data/up_down_expression.txt", sep="	")

data_unchange = data_set[data_set["State"] == 'unchanging']
data_up = data_set[data_set["State"] == 'up']
data_down = data_set[data_set["State"] == 'down']

plt.title("Dispersion Graph")
plt.xlabel("Condition 1")
plt.ylabel("Condition 2")


pop1 = plt.scatter(data_unchange["Condition1"], data_unchange["Condition2"], color="gray")
pop2 = plt.scatter(data_up["Condition1"], data_up["Condition2"], color="red")
pop3 = plt.scatter(data_down["Condition1"], data_down["Condition2"], color = "blue")
plt.legend([pop1, pop2, pop3], ["State = unchanging", "State = up", "State = down"])
plt.show()
