# Ejemplo de iterador
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        value = self.counter
        self.counter += 1
        return value

# Uso del iterador
for num in MyIterator(5):
    print(num)

# Ejemplo de yield (generador)
def my_generator(n):
    for i in range(n):
        yield i

# Uso del generador
for num in my_generator(5):
    print(num)

# Ejemplo de expresión condicional
print(True if 0 >= 0 else False)

# Lista por comprensión convertida en generador
for x in (el * 2 for el in range(5)):
    print(x)

# Ejemplo de función lambda
print((lambda x: x ** 0.5)(9))

def foo(x, f):
    return f(x)

print(foo(9, lambda x: x ** 0.5))

# Ejemplo de map()
short_list = ['mython', 'python', 'cayó', 'en', 'el', 'piso']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

# Ejemplo de filter()
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

# Ejemplo de cierre (closure)
def tag(tg):
    tg2 = tg[0] + '/' + tg[1:]
    
    def inner(str):
        return tg + str + tg2
    return inner

b_tag = tag('<b>')
print(b_tag('Monty Python'))
