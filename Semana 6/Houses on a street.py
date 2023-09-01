# Se dispone de listas que contienen, cada una, las alturas (número de pisos) de los distintos edificios de una calle.

# Desarrolle una función llamada house_position, que tome como parámetros una de dichas listas y un número entero.
# La función debe devolver la posición del primer edificio que tenga el número de pisos indicado por el segundo parámetro.
# En caso de que no haya ninguno con el número de pisos indicado, deberá devolver el valor None.

# Por ejemplo:

# input: [1, 1, 3, 2, 1, 2] 3
# output: 2
# input: [1, 1, 3, 2, 1, 2] 5
# output: None

# Contenido del módulo main.py
# import functions

# houses = [1, 1, 3, 2, 1, 0, 2]
# search_for = 3
# found = functions.house_position(houses, search_for)
# print("La primera casa con", search_for, "pisos, está en la posición", found)

def house_posititon(houses_list, num):

    for index, house_floors in enumerate(houses_list):
        if house_floors == num:
            return index
    
    return None
