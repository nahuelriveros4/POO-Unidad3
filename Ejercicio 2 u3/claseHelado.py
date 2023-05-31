class Helado:
     __gramos:float
     __precio:float
     __sabores:list
     def __init__(self, gramos, precio):
         self.__gramos=gramos
         self.__precio=precio
         self.__sabores=[]
               
     def addSabor(self, sabor):
        self.__sabores.append(sabor)

     def mostrarDatos(self):
         print(f"Gramos: {self.__gramos}\nPrecio: {self.__precio}")
         print('Sabores: ')
         for sabor in self.__sabores:
            print(sabor.getNombre())
    
     def getSabores(self):
         return self.__sabores
     
     def getGramos(self):
         return self.__gramos
     
     def getPrecio(self):
         return self.__precio