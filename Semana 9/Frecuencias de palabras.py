# Desarrolle una función llamada words_frecs que tome como parámetro una string y devuelva un diccionario con las
# frecuencias de aparición de cada palabra de la string (las claves serán las palabras y los valores su frecuencia
# absoluta de aparición, es decir, el número de veces que aparecen).
# La string pasada como parámetro estará compuesta exclusivamente por palabras separadas por espacios (whitespaces);
# cualquier secuencia de caracteres que no contenga un espacio se considerará una palabra.

# Ejemplo:
# input:  "Esto es una string, no es una lista"
# output:  {'Esto': 1, 'es': 2, 'una': 2, 'string,': 1, 'no': 1, 'lista': 1}

# Contenido del módulo main.py
# import string_utils

# text = "Esto es una string, no es una lista"
# frecs = string_utils.words_frecs(text)
# print(frecs)

def words_frecs(sentence: str):

    words = []
    for word in sentence.split():
        if word not in words:
            words.append(word)
    
    return {word: sentence.count(word) for word in words}