try:
    file = open("example.txt", "w", encoding="utf-8")
    file.write("Este es un archivo de ejemplo.\n")
finally:
    try:
        file.close()
        print("El archivo se cerró correctamente.")
    except IOError:
        print("Error al cerrar el archivo.")
