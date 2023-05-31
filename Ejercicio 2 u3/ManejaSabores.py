import csv
from claseSabor import Sabor

class ManejadorSabores:
    __listaM:list
    def __init__(self):
        self.__listaM=[]

    def cargarDatos(self):
        archivo=open("sabores.csv", encoding='utf-8')
        reader = csv.reader(archivo,delimiter=';')
        cabecera=True
        for fila in reader:
            if cabecera:
                cabecera=False
            else:
                idSabor=int(fila[0])
                nombre=fila[1]
                ingredientes=fila[2]
                sabor=Sabor(idSabor, nombre, ingredientes)
                print(sabor)
                self.__listaM.append(sabor)
        archivo.close()
        return self.__listaM
       