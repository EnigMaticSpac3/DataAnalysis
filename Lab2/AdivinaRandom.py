import random

# Fijar la semilla para obtener el mismo número aleatorio en cada ejecución
random.seed(43)

# Generar un número aleatorio entre 1 y 99
numero_secreto = random.randint(1, 99)

# Solicitar al usuario la cantidad de intentos que desea realizar
intentos = int(input("¿Cuántas veces desea jugar hoy? "))
print()

# Iterar sobre la cantidad de intentos especificados por el usuario
for i in range(intentos):
    suposicion = int(input("¿Cuál cree que es el número? "))

    # Comprobar si es correcto
    if suposicion == numero_secreto:
        print(f"Increíble, su suposición fue correcta! {numero_secreto} fue el número correcto!")
        break
    else:
        # Calcular los intentos restantes
        intentos_restantes = intentos - i - 1
        
        # Verificar si el usuario ha agotado todos los intentos
        if intentos_restantes == 0:
            print(f"Usted agotó sus {intentos} intentos. El número real era {numero_secreto}.")
        else:
            print(f"Su suposición es falsa. Por favor, inténtelo de nuevo; Tiene {intentos_restantes} turnos restantes para averiguar.")

