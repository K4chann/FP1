# Desarrolle una función llamada factorial, que tome como parámetro un número entero mayor o igual que cero y devuelva su factorial.
# El factorial de 0 es 1. Para cualquier número entero n mayor que cero, su factorial se calcula multiplicando todos los números
# enteros en el rango 1··n.

# Ejemplos:

# Factorial de 3 es 1 × 2 × 3 = 6

# Factorial de 5 = 1 × 2 × 3 × 4 × 5 = 120

# Contenido del módulo main.py
# import functions

# num = int(input("Dame un número entero mayor o igual que cero: "))
# fact = functions.factorial(num)
# print("El factorial de", num, "es", fact)

def factorial(int_num):

    result = 1

    for num in range(1,int_num + 1):
        result *= num

    return result
