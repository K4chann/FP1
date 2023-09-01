# Desarrolle una función llamada change_sign que tome como parámetro una lista de números enteros.
# La función debe modificar la lista cambiando el signo de todos los números que contiene.

# Ejemplo:

# input:  [ 1, -1, 0,  7, -4]
# output: [-1,  1, 0, -7,  4]

# Contenido del módulo main.py
# import number_functions

# numbers = [1, 4, 7, 8, 3, 10, 12, 13, 14, 15]
# number_functions.change_sign(numbers)
# print(numbers)

def change_sign(ints_list):

    for index in range(len(ints_list)):
        ints_list[index] = - ints_list[index]

