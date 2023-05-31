class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = {
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            0:self.opcion0
        }

    def opcion1(self, helado,sabores):
        print("Registrar helado vendido")
        helado.cargarDatos(sabores)
   
    def opcion2(self, helado):
        #helado.mostrarDatos()
        print("Mostrar los 5 sabores de helado más pedidos")
        Pedidos=helado.masPedidos()
        print("Los 5 sabores de helado más pedidos son:")
        for sabor, contador in Pedidos:
            print(sabor, contador)
        
    def opcion3(self, helado):
        print("Estimar gramos vendidos de un sabor")
        id=int(input("Ingresar un numero de sabor (1 al 4): "))
        if id > 4:
            print("Opcion invalida")
        else:
            helado.totalGramos(id)
    
    def opcion4(self, helado):
        print("Mostrar sabores vendidos en un tipo de helado")
        gramos=float(input("Ingrese un tipo de helado (100, 150, 250, 500 y 1000): "))
        listaS=helado.tipoHelado(gramos)
        for sabor in listaS:
            print(sabor)

    def opcion5(self, helado):
        print("Importe total recaudado por la Heladeria")
        diccImporte=helado.totalRecaudado()
        for gramos, importe in diccImporte.items():
            print(f"El importe total recaudado por el tipo de helado de {gramos}gr es de: ${importe}")

    def opcion0(self):
        print("Usted esta saliendo del Programa")
        
        
    def ejecutar(self, listaS, manejadorH):
            while True:
                print("----- Menú -----")
                print("1. Registrar helado vendido")
                print("2. Mostrar los 5 sabores de helado más pedidos")
                print("3. Estimar gramos vendidos de un sabor")
                print("4. Mostrar sabores vendidos en un tipo de helado")
                print("5. Importe total recaudado por la Heladeria")
                print("0. Salir")
                op = int(input("Ingrese una Opcion: "))

                func = self.__switcher.get(op, lambda: print("Opción no válida"))
                if op==1:
                    func(manejadorH, listaS)
                elif op==2 or 3 or 4 or 5:
                    func(manejadorH)
                else: 
                    func()
                if 0==op:
                    break