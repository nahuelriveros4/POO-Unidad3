from ManejaFacultades import Maneja_Facultades

if __name__=="__main__":
    mf = Maneja_Facultades()
    mf.cargarArchivo()


    print("--------- MENU --------")
    print("1 - Mostrar datos de la facultad")
    print("2 - Mostrar datos de la carrera")
    print("0 - Salir")
    
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        mf.BuscarFacultad()
    elif opcion == 2:
        mf.MostrarCarrera()
    elif opcion == 0:
        print("Esta saliendo del programa")
    else:
        print("Opcion incorrecta")