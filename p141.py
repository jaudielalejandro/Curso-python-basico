#Pregunta 1: Iterador que devuelve vocales
class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Incluye espacio al final
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
