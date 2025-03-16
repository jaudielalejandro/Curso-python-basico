# Ejemplo de apertura de archivos en diferentes modos

# Modo de lectura ('r')
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("Contenido del archivo en modo lectura:")
        print(content)
except FileNotFoundError:
    print("El archivo no existe.")

# Modo de escritura ('w')
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Este es un nuevo archivo creado en modo escritura.\n")
    file.write("El contenido anterior se ha eliminado.\n")

print("Archivo escrito en modo 'w'.")

# Modo de adjuntar ('a')
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write("Se ha agregado esta línea en modo adjuntar.\n")

print("Archivo actualizado en modo 'a'.")

# Modo de lectura y actualización ('r+')
try:
    with open('example.txt', 'r+', encoding='utf-8') as file:
        print("Lectura del archivo en modo 'r+':")
        print(file.read())
        file.write("Añadiendo contenido con 'r+'.\n")
except FileNotFoundError:
    print("El archivo no existe.")

# Modo de escritura y actualización ('w+')
with open('example.txt', 'w+', encoding='utf-8') as file:
    file.write("Nuevo contenido con 'w+'.\n")
    file.seek(0)  # Volver al inicio para leer lo escrito
    print("Lectura tras escribir con 'w+':")
    print(file.read())
