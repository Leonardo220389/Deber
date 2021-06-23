class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        #ciclo repetitivo de incremento o decremento se ejecta por verdadero
        # nombre = "Daniel"
        # datos=["Daniel", 50, True]
        # numeros=(2,5,6,4,1)
        # docente= {"Nombre":"Daniel", "edad":50, "fac":"faci"}
        # #listaNotas=[(30, 40), (20, 40), (50, 40)]
        # listaAlumnos = [{"nombre":"Erick", "final":70},{"nombre":"Yady", "final":60}, {"nombre":"Danny", "final":70}]
        
        listaNotas=[(30, 40, 10, 20), (20, 40, 50), (50, 40, 10),(10, 20)]
        acum,cont=0,0
        for notas in listaNotas:
            #print("primer for",notas)
            acumparcial=0
            for nota in notas:
                #print("segundo for",nota)
                acumparcial+=nota
                cont=cont+1
            acum=acum+acumparcial
            print("Total Parcial: {}, Promedio Parcial: {}",format(acumparcial,acumparcial/len(notas))
        print("Totalgeneral: {} , PromedioGeneral: {}",format(acum,acum/cont))
        
        
bucle= For()
bucle.usoFor()