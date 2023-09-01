# Desarrolle una función recursiva llamada filter_names que tome como parámetros una lista de nombres de persona
# (cada nombre es una palabra que empieza con una letra mayúscula) y una letra mayúscula. La función debe devolver
# una nueva lista conteniendo los nombres de la lista pasada como primer parámetro que empiecen por la letra pasada como segundo parámetro.
# Los nombres en la nueva lista mantendrán el orden que tenían en la original.

# Ejemplo:

# input: ['John', 'Paul', 'Martin', 'Peter', 'Max', 'Mia'] M
# output: ['Martin, 'Max','Mia']
         
# Contenido del módulo main.py
# import string_utils

# names = ['John', 'Paul', 'Martin', 'Peter', 'Max', 'Mia']
# initial = 'M'
# filtered_names = string_utils.filter_names(names, initial)
# print(filtered_names)

def filter_names(names_list: list, initial: str):

    if len(names_list) == 0:
        return []
    elif names_list[0][0] != initial:
        return filter_names(names_list[1:], initial)
    elif names_list[0][0] == initial:
        return [names_list[0]] + filter_names(names_list[1:], initial)