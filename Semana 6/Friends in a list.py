# Desarrolle una función llamada is_friend que tome como parámetros una lista de nombres y un nombre.
# La función debe devolver True si el nombre pasado como segundo parámetro está en la lista pasada como primer parámetro.

# Por ejemplo:

# input: ['Michael', 'George', 'Martin', 'Peter', 'Mathew', 'John', 'Paul'], George
# output: True
# input: ['Michael', 'George', 'Martin', 'Peter', 'Mathew', 'John', 'Paul'], Sophia
# output: False

# Contenido del módulo main.py
# import functions

# friends = ['Michael', 'George', 'Martin', 'Peter', 'Mathew', 'John', 'Paul']
# person = input("Dame un nombre: ")
# if functions.is_friend(friends, person):
#     print("Sí")
# else:
#     print("No")

def is_friend(names_list, name):
    return name in names_list

    # Alternativa
    for item in names_list:
        if item == name:
            return True
    
    return False

    # Alternativa
    if name in names_list:
        return True
    else:
        return False