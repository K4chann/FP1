# Escriba una función llamada valores_en_rango, a la que se le pasen tres parámetros: una lista de números enteros y dos números enteros.
# La función debe devolver un conjunto con los elementos de la lista cuyos valores sean mayores o iguales que el segundo número y menores
# o iguales que el tercero.

# Contenido del módulo main.py
# from functions import valores_en_rango

# lista = [12, 34, 12, 56, 123, 12, 45]
# num1 = 14
# num2 = 54

# print(valores_en_rango(lista, num1, num2))

def valores_en_rango(ints_list, num_1, num_2):

    return {
        num for num in ints_list if num in range(num_1, num_2 + 1)
    }