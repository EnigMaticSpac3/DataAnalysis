import sys
print("Argumentos leidos: ", sys.argv)

if len(sys.argv) > 1:
  print("1er Argumento: ", sys.argv[1])
  print("2do Argumento: ", sys.argv[2])

print("La frase es: ", sys.argv[1] + sys.argv[2])


