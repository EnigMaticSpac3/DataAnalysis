# tomaremos dos cadenas de texto y verificaremos si son anagramas
cadena1 = input("Ingrese la primera cadena de texto: ")
# validar que la cadena ingresada no sea vacía
while not cadena1:
    print("La cadena no puede ser vacía")
    cadena1 = input("Ingrese la primera cadena de texto: ")

cadena2 = input("Ingrese la segunda cadena de texto: ")
while not cadena2:
    print("La cadena no puede ser vacía")
    cadena2 = input("Ingrese la segunda cadena de texto: ")

# verificar si las cadenas son anagramas
if sorted(cadena1) == sorted(cadena2):
    print("Las cadenas ingresadas son anagramas. TRUE")
else:
    print("Las cadenas ingresadas no son anagramas. FALSE")