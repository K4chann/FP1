# Desarrolle una función llamada create_tables, que tome dos parámetros. El primer parámetro es una conexión abierta con una base de datos SQLite 3
# y el segundo el nombre de un fichero csv. Cada línea de este fichero tiene información para crear una tabla en la base de datos a la que hace
# referencia la conexión del primer parámetro. El primer valor de cada línea es el nombre de la tabla a crear, y el resto de los valores son parejas
# con los nombres de los campos y sus tipos separados por un espacio; por ejemplo:

# "Pilotos,id INTEGER,Piloto TEXT(20),Escudería TEXT(20),País TEXT(20),Puntos INTEGER,Victorias INTEGER"
# El objetivo de la función create_tables es crear las tablas indicadas en el fichero.

# Nótese que se pasa una conexión abierta con la base de datos, por lo que la función no tendrá que crear una conexión, ni tampoco cerrarla.

# Contenido del módulo main.py
# import db_utils
# import sqlite3
# import dataset_utils

# db = sqlite3.connect("ProductsCustomersAndSupliers")
# db_utils.create_tables(db, "tables.csv")

# for table in dataset_utils.list_tables(db):
#     print(table)

# db.close()

def create_tables(connection, file):

    with open(file, "r") as fr:
        for line in fr:
            line = line.strip().split(",")
            db = connection.cursor()
            db.execute(
                f"CREATE TABLE {line[0]} ({', '.join(line[1:])})"
            )