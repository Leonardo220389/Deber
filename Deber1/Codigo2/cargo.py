class Cargo:
    secuencia=0 #Variable de la clase, ese atributo es valida para toda los metodos
    def __init__(self,cod=99,des="Sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        #self.__codigo = 99 #__ este simbolo indica que es un atributo privado de la clase
        self.descripcion="Sin Cargo"
        
if __name__ == "__main__":       
    cargo1 = Cargo()
    print("Ejecutando desde el archivo cargo.py")
    print("Cargo",cargo1.codigo,cargo1.descripcion)
    cargo2 = Cargo()
    print("Cargo2",cargo2.codigo,cargo2.descripcion)
    cargo3 = Cargo()
    print("Cargo3",cargo3.codigo,cargo3.descripcion)
    print(Cargo.secuencia)