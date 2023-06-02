class Persona:
    __nombre = str()
    __direccion = str()
    __dni = int()
    
    def __init__(self, nom, dire, dni):
        self.__nombre = nom
        self.__direccion = dire
        self.__dni = dni

    def getDni(self):
        return self.__dni
    
    def printPersona(self):
        print('\nDni: ', self.__dni,'\nNombre: ',self.__nombre,'\nDireccion: ',self.__direccion)
        