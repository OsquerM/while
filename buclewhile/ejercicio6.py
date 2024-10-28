# Usar while-else para validar un correo electrónico.
# Pide al usuario que introduzca su correo electrónico. Si el correo contiene "@" y ".", muestra "Correo válido" y termina el programa. Si el usuario falla tres veces seguidas, muestra "Correo inválido" y termina el programa.

usuario = input("Introduce tu correo electronico: ")
intentos = 0

while intentos < 3:
    posicionArroba = 0
    posicionPunto = 0
    if "@" in usuario and "." in usuario:
        posicionArroba = usuario.find("@")
        posicionPunto = usuario.find(".")
    if posicionArroba < posicionPunto:
        print("Correo valido")
        break
    else:
        print("Correo invalido") 
else:   
    print("Correo invalido")
    intentos += 1
   
if intentos == 3:
    print("Has agotado el numero de intentos")