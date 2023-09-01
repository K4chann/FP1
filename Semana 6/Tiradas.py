# Considérense listas que contienen, cada una de ellas, los resultados de una secuencia de tiradas de un dado.

# Desarrolle una función llamada dice_freqs, que tome como parámetro una lista como las descritas y devuelva una
# lista de 6 elementos conteniendo la frecuencia de aparición de los números del 1 al 6, en este orden.

# Ejemplos:

# input: [4, 2, 3, 1, 4, 4, 4, 4, 6, 1, 5, 5] 
# output: [2, 1, 1, 5, 2, 1] 
# input: [1, 2, 2, 6, 3, 1, 6]
# output: [2, 2, 1, 0, 0, 2]
# input: [3]
# output: [0, 0, 1, 0, 0, 0]

# Contenido del módulo main.py
# import functions

# throws = [4, 2, 3, 1, 4, 4, 4, 4, 6, 1, 5, 5]
# frecs = functions.dice_freqs(throws)
# print(frecs)

def dice_freqs(secs_list):

    return [secs_list.count(index) for index in range(1, 7)]