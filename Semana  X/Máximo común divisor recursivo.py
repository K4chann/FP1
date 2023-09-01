# Desarrolle una función recursiva llamada mcd que tome como parámetros dos números enteros positivos, el primero mayor o igual que el segundo, y
# devuelva su máximo común divisor.

# El máximo común divisor entre cero y cualquier otro número (mayor que cero) es el otro número.

# Dados dos números distintos de cero, su máximo común divisor es el mismo que el máximo común divisor entre el menor de ellos y el resto de la división
# del mayor entre el menor. Por ejemplo:

# mcd(234, 62) = mcd(62, 48) = mcd(48, 14) = mcd(14, 6) = mcd(6, 2) = mcd(2, 0) = 2

# Proceso para calcular el máximo común divisor entre 135 y 40:

# En la pareja (135, 40), 40 es distinto de 0; se calcula el resto de 135 entre 40 que da 15; Hay que calcular el máximo común divisor entre 40 y 15.
# En la pareja (40, 15), 15 es distinto de 0; se calcula el resto de 40 entre 15 que da 10; Hay que calcular el máximo común divisor entre 15 y 10.
# En la pareja (15, 10), 10 es distinto de 0; se calcula el resto de 15 entre 10 que vale 5; Hay que calcular el máximo común divisor entre 10 y 5.
# En la pareja (10, 5), 5 es distinto de 0; se calcula el resto de 10 entre 5 que es 0; Hay que calcular el máximo común divisor entre 5 y 0.
# El menor de la pareja (5, 0) es cero; por tanto, el máximo común divisor es 5.

# Contenido del módulo main.py
# import functions

# print(functions.mcd(135, 40))

def mcd(num_1, num_2):

    if num_2 == 0:
        return num_1
    else:
        result = mcd(num_2, num_1 % num_2)

    return result