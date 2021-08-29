
class Ordenar:
    def __init__(self,lista):
        self.lista=lista
    
    def ordenarAsce(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista [pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux
  
    # def ordenarDes(self):
    #      for pos, ele in enumerate(self.lista):
    #          for sig in range (pos+1, len(self.lista)):
    #              if ele < self.lista[sig]:
    #                  aux = self.lista[pos]
    #                  self.lista[pos]=self.lista[sig]
    #                  self.lista[sig]=aux 
    
    def insertar(self):
        self.ordenarAsce()
        for recorrido in range(0, len(self.lista)):
            for posicion in range(len(self.lista-recorrido)):
                if dato > lista[posicion+1]:
                    aux = dato
                    dato = lista[posicion+1]
                    lista[posicion+1]=aux
                            

lista = [2,3,1,5,8,10]
dato = 4
res = Ordenar()
print(res.insertar())


