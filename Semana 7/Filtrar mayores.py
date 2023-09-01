# Desarrolle una función llamada pass_highers que tome como parámetro una lista de listas de números enteros y un número entero.
# La función debe devolver una nueva lista de listas de números enteros que sea como la pasada como primer parámetro,
# pero sin los valores que sean menores que el pasado como segundo parámetro.

# Ejemplo:

# input:
# [
#     [3, 5, 4, 3], 
#     [6, 7, 5, 8, 9], 
#     [2, 1,  5]
#     [2, 3, 1]
#     [8, 3, 2, 4]
# ]
# 4
# output: 
# [
#     [5, 4], 
#     [6, 7, 5, 8, 9], 
#     [5]
#     []
#     [8, 4]
# ]

# Contenido del módulo main.py
# import matrix_functions

# numbers = [
#     [3, 5, 4, 3],
#     [6, 7, 5, 8, 9],
#     [2, 1, 5],
#     [2, 3, 1],
#     [8, 3, 2, 4]
# ]
# threshold = 4
# result = matrix_functions.pass_highers(numbers, threshold)
# print(result)

def pass_highers(ints_matrix, num):

    return [
        [
            column_item for column_item in row if column_item >= num
        ]
        for row in ints_matrix
    ]
