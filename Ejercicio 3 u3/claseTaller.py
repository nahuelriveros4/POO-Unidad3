from claseInscripcion import Inscripcion
class TallerCapacitacion:
    __idTaller = int()
    __nombre = str()
    __vacantes = int()
    __montoInscripcion = int()
    __inscripciones = list()
    
    def __init__(self, idt, nom, vac, mins):
        self.__idTaller = idt
        self.__nombre = nom
        self.__vacantes = vac
        self.__montoInscripcion = mins
        self.__inscripciones = []
    
    def realizarInscripcion(self,persona):
        fecha = input('Ingresar fecha de inscripcion: ')
        pago = input('¿Pago la inscipcion? ')
        if pago == 'no':
            pago = False
        else:
            pago = True
        unaInscripcion = Inscripcion(fecha, pago, persona, self)
        self.__inscripciones.append(unaInscripcion)
        self.vacanteMenos()
        print('se inscribio correctamente')
        return unaInscripcion
    
    def getVacantes(self):
        return self.__vacantes
    
    def vacanteMenos(self):
        self.__vacantes -= 1
        print(f'vacantes: {self.__vacantes}')
    
    def getNombre(self):
        return self.__nombre
        
    def getInscripcionesDelTaller(self):
        return self.__inscripciones
    
    def getIdTaller(self):
        return self.__idTaller
    
    def getMonto(self):
        return self.__montoInscripcion
    