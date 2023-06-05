from Empleado import Empleado
class DePlanta(Empleado):
    __sueldoBasico:float 
    __antiguedad=0
    def __init__(self, dni, nom, direc, tel, sueldo, antiguedad):
        super().__init__(dni, nom, direc, tel)
        self.__sueldoBasico=sueldo
        self.__antiguedad = antiguedad
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def CalcularSueldo(self):
        porcentaje = (self.__sueldoBasico*self.__antiguedad)/100
        Sueldo = self.__sueldoBasico + porcentaje
        return Sueldo