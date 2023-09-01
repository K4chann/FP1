# Desarrolle una función llamada transpose que tome como parámetro una lista de listas de números enteros que representa una matriz.
# La función debe devolver una nueva lista de listas que represente la matriz traspuesta de la pasada como parámetro.
# La traspuesta de una matriz se obtiene cambiando las filas por columnas.

# Ejemplo:

# input: [
#     [3, 5, 4, 3], 
#     [6, 7, 5, 8], 
#     [2, 1, 5, 0]
# ] 
# output:[
#     [3, 6, 2],
#     [5, 7, 1],
#     [4, 5, 5],
#     [3, 8, 0]
# ]

# Contenido del módulo main.py
# import matrix_functions

# numbers = [
#     [1,  3,  4,  7],
#     [8,  3, 10, 12],
#     [3, 14, 15,  0]
# ]
# tansposed = matrix_functions.transpose(numbers)
# print(tansposed)

import numpy


def transpose(matrix):

    return [
        [matrix[column][row] for column in range(len(matrix))]
        for row in range(len(matrix[0]))
    ]

    #Alternativa
    return [
        list(new_row)
        for new_row in zip(*matrix)
    ]

    #Alternativa
    trnasposed_matrix = []
    for row in range(len(matrix[0])):
        new_row = []

        for column in range(len(matrix)):
            new_row.append(matrix[column][row])
        
        transpose_matrix.append(new_row)
    
    return transpose_matrix

# El módulo numpy no es necesario, solo es útil en este caso para visualizar la matriz de una mejor manera.
print(numpy.matrix(transpose([[3, 5, 4, 3], [6, 7, 5, 8], [2, 1, 5, 0]])))