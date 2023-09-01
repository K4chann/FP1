# En una base de datos SQLite 3 se tiene una tabla llamada Persons con dos columnas: name y dni. Ambas columnas son de tipo TEXT
# la primera contiene el nombre de una persona y la segunda el número de su DNI (sin letra).

# Desarrolle una función llamada update_dnis, que tome como parámetro una conexión abierta con una base de datos SQLite 3 y
# proceda a actualizar los DNIs de la tabla Persons, completándolos con la letra correspondiente. Para calcular la letra que 
# corresponde a un DNI, se dispone de una función llamada dni_letter, en el módulo string_utils, que recibe como parámetro una
# string con un número de DNI, sin letra, y devuelve la letra que corresponde a ese número.

# Contenido del módulo main.py
# import db_utils
# import sqlite3
# import dataset_utils

# db = sqlite3.connect("PersonsDB")

# dataset_utils.load_dataset(db, "persons.sql")  # Inicializa la DB de prueba
# db_utils.update_dnis(db)

# for row in dataset_utils.get_table_data(db, "Persons"):
#     print(row)

# db.close()

from string_utils import dni_letter

def update_dnis(connection):

    for dni in connection.execute("SELECT dni FROM Persons").fetchall():
        connection.execute(
            f"UPDATE Persons SET dni = '{dni[0]}{dni_letter(dni[0])}'\
            WHERE dni = '{dni[0]}'"
        )