from Empleado import Empleado
class Contratado(Empleado):
    __fechaInicio=''
    __fechaFinal='' 
    __horasTrabajadas=0
    __valorHora:float
    def __init__(self, dni, nom, direc, tel, inicio, final, horas, valorhora):
        super().__init__(dni, nom, direc, tel)
        self.__fechaInicio = inicio
        self.__fechaFinal = final
        self.__horasTrabajadas = horas
        self.__valorHora = valorhora

    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFinal(self):
        return self.__fechaFinal
    
    def getHorasTrabajadas(self):
        return self.__horasTrabajadas
    
    def getValorHora(self):
        return self.__valorHora
    
    def CalcularSueldo(self):
        Sueldo = self.__horasTrabajadas * self.__valorHora
        return Sueldo
    
    def aumentarHoras(self, aumento):
        self.__horas += aumento        
    
    def imprimirContratado(self):
        super().imprimirEmpleado()
        print('Fecha de Inicio: ',self.__fInicio,'\nFecha de Finalización: ', self.__fFin,'\nHoras: ',self.__horas,'\nValor por Hora: ',self.__valorHora)
