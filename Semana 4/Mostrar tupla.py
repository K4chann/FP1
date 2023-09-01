# Desarrolle una función llamada show que tome como parámetro una tupla y muestre, uno por línea, todos los elementos de la tupla.

# Por ejemplo:

# Se pasa: (12, 14, 17, 22, 140)

# Se muestra:

# 12
# 14
# 17
# 22
# 140

# Contenido del módulo main.py
# import functions

# t = (10, 12, 34, 56, 78, 90)
# functions.show(t)

def show(tupla):

    for item in tupla:
        print(item)

    # Alternativa:
    for index in range(len(tupla)):
        print(tupla[index])