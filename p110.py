list_1 = [1]  # Creamos una lista con un solo elemento
list_2 = list_1  # Ambas variables apuntan a la misma lista

list_1[0] = 2  # Modificamos el único elemento de list_1
print(list_2)  # Salida: [2]
