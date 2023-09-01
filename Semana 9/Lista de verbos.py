# El presente de indicativo de los verbos regulares de la primera conjugación se conjuga sustituyendo la terminación "ar",
# por las terminaciones "o", "as", "a", "amos", "áis", "an"; por ejemplo:

# cantar: canto, cantas, canta, cantamos, cantáis, cantan

# Desarrolle una función llamada verbs que tome como parámetro un texto y devuelva una lista con todas las formas conjugadas
# que encuentre, en orden de aparición (si están repetidas en el texto, se repiten en la lista). Se supone que todas las
# palabras que tienen una de tales terminaciones corresponden a verbos regulares de la primera conjugación en presente de indicativo.

# Por ejemplo:

# Entra: "Trabajo, Judit canta, vosotros nadáis y ellos bailan"
# Devuelve: ['Trabajo', 'canta', 'nadáis', 'bailan']

# Contenido del módulo main.py
# import string_utils

# test_string = "Trabajo, Judit canta, vosotros nadáis y ellos bailan"

# print(string_utils.verbs(test_string))

import re

def verbs(sentence):

    pattern = r"(\w+(o|as|a|amos|áis|an)\b)"

    return [group[0] for group in re.findall(pattern, sentence)]