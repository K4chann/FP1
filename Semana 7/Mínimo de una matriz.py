# En matemáticas, una matriz es un cuadro de números o de símbolos algebraicos distribuidos en filas y columnas y dispuestos en forma de rectángulo.
# El siguiente ejemplo muestra una matriz de dimensión 3x5 (3 filas por 5 columnas).

# 12 23 44  8  5
#  6 21 89 12  1
# 10 78 43 12 88
# Se ha ideado representar una matriz como una tupla de tuplas: una tupla cuyos elementos representan cada fila de una matriz en forma de tupla de números:

#   --primera fila--    --segunda fila--    ---tercera fila---
# ((12, 23, 44, 8, 5), (6, 21, 89, 12, 1), (10, 78, 43, 12, 88))
# Desarrolle una función llamada min_of_matrix que tome como parámetro una tupla que representa una matriz en la forma descrita y devuelva el valor 
# mínimo de sus elementos. En el ejemplo anterior, el valor mínimo es el  1 (2ª fila, 5 ª columna de la matriz o posición [1][4]
# de la tupla que la representa).

# Contenido del módulo main.py
# import matrices

# matrix = ((10, 21, 13), (4, 5, 6), (8, 12, 34))
# result = matrices.min_of_matrix(matrix)
# print(result)

def min_of_matrix(matrix):

    return min([min(row) for row in matrix])

    #Alternativa
    minimum = 9 * 99
    for row in matrix:

        for item in row:

            if item < minimum:
                minimum = item
        
        return minimum