email = "john.smith@pythoninstitute.org"  # Dirección de correo electrónico
username = ""  # Variable para almacenar la parte antes del @

for ch in email:
    if ch == "@":  # Si encontramos @, rompemos el bucle
        break
    username += ch  # Concatenamos los caracteres antes del @

print(username)  # Imprimimos la parte antes del @
