# Paso 1: Crear una lista vacía
beatles = []
print("Paso 1:", beatles)

# Paso 2: Agregar miembros iniciales con append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# Paso 3: Usar un bucle for para agregar a Stu Sutcliffe y Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(input(f"Agrega a {member} a la banda: "))  # Simula la entrada del usuario
print("Paso 3:", beatles)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best de la lista
del beatles[-1]  # Elimina el último elemento (Pete Best)
del beatles[-1]  # Elimina el penúltimo elemento (Stu Sutcliffe)
print("Paso 4:", beatles)

# Paso 5: Insertar a Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

# Resultado final
print("\nLos Beatles finales:", beatles)
