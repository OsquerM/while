# Trabajar con cadenas y while para generar slugs de URL.
# Pide al usuario que introduzca títulos de artículos de un blog. Cada título debe convertirse a un "slug" (todo en minúsculas, sin espacios, reemplazando estos con guiones). Permite al usuario crear varios slugs hasta que introduzca "salir".


slug = ""
salida = True


while salida:
        titulo = input("Introduce un titulo o pon salir: ").lower()
        if titulo == "salir":
            salida = False
        else:
            slug = titulo.lower()
            slug = slug.replace(" ", "-")
            print(f"Slug generado: {slug}")