# Desarrolle una función llamada sumar_multiplos que tome como parámetros dos listas de números enteros
# del mismo tamaño y un número entero. La función debe devolver un número entero resultante de sumar
# los componentes de todas las parejas de números que ocupen la misma posición en ambas listas que
# cumplan el criterio de que la suma de la pareja es múltiplo del número pasado como tercer parámetro.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6, 8]
#         b = [2, 3, 5, 8, 2, 4]
#         m = 3 
# output: 21
# --Hay dos parejas cuya suma es múltiplo de 3 (4 + 5 = 9, 8 + 4 = 12)

# Contenido del módulo main.py

# import number_functions

# numbers1 = [3, 5, 4, 3, 6, 8]
# numbers2 = [2, 3, 5, 8, 2, 4]
# mul = 3
# suma = number_functions.sumar_multiplos(numbers1, numbers2, mul)
# print(suma)

def sumar_multiplos(ints_list_1, ints_list_2, num):

    output = 0

    for index in range(len(ints_list_1)):

        if (ints_list_1[index] + ints_list_2[index]) % num == 0:
            output += ints_list_1[index] + ints_list_2[index]
    
    return output
