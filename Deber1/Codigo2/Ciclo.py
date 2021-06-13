class Ciclo:
    def __init__(self, numero=5):
        self.numero=numero
        self.numero2=0
    def usowhile(self):
        #ciclo repetitivo que se ejecuta mientras la condicion se cumple(verdader)
        #es decir sale por falso
        car=input("Ingrese vocal:")
        car= car.lower()#transforma a minusculas
        while car not in ("a", "e", "i", "o", "u"):#mientras car ingreso no es vocal:
            car=input("Ingrese vocal:").lower() #transforma a minuscula
        print("Felicitacion su vocal es:{}".format(car))
        
        
    
Ciclo1 = Ciclo()
Ciclo1.usowhile()
print("Fin de uso ciclo")
