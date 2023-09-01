# Se ha usado una base de datos SQLite 3 para representar un diccionario multilingüe. La base de datos está formada por varia tablas, una por cada lenguaje contemplado. Los nombres de las tablas están formados por el prefijo "lang_" seguido del código de dos letras que representa el lenguaje;

# por ejemplo:

# lang_es - español
# lang_en - inglés
# lang_fr - francés
# Cada tabla está formada por dos columnas:
# id, de tipo INTEGER, es un código de identificación de palabra.
# word, de tipo TEXT, una palabra en el idioma de la tabla.
# Las versiones de una palabra en los diferentes lenguajes tendrán el mismo código de identificación, lo que permite establecer la relación entre ellas.
# Desarrolle, en el módulo db_utils, una función llamada translate, para obtener la traducción de una palabra de un idioma a otro, con cuatro parámetros,
# en el orden indicado:

# Una conexión abierta con la base de datos,
# La palabra a traducir,
# El código de dos letras del lenguaje origen y
# El código de dos letras del lenguaje destino.
# La función devolverá la palabra en el lenguaje destino que corresponda con la palabra a traducir. En caso de que esta no se encuentre en la tabla del
# lenguaje origen, se devolverá el valor entero -1. Si sí se encuentra, pero no se encuentra su correspondiente en el lenguaje destino, se devolverá el
# valor entero -2.

# Contenido del módulo main.py
# import db_utils
# import sqlite3
# import dataset_utils

# db = sqlite3.connect("Languages")

# dataset_utils.load_dataset(db, "dataset1.sql")  # Inicializa la DB de prueba
# translated = db_utils.translate(db, "capacidad", "es", "en")
# print(translated)
# translated = db_utils.translate(db, "never", "en", "es")
# print(translated)
# translated = db_utils.translate(db, "nevar", "en", "es")
# print(translated)
# translated = db_utils.translate(db, "dentro", "es", "fr")
# print(translated)

# db.close()

def translate(db, word_tl, cod_o, cod_des):

    id = db.execute(f"SELECT id FROM lang_{cod_o}\
    WHERE word = '{word_tl}'").fetchall()
    if len(id) == 0:
        return -1

    tsl = db.execute(f"SELECT word FROM lang_{cod_des}\
    WHERE id = '{id[0][0]}'").fetchall()
    return tsl[0][0] if len(tsl) != 0 else -2
