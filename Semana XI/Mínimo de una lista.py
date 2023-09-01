# Desarrolle una función recursiva llamada list_min que tome como parámetro una lista no vacía de números y devuelva el valor menor de
# entre los almacenados en la lista.

# Por ejemplo:

# list_min([12, 23, 34, 45, 67, 89]) -> devuelve 12
# list_min([10, -12, 35, 12, -10])   -> devuelve -12

# Contenido del módulo main.py
# import math_utils

# my_list = [12, 23, 34, 45, 67, 89]
# print(math_utils.list_min(my_list))

def list_min(nums_list: list, minimum = None):

    if not minimum:
        minimum = nums_list[0]
    else:
        if nums_list[0] < minimum:
            minimum = nums_list[0]
    
    nums_list.pop(0)
    return minimum if len(nums_list) == 0 else list_min(nums_list, minimum)