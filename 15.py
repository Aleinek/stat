import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.normal(700, 100, 100)

def statystyki(dane):
    q1, q3 = np.percentile(dane, [25, 75])
    print("Średnia:", np.mean(dane))
    print("Odchylenie:", np.std(dane, ddof=1))
    print("Mediana:", np.median(dane))
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", q3 - q1)
    print("-" * 20)

statystyki(x)

plt.hist(x, bins=10)
plt.show()

plt.hist(x, bins=30)
plt.show()

plt.plot(np.sort(x), np.arange(1, len(x) + 1) / len(x), drawstyle='steps-post')
plt.show()

plt.boxplot(x)
plt.show()

x_out = np.append(x, [1500] * 5)
statystyki(x_out)