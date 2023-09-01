# Como resultado del análisis de un lote de equipos informáticos que funcionaban mal, se obtuvieron dos conjuntos de códigos de
# identificación de equipos; el primero con códigos de equipos a los que les fallaba el disco duro, y el segundo con códigos de
# equipos a los que les fallaba la placa base. A algunos equipos les fallaban ambos elementos.

# Escriba una función llamada fallo_HD a la que se le pasen los dos conjuntos citados, en el orden descrito, y
# devuelva un nuevo conjunto con los identificadores de los equipos a los que solo les falla el disco duro.

# Contenido del módulo main.py
# from functions import fallo_HD

# set1 = {"PC001", "PC003", "PC005", "PC011"}
# set2 = {"PC001", "PC005"}

# print(fallo_HD(set1, set2))

def fallo_HD(disk_set, board_set):

    return (disk_set - board_set)