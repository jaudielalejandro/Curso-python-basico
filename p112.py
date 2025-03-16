list_1 = ["A", "B", "C"]
list_2 = list_1  # Ambas listas apuntan a la misma referencia en memoria
list_3 = list_2  # También apunta a la misma referencia en memoria

del list_1[0]  # Elimina "A" de la lista
del list_2[0]  # Elimina "B" de la lista (porque list_2 y list_1 son la misma lista)

print(list_3)  # ¿Qué contiene list_3?
