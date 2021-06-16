class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        #ciclo repetitivo de incremento o decremento se ejecta por verdadero
        nombre = "Daniel"
        datos=["Daniel", 50, True]
        numeros=(2,5,6,4,1)
        docente= {"Nombre":"Daniel", "edad":50, "fac":"faci"}
        listaNotas=[(30, 40), (20, 40), (50, 40)]
        listaAlumnos = [{"nombre":"Erick", "final":70},{"nombre":"Yady", "final":60}, {"nombre":"Danny", "final":70}]
    # j=0
    # while j<5:
    #     print("While", j)
    #     j=j+1  
      
        # for i in range(5):#rango(0,1,2,3,4)
        #     print("for",i, end=" ")  
        # print()
        # for i in range(1,5):#rango(1,2,3,4)
        #     print("for",i, end=" ")
        # print()
        # for i in range(2, 10, 2):#rango(2,4,6,8)
        #     print("for",i, end=" ")
        # print()
        # for i in range(12, 3,-3):#rango(12,9,6)
        #     print("for",i, end=" ")
        
         
        #for se trabaja con rango y colecciones
        
        # for elem in datos:
        #     print(elem, end =" ") 
        # for elem in nombre:
        #     print(elem, end =" ") 
        
        
        # lon = len(datos) 
        # for pos in range(lon):
        #     print(pos,datos[pos])  
            
        # for pos, valor in enumerate(datos):
        # # enumerate genera posicion y valor
        #     print(pos, valor)    
        
        # for clave, valor in docente.items():
        #     print(clave, valor, end=" ")
        print(listaNotas)
        for notas in listaNotas:
            acum = 0
            for nota in notas:
                acum = acum + nota
            print(acum/len(notas), end=" ")
                   
        print("\n Diccionario de notas")
        print(listaAlumnos)
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":", valor, end=" ")
            print()
bucle= For()
bucle.usoFor()