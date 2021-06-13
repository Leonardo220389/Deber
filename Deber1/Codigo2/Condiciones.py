
class Condicion:
    def __init__(self,num1=5,num2=4):
        self.numero1=num1
        self.numero2=num2
        numero= self.numero1 + self.numero2
        self.numero3=numero
        
    def usoIF(self):
        if self.numero1 == self.numero2:
           print("numero1={} = numero2={}: son iguales".format(self.numero1, self.numero2)) 
        elif self.numero1 == self.numero3:
            print("Numero1 y Numero3 son iguales")
        else:
            print("Numeros diferentes")       

# print("instancia de la clase")
# cond1=Condicion(10,20)
# cond2=Condicion()
# print(cond2.numero3)
cond1=Condicion(10,10)
cond1.usoIF()
print("Gracias por su visita")  