from Empleado import Empleado

class Externos(Empleado):
    __tarea=''
    __fechaInicio='' 
    __fechaFinal=''
    __montoViatico:float 
    __costoObra:float
    __seguroDeVida:float
    def __init__(self, dni, nom, direc, tel, tarea, fechaI, fechaF, monto, costo,seguro):
        super().__init__(dni, nom, direc, tel)
        self.__tarea=tarea
        self.__fechaInicio= fechaI
        self.__fechaFinal = fechaF
        self.__montoViatico = monto
        self.__costoObra = costo
        self.__seguroDeVida = seguro

    def getTarea(self):
        return self.__tarea
    
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFinal(self):
        return self.__fechaFinal
    
    def getMontoViatico(self):
        return self.__montoViatico
    
    def getCostoObra(self):
        return self.__costoObra
    
    def getSeguroVida(self):
        return self.__seguroDeVida
    
    def CalcularSueldo(self):
        sueldo = self.__costoObra - self.__montoViatico - self.__seguroDeVida
        return sueldo
    
    def imprimirExterno(self):
        super().imprimirEmpleado()
        print('Tarea: ',self.__tarea,'Fecha de Inicio: ',self.__fInicio,'\nFecha de Finalización: ', self.__fFin,'\nMonto Viatico: ',self.__viatico,'\nCosto de Obra: ',self.__costoObra,'\nMonto Seguro: ',self.__seguro)
    