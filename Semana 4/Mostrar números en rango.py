# Desarrolle una función llamada show_numbers que tome como parámetros dos números enteros y muestre, uno por línea y de
# menor a mayor, todos los números mayores o iguales que el primer número y menores o iguales que el segundo.

# Por ejemplo:

# Se pasa: 12, 17

# Se muestra:

# 12
# 13
# 14
# 15
# 16
# 17

# Se pasa: 14, 10

# No se muestra nada, dado que ningún número cumple las condiciones

# Contenido del módulo main.py
# import functions

# num1 = int(input("Dame un número entero: "))
# num2 = int(input("Dame un otro número entero igual o mayor que el anterior: "))
# functions.show_numbers(num1, num2)

def show_numbers(int_1, int_2):

    for num in range(int_1, int_2 + 1):
        print(num)