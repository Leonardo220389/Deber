class Ejercicios:
    def __init__(self,datos):
        self.lista = datos
        
    def parImpar(self, numero):
        if numero % 2 == 0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))
            

    def perfecto(self, numero):
        acu=0
        for i in range(1, numero):
            if numero % i == 0:
                acu = acu+i
        if acu == numero:
            print("{} es Perfecto".format(numero))
        else:
            print("{} no es Perfecto".format(numero))
             
    def perfecto2(self, numero):
        acu=0
        for i in range(1, numero):
            if numero % i == 0:
                acu = acu+i
        return acu
    
    def divisores (self,num):
        divisores=[]
        for cont in range(1,num):
            rec = num % cont
            if  rec == 0:
                divisores.append(cont)
        return divisores
            
# ejer = Ejercicios()
# # num = int (input("Ingrese un numero: "))
# # print("Llamada 1")
# lista = [2,3,1,5,6,8,10]
# print("llamada 2")
# perfetos = []
# for num in lista:
#     if ejer.perfecto2(num) == num:
#         perfetos.append(num)
# print(perfetos)
        


class Programacion(Ejercicios):
    def __init__(self,valor):
        self.dato = valor
        super().__init__(valor)
        self.dato=valor
            
    def divisores (self,num):
        super.(parImpar(num))
        cont=1
        divisores=[]
        while cont < num:
            rec = num % cont
            if  rec == 0:
                divisores.append(cont)
            cont = cont + 1
        return divisores
    
        
    
    
prog1 = Programacion(20)
print(prog1.divisores(4))
print(prog1.lista)



# div = prog1.divisores(6)
# lista = [1,2]
# lista2 = lista+div
# print(lista2)





# num=7
# acumdivisor = prog1.perfecto2(num)
# if acumdivisor == num:
#     print(num,"es perfecto")
# else:
#     print(num,"No es perfecto")
    
# numeros = [3,6,24,28]
# perfectos = []
# for numero in numeros:
#     if prog1.perfecto2(numero) == numero:
#         perfectos.append(numero)
# print(perfectos)
    



# input()
# print("Llamada 2")    
# ejer.parImpar(23)