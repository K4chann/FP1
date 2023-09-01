# Se tienen listas conteniendo nombres de chicos y chicas de forma que en los índices pares siempre hay nombres de chicas y, en los impares, de chicos.

# Desarrolle una función llamada filter_names, que tome por parámetro una lista como las descritas y un número entero.

# Si el número pasado como segundo parámetro es par, la función debe devolver una nueva lista con todos los nombres de
# chicas en el mismo orden que en la lista original.

# Si el número pasado como segundo parámetro es impar, la función debe devolver una nueva lista con todos los nombres de
# chicos en el mismo orden que en la lista original.

# Ejemplo:

# input: ['Anna','Peter','Martha','John','Andrea','Mike'] 2
# output: ['Anna','Martha','Andrea']
# input: ['Anna','Peter','Martha','John','Andrea','Mike'] 1
# output: ['Peter','John','Mike']

# Contenido del módulo main.py
# import string_utils

# names = ['Anna', 'Peter', 'Martha', 'John', 'Andrea', 'Mike']
# opt = 1
# filtered_names = string_utils.filter_names(names, opt)
# print(filtered_names)

def filter_names(names_list, num):

    return [
        names_list[index] for index in range(len(names_list))
        if (index % 2 == 0 if num == 2 else index % 2 != 0)
    ]