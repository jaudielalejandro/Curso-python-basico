# Crear una lista vacía para almacenar los números
numbers = []

# Pedir al usuario que ingrese cinco números
for i in range(5):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numbers.append(num)  # Agregar el número a la lista

# Ordenar la lista en orden ascendente
numbers.sort()

# Imprimir los números ordenados
print("Números en orden ascendente:")
for num in numbers:
    print(num)
