import numpy as np
import matplotlib.pyplot as plt

# Leer los datos del archivo
filename = "DatasaurusDozen.tsv"  # Cambiar el nombre del archivo si es necesario
data = np.genfromtxt(filename, delimiter="\t", names=True, dtype=None)

# Filtrar los datos de 'dino'
dino_data = data[data['dataset'] == b'dino']

# Crear la primera figura con los datos de 'dino'
plt.figure(1, figsize=(8, 6))
plt.scatter(dino_data['x'], dino_data['y'], label='dino')
plt.title('Conjunto de Datos "dino"')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Crear la segunda figura con los otros 12 conjuntos de datos
plt.figure(2, figsize=(12, 9))
for i, dataset in enumerate(np.unique(data['dataset'])):
    if dataset != b'dino':
        plt.subplot(3, 4, i+1)
        current_data = data[data['dataset'] == dataset]
        plt.scatter(current_data['x'], current_data['y'], label=dataset.decode('utf-8'))
        plt.title('Conjunto de Datos "{}"'.format(dataset.decode('utf-8')))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        if i+1 == 12:  # Salir del bucle cuando se alcanza el último conjunto de datos
            break

# Calcular y mostrar las estadísticas para cada conjunto de datos
for dataset in np.unique(data['dataset']):
    current_data = data[data['dataset'] == dataset]
    x_mean = np.mean(current_data['x'])
    y_mean = np.mean(current_data['y'])
    x_var = np.var(current_data['x'], ddof=1)
    y_var = np.var(current_data['y'], ddof=1)
    correlation = np.corrcoef(current_data['x'], current_data['y'])[0, 1]
    print("Conjunto de Datos:", dataset.decode('utf-8'))
    print("Promedio de X:", x_mean)
    print("Promedio de Y:", y_mean)
    print("Varianza de X:", x_var)
    print("Varianza de Y:", y_var)
    print("Correlación de Pearson:", "{:.3f}".format(correlation))
    print()

# Mostrar las figuras
plt.tight_layout()
plt.show()
