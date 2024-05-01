# """
# Creación de graficos y uso de scipy.
# """

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from scipy.stats import skew, norm

MU = 0
SIGMA = 0.1
random1 = np.random.uniform(MU, SIGMA, 1000)
random2 = np.random.random(1000)
samples = np.random.normal(size=1000)

bins_normal = np.linspace(MU,SIGMA,30)
# print(bins_normal)
# mostrar los valores aleatorios generados con random Uniform
plt.figure(figsize=(10, 5))
plt.plot(random1, '.')
plt.title('Gráfico de valores aleatorios con Random.Uniform: 0 - 0.1')
plt.show()

# mostrar los valores aleatorios generados con random.random
plt.figure(figsize=(10, 5))
plt.plot(random2)
plt.title('Gráfico de valores aleatorios con Random.Random')
plt.show()

# mostrar el histograma y verificar la distribución de los datos
# Random.Uniform
plt.figure(figsize=(10, 5))
plt.title('Histograma de random.uniform')
cuenta, bins, ignorados = plt.hist(random1, bins=100, color='c', edgecolor='black', density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()

# Random.Random
plt.figure(figsize=(10, 5))
plt.title('Histograma de random.random')
cuenta, bins, ignorados = plt.hist(random2, bins=100, color='c', edgecolor='black', density=True)
plt.plot(bins, 1/(SIGMA * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - MU)**2 / (2 * SIGMA**2) ),
         linewidth=2, color='r')
plt.show()

# sobreponer un histograma de distribución normal
# Random.Uniform
plt.figure(figsize=(10, 5))
plt.title('Histograma de random.uniform con distribución normal')
cuenta, bins, ignorados = plt.hist(
    random1, bins=100, color='c', edgecolor='black', density=True, label='Histograma'
    )
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r', label='Distribución uniforme')
histogram, bins_normal = np.histogram(samples, bins=bins_normal, density=True)
bin_centers = 0.5*(bins_normal[1:] + bins_normal[:-1])
pdf = stats.norm.pdf(bin_centers)
plt.plot(bin_centers, histogram, label="Distribución normal")
plt.plot(bin_centers, pdf, label="PDF")
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, 0, 0.1)
plt.plot(x, p, 'y', linewidth=2)
plt.legend()
plt.show()

# 5 calcular asimetria o normalidad de los datos con skew
valor_skew_uniform  = skew(random1)
valor_skew_random   = skew(random2)
valor_skew_normal   = skew(samples)

print(f'Skew de los datos [uniforme]: {valor_skew_uniform}')
print(f'Skew de los datos [random]: {valor_skew_random}')
print(f'Skew de los datos [normal]: {valor_skew_normal}')


# 6 trabajar lo mismo con el nba.csv
with open('nba.csv', 'r') as archivo:
    header = archivo.readline().strip().split(',')
    data = np.genfromtxt(archivo, delimiter=',', skip_header=1)

indice_columna_salary   = header.index('Salary')
columna_salary          = data[:, indice_columna_salary] 

plt.figure(figsize=(10, 5))
plt.plot(columna_salary, markersize=5, label='Salarios')
plt.title('Gráfico de Salarios')
plt.xlabel('Índice')
plt.ylabel('Salario')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(columna_salary, bins=30, color='c', edgecolor='black', alpha=0.7, density=True)
plt.title('Histograma de Salarios')
plt.xlabel('Salario')
plt.ylabel('Frecuencia')
plt.grid(True)

mu, sigma = np.mean(columna_salary), np.std(columna_salary)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'r', linewidth=2)
plt.legend(['Distribución Normal', 'Histograma'])
plt.show()

skewness = skew(columna_salary)
print(f'Valores de columna_salary\n{columna_salary}')
print("Asimetría de los salarios:", skewness) # nan debido a datos faltantes

# si se filtran
columna_salary_valida = columna_salary[~np.isnan(columna_salary)]
skewness = skew(columna_salary_valida)
print("Asimetría de los salarios: ", skewness)
print("""
En este conjunto de datos, una asimetría positiva podría indicar que hay algunos jugadores con salarios muy altos,lo que hace que la distribución se sesgue hacia la derecha.
""")
