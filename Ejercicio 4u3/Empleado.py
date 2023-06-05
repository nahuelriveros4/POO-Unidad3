class Empleado:
    __DNI=''
    __nombre=''
    __direccion=''
    __telefono=''

    def __init__(self, dni, nom,direc,tel):
        self.__DNI = dni
        self.__nombre = nom
        self.__direccion = direc
        self.__telefono = tel

    def getDNI(self):
        return self.__DNI
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
        
    def imprimirEmpleado(self):
        print('Dni: ',self.__dni, '\nNombre: ',self.__nombre, '\nDireccion: ',self.__direccion,'\nTelefono: ',self.__telefono)
    