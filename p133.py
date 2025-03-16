class Fib:
    def __init__(self, n):
        print("__init__")
        self.__n = n  # Límite de la serie Fibonacci
        self.__i = 0  # Contador de iteraciones
        self.__p1, self.__p2 = 0, 1  # Variables para almacenar los valores anteriores
    
    def __iter__(self):
        print("__iter__")
        return self  # Devuelve el objeto iterador
    
    def __next__(self):
        print("__next__")
        if self.__i >= self.__n:  # Condición de parada
            raise StopIteration
        
        if self.__i == 0:
            self.__i += 1
            return 1
        
        value = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, value
        self.__i += 1
        return value

class Class:
    def __init__(self, n):
        self.fib = Fib(n)  # Instanciamos el iterador dentro de la clase
    
    def __iter__(self):
        return self.fib  # Retornamos el iterador cuando se invoca __iter__

# Uso del iterador en un bucle for
for num in Class(10):
    print(num)
