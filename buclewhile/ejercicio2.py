# Objetivo: Usar while para validar URLs.
# Pide al usuario que introduzca una URL y sigue pidiéndola hasta que comience con "http://" o "https://". Si es válida, muestra "URL válida", de lo contrario, muestra un mensaje de error y vuelve a pedirla.


sigue = True
# Validar la URL
while sigue:
    url = input("Ingrese una URL: ")
    if (url.startswith("http://") or url.startswith("https://")) and (url.count(".") > 0):
        print("URL válida")
        sigue = False
    else:
        print("URL inválida")