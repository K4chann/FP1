# Desarrolle una función llamada filter_numbers, que tome como parámetros una lista de números enteros y dos números enteros.
# La función debe devolver una nueva lista conteniendo los números de la lista pasada como primer parámetro cuyos valores se
# encuentren en el rango comprendido entre el segundo y tercer parámetro, ambos inclusive.

# Ejemplo:

# input: [1, 4, 7, 8, 3, 10, 12, 13, 14, 15] 4 10
# output: [4, 7, 8, 10] 
# input: [0, 0, 1, 18, 2, -2] -5 5 
# output: [0, 0, 1, 2, -2]

# Contenido del módilo main.py
# import number_functions

# numbers = [1, 4, 7, 8, 3, 10, 12, 13, 14, 15]
# start = 4
# end = 10
# filtered_numbers = number_functions.filter_numbers(numbers, start, end)
# print(filtered_numbers)

def filter_numbers(ints_list, int_1, int_2):

    return [
        num for num in ints_list
        if num >= int_1 and num <= int_2
    ]
