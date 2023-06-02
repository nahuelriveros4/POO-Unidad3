import numpy as np
from claseTaller import TallerCapacitacion
class ManejadorTalleres:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __talleres = None
    
    def __init__(self,dim):
        self.__talleres =  np.empty(dim, dtype = TallerCapacitacion)
        self.__cantidad = 0
        self.__dimension = dim
        
    def agregarTaller(self, idt, nom, vac, mins):
        
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__talleres.resize(self.__dimension)
        self.__talleres[self.__cantidad] = TallerCapacitacion(idt, nom, vac, mins)
        self.__cantidad += 1
        
    
    def getCantTalleres(self):
        return len(self.__talleres)
    
    def getTalleres(self):
        return self.__talleres


