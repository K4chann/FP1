# Desarrolle una función llamada normalize que tome como parámetro una string compuesta de palabras y espacios y devuelva una copia
# de la misma string normalizada de forma que no haya espacios ni al principio ni al final y haya solo un espacio entre palabras.

# Contenido del módulo main.py
# import string_utils

# test_string = "    esta    string    se va a     normalizar     "

# print(string_utils.normalize(test_string))
# print("Original :", test_string)
# print("Resultado:", string_utils.normalize(test_string))

import re

def normalize(text):

    return re.sub(r"\s+", " ", text).strip()