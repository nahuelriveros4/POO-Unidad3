from claseHelado import Helado

class ManejadorHelado:
    __listaM=[]
    def __init__(self):
        self.__listaM=[]

    def cargarDatos(self, listaSabor):
        gramos=float(input("Ingresar Gramos (100gr, 150 gr, 250 gr, 500 gr y 1000gr): "))
        precio=float(input("Ingresar Precio: "))
        nombre=input("Ingresar Sabor: ")
        helado=Helado(gramos,precio)
        while nombre != "salir":
            i=0
            encontrado=False
            while i < len(listaSabor) and not encontrado:
                if listaSabor[i].getNombre() == nombre:
                    helado.addSabor(listaSabor[i])
                    encontrado=True
                    print("Sabor regitrado con exito")
                else:
                    i+=1
            nombre=input("Ingresar Sabor (finalizar con 'salir'): ")
        self.__listaM.append(helado)
        print("Helado regitrado con exito")
    
    def mostrarDatos(self):
        for helado in self.__listaM:
            helado.mostrarDatos()
    
    def masPedidos(self):
        cont_sabores={}
        for helado in self.__listaM:
            for sabor in helado.getSabores():
                if sabor.getNombre() in cont_sabores:
                    cont_sabores[sabor.getNombre()] += 1
                else:
                    cont_sabores[sabor.getNombre()] = 1
        sabores_mas_pedidos = sorted(cont_sabores.items(), key=lambda item: item[1], reverse=True)[:5]
        return sabores_mas_pedidos
    
    def totalGramos(self, id):
        total=0
        for helado in self.__listaM:
            i=0
            encontrado=False
            lista=helado.getSabores()
            while i < len(lista):
                if lista[i].getId() == id and not encontrado:
                    encontrado=True
                    nombre=lista[i].getNombre()
                    gramos=helado.getGramos()/len(helado.getSabores())
                    total+=gramos
                else:
                    i+=1
        print(f"La cantidad de gramos vendidos para el sabor {nombre} con Id: {id} es de: {total:.2f}gr")
       
    def totalRecaudado(self):
        importe={}
        for helado in self.__listaM:
            precio=helado.getPrecio()
            if helado.getGramos() in importe:
                importe[helado.getGramos()] += precio
            else:
                importe[helado.getGramos()] = precio
        return importe

    def tipoHelado(self, gramos):
        sabores=[]
        i=0
        while i < len(self.__listaM):
            if self.__listaM[i].getGramos() == gramos:
                for sabor in self.__listaM[i].getSabores():
                    if sabor.getNombre() not in sabores:
                        sabores.append(sabor.getNombre())
                i+=1
            else:
                i+=1
        return sabores              
