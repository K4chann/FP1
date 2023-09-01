# Desarrolle una función llamada sum_columns que tome como parámetro una lista de listas de números enteros que representa una matriz.
# La función debe devolver una nueva lista de enteros que represente la suma por columnas de los elementos de la matriz pasada como parámetro.

# Ejemplo:

# input: [
#         [ 3,  5,  4,  3], 
#         [ 6,  7,  5,  8], 
#         [ 2,  1,  5,  0]
# ]     + ----------------
# output: [11, 13, 14, 11]

# Contenido del módulo main.py
# import matrix_functions

# numbers = [
#     [1,  3,  4,  7],
#     [8,  3, 10, 12],
#     [3, 14, 15,  0]
# ]
# result = matrix_functions.sum_columns(numbers)
# print(result)

def sum_columns(matrix):

    return [sum(column) for column in zip(*matrix)]

    #Alternativa

    to_return = []
    for row in range(len(matrix[0])):

        suma = 0
        for column in range(len(matrix)):
            suma += matrix[column][row]
        
        to_return.append(suma)
    
    return to_return
