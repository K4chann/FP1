# El presente de indicativo de los verbos regulares de la primera conjugación se conjuga sustituyendo la terminación "ar",
# por las terminaciones "o", "as", "a", "amos", "áis", "an"; por ejemplo:

# cantar: canto, cantas, canta, cantamos, cantáis, cantan

# Desarrolle una función llamada replace_verbs que tome como parámetro un texto y devuelva una copia del texto en la que todas
# las formas conjugadas de verbos regulares de la primera conjugación han sido sustituidas por su infinitivo. Se supone que todas
# las palabras con dichas terminaciones son verbos regulares de la primera conjugación en presente de indicativo.

# Por ejemplo:

# Entra: "Trabajo, Judit canta, vosotros nadáis y ellos bailan"
# Devuelve: "Trabajar, Judit cantar, vosotros nadar y ellos bailar"

# Contenido del módulo main.py
# import string_utils

# test_string = "Trabajo, Judit canta, vosotros nadáis y ellos bailan"

# print(string_utils.replace_verbs(test_string))

import re

def replace_verbs(sentence):

    pattern = r"(o|a|as|áis|amos)\b"

    return re.sub(pattern, "ar", sentence)