# Usar while y match-case para simular peticiones de API.
# Simula una API en la que el usuario puede realizar consultas de tipo GET, POST, PUT y DELETE. Usa match-case para gestionar cada consulta:
# GET: Muestra "Consulta de datos".
# POST: Muestra "Añadiendo datos".
# PUT: Muestra "Actualizando datos".
# DELETE: Muestra "Eliminando datos". El bucle termina cuando el usuario escribe "salir"

salir = True

while salir:
    usuario  = input("Introduce tu consulta (GET/POST/PUT/DELETE) o pon salir: ").upper()
    match usuario:
        case "GET":
            print("Consulta de datos")
        case "POST":
            print("Añadiendo datos")
        case "PUT":
            print("Actualizando datos")
        case "DELETE":
            print("Eliminando datos")
        case "SALIR":
            salir = False