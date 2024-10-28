#  Usar while y match-case para aplicar descuentos por tipo de usuario.
# Simula un sistema de descuentos. Pide al usuario que introduzca su tipo (nuevo, frecuente, vip). Usa match-case para aplicar un descuento:
# nuevo: "Descuento del 10% aplicado."
# frecuente: "Descuento del 15% aplicado."
# vip: "Descuento del 20% aplicado." Continúa pidiendo el tipo de usuario hasta que el usuario escriba "salir".

salir = True
while salir:
    usuario = input("Introduce tu tipo (nuevo/frecuente/vip) o si quieres salir, indica salir: ")
    match usuario:
        case "nuevo":
            print("Descuento del 10 aplicado")
        case "frecuente": 
            print("Descuento del 15 aplicado")
        case "vip":
            print("Descuento del 20 aplicado")
        case "salir":
            salir = False