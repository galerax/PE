import matplotlib.pyplot as plt
import scipy.stats as stats

#Questão 3

normal1 = stats.norm.rvs(loc = 0, size=10000)
normal2 = stats.norm.rvs(loc = 4, size=10000)


plt.title("Mixed distribution histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.hist(normal1,bins=100, label = "loc = 0", color="gray")
plt.hist(normal2,bins=100, label = "loc = 4", color="black")

plt.legend()
plt.show()