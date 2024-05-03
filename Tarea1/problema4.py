"""
Filtrado de texto en Pandas. Y uso de archivos Parquet

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Cargar los datos desde el archivo .parquet
data = pd.read_parquet("./yellow_tripdata_2022-11.parquet")

# a. Verificar cuántos registros tiene el archivo
total_records = len(data)
print("Total de registros en el archivo:", total_records)

# b. Verificar cómo es la cabecera y el final del archivo
print("Cabecera del archivo:")
print(data.head())
print("\nFinal del archivo:")
print(data.tail())

# identificar cuántos proveedores únicos existen (VendorID)
unique_vendors = data["VendorID"].nunique()
print("\nCantidad de proveedores únicos:", unique_vendors)

# Comprobación de la suma de registros por proveedor
sum_records_vendors = data.groupby("VendorID").size()
print("Suma de registros por proveedor:")
print(sum_records_vendors)

# cantidad de viajes con un solo pasajero y más de un pasajero para VendorID = 1
data_vendor_1 = data[data["VendorID"] == 1]

# cantidad de viajes con UN SOLO pasajero
cont_un_pasajero = data_vendor_1[data_vendor_1["passenger_count"] == 1].shape[0]
print("\nCantidad de viajes con un solo pasajero para VendorID = 1:", cont_un_pasajero)

# cantidad de viajes con más de un pasajero
cont_multiples_pasajeros = data_vendor_1[data_vendor_1["passenger_count"] > 1].shape[0]
print("Cantidad de viajes con más de un pasajero para VendorID = 1:", cont_multiples_pasajeros)

# promedio total de pasajeros para VendorID = 1
promedio_pasajeros = data_vendor_1["passenger_count"].mean()
print("Promedio total de pasajeros para VendorID = 1:", promedio_pasajeros)

# identificar los viajes que costaron más de $16.50 para todos los VendorID
trips_precios_altos = data[data["fare_amount"] > 16.50]

# a. Extraer viajes del mismo vendedor
high_fare_vendor_1 = trips_precios_altos[trips_precios_altos["VendorID"] == 1]

# b. Graficar el costo en función de la distancia
plt.figure(figsize=(10, 6))
plt.scatter(high_fare_vendor_1["trip_distance"], high_fare_vendor_1["fare_amount"])
plt.title("Costo vs Distancia para VendorID = 1")
plt.xlabel("Distancia del viaje (millas)")
plt.ylabel("Tarifa del viaje ($)")
plt.show()

coeficiente_correlacion = high_fare_vendor_1["fare_amount"].corr(high_fare_vendor_1["trip_distance"])

print("Coeficiente de correlación de Pearson entre fare_amount y trip_distance:",
coeficiente_correlacion)

# RESPONDIENDO LAS PREGUNTAS
print("\nRespuestas a las preguntas:")
print("1. ¿Cómo es el comportamiento de los costos?")
print("""
El coeficiente de correlación de Pearson de 0.7295 indica una correlación positiva entre el costo del viaje y la distancia recorrida. Esto significa que, en general, a medida que aumenta la distancia del viaje, el costo del mismo tiende a aumentar. Por lo tanto, el comportamiento de los costos es positivo, lo que implica que los viajes más largos suelen tener tarifas más altas.
""")
print("2. ¿Están relacionados los costos con la distancia recorrida?")
print("""
Sí, hay una correlación significativa entre los costos del viaje y la distancia recorrida. Esto se confirma con el coeficiente de correlación de Pearson de 0.7295, que es cercano a 1. Esto indica que los costos y la distancia están positivamente relacionados; es decir, a medida que aumenta la distancia del viaje, generalmente aumenta el costo del mismo.
""")
print("""
3¿En qué grado?: \nEl coeficiente de correlación de Pearson de 0.7295 sugiere una correlación lineal positiva moderadamente fuerte entre el costo del viaje y la distancia recorrida. Esto significa que hay una asociación considerable entre estas dos variables, donde un cambio en una variable está asociado con un cambio proporcional en la otra variable, pero no necesariamente de manera lineal perfecta.
""")

# 3. Tercer filtro: Enfoque en la columna congestion_surcharge y análisis de horas pico
# Filtrar los viajes que tienen sobrecargos
congestion_surcharge_trips = data[data["congestion_surcharge"] > 0]

# horas pico: 6-8am, 12-1pm y 5-7pm
peak_hours = [6, 7, 8, 12, 13, 17, 18, 19]

# Función para clasificar las horas en picos y no picos
def classify_hour(hour):
    if hour in peak_hours:
        return "Hora pico"
    else:
        return "Hora no pico"

# Aplicar la función para clasificar las horas en el dataframe
congestion_surcharge_trips["hour_category"] = congestion_surcharge_trips["tpep_pickup_datetime"].dt.hour.apply(classify_hour)

# Contar el número de viajes con sobrecargo en cada categoría de hora
trips_by_hour_category = congestion_surcharge_trips.groupby("hour_category").size()

print("Número de viajes con sobrecargo en horas pico y no pico:")
print(trips_by_hour_category)

# Convertir la categoría de horas pico en valores numéricos
hour_category_numeric = congestion_surcharge_trips["hour_category"].apply(lambda x: 1 if x == "Hora pico" else 0)

# Calcular la correlación de Pearson entre congestión y horas pico
correlation = congestion_surcharge_trips["congestion_surcharge"].corr(hour_category_numeric)

# Graficar la relación entre congestión y horas pico
plt.figure(figsize=(8, 6))
plt.scatter(congestion_surcharge_trips["congestion_surcharge"], hour_category_numeric)
plt.title("Correlación de Pearson entre Congestion Surcharge y Horas Pico")
plt.xlabel("Congestion Surcharge ($)")
plt.ylabel("Hora del día (Pico = 1 / No pico = 0)")
plt.text(2, 0.5, f'Correlación de Pearson: {correlation:.2f}', fontsize=12, color='red')
plt.grid(True)
plt.show()


# Respuesta a la pregunta:
print(f"La correlacion de Pearson entre la sobrecarga de congestión y las horas pico es de {correlation:.2f}")
print("¿Está ligado el sobrecosto a que el viaje se haga en hora pico?")
print("""
Esta tiene una correlación débil o nula, lo que significa que no hay una relación lineal clara entre los sobrecargos de congestión y las horas pico.
""")

