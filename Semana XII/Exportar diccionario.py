# Un fichero csv (comma-separated values) es un fichero de texto en el que cada línea contiene un conjunto de valores separada por comas.

# Desarrolle una función llamada export_dict, que reciba como parámetros un diccionario y una string. Las claves del diccionario serán
# strings y los valores tuplas de números enteros. La función debe crear un fichero csv usando como nombre la string pasada como segundo
# parámetro y usarlo para guardar el diccionario en formato csv: en cada línea del fichero habrá una clave del diccionario seguida de los
# números que forman su tupla de valores, todos separados por comas.

# Las líneas del fichero estarán ordenadas de mayor a menor por el valor de las claves. Recuerde que hay una forma de obtener una list
# ordenada de los componentes de un diccionario (ver Diccionarios). Ejemplo:

# Diccionario:

# {"agua": (30, 10, 8), "pescado": (32, 78), "arroz": (50, 25, 12)}
# Fichero:

# agua,30,10,8
# arroz,50,25,12
# pescado,32,78

# Contenido del módulo main.py
# import file_utils
# import string_utils

# test_dict = {"agua": (30, 10, 8), "pescado": (32, 78), "arroz": (50, 25, 12)}
# string_utils.export_dict(test_dict, "output.csv")
# file_utils.show_file("output.csv")

def export_dict(dictionarie: dict, string: str):

    with open(f"{string}.csv", mode="w", encoding="utf-8") as fw:
        for key, value in dictionarie.items():
            print(key + "," + ",".join(value), file=fw)