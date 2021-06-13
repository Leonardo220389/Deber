x = int(input("Ingresa un numero entero: "))
if x < 0:
    x = 0
    print("Negativo cambio a cero")
elif x == 0:
    print("cero")
elif x == 1:
    print("Uno")
else:
    print("Ninguna opcion")

print("ok") if type(x) == int else print("-")