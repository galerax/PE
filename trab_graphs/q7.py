import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Questão 7
data_set = pd.read_csv("data/brain_bodyweight.txt", sep="	")

brain_w = data_set["Brainweight"]
body_w = data_set["Bodyweight "]
brain_e = data_set["Brainweight.SEM"]
body_e = data_set["Bodyweight.SEM"]
animal_names = data_set["Species "]


plt.title("Animal's Body weight X Brain weight")
plt.xlabel("Brain weight")
plt.ylabel("Body weight")


plt.scatter(brain_w, body_w)
plt.errorbar(brain_w, body_w, xerr= brain_e, yerr=body_e, fmt="o", color="black" )

for i in range(len(brain_w)):
	plt.text(brain_w[i] , body_w[i] -0.3 , s =  animal_names[i])


plt.show()