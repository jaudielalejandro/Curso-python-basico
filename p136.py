# Definición de funciones lambda

two = lambda: 2  # Función sin parámetros que siempre devuelve 2
sqr = lambda x: x ** 2  # Función que devuelve el cuadrado del argumento
pow_ = lambda x, y: x ** y  # Función que eleva el primer argumento al segundo

# Pruebas de las funciones lambda
print(sqr(2), pow_(2, 2))  # 4 4
print(sqr(1), pow_(1, 1))  # 1 1
print(sqr(0), pow_(0, 0))  # 0 0
print(sqr(1), pow_(1, 1))  # 1 1
print(sqr(2), pow_(2, 2))  # 4 4
