
class Ordenar:
    def __init__(self,lista):
        self.lista=lista
        
    # def recorrerElemento(self):
    #     for ele in self.lista:
    #         print(ele)
            
    # def recorrerPosicion(self):
    #     for pos,ele in enumerate(self.lista):
    #         print(pos,ele)
    
    # def recorrerRange(self):
    #     for pos in range(len(self.lista)):
    #         print(pos,self.lista[pos])
            
    # def buscar (self,buscado):
    #     enc=False
    #     for pos,ele in enumerate(self.lista):
    #         if ele == buscado:
    #             enc=True
    #             break
    #     if enc == True:
    #         return pos
    #     else:
    #         return -1
    
    def ordenarAsce(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista [pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux

     
    def ordenarDes(self):
         for pos, ele in enumerate(self.lista):
             for sig in range (pos+1, len(self.lista)):
                 if ele < self.lista[sig]:
                     aux = self.lista[pos]
                     self.lista[pos]=self.lista[sig]
                     self.lista[sig]=aux
                     
    def primer(self):
        return self.lista[0]
    
    def primerEliminado(self):
        primer = self.lista[0]
        auxlista = []
        for pos in range(1, len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primer    
    
    def primerEliminado2(self):
        primer = self.lista[0]
        auxlista = []
        self.lista=self.lista[1:]
        return primer    
    
    def ultima(self):
        return self.lista[-1]
    
    def primerEliminado(self):
        primer = self.lista[0]
        auxlista = []
        for pos in range(0, len(self.lista)-1):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primer    
        
    def ultimoEliminado2(self):
        ultimo = self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo  
    
    def insertar(self):
        self.ordenarAsce()
        
        
          
lista = [2,3,1,5,8,10]
ord1 = Ordenar(lista)
print(ord1.primerEliminado2())
print(ord1.lista)


# print(ord1.lista)
# ord1.ordenarAsce()
# print(ord1.lista)
# ord1.ordenarDes()
# print(ord1.lista)
# print("Primero",ord1.primer())
# print("Segundo",ord1.ultima())