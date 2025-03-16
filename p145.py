import sys

# Lectura desde sys.stdin
print("Ingresa un texto:")
user_input = sys.stdin.readline().strip()
print(f"Texto ingresado: {user_input}")

# Escritura en sys.stdout
sys.stdout.write("Este es un mensaje enviado a stdout.\n")

# Escritura en sys.stderr (error estándar)
sys.stderr.write("Este es un mensaje de error enviado a stderr.\n")

# Redirección de salida a un archivo
with open("output.txt", "w", encoding="utf-8") as file:
    sys.stdout = file  # Redirigir stdout al archivo
    print("Este mensaje se escribirá en output.txt en lugar de la pantalla.")
    sys.stdout = sys.__stdout__  # Restaurar stdout a su valor original

print("Fin del programa.")
