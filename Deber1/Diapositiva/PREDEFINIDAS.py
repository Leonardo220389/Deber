#Funciones matematicas
import math
num1, num2, num, men = 12.572, 15.4, 4, "1234"
print(math.ceil(num1), "\t", math.floor(num1))
print(round(num1,1),"\t", type(num),"\t", -type(men))
#funcion de cadena
mensaje = "Hola" + "mundo" + "Python"
men1 = mensaje.split()
men2 = "".join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("mundo"), mensaje.lower())
# funciones de fecha
from datetime import datetime,timedelta,date
hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days=30)
dif, aa, mm, dd = futuro = hoy, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd+2)
print(hoy, fdia, futuro, dif, fecha)
# Tuplas – Listas - Diccionarios
usuario = ('dchiki','1234','chiki@gmail.com')
materias = ["Python","PHP","POO","Go"]
docente = {"nombre":"Daniel","edad":50,"fac":"faci"}
print(usuario[0],materias[1],docente['nombre'])
print(usuario[0:2],docente.keys(),docente.values())
materias.append('Programacion Movil')
docente['sexo’], docente['edad']=‘M’, 51
print(materias,docente)
tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)
# Recorridos diccionario con items
for c, v in docente.items(): print(c,':',v)

