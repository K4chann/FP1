# Considérense listas de números enteros que contienen alturas (en centímetros) de jugadores de baloncesto. Las listas no están vacías.

# Desarrolle una función llamada smallest, que tome como parámetro una lista como las descritas y devuelva una
# tupla con la altura y el índice en la lista del jugador más pequeño. Caso de haber varios jugadores que tengan
# la altura mínima se devolverá el índice del que aparezca antes en la lista.

# Por ejemplo:

# input: [175,175,205,175,167] 
# output: (167, 4)
# input: [205,178,178,201]
# output: (178, 1)
# input: [185]
# output: (185, 0)

# Contenido del módulo main.py
# import functions

# heights = [188, 198, 199, 1855, 196, 184, 197, 184, 210]
# data = functions.smallest(heights)
# print(
#     "El jugador más pequeño mide",
#     data[0],
#     "centímetros y está en la posición",
#     data[1]
# )

def smallest(measures_list: list):

    smallest_player = min(measures_list)
    return (smallest_player, measures_list.index(smallest_player))

    # Alternativa

    smallest_player = (9 * 99, 9 * 99)

    for index in range(len(measures_list)):
        if measures_list[index] < smallest_player[0]:
            smallest_player = (measures_list[index], index)
    
    return smallest_player

    # Alternativa

    smallest_player = (9 * 99, 9 * 99)

    for item in enumerate(measures_list):
        if item[1] < smallest_player[0]:
            smallest_player = item[::-1]
    
    return smallest_player