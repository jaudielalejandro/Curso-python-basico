# Pedir al usuario que ingrese un número natural
c0 = int(input("Ingresa un número natural: "))

# Verificar que el número sea positivo y mayor que 0
if c0 <= 0:
    print("Debes ingresar un número entero positivo mayor que 0.")
else:
    pasos = 0  # Contador de pasos

    # Bucle while hasta que c0 sea 1
    while c0 != 1:
        if c0 % 2 == 0:  # Si es par
            c0 = c0 // 2
        else:  # Si es impar
            c0 = 3 * c0 + 1

        print(c0)  # Imprimir el valor de c0 en cada paso
        pasos += 1  # Incrementar el contador de pasos

    # Imprimir la cantidad de pasos tomados
    print(f"pasos = {pasos}")
