# Desarrolle una función llamada chars_frecs que tome como parámetro una string y devuelva un diccionario con las frecuencias de
# aparición de cada carácter de la string (las claves serán los caracteres y los valores su frecuencia absoluta de aparición, es
# decir, el número de veces que aparecen).

# Ejemplo:
# input:  "Esto es una string de prueba"  
# output:  {'E': 1, 's': 3, 't': 2, 'o': 1, ' ': 5, 'e': 3, 'u': 2, 'n': 2, 'a': 2, 'r': 2, 'i': 1, 'g': 1, 'd': 1, 'p': 1, 'b': 1}

# Contenido del módulo main.py
# import string_utils

# text = "Esto es una string de prueba"
# frecs = string_utils.chars_frecs(text)
# print(frecs)

def chars_frecs(sentence: str):

    return {character: sentence.count(character) for character in sentence}