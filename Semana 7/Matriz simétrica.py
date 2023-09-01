# Desarrolle una función llamada symmetrical que tome como parámetro una lista de listas de números enteros que representa una matriz cuadrada.
# La función debe devolver True si la lista pasada como parámetro representa una matriz simétrica, y False si no.
# Una matriz se dice simétrica si es cuadrada y
# a[i][j] == a[j][i]  para todo i, j.

# Ejemplo:

# [
#     [ 3,  5,  4,  3], 
#     [ 5,  7,  5,  8], 
#     [ 4,  5,  5,  0],
#     [ 3,  8,  0,  9],
# ]

# Contenido del módulo main.py
# import matrix_functions

# numbers = [
#     [3,  5,  4,  3],
#     [5,  7,  5,  8],
#     [4,  5,  5,  0],
#     [3,  8,  0,  9]
# ]
# result = matrix_functions.symmetrical(numbers)
# print(result)

def symmetrical(matrix):

    for row in range(len(matrix)):

        for column in range(len(matrix[row])):
            if matrix[row][column] != matrix[column][row]:
                return False
    
    return True

print(symmetrical())