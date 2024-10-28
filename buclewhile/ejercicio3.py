#  Usar while y continue.
# Simula un contador de visitas diarias para una página web. Pide al usuario que introduzca "visit" para incrementar el contador. Usa continue para ignorar cualquier entrada que no sea "visit". Cuando el contador llega a 100 visitas, muestra "Límite diario alcanzado" y termina el programa.

visitasDiarias = 0 

limiteDiario = 0

while visitasDiarias <= 100:
    pregunta = input("Introduce visit y sube el contador: ")
    if pregunta == "visit":
         limiteDiario +=1
         print(limiteDiario)
         continue
    # else:
    #     print("No entiendo tu pregunta")