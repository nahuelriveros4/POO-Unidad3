class Carrera:
    __codigoCarrera=0
    __nombreCarrera=''
    __fechaInicio=''
    __duracion=''
    __titulo=''
    
    def __init__(self, cod, nom,fecha,duracion,titulo) -> None:
        self.__codigoCarrera = cod
        self.__nombreCarrera = nom
        self.__fechaInicio = fecha
        self.__duracion = duracion
        self.__titulo = titulo

    def __str__(self) -> str:
        return (f"{self.__codigoCarrera,self.__nombreCarrera,self.__fechaInicio,self.__duracion,self.__titulo}")

    def getCodCarrera(self):
        return self.__codigoCarrera
    
    def getNomCarrera(self):
        return self.__nombreCarrera
    
    def getFecha(self):
        return self.__fechaInicio
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo
        