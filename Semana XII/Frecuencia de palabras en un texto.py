# Un fichero csv (comma-separated values) es un fichero de texto en el que cada línea contiene un conjunto de valores separada por comas.

# Desarrolle una función llamada words_frec, que reciba como parámetros dos strings. La primera string es el nombre de un fichero de
# texto conteniendo palabras y otros elementos (fechas, números, códigos, ...) separados por espacios. La función debe contar el número
# de apariciones de cada palabra del texto del primer fichero y crear un fichero csv en el que cada línea contenga una palabra y el número
# de veces que aparece, separados por comas. Las líneas del fichero csv estarán ordenadas en orden ascendente según las palabras.

# A efectos del problema, una palabra es una letra mayúscula o minúscula que puede ir seguida por una secuencia de letras minúsculas.
# A efectos de conteo, no se diferenciará entre mayúsculas y minúsculas.

# Las palabras en el fichero csv estarán normalizadas en minúsculas.

# Ejemplo:

# Fichero de entrada

# En el año 2007 Juan
# tenía 25 años 
# Trabajaba en la UNED
# Fichero csv

# año,1
# años,1
# el,1
# en,2
# juan,1
# la,1
# tenía,1
# trabajaba,1

# Contenido del módulo main.py
# import file_utils
# import string_utils

# string_utils.words_frec("input.txt", "output.csv")
# file_utils.show_file("output.csv")

# Contenido del fichero input.txt
# En el año 2007 Juan
# tenía 25 años 
# Trabajaba en la UNED

import re

def words_frec(file_name, output_file):

    pattern = r"\b[A-Za-zÁÉÍÓÚáéíóú][a-zñáéíóú]*\b"

    with open(file_name, "r") as fr, open(output_file, "w") as fw:
        words = dict()

        for line in fr:

            for word in re.findall(pattern, line.strip()):
                if word.lower() not in words.keys():
                    words[word.lower()] = "1"
                else:
                    words[word] = str(int(words[word]) + 1)
        
        for item in sorted(words.items()):
            print(",".join(item), file=fw)

words_frec("input.txt", "output.csv")