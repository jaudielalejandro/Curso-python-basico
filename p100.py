modified_string = ""  # Variable para almacenar la cadena modificada

for digit in "0165031806510":
    if digit == "0":  
        modified_string += "x"  # Reemplaza '0' con 'x'
        continue  # Salta al siguiente carácter
    
    modified_string += digit  # Agrega el dígito original si no es '0'

print(modified_string)  # Imprime la cadena modificada
