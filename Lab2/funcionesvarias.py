# recibir lista como argumento e imprimir reverso
def cadenareversa(lista):
    """
    Función que imprime los elementos de una lista en orden inverso
    :param lista: Lista de elementos
    :return: None
    """
    listaB = lista.copy()
    listaB.reverse()
    return listaB

def combinalista(lista1, lista2):
    """
    Función que combina dos listas en una sola y la retorna ordenada
    :param lista1: Lista 1
    :param lista2: Lista 2
    :return: Lista combinada ordenada
    """
    return sorted(lista1 + lista2)
# recibir lista
lista1 = input("Ingrese una lista de elementos separados por coma: ")
lista1 = lista1.split(",")
print("La lista en orden normal es: ", lista1)
print("La lista en inverso es: ",cadenareversa(lista1))


# pedir dos listas 
print("\n\n_____________________________________\nAhora se combinarán dos listas y se ordenarán")
lista2 = input("Ingrese una lista de numeros separados por coma LISTA 1: ")
lista2 = lista2.split(",")
# validar que todos los elementos sean numeros
while not all([x.isdigit() for x in lista2]):
    print("Todos los elementos deben ser números enteros")
    lista2 = input("Ingrese una lista de numeros separados por coma LISTA 1: ")
    lista2 = lista2.split(",")

lista3 = input("Ingrese una lista de numeros separados por coma LISTA 2: ")
lista3 = lista3.split(",")
# validar que todos los elementos sean numeros
while not all([x.isdigit() for x in lista3]):
    print("Todos los elementos deben ser números enteros")
    lista3 = input("Ingrese una lista de numeros separados por coma LISTA 2: ")
    lista3 = lista3.split(",")

print("La lista combinada y ordenada es: ", combinalista(lista2, lista3))

