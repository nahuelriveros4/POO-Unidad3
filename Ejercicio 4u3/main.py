from manejadorEmpleados import ColeccionEmpleados

if __name__ == '__main__':
    tamaño = int(input("Ingrese cantidad de emplados: "))
    empleados = ColeccionEmpleados(tamaño)

 
    empleados.testEmpleados()
    
    
    empleados.RegistrarHoras()
    

    empleados.totalDeTarea()
    
    
    print('\n\n3.   Ayuda Económica.')
    empleados.ayudaEconomica()
    
 
    print('\n\n4.   Calcular sueldo:')
    empleados.calcularSueldos()