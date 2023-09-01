# Desarrolle una función recursiva llamada sum_lists que tome como parámetros dos listas de números enteros de la misma longitud.
# La función debe devolver una nueva lista cuyos elementos serán la suma de los elementos que ocupan la misma posición en cada una
# de las dos listas de entrada.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6]
#         b = [2, 3, 5, 6, 2]  

# output:     [5, 8, 9, 9, 8]

# Contenido del módulo main.py
# import number_functions

# numbers1 = [3, 5, 4, 3, 6]
# numbers2 = [2, 3, 5, 6, 2]
# sun_numbers = number_functions.sum_lists(numbers1, numbers2)
# print(sun_numbers)

def sum_lists(list_1, list_2):

    return [list_1[0] + list_2[0]] if len(list_1) == 0\
        else sum_lists(list_1[1:], list_2[1:])