# Desarrolle una función llamada concat que tome como parámetros una tupla con valores de tipo str y devuelva
# un valor de tipo str que será el resultado de concatenar todos los elementos de la tupla pasada como parámetro,
# en el orden en que aparecen en la misma.

# Por ejemplo:

# Entra: ("¡Hola", ", ", "mundo!")

# Devuelve: "¡Hola, mundo!"

# Contenido del módulo main.py
# import string_utils

# t = ("¡Hola", ", ", "mundo!")
# text = string_utils.concat(t)
# print(text)

def concat(tupla):

    return "".join(tupla)

    # Alternativa
    string = ""

    for item in tupla:
        string += item