while True:  # Bucle infinito hasta que el usuario escriba "chupacabra"
    palabra = input("Ingresa una palabra: ")
    
    if palabra.lower() == "chupacabra":  # Verificamos si la palabra es "chupacabra"
        print("Has dejado el bucle con éxito.")
        break  # Se rompe el bucle cuando se ingresa la palabra secreta
