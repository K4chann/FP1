# Desarrolle una función llamada sum_ints que tome como parámetro una tupla con valores de diferentes tipos y
# devuelva la suma de los elementos de tipo int que haya en dicha tupla.

# Por ejemplo:

# Entra: (10,  "Pedro", 42, "Margarita", 18.5, 8)

# Devuelve: 10 + 42 + 8 = 60

# Nota: recuerde que la función type() devuelve el tipo de un objeto

# Contenido del módulo main.py
# import functions

# t = (10,  "Pedro", 42, "Margarita", 18.5, 8)
# suma = functions.sum_ints(t)
# print("la suma de los elementos de tipo int de la tupla es:", suma)

def sum_ints(tupla):

    result = 0

    for item in tupla:
        if type(item) == int:
            result += item
    
    return result