# Desarrolle una función llamada initials que tome por parámetro una lista de listas de strings conteniendo nombres propios de personas.
# La función debe devolver una nueva lista de listas de strings que será como la pasada por parámetro, pero sustituyendo cada nombre por su letra inicial.

# Ejemplo:

# input:
# [
#     ['Juan', 'Pedro', 'Sofia', 'Elena'], 
#     ['Octavio', 'Gustavo', 'José', 'Mária', 'Leopoldo'], 
#     ['Francisco', 'Herminia', 'Nauzet'],
#     ['Yaiza', 'Idafen']
# ]
# 4
# output: 
# [

#     ['J', 'P', 'S', 'E'], 
#     ['O', 'G', 'J', 'M', 'L'], 
#     ['F', 'H', 'N'],
#     ['Y', 'I']

# ]

# Contenido del módulo main.py
# import string_utils

# names = [
#     ['Juan', 'Pedro', 'Sofia', 'Elena'],
#     ['Octavio', 'Gustavo', 'José', 'Mária', 'Leopoldo'],
#     ['Francisco', 'Herminia', 'Nauzet'],
#     ['Yaiza', 'Idafen']
# ]
# result = string_utils.initials(names)
# print(result)

def initials(names_matrix):

    return [
        [name[0] for name in row]
        for row in names_matrix
    ]
