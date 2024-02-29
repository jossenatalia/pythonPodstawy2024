import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Wartości")
plt.ylabel("Częstotliwość")

plt.savefig("histogram.png")
plt.savefig("histogram.pdf")
plt.show()
