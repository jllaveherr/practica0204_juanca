entero = int(input("Introduce número entero"))
for fila in range(1, entero+1):
    for numero in range(2*fila-1, 1, -2,):
        print(numero, end=" ")
    print("")
