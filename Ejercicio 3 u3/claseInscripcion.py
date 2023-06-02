class Inscripcion:
    __fechaInscripcion = str()
    __pago = bool()
    __persona = object()
    __tallerCapacitacion = object()
    
    def __init__(self, fecha, pago, persona, taller):
        self.__fechaInscripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__tallerCapacitacion = taller
    
    def getPersona(self):
        return self.__persona
    
    def getPago(self):
        return self.__pago
    
    def getFecha(self):
        return self.__fechaInscripcion
    
    def getTaller(self):
        return self.__tallerCapacitacion
    
    def realizarPago(self):
        self.__pago = True
    
    def imprimirInscripcion(self):
        print('Fecha',self.__fechaInscripcion)
        print('Dni Persona: ', self.__persona.getDni())
        if self.__pago:
            print('Pago realizado del taller ', self.__tallerCapacitacion.getNombre())
        else:
            print('Pago no realizado del taller ', self.__tallerCapacitacion.getNombre())