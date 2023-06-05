from interface import Coleccion

class MiColeccion(Coleccion):
    __coleccion=[]
    def __init__(self):
        self.__coleccion = []

    def insertarElemento(self, objeto, posicion):
        try:
            if posicion < 0 or posicion > len(self.__coleccion):
                raise ValueError("Posición no válida")
            self.__coleccion.insert(posicion, objeto)
        except ValueError as e:
            print(f"Error al insertar elemento: {str(e)}")

    def agregarElemento(self, objeto):
        self.__coleccion.append(objeto)

    def mostrarElemento(self, posicion):
        try:
            if posicion < 0 or posicion >= len(self.__coleccion):
                raise IndexError("Posición no válida")
            print(self.__coleccion[posicion])
        except IndexError as e:
            print(f"Error al mostrar elemento: {str(e)}")