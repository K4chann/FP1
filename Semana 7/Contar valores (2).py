# Desarrolle una función llamada count_values que tome como parámetros dos listas de números enteros.
# La función debe modificar la segunda lista sustituyendo cada elemento por una tupla en la que esté
# el elemento original acompañado del número de veces que aparece en la primera lista.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6, 7, 5, 8, 2, 1, 5] b = [2, 3, 5]  
# output: b = [(2, 1), (3, 2), (5, 3)]

# Contenido del módulo main.py
# import number_functions

# numbers = [1, 3, 4, 7, 8, 3, 10, 12, 3, 14, 15]
# counters = [3, 8, 5]
# number_functions.count_values(numbers, counters)
# print(counters)

def count_values(ints_list_1, ints_list_2):

    for index in range(len(ints_list_2)):

        ints_list_2[index] = (
            ints_list_2[index],
            ints_list_1.count(ints_list_2[index])
        )
    
    # Alternativa
    for index in range(len(ints_list_2)):
        counter = 0

        for index in range(len(ints_list_1)):
            if ints_list_1[index] == ints_list_2[index]:
                counter += 1
            
        ints_list_2[index] = (ints_list_2[index], counter)