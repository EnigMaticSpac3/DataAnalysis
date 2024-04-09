def nparesab(num_inf, num_sup):
    """
    Función que imprime los números pares entre dos números dados
    :param num_inf: Número entero inferior
    :param num_sup: Número entero superior
    :return: None
    """
    for i in range(num_inf, num_sup+1):
        if i % 2 == 0:
            print(i, end=" ")

# recibir dos argumentos desde la línea de comandos
# validar que los numeros ingresados sean enteros
num_inf = input("Ingrese el primer número: ")
while not num_inf.isdigit():
    print("El número ingresado no es un número entero")
    num_inf = input("Ingrese el primer número: ")
num_inf = int(num_inf)

num_sup = input("Ingrese el segundo número: ")
while not num_sup.isdigit() or int(num_sup) <= int(num_inf):
    if int(num_sup) <= int(num_inf):
        print("El segundo número debe ser mayor al primer número")
    else:
        print("El número ingresado no es un número entero")
    num_sup = input("Ingrese el segundo número: ")
num_sup = int(num_sup)

print("Los números pares entre", num_inf, "y", num_sup, "son: ")
nparesab(num_inf, num_sup)
