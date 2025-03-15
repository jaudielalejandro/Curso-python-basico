# Pedir al usuario que ingrese la cantidad de bloques
bloques = int(input("Ingresa la cantidad de bloques: "))

# Inicializar variables
altura = 0
bloques_usados = 0

# Construcción de la pirámide
while bloques_usados + (altura + 1) <= bloques:
    altura += 1  # Aumenta la altura de la pirámide
    bloques_usados += altura  # Se usan más bloques

# Imprimir la altura de la pirámide
print(f"La altura de la pirámide es: {altura}")
