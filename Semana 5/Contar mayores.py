# Desarrolle una función llamada contar_mayores que tome como parámetros una tupla con valores de tipo
# float y un valor de tipo float. La función debe devolver un int que representa el número de elementos de
# la tupla pasada como primer parámetro que son mayores que el valor pasado como segundo parámetro.

# Por ejemplo:

# Entra: (8.0, 20.8, 14.5, 3.9, 18.3, 14.8) y 15.0

# Devuelve: 2 (ya que el 20.8 y el 18.3 son los únicos valores mayores que 15.0 que hay en la tupla)

# Contenido del módulo main.py
# import functions

# t = (8.0, 20.8, 14.5, 3.9, 18.3, 14.8)
# umbral = 15.0

# cuenta = functions.contar_mayores(t, umbral)
# print("Hay", cuenta, "valores mayores que", umbral, "en la tupla", t)

def contar_mayores(tupla, comparator):

    counter = 0

    for item in tupla:
        if item > comparator:
            counter += 1
    
    return counter