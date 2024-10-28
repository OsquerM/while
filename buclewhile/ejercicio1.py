# Simula una autenticación en la que el usuario debe introducir la contraseña correcta para acceder. Permite hasta 3 intentos. Si acierta, muestra "Acceso concedido" y termina el programa. Si falla tres veces, muestra "Acceso denegado" y termina.

pregunta = input("Introduce la contraseña: ")
continuar = True
contrasenia = "cachopo"
intentos = 0
while intentos < 3 and pregunta != contrasenia:
    pregunta = input("Vuelve a introducir la contraseña: ")
    intentos += 1
    if pregunta == contrasenia:
        print("Acceso concedido")        
    else:
        print("Acceso denegado")