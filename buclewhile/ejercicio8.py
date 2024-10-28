# Simulación de carrito de compras con límite de productos
# Objetivo: Usar while con break para añadir productos a un carrito.
# Permite al usuario introducir nombres de productos que quiera añadir al carrito hasta un límite de 5 productos. Al alcanzar el límite, muestra "Carrito lleno" y termina el programa.


contador = 0
cesta = []
while contador < 5:
    producto = input("Introduce el producto deseado: ")
    cesta.append(producto)
    contador += 1
    print("Producto añadido a la cesta correctamente")
    print(f"Total de productos en la cesta: {contador}")

print("Carrito lleno")
print("Productos en la cesta:", cesta)