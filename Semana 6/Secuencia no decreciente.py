# Desarrolle una función llamada no_decreasing, que tome como parámetro una lista de números enteros y
# devuelva True si es una lista no decreciente y False si no lo es. Una lista no decreciente es una en
# la que cada valor, excepto el primero, es mayor o igual que el valor que está en la posición anterior.
# Una lista con un solo elemento es no decreciente.

# Por ejemplo:

# input: [1,2,2,5,8,12] 
# output: True
# input: [-1,0,2,3,0,44,99,50]
# output: False
# input: [5]
# output: True

# Contenido del módulo main.py
# import functions

# list = [8, 8, 9, 5, 6, 4, 7, 4, 10]
# if functions.no_decreasing(list):
#     print("La lista es no decreciente")
# else:
#     print("La lista no es no decreciente")

def no_decreasing(ints_list):

    for index in range(1, len(ints_list)):

        if ints_list[index] < ints_list[index -1]:
            return False
    
    return True