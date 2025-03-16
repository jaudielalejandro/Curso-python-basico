# Crear un arreglo 3D para modelar los edificios, pisos y habitaciones
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Reservar una habitación: Segundo edificio (índice 1), décimo piso (índice 9), habitación 14 (índice 13)
rooms[1][9][13] = True
print("Habitación reservada en el segundo edificio, piso 10, habitación 14.")

# Desocupar una habitación: Primer edificio (índice 0), quinto piso (índice 4), segunda habitación (índice 1)
rooms[0][4][1] = False
print("Habitación desocupada en el primer edificio, piso 5, habitación 2.")

# Verificar disponibilidad en el piso 15 del tercer edificio
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:  # Piso 15 (índice 14), tercer edificio (índice 2)
        vacancy += 1

# Imprimir el número de habitaciones disponibles en el piso 15 del tercer edificio
print(f"Habitaciones disponibles en el piso 15 del tercer edificio: {vacancy}")
