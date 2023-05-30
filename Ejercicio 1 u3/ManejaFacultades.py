import csv
from claseFacultad import Facultad
from claseCarrera import Carrera

class Maneja_Facultades:
    __facultades = []

    def __init__(self) -> None:
        self.__facultades = []

    def agregarFacultad(self,unaFacultad):
        self.__facultades.append(unaFacultad)
    
    def cargarArchivo(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=",")
        cod=0
        facu = True
        for i in reader:
            if (facu):
                #entra facultades
                unaFacultad = Facultad(int(i[0]), i[1], i[2], i[3], i[4])
               
                self.agregarFacultad(unaFacultad)
                cod = int(i[0])
                facu= False
            elif cod == (int(i[0])):
                #entran las carreras
                unaFacultad.agregarCarrera(int(i[1]), i[2], i[3], i[4], i[5])
            else: 
                #nueva facultad
                unaFacultad = Facultad(int(i[0]), i[1], i[2], i[3], i[4])
                self.agregarFacultad(unaFacultad)
                cod = int(i[0])
 


    def BuscarFacultad(self):    
        facu=0    
        facu = int(input("Ingrese Codigo de una Facultad: "))
        for i in self.__facultades:
         if i.getCodFacultad() == facu:
            print(f"\nFacultad: {i.getNomFacultad()}")
            for carrera in i.getCarreras():
                print(f'\nNombre carrera: {carrera.getNomCarrera()}')
                print(f'Duracion carrera: {carrera.getDuracion()}')
       
    
    def MostrarCarrera(self):
        nombreCarrera= input("Ingrese Nombre de la carrera: ")
        for i in self.__facultades:
            for j in i.getCarreras():
                if j.getNomCarrera() == nombreCarrera:
                    print("Carrera Encontrada")
        
