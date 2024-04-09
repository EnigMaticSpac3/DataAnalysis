import sys
print("Argumentos leidos: ", sys.argv)

if len(sys.argv) > 1:
  print("1er Argumento: ", sys.argv[1])
  print("2do Argumento: ", sys.argv[2])

try:
    print("La multiplicacion de ambos es: {:.2f}".format(float(sys.argv[1]) * float(sys.argv[2])))
except ValueError:
    print("No se puede multiplicar los argumentos")

sys.exit(1)

