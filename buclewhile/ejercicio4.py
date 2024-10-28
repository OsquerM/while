# Usar while con break y if-else.
# Pide al usuario que introduzca un nombre de producto y simula una búsqueda en una tienda online. Si el producto es "teclado", "ratón" o "monitor", muestra que el producto está en stock y termina el programa. Si el usuario introduce "salir", termina sin mostrar mensaje. Usa break para salir del bucle cuando se encuentra el producto.

nombreProducto = input("Introduce el producto que quieres buscar: ")
salir = True
stock = ["teclado", "ordenador", "monitor"]

while salir:
    if nombreProducto in stock:
        print("El producto está en stock")
        break
    else:
        salir = False
