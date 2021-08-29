
class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        total_Sum= self.num1 + self.num2
        print("La suma de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Sum))
    
    def resta(self):
        total_Res= self.num1 - self.num2
        print("La resta de los numeros {} y {} es de: {}".format(self.num1, self.num2, total_Res))
    
    def multiplicacion(self):
        total_Mul= self.num1 * self.num2
        print("La multiplicación de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Mul))
                
    def division(self):
        total_Div=self.num1 / self.num2
        print("La division de los numeros es de: {}".format(total_Div))
        
class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
        
    def multiplicacion(self):
        Resultado= self.num1 * self.num2
        return Resultado
    
    def exponente(self):
        total_Exp = self.num1**self.num2
        print("la respuesta es: ",total_Exp)

    def valorAbsoluto(sefl,numero3):
        if numero3 < 0:
            numero3 = numero3 *- 1
        return numero3

    
class calCientifica(Calculadora):
    Pi = 3.1416
    
                        #radio  #lado
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def circunferencia(self):
        Perimetro = 2 * calCientifica.Pi * self.num1
        return Perimetro
    
    def areaCirculo(self):
        area = calCientifica.Pi * (self.num1**2)
        return area
    
    def areaCuadrado(self):
        return self.num2 ** 2
    

# cal = calCientifica(1,2,3,4)
# print(cal.circunferencia())
# print(cal.areaCirculo())
# print(cal.areaCuadrado())
