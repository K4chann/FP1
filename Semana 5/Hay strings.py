# Desarrolle una función llamada contains_strs que tome como parámetro una tupla con valores de diferentes tipos.
# La función debe devolver True, si algún elemento de la tupla es de tipo str, o False, si no hay ningún elemento de tipo str en la tupla.

# Por ejemplo:

# Entra: (10,  "Pedro", 42, "Margarita", 18.5, 8)

# Devuelve: True

# Nota: recuerde que la función type() devuelve el tipo de un objeto.

# Contenido del módulo main.py
# import functions

# t = (10,  "Pedro", 42, "Margarita", 18.5, 8)

# if functions.contains_strs(t):
#     print("Hay al menos una string en la tupla", t)
# else:
#     print("No hay ninguna string en la tupla", t)

def contains_strs(tupla):

    for item in tupla:
        if type(item) == str:
            return True
        
    return False