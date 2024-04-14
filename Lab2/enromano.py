# Este programa convierte un número entero a su representación en números romanos.

def enromano():
    numero = int(input("Ingrese un número entre 1 y 1000: "))
    if numero < 1 or numero > 1000:
        print("Número fuera de rango")
    else:
        romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                   500: 'D', 900: 'CM', 1000: 'M'}
        resultado = ''
        for valor, letra in sorted(romanos.items(), reverse=True):
            while numero >= valor:
                resultado += letra
                numero -= valor
        print(resultado)

enromano()

'''def numero_entero_a_romano(num):
    numbers=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_rom=['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    conversion = ''
    k = 0

    while num > 0:
        for _ in range(num // numbers[k]):
            conversion += num_rom[k]
            num -= numbers[k]

        k += 1

    return conversion


#Proceso de ingreso del numero
while True:
    try:
        numero = (int(input("Ingrese un numero para su conversion a numero romano [1-1000]: ")))
        
        if numero <= 0 or numero > 1000:
            print("Vuelve a ingresar un valor dentro del rango de 1 a 1000.")
        else:
            break

    except ValueError:
        print("Vuelve a ingresar un valor dentro del rango de 1 a 1000.")


resultado = numero_entero_a_romano(numero)
print("El numero ingresado es", numero, "Y su conversion a romando es: ", resultado)'''
