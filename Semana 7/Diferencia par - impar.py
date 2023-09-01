# Desarrolle una función llamada dif_par_impar que tome como parámetros dos listas de números enteros del mismo tamaño.
# La función debe devolver una tupla de dos números enteros cuyo primer elemento indicará cuántas parejas de elementos
# de las listas pasadas como parámetros tienen suma par, y su segundo elemento indicará cuántas tienen suma impar.
# Una pareja son dos elementos, uno de la primera lista y otro de la segunda, que ocupan la misma posición.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6]
#         b = [2, 3, 5, 8, 2] 
# output: (2, 3)
# --Hay dos parejas con suma par (5 + 3, 6 + 2) y tres con suma impar (3 + 2, 4 + 5, 3 + 8)

# Contenido del módulo main.py
# import number_functions

# numbers1 = [3, 5, 4, 3, 6]
# numbers2 = [2, 3, 5, 8, 2]
# par_impar = number_functions.dif_par_impar(numbers1, numbers2)
# print(par_impar)

def dif_par_impar(ints_list_1, ints_list_2):

    par = 0
    impar = 0

    for index in range(len(ints_list_1)):

        if (ints_list_1[index] + ints_list_2[index]) % 2 == 0:
            par += 1
        else:
            impar += 1
    
    return (par, impar)