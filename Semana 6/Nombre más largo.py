# Se tienen listas de nombres de personas.

# Desarrolle una función llamada longest que tome como parámetro una lista como las descritas y devuelva la longitud del nombre más largo.

# Por ejemplo:

# input: ['John', 'Paul', 'Christopher', 'Peter'] 
# output: 11
# input: ['Max', 'Kate', 'Fred']
# output: 4
# input: ['Steven']
# output: 6

# Contenido del módulo main.py
# import functions

# names = ['John', 'Paul', 'Christopher', 'Peter']
# length = functions.longest(names)
# print("El nombre más largo tiene longitud", length)

def longest(names_list):

    return max(names_list, key=len)

    # Alternativa

    longest = 0

    for name in names_list:
        if len(name) > longes:
            longest = len(name)

    return longest