from coleccion import MiColeccion

def test():
    coleccion= MiColeccion()

    coleccion.agregarElemento("Elemento 1")
    coleccion.agregarElemento("Elemento 2")
    coleccion.agregarElemento("Elemento 3")

    coleccion.mostrarElemento(1)  # Mostrar "Elemento 2"
    coleccion.mostrarElemento(5)  # Error: Posición no válida

    coleccion.insertarElemento("Elemento X", 0)
    coleccion.insertarElemento("Elemento Y", 5)  # Error: Posición no válida

    coleccion.mostrarElemento(0)  # Mostrar "Elemento X"
    coleccion.mostrarElemento(1)  # Mostrar "Elemento 1"

if __name__ == '__main__':
    test()