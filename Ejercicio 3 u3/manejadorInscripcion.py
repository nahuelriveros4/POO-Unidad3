
class ManejadorIncripciones:
    __inscripciones = list()
    
    def __init__(self):
        self.__inscripciones = []
        
        
    def agregarInscripcion(self, unaInscripcion):
        self.__inscripciones.append(unaInscripcion)
        
    def getInscripciones(self):
        return self.__inscripciones