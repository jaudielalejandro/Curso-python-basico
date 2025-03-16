my_list = [8, 10, 6, 2, 4]  # Lista desordenada
swapped = True  # Variable de control para detectar intercambios

while swapped:  # Mientras haya intercambios, seguimos ordenando
    swapped = False  # Inicialmente asumimos que no habrá intercambios
    for i in range(len(my_list) - 1):  # Recorremos la lista
        if my_list[i] > my_list[i + 1]:  # Comparamos elementos adyacentes
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Intercambio
            swapped = True  # Marcamos que hubo un intercambio

print("Lista ordenada:", my_list)
