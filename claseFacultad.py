from claseCarrera import Carrera
class Facultad:
    __codigoFacultad=0
    __nombreFacultad=''
    __direccion=''
    __localidad=''
    __telefono=''
    __carreras=[]

    def __init__(self,cod,nomb,direc,local,tel) -> None:
        self.__codigoFacultad = cod
        self.__nombreFacultad = nomb
        self.__direccion =direc
        self.__localidad = local
        self.__telefono = tel
        self.__carreras=[]

    def agregarCarrera(self,cod, nom, ini, dur, tit):
        self.__carreras.append(Carrera(cod, nom, ini, dur, tit))

    def getCarreras(self):
        return self.__carreras
              
    def getCodFacultad(self):
        return self.__codigoFacultad
    
    def getNomFacultad(self):
        return self.__nombreFacultad
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono
        