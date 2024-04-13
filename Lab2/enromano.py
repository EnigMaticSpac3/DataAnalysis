# Este programa convierte un número entero a su representación en números romanos.

def enromano():
    numero = int(input("Ingrese un número entre 1 y 1000: "))
    if numero < 1 or numero > 1000:
        print("Número fuera de rango")
    else:
        # diccionario con los valores de los números romanos
        romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                   500: 'D', 900: 'CM', 1000: 'M'}
        resultado = '' # variable para almacenar el resultado

        # se recorre el diccionario de mayor a menor
        for valor, letra in sorted(romanos.items(), reverse=True):
            while numero >= valor:
                resultado += letra
                numero -= valor
        print(resultado)

enromano()