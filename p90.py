# Número secreto del mago
numero_secreto = 7  

# Solicita al usuario un número
numero_usuario = int(input("Adivina el número del mago: "))

# Bucle while para seguir pidiendo hasta que el usuario acierte
while numero_usuario != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero_usuario = int(input("Intenta de nuevo: "))

# Mensaje cuando el usuario acierta
print(f"""
{numero_usuario}
¡Bien hecho, muggle! Eres libre ahora.
""")
