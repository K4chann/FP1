# Desarrolle una función llamada divisibles, que tome como parámetros una lista de números enteros positivos y un
# número entero positivo. La función  debe devolver la cuenta de cuántos de los números contenidos en la lista son
# divisibles por el número proporcionado como segundo parámetro.

# Por ejemplo:

# input: [3,8,14,33,77,2] 7
# output: 2
# input: [13,22,145] 10
# output: 0

# Contenido del módulo main.py
# import functions

# numbers = [3, 8, 14, 33, 77, 2]
# divisor = 3
# found = functions.divisibles(numbers, divisor)
# print("Hay", found, "números divisibles por", divisor, "en", numbers)

def divisibles(ints_list, num):

    counter = 0

    for item in ints_list:
        counter += 1 if item % num == 0 else 0

    return counter