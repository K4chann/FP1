# Desarrolle una función llamada longest_word que admita por parámetro una string y devuelva otra string cuyo contenido
# será la palabra más larga de la string pasada. En caso de que haya más de una palabra con la longitud máxima, debe
# devolverse la última de ellas.

# Ejemplo:
# longest_word("El policía alto dio el alto al ladrón maniático")

# RESULTADO: "maniático"

# Contenido del módolu main.py
# import string_utils

# print(
#     string_utils.longest_word(
#         "El policía alto dio el alto al ladrón maniático"
#     )
# )

def longest_word(sentence):

    return max(sentence.split(), key=len)