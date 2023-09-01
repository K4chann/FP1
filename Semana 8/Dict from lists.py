# Desarrolle una función llamada join_lists, que tome como parámetros dos listas de números enteros.
# La función debe devolver un diccionario con tantos elementos como la lista más corta, cuyas claves
# sean los valores de la primera lista, y cuyos valores sean los elementos correspondientes de la segunda lista.
# Se supone que en la primera lista no hay valores repetidos.

# Ejemplo:

# input:  a = [3, 5, 4, 6]
#         b = [2, 3, 5]  
# output:     {3: 2, 5: 3, 4: 5}

# Contenido del módulo main.py
# import number_functions

# numbers1 = [1, 3, 4, 7, 8]
# numbers2 = [3, 8, 5]
# sun_numbers = number_functions.join_lists(numbers1, numbers2)
# print(sun_numbers)

def join_lists(ints_list_1, ints_list_2):

    return {k: v for k, v in zip(ints_list_1, ints_list_2)}
