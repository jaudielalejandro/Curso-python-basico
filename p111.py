# Lista original con números repetidos
original_list = [1, 2, 3, 2, 4, 1, 5, 6, 4, 7]

# Crear una nueva lista sin duplicados
unique_list = []

# Recorrer la lista original y agregar solo los valores únicos a unique_list
for num in original_list:
    if num not in unique_list:
        unique_list.append(num)

# Imprimir la lista sin duplicados
print("Lista sin duplicados:", unique_list)
