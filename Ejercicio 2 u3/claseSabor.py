class Sabor:
     __idSabor:int
     __nombre:str
     __ingredientes:str
     def __init__(self, id, nombre, ingredientes):
          self.__idSabor=id
          self.__nombre=nombre
          self.__ingredientes=ingredientes

     def __str__(self):
        return (f"Id: {self.__idSabor}\nNombre: {self.__nombre}\nIngredientes: {self.__ingredientes}")

     def getNombre(self):
         return self.__nombre
     
     def getId(self):
         return self.__idSabor