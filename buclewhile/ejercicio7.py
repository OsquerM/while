# Ejercicio 7: Gestión de roles de usuario en un sistema
# Objetivo: Usar while con match-case para verificar roles de usuario.
# Crea un sistema que permite al usuario introducir su rol (admin, editor, visitante). Usa while para solicitar el rol hasta que el usuario escriba "salir". Según el rol, muestra:
# admin: "Tienes acceso completo."
# editor: "Tienes acceso a la edición."
# visitante: "Tienes acceso de visualización."


salida = True
while salida:
    rol = input("Introduce tu rol: ")
    match rol:
        case "admin":
            print("Tienes acceso")
        case "editor":
            print("Tiene acceso a la edición")
        case "visitante":
            print("Tienes acceso de visualización")
        case "salir":
            salida = False
            print("Has salido correctamente")