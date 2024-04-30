import numpy as np
from matplotlib import pyplot as plt


mu = 0
sigma = 0.1
x = np.random.normal(mu, sigma, 1000)
# # print(x)

# xmin, xmax = plt.xlim()
# bins = np.linspace(xmin, xmax, 50)
# histo, bins = np.histogram(x, bins=50, density=True)
# # plt.figure(figsize=(10, 5))

# plt.plot(x, histo, label="Histograma numpy")
# plt.show()
plt.figure(figsize=(10, 5))
# plt.title('Grafico de x')
# plt.plot(x, 'bo')     
# plt.show()
plt.plot(x, 'bo')
plt.show()
plt.hist(x, bins=50, color='c', edgecolor='black')
plt.title('Histograma de x')
plt.show()