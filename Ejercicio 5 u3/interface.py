from abc import ABC, abstractmethod

class Coleccion(ABC):
    @abstractmethod
    def insertarElemento(self, objeto, posicion):
        pass

    @abstractmethod
    def agregarElemento(self, objeto):
        pass

    @abstractmethod
    def mostrarElemento(self, posicion):
        pass