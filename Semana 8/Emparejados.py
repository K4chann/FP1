# Desarrolle una función llamada emparejados, que tome como parámetros tres conjuntos y devuelva un nuevo conjunto que contenga
# los elementos que pertenezcan a dos cualquiera de los tres conjuntos pasados como parámetros, pero no a los tres.

# Ejemplo:

# input:  a = {3, 5, 4, 6}
#         b = {2, 3, 5}
#         c = {3, 8, 6}  
# output:     {5, 6}

# Contenido del módulo main.py
# from functions import emparejados

# set1 = {3, 5, 4, 6}
# set2 = {2, 3, 5}
# set3 = {3, 8, 6}

# print(emparejados(set1, set2, set3))

def emparejados(set_1, set_2, set_3):

    return (
        (set_1 & set_2)
        (set_1 & set_3)
        (set_2 & set_3)
    ) - (set_1 & set_2 & set_3)