# Un diptongo está formado por una vocal fuerte (‘a’, ‘e’, u ‘o’), con o sin acentuar, seguida de una vocal débil (‘i’ o ‘u’), o por una vocal
# débil sin acentuar seguida de una vocal fuerte, con o sin acentuar. Entre la vocal débil y la fuerte puede haber una ‘h’. Una palabra en
# minúscula que contiene un diptongo (por ejemplo, "agua") sigue el siguiente esquema:

# Diptongo

# Desarrolle una función llamada d_words, que reciba como parámetros una conexión abierta con una base de datos SQLite 3 y dos strings.
# La primera string es el nombre de un fichero de texto. La función debe encontrar en el texto las palabras en minúscula que contengan
# diptongos y crear, en la base de datos referida por el primer parámetro, una tabla en la que almacenará información sobre cada palabra que encuentre.
# El nombre de la tabla será la string pasada como tercer parámetro y deberá tener las siguientes columnas, en el orden indicado:

# line: de tipo integer, nº de línea en que se ha encontrado esta palabra (la primera línea se numera como 1)
# word: de tipo text, palabra encontrada
# start: de tipo integer, índice dentro de la línea en la que se ha encontrado la palabra

# Contenido del módulo main.py 
# import db_utils
# import sqlite3
# import dataset_utils

# db = sqlite3.connect("WordsDB")
# db_utils.d_words(db, "text.txt", "d_words")


# for row in dataset_utils.get_table_data(db, "d_words"):
#     print(row)

# db.close()

import re


def d_words(db, file, table):

    pattern = r"(\b[a-z]*([aeoáéó]h?[iu]|[iu]h?[aeoáéó])[a-z]*\b)"
    db.execute(
        f"CREATE TABLE IF NOT EXISTS {table}\
        (line INTEGER, word TEXT, start INTEGER)"
    )

    with open(file, "r") as fr:
        for i, line in enumerate([line.strip() for line in fr], start=1):
            for match in re.finditer(pattern, line):
                db.execute(
                    f"INSERT INTO {table}\
                    VALUES({i}, '{match.group(0)}', {match.start()})"
                )
