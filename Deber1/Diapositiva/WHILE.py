#Uso de while infinito - es un ciclo que se ejecuta mientras la condicion sea verdadera
# c=1
# while True:
#     print(c)
    
# while validacion
vocal = input("Ingrese vocal: ")
while vocal not in ("a", "e", "i", "o", "u"):
    if vocal == ".":
        break
    vocal = input ("Ingresar nuevamente Vocal:")
print ("Su vocal o punto es: {}".format (vocal))