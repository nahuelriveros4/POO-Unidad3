from manejadorTaller import ManejadorTalleres
from manejadorPersonas import ManejadorPersona
from manejadorInscripcion import ManejadorIncripciones
import csv
if __name__ == '__main__':
    personas = ManejadorPersona()
    inscripciones = ManejadorIncripciones()
    #Cargar los datos de los talleres
    print('\n1.     Cargar los datos de los talleres')
       
    archivo = open('Talleres.csv')
    reader = csv.reader(archivo, delimiter = ';')
    cabecera = True
    for fila in reader:
        if cabecera:
            talleres = ManejadorTalleres(int(fila[0]))
            cabecera = False
        else:
            talleres.agregarTaller(int(fila[0]), fila[1], int(fila[2]), int(fila[3]))
    
    #inscribir una perona en un taller. Regisztrar la inscripion y la 
    #cantidad de vacantes el taller
    print('\n\n2.     Inscribir una persona en un taller (finaliza con 0)')
    
    idtaller = int(input('\nIngrese el nro del taller a inscribirse: '))
    while idtaller != 0:
        i=0
        while i < talleres.getCantTalleres() and idtaller != talleres.getTalleres()[i].getIdTaller():
            i += 1
        if i < talleres.getCantTalleres() :
            if talleres.getTalleres()[i].getVacantes() > 0:
                unaPersona = personas.agregarPersona()
                unaInscripcion = talleres.getTalleres()[i].realizarInscripcion(unaPersona)
                inscripciones.agregarInscripcion(unaInscripcion)
            else:
                print('No hay vacante disponible.')
        else:
            print('El taller ingresado no existe.')
            
        idtaller = int(input('\nIngrese el nro del taller a inscribirse: '))
    
    
    #Ingresar el DNI de una persona, si está inscripta mostrar
    #el nombre del taller en el que se inscribió y el monto que adeuda
    print('\n\n3.   Consultar Inscripcion')
    dni_bus = int(input('\nIngrese el dni de la persona q busca: '))
    i=0
    while i < len(personas.getPersonas()) and dni_bus != personas.getPersonas()[i].getDni():
        i += 1
    if i < len(personas.getPersonas()):
        j=0
        while j < len(inscripciones.getInscripciones()) and dni_bus != inscripciones.getInscripciones()[j].getPersona().getDni():
            j += 1
        if dni_bus == inscripciones.getInscripciones()[j].getPersona().getDni():
            inscripcion_bus = inscripciones.getInscripciones()[j]
            print(f'\nLa persona está inscripta en el taller {inscripciones.getInscripciones()[j].getTaller().getNombre()}')
            if not inscripciones.getInscripciones()[j].getPago():
                print(f'y adeuda {inscripciones.getInscripciones()[j].getTaller().getMonto()} pesos')
            else:
                print('y no adeuda.')
    else:
        print('Ninguna persona se regisro con el dni ingresado.')
    # Ingresar el identificador de un taller y listar los datos de los
    #alumnos que se inscribieron en él.
    print('\n\n4.   Consultar Inscriptos')
    band = False
    idtaller = int(input('\nIngrese el nro del taller a consultar: '))
    for inscripcion in inscripciones.getInscripciones():
        if idtaller == inscripcion.getTaller().getIdTaller():
            inscripcion.getPersona().printPersona()
            band = True
    if not band:
        print('No hay inscriptos en ese taller.')
        
    
    #Ingresar el DNI de una persona y registrar el pago (dar al atributo
    #pago el valor True).
    print('\n\n5.   Registrar Pago')
    dni_bus = int(input('Ingrese el dni de la parsona: '))
    i = 0
    while i < len(inscripciones.getInscripciones()) and dni_bus != inscripciones.getInscripciones()[i].getPersona().getDni():
        i += 1
    if i < len(inscripciones.getInscripciones()):
        if not inscripciones.getInscripciones()[i].getPago():
            inscripciones.getInscripciones()[i].realizarPago()
        else:
            print('Esta persona ya pagó.')
        inscripciones.getInscripciones()[i].imprimirInscripcion()
    else:
        print('Ninguna persona se registro con ese dni.')
        
    #Generar un nuevo archivo que contenga los siguientes datos de las 
    #inscripciones: DNI de la persona, idTaller, fechaInscripcion y pago
    print('\n\n6.   Guardar Inscripciones')
    with open('Inscripciones.csv', 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        for inscripcion in inscripciones.getInscripciones():
            fila = []
            fila.append(inscripcion.getPersona().getDni())
            fila.append(inscripcion.getTaller().getIdTaller())
            fila.append(inscripcion.getFecha())
            fila.append(inscripcion.getPago())
            escritor_csv.writerow(fila)