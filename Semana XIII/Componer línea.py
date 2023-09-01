# En una base de datos SQLite 3 se tiene una tabla llamada text, que se ha usado para almacenar un texto, convenientemente descompuesto para
# su almacenamiento en la tabla, constando de los siguientes campos:

# line: de tipo INTEGER, representa un número de línea del texto.
# word: de tipo TEXT, representa una palabra que está en la línea del texto representada por line.
# pos: de tipo INTEGER, representa la posición ordinal de la palabra representada por word en línea representada por line.

# Contenido del módulo main.py
# import sqlite3
# import dataset_utils
# import db_utils

# db = sqlite3.connect("TextsDataDB")
# dataset_utils.load_dataset(db, "dataset.sql")  # Inicializa la DB de prueba

# for line_num in range(1, 4):
#     line_text = db_utils.get_line(db, line_num)
#     print(line_num, "->", line_text)

# db.close()

def get_line(db, num):

    return " ".join(
        [
            w[0] for w in db.execute(
                f"SELECT word FROM text WHERE line = '{num}' ORDER BY pos"
            ).fetchall()
        ]
    )
