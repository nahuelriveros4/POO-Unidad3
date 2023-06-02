from clasePersona import Persona
class ManejadorPersona:
    __personas = list()
    
    def __init__(self):
        self.__personas = []
    
    def agregarPersona(self):
        nom = input('Ingrese el nombre de la persona: ')
        dire = input('Ingrese la direccion de la persona: ')
        dni = int(input('Ingrese el dni de la persona: '))
        unaPersona = Persona(nom, dire, dni)
        self.__personas.append(unaPersona)
        return unaPersona
    
    def getPersonas(self):
        return self.__personas