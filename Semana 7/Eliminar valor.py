# Desarrolle una función llamada delete_value que tome como parámetros una lista de números enteros y un número entero.
# La función debe modificar la lista eliminando todas las ocurrencias del número pasado como segundo parámetro.

# Ejemplo:

# input:  [ 1, -1, 0, 7, -4] 1
# output: [ -1, 0, 7, -4]
# Téngase en cuenta que el mecanismo interno del for de Python no prevé que la secuencia iterable cambie de longitud.
    
# Contenido del módulo main.py
# import number_functions

# numbers = [1, 4, 7, 8, 3, 10, 12, 13, 14, 15]
# value = 8
# number_functions.delete_value(numbers, value)
# print(numbers)

def delete_value(ints_list: list, num: int):

    ints_list[:] = [item for item in ints_list if item != num]
