""" num = 20 
nombre = "ana"
print(num, type(num))
print(nombre, type(nombre))

def mensaje(msg):
    print(msg)
    
mensaje("Mi primer programa en Python")
mensaje("Mi segundo programa en Python") """


class Sintaxis:
    instancia=0 #atributo de clase
    
    def __init__(self, dato="llamado al constructor"):
        self.frase=dato #atributo de instancia
        Sintaxis.instancia = Sintaxis.instancia+1
        
    def usoVariables(self):
        edad, _peso = 32, 70.5
        nombres ="leonardo Altamirano"
        car = nombres[0]
        tipo_sexo= "M"
        civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario = ()
        usuario = ("laltamirano", "1234", "laltamiranor@gmail.com")
        #usuario[]3= "milagro"
        #lista = [] coñecciones mutables
        materias = []
        materias = ["Programacion web", "PHP", "POO"]
        aux = materias[1]
        materias[1]="Python"
        materias.append("Go")
        print(materias, aux, materias[1])
        # #diccionario = () colecciones de objetos clave:valor tipo json
        docente = {}
        docente = {"nombre" : "Leonardo", "edad":32, "activo":True}
        edad=docente["edad"]
        docente["edad"]=33
        docente["carrera"] = "IS"
        #print(docente, edad, docente["edad"])
        print(usuario, usuario[0], usuario[0:2],usuario[-1])
        print(nombres, nombres[0], nombres[0:2], nombres[-1])
        print(materias, materias[2:], materias[:3], materias[::-1], materias[-2:])
        
        # presentacion con format
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres, edad))   
        
# print("Sintaxis de antes de instancia es: {}".format(Sintaxis.instancia))        
# ejer1 = Sintaxis() # Instancia la clase sintaxis y crea el objeto ejer1(copia la clase)
# print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))
# ejer2 = Sintaxis("instancia2")
# print(ejer.frase)
# print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
# print("Sintaxis nuevamente de ejer1 es:{ }", format(Sintaxis.instancia))  
# print(ejer2.frase)   

        