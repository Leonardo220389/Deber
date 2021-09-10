class Lista:
    def __init__(self,listas):
        self.__lista = listas #atributo privado
        
    @property  #Unicamente trabaja con los atributos privados,cambia el comportamiento
    def lista(self):
        return self.__lista
    
    # busca un valor en la lista; retorna la posicion si lo encuentra
    # y si no lo encuentra retorna -1    
    def busquedaLineal(self,buscado):
        pos=0
        enc = False
        lon = len(self.__lista)
        # Recorre la lista hasta que la posicion sea igual a la longitud
        # o encontrado sea igual a TRUE  
        while pos < lon and enc == False:
            if self.__lista[pos]["nombre"] == buscado:
                enc = True
            else:
                pos = pos+1
                
        if enc == True:
            return pos
        else:
            return -1
            
                

            
    
    def ordenar(self,orden):
        orden  = orden.lower()
        if orden =="asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self._lista)):
                    if self.__lista[pos]["nombre"]>self.__lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos] = self.lista[sig]
                        self.__lista[sig] = aux
        
    def busquedaBinaria(self,buscado):
        self.ordenar("acs")
        fin = len(self.__lista)-1
        inicio = 0
        enc = False
        while inicio < fin and enc ==False:
            medio = (inicio+fin)//2
            if self.lista[medio]["nombre"] == buscado: enc == True
            elif self.lista[medio]["nombre"] < buscado: inicio = medio +1
            else: fin = medio - 1
        if enc: return medio
        else: return -1
    
    def busquedaEficiente(self):
        pass
        
 
notas = [
    {"nombre":"Daniel","n1":20,"n2":40},
    {"nombre":"Danny","n1":30,"n2":50},
    {"nombre":"Dayanna","n1":40,"n2":50},
    {"nombre":"Erick","n1":50,"n2":40},
    {"nombre":"Romina","n1":55,"n2":40},
    {"nombre":"Yady","n1":60,"n2":40}
         ] 
 
        
bus = Lista(notas)
posicion = bus.busquedaLineal("Erick")
if posicion != -1:
    print()

