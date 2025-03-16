my_list = [10, 1, 8, 3, 5]  # Lista original
length = len(my_list)  # Obtener la longitud de la lista

# Intercambiar elementos para invertir la lista
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# Imprimir la lista invertida
print("Lista invertida:", my_list)
