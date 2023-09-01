# Desarrolle una función recursiva llamada merge que tome como parámetros dos listas ordenadas de números (de menor a mayor)
# y devuelva una nueva lista igualmente ordenada de números que contenga todos los elementos de las dos listas pasadas como
# parámetros, incluyendo posibles repeticiones de valores.

# Por ejemplo:

# 1ª lista: [ 2,  3, 43, 43, 67, 67, 89]
# 2ª lista: [10, 12, 35, 43, 65]

# Resultado: [2, 3, 10, 12, 35, 43, 43, 43, 65, 67, 67, 89]

# Contenido del módulo main.py
# import math_utils

# l1 = [12, 23, 34, 45, 67, 89]
# l2 = [10, 12, 35, 43, 65]
# print(math_utils.merge(l1, l2))

def merge(list_1: list, list_2: list):

    if len(list_1) == 0:
        return list_2.copy()
    elif len(list_2) == 0:
        return list_1.copy()
    elif list_1[0] <= list_2[0]:
        return [list_1[0]] + merge(list_1[1:], list_2)
    else:
        return [list_2[0]] + merge(list_1, list_2[1:])