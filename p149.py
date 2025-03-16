import sys

def open_file(file_name, mode):
    try:
        with open(file_name, mode, encoding='utf-8') as file:
            print(f"Archivo '{file_name}' abierto correctamente en modo '{mode}'.")
            return file.read()
    except IOError as e:
        print(f"Error al abrir el archivo: {e}")
        print(f"Código de error: {e.errno}", file=sys.stderr)

# Intento de abrir un archivo de ejemplo
file_content = open_file("ejemplo.txt", "r")
if file_content:
    print("Contenido del archivo:")
    print(file_content)
