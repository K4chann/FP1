# Desarrolle una función llamada vector_sum, que tome como parámetros dos vectores tridimensionales y devuelva el vector suma de los mismos.

# Un vector tridimensional se representa mediante una tupla de tres números reales, que representan la proyección del vector sobre los ejes xyz.
# La suma de dos vectores es un nuevo vector en el que cada elemento es la suma de los elementos correspondientes de los sumandos.

# Por ejemplo:

# (3.0, 8.0, 1.0) + (2.0, -5.0, 4.0) = (5.0, 3.0, 5.0)

# Contenido del módulo main.py
# import vectors

# vector1 = (1, 2, 3)
# vector2 = (4, 5, 6)
# result = vectors.vector_sum(vector1, vector2)
# print(result)

def vector_sum(vector_1, vector_2):

    return (
        vector_1[0] + vector_2[0],
        vector_1[1] + vector_2[1],
        vector_1[2] + vector_2[2]
    )