any_list = [1, 2, 3, 4]
even_list = list(map(lambda x: x + (x % 2), any_list))  # Asegura que los números sean impares
print(even_list)  # Salida esperada: [1, 3, 3, 5]
