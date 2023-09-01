# Un fichero csv (comma-separated values) es un fichero de texto en el que cada línea contiene una serie de valores separados por comas.

# Un diptongo está formado por una vocal fuerte (‘a’, ‘e’ u ‘o’), con o sin acentuar, seguida de una vocal débil (‘i’ o ‘u’) sin acentuar,
# o por una vocal débil sin acentuar seguida de una vocal fuerte, con o sin acentuar. Entre la vocal débil y la fuerte puede haber una ‘h’.
# Una palabra en minúscula que contenga un diptongo (por ejemplo "agua") se adecuará al siguiente esquema:

# Desarrolle una función llamada d_words, que reciba como parámetros dos strings. La primera string es el nombre de un fichero de texto.
# La función debe encontrar en el texto las palabras en minúscula que contengan diptongo y crear un fichero csv usando como nombre la string
# pasada como segundo parámetro.

# Cada línea del fichero de salida contendrá, separados por comas, elementos con información sobre las sucesivas palabras con diptongo
# encontradas en la correspondiente línea del fichero de entrada; elementos formados por la palabra en sí separada por dos puntos del
# índice de su posición en la línea. Por ejemplo:

# Una línea del texto:
# 012345678901234567890123456789012345678901234567890
# "El agua es una palabra y tiene diptongo, repito agua"
# Correspondiendte línea csv: 
# "agua:3,tiene:25,agua:48"

# Contenido del módulo main.py
# import file_utils
# import string_utils

# string_utils.d_words("input.txt", "output.csv")
# file_utils.show_file("output.csv")

# Contenido del fichero input.txt
# agua tiene diptongo y perro no lo tiene
# otras palabra con diptongo son aurora y europa
# también lo es también

import re

def d_word(file_name, output_name):

    pattern = r"\b[a-z]*([aeoáéó]h?[iu]|[iu]h?[aeoáéó])[a-z]*\b"
    with open(file_name, "r") as fr, open(output_name, "w") as fw:
        for line in fr:
            diptongos = []
            for word in re.finditer(pattern, line):
                diptongos.append(f"{word.group(0)}:{word.start()}")
            fw.write(",".join(diptongos) + "\n")
