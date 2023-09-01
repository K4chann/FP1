# Desarrolle una función llamada maxs que tome como parámetros dos listas de números enteros positivos.
# La función debe devolver una nueva lista en la que cada uno de cuyos elementos será el mayor de los
# elementos que ocupan la misma posición en cada una de las dos listas de entrada. Si alguna de las
# listas es de menor tamaño que la otra, se considerará que los elementos que faltan tienen el valor -1.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6]
#         b = [2, 3, 5]  
# output:     [3, 5, 5, 3, 6]

# Contenido del módulo main.py
# import number_functions

# numbers1 = [1, 3, 4, 7, 8, 3]
# numbers2 = [3, 8, 5]
# sum_numbers = number_functions.maxs(numbers1, numbers2)
# print(sum_numbers)

from itertools import zip_longest


def maxs(ints_list_1, ints_list_2):
    
    return [
        max(num_1, num_2) for num_1, num_2 in
        zip_longest(ints_list_1, ints_list_2, fillvalue=-1)
    ]