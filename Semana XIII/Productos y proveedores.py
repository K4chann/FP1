# Se tiene una base de datos SQLite 3 con tres tablas:

# Products, que es un listado de productos y tiene dos columnas: id, de tipo INTEGER; y description, de tipo TEXT.
# Suppliers, que es un listado de proveedores de los productos de la tabla anterior y tiene tres columnas: id, de tipo INTEGER;
# name, de tipo TEXT; y city, de tipo TEXT.
# Products_Suppliers, que establece la relación entre los productos y los proveedores que los suministran y tiene tres columnas:
# product_id, que se corresponde con el id del producto en la tabla Products; supplier_id, que se corresponde con el id del proveedor
# en la tabla Suppliers; y price, de tipo REAL, que indica a qué precio suministra el producto ese proveedor.
# Desarrolle una función llamada get_products_for_supplier, que tome como parámetro una conexión abierta con una base de datos SQLite
# 3 y un número entero, correspondiente al identificador de un proveedor, y devuelva una tupla de dos elementos: el primer elemento
# será el nombre del proveedor y el segundo una lista con las descripciones de los productos suministrados por ese proveedor.

# Contenido del módulo main.py
# import db_utils
# import sqlite3
# import dataset_utils

# db = sqlite3.connect("ProductsAndSuppliers")

# dataset_utils.load_dataset(db, "dataset.sql")  # Inicializa la DB de prueba
# products = db_utils.get_products_for_supplier(db, 103)
# print(products)

# db.close()

def get_products_for_supplier(db, num):

    return (
        db.execute(
            f"SELECT name FROM Suppliers WHERE id = '{num}'"
        ).fetchall()[0][0], [
            desc[0] for desc in db.execute(
                f"SELECT description FROM PRODUCTS WHERE id IN\
                (SELECT product_id FROM Products_Suppliers\
                WHERE supplier_id = '{num}')"
            ).fetchall()
        ]
        )