# Desarrolle una función llamada first_plus_last, que tome como parámetros una tupla con valores de tipo
# int y devuelva la suma del primer y el último elemento.

# Por ejemplo:

# Entra: (13, 15, 10, 8, 12)

# Devuelve: 25 (12 + 13)

# Contenido del módulo main.py
# import functions

# t = (14, 10, 23, 4, 12)
# result = functions.first_plus_last(t)
# print(result)

def first_plus_last(int_tuple: tuple) -> int:

    return int_tuple[0] + int_tuple[-1]