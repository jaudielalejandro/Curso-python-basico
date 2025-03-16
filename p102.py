# Lista inicial con cinco números
numbers = [10, 5, 7, 2, 1]

# Paso 1: Reemplazar el número central con un número ingresado por el usuario
numbers[2] = int(input("Ingrese un número para reemplazar el número central: "))

# Paso 2: Eliminar el último elemento de la lista
numbers.pop()

# Paso 3: Imprimir la longitud de la lista existente
print("La longitud de la lista es:", len(numbers))

# (Opcional) Imprimir la lista resultante
print("Lista actualizada:", numbers)
