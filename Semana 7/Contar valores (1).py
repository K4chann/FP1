# Desarrolle una función llamada count_values que tome como parámetros dos listas de números enteros.
# La función debe devolver una nueva lista, del mismo tamaño que la segunda.
# Cada elemento de la nueva lista indicará el número de veces que el elemento correspondiente de la segunda lista aparece en la primera.

# Ejemplo:

# input:  a = [3, 5, 4, 3, 6, 7, 5, 8, 2, 1, 5] b = [2, 3, 5]  
# output: [1, 2, 3]

# Contenido del módulo main.py
# import number_functions

# numbers = [1, 3, 4, 7, 8, 3, 10, 12, 3, 14, 15]
# counters = [3, 8, 5]
# res = number_functions.count_values(numbers, counters)
# print(res)

def count_values(ints_list_1: list, ints_list_2: list):

    return [ints_list_1.count(num) for num in ints_list_2]

    #Alternativa
    to_return = []

    for num_1 in ints_list_2:
        counter = 0

        for num_2 in ints_list_1:
            if num_2 == num_1:
                counter += 1
        
        to_return.append(counter)
    
    return to_return