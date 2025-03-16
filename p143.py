def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement

stars = replace_spaces()
print(stars("And Now for Something Completely Different"))  # Salida esperada: "And*Now*for*Something*Completely*Different"

# Ejemplo de PEP 8 sobre lambdas vs. def
# Recomendado:
def f(x): return 3*x

# No recomendado:
f_lambda = lambda x: 3*x  # Aunque válido, no es la mejor práctica según PEP 8
