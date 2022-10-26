entero = int(input("Introduce un número entero "))
for numero in range(1, entero+1):
    for fila in range(numero):
        print("*", end=" ")
    print("")
