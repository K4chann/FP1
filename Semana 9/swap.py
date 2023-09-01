# Desarrolle una función llamada swap que admita como parámetro una string y devuelva una nueva string que contenga
# las mismas palabras que la pasada por parámetro, en orden inverso, separadas por un único espacio y con la inicial
# de cada palabra en mayúscula y el resto en minúscula. La string pasada como parámetro sólo contiene palabras y espacios.

# Ejemplo:
# print(swap("esto es una STRING de prueba"))

# RESULTADO:
# Prueba De String Una Es Esto⏎

# Contenido del módulo main.py
# import string_utils

# print(string_utils.swap("esto es una STRING de prueba"))

def swap(sentence: str):

    return sentence[::-1].title()