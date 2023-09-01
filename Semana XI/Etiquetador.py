# Desarrolle una función llamada tagger con dos parámetros de tipo string formados solamente por letras mayúsculas y minúsculas, números y espacios.

# La string representada por el segundo parámetro no estará vacía ni tendrá caracteres repetidos.

# La función devolverá una nueva string, que será una copia de la pasada como primer parámetro en la que, a todas las substrings de la string
# pasada como primer parámetro que estén formadas sólo por caracteres contenidos en la string representada por el segundo parámetro y que no
# estén contenidas en una substring mayor de las mismas características, se les habrá añadido por delante la string "[target]" y por detrás la
# string "[endtarget]". 

# >Ejemplo:

# Parámetro 1:

# "alsikjuyZB8we4 aBBe8XAZ piarBq8 Bq84Z "
# Parámetro 2:

# "XYZAB"
# Substrings de máxima longitud formadas sólo por caracteres contenidos en el segundo parámetro:

# "ZB", "BB", "XAZ", "B", "B", "Z"
# El resultado es:

# "alsikjuy[target]ZB[endtarget]8we4 a[target]BB[endtarget]e8[target]XAZ[endtarget] piar[target]B[endtarget]q8 [target]B[endtarget]q84[target]Z[endtarget] "

# Contenido del módulo main.py
# import string_utils

# test_string = "alsikjuyZB8we4 aBBe8XAZ piarBq8 Bq84Z "
# pattern = "XYZAB"

# print(string_utils.tagger(test_string, pattern))

import re

def tagger(tag, pattern):

    return re.sub(
        "([" + pattern + "]+)", "[target]" + r"\1" + "[endtarget]", tag
    )
