# Un fichero csv (comma-separated values) es un fichero de texto en el que cada línea contiene un conjunto de valores separada por comas.

# Desarrolle una función llamada export_tables, a la que se al pasarle una conexión abierta con una base de datos SQLite 3 y el nombre de
# una tabla de la misma, cree un fichero en formato csv con el mismo nombre que la tabla y extensión .tbl donde se han exportado los registros
# de la tabla: cada registro en una línea, con los valores de los campos separados por comas.

# Contenido del módulo main.py
# import db_utils
# import sqlite3
# import dataset_utils

# # Se ejecuta la función export_tables() con unos datos de prueba

# db = sqlite3.connect("PersonsDB")
# dataset_utils.load_dataset(db, "dataset.sql")  # Inicializa la DB de prueba
# db_utils.export_tables(db, "Persons")
# db.close()

# # Se muestran los resultados de la ejecución

# f = open("Persons.tbl", "r")
# f_content = "".join(f.readlines())
# f.close()
# print(f_content)

def export_tables(db, table):

    with open(f"{table}.tbl", "a") as fw:
        for i in db.execute(f"SELECT * FROM {table}"):
            fw.write(",".join([str(num) for num in i]) + "\n")
