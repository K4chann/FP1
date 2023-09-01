# Desarrolle una función llamada sum_numbers que tome como parámetros dos números enteros y devuelva la suma de todos
# los valores comprendidos entre el primero y el segundo (excluidos ambos).

# Por ejemplo:

# Se recibe: 12, 17
# Se devuelve: 13+14+15+16 = 58

# Se recibe: 14, 10
# Se devuelve 0, dado que ningún número cumple las condiciones

# Contenido del módulo main.py
# import functions

# num1 = int(input("Dame un número entero: "))
# # Aunque la función acepte que el segundo sea menor, hemos querido pedirle al
# # usuario que no lo sea:
# num2 = int(input("Dame un otro número entero igual o mayor que el anterior: "))
# print(functions.sum_numbers(num1, num2))

def sum_numbers(int_1, int_2):
    return sum(range(int_1 + 1, int_2))

    # Alternativa
    result = 0

    for num in range(int_1 + 1, int_2):
        result += num

    return result
