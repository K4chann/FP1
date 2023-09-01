# Desarrolle una función llamada load_list, que reciba como parámetro una string que representa el nombre de un fichero de texto.
# Las líneas de este fichero contienen números enteros separados por espacios.
# Por ejemplo:

# 123 24 456 34 899 123
# 1324 5123 123 1
# 123 5 46 2 46 623 745
# 2346  7468 8 967 969
# En el fichero no hay otros caracteres ni líneas vacías.

# La función debe devolver una lista de listas de números enteros tal que cada lista de esta estructura almacene los números de la línea correspondiente
# del fichero, en el mismo orden que se encuentran en dicha línea.

# Contenido del módulo main.py
# import string_utils

# resulting_list = string_utils.load_list("input.txt")
# print(resulting_list)

# Contenido del fichero input.txt
# 123 24 456 34 899 123
# 1324 5123 123 1
# 123 5 46 2 46 623 745
# 2346  7468 8 967 969

def load_list(file_name):
    
    with open(file_name, "r") as fr:
        return [
            [int(num) for num in line.strip().split()]
            for line in fr
        ]