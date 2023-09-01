# Desarrolle una función llamada concat que tome como parámetros dos listas y devuelva una nueva lista que
# al principio y al final tenga los elementos de la primera lista y en medio, los de la segunda, repetidos tres veces.

# Por ejemplo:

# input: [1,2] [3,4,5]
# output: [1,2,3,4,5,3,4,5,3,4,5,1,2]
# input: [] [0,0]
# output: [0,0,0,0,0,0]

# Contenido del módulo main.py
# import functions

# list1 = [1, 2]
# list2 = [3, 4, 5]
# text = functions.concat(list1, list2)
# print(text)

def concat(lista_1, lista_2):
    return lista_1 + lista_2 * 3 + lista_1