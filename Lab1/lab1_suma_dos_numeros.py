import sys
print("Argumentos leidos: ", sys.argv)

if len(sys.argv) > 1:
  print("1er Argumento: ", sys.argv[1])
  print("2do Argumento: ", sys.argv[2])

try:
  print("La suma de ambos es: ", int(sys.argv[1]) + int(sys.argv[2]))
except ValueError:
  print("No se puede sumar los argumentos")

