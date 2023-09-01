# Desarrolle una función llamada pack que tome como parámetros dos listas de números enteros.
# La función debe devolver una nueva lista, cada uno de cuyos elementos será una tupla formada por
# los elementos que ocupan la misma posición en cada una de las dos listas de entrada
# (primero el de la primera y luego el de la segunda). Se supone que las dos listas son del
# mismo tamaño y no están vacías. El problema debe resolverse sin usar, ni referirse para nada, las funciones zip() o zip_longest().

# Ejemplo:

# input:  a = [3, 5, 4,]
#         b = [2, 3, 5]  
# output:     [(3, 2), (5, 3), (4, 5)]

# Contenido del módulo main.py
# import number_functions

# numbers1 = [1, 3, 4]
# numbers2 = [3, 8, 5]
# result = number_functions.pack(numbers1, numbers2)
# print(result)

def pack(ints_list_1, ints_list_2):

    return [
        (ints_list_1[index], ints_list_2[index])
        for index in range(len(ints_list_1))
    ]
