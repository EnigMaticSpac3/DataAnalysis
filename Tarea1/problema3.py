"""
Se ven algunas	de	las	propiedades	de	las	funciones	vistas	en	clase	para	
estandarización	de	datos a	través	de	su	implementación	en	código	en	Python
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# cargar el archivo 
ARCHIVO = "./airfoil_self_noise.dat"
data = np.genfromtxt(ARCHIVO)


numeric_data = data[:, :-1]  # Excluir la última columna que no es numérica

# se aplica normalización estándar a 3 columnas
scaler = StandardScaler()
numeric_data[:, [0, 2, 4]] = scaler.fit_transform(numeric_data[:, [0, 2, 4]])

# visualizar la distribución de los datos antes y después de la normalización
plt.figure(figsize=(10, 6))

for i, column in enumerate([0, 2, 4]):
    plt.subplot(3, 2, i*2+1)
    plt.hist(data[:, column], bins=20, color='blue', alpha=0.5, label='Original')
    plt.title(f"Columna {column + 1} (Antes de la Normalización)")
    plt.subplot(3, 2, i*2+2)
    plt.hist(numeric_data[:, column], bins=20, color='red', alpha=0.5, label='Normalizado')
    plt.title(f"Columna {column + 1} (Después de la Normalización)")

plt.tight_layout()
plt.show()
