# Se tienen listas conteniendo cada una 12 números que representan los beneficios mensuales de una cierta inversión durante un año natural.

# Desarrolle una función llamada best_semester, que tome por parámetro una lista como las descritas y devuelva un 1 si se han
# tenido más beneficios en la primera mitad del año y un 2 si se han tenido más beneficios en la segunda mitad del año.
# En caso de igualdad, debe devolver un cero

# Ejemplo:

# input: [1000, 200, 300, 200, 120, 100, 200, 300, 200, 120, 400, 500]
# output: 1
# input: [0, 0, 0, 200, 100, 100, 100, 300, 200, 100, 400, 0]
# output: 2

# Contenido del módulo main.py
# import finances

# earnings = [1000, 200, 300, 200, 120, 100, 200, 300, 200, 120, 400, 500]
# best = finances.best_semester(earnings)
# print(best)

def best_semester(profits_list):

    first_half = 0
    second_half = 0

    for index in range(len(profits_list)):
        if index < 6:
            first_half += profits_list[index]
        else:
            second_half += profits_list[index]
    
    return 1 if first_half > second_half else 2