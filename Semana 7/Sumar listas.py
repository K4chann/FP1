# Desarrolle una función llamada sum_lists que tome como parámetros dos listas de números enteros.
# La función debe devolver una nueva lista cuyos elementos serán la suma de los elementos que ocupan
# la misma posición en cada una de las dos listas de entrada. Si alguna de las listas es de menor tamaño
# que la otra, se considerará que los elementos que faltan tienen el valor cero.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6]
#         b = [2, 3, 5]  
# output:     [5, 8, 9, 3, 6]

# Contenido del módulo main.py
# import number_functions

# numbers1 = [1, 3, 4, 7, 8, 3]
# numbers2 = [3, 8, 5]
# sun_numbers = number_functions.sum_lists(numbers1, numbers2)
# print(sun_numbers)

from itertools import zip_longest

def sum_lists(ints_list_1, ints_list_2):

    return [
        num_1 + num_2 for num_1, num_2 in
        zip_longest(ints_list_1, ints_list_2, fillvalue=0)
    ]
