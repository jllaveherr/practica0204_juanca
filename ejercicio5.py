sexo = input("Introduce tu sexo ")
nombre = input("Introduce tu nombre ")
if sexo == "M":
    if nombre[0].upper() < "M":
        print("Tu casa es Gryffindor ")
    else:
        print("Tu casa es Slytherin ")
else:
    if nombre[0].upper() > "N":
        print("Tu casa es Gryffindor ")
    else:
        print("Tu casa es Slytherin ")
