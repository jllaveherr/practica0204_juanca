edad = int(input("¿Cuantos años tienes? "))
ingreso = float(input("¿Cuales son tus ingresos mensaules? "))
if edad > 16 and ingreso >= 1000:
    print("tienes que tributar ")
else:
    print("no tienes que tributar ")
