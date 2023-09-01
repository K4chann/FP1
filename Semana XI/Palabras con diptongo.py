# Un diptongo está formado por una vocal fuerte («a», «e» u «o»), con o sin acentuar, seguida de una vocal débil («i» o «u»); o por una vocal débil
# sin acentuar seguida de una vocal fuerte, con o sin acentuar. Entre una y otra de tales vocales puede haber una «h». Asumimos que una palabra en
# minúscula que contenga un diptongo (por ejemplo, «agua») debe seguir el siguiente esquema:

# Palabras con diptongo

# Desarrolle una función llamada d_words que tome como parámetro un string y devuelva una lista de las palabras en minúscula con diptongo que contiene.
# Las palabras en la lista estarán en el orden en que aparecen en la string. En caso de palabras repetidas, se tendrá en cuenta sólo su primera aparición.

# Contenido del módulo main.py 
# import string_utils

# test_string = "agua tiene diptongo y perro no lo tiene"
# print(string_utils.d_words(test_string))

import re

def d_words(text):

    pattern = r"\b([a-z]*([aeoáéó]h?[iu]|[iu]h?[aeoáéó])[a-z]*)\b"
    lista = []

    for item in re.finditer(pattern, text):
        if item.group(0) not in lista:
            lista.append(item.group(0))

    return lista

    #Alternativa
    return list(
        set([item[0] for item in re.findall(pattern, text)])
    )