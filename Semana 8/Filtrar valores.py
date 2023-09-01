# Desarrolle una función llamada filter_values, que tome como parámetros un diccionario de parejas (str:int)
# y dos números enteros. La función debe devolver un nuevo diccionario conteniendo las parejas del diccionario
# pasado como primer parámetro cuyos valores se encuentren en el rango comprendido entre el segundo y tercer parámetro, ambos inclusive.

# Ejemplo:

# input: {'a': 1, 'b': 4, 'c': 7, 'd': 8, 'e': 3, 'f': 10, 'g': 12, 'h': 13, 'i': 14, 'j': 15} 4 10
# output: {'b': 4, 'c': 7, 'd': 8, 'f': 10}
# input: {'a': 0, 'b': 0, 'c': 1, 'd': 18, 'e': 2, 'f':-2} -5 5 
# output: {'a':0, 'b':0, 'c':1, 'e':2, 'f':-2}

# Contenido del módulo main.py
# import number_functions

# numbers = {
#     'a': 1, 'b': 4, 'c': 7, 'd': 8, 'e': 3,
#     'f': 10, 'g': 12, 'h': 13, 'i': 14, 'j': 15
# }
# start = 4
# end = 10
# filtered_numbers = number_functions.filter_values(numbers, start, end)
# print(filtered_numbers)

def filter_values(dictionarie, num_1, num_2):

    return {k: v for k, v in dictionarie.items() if v in range(num_1, num_2 + 1)}
