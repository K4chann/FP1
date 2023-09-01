# Dados dos números enteros, a y b, tal que b≥1, el método de la multiplicación rusa para obtener a × b
# se puede definir recursivamente como se indica a continuación, dependiendo del valor de b:

# a × b = a                     si b es igual a 1
# a × b = (a + a) × (b / 2)     si b es par 
# a × b = a + (a + a) × (b / 2) si b es impar y distinto de 1
# (las divisiones son divisiones enteras)

# Desarrolle una función recursiva llamada product que implemente el método de la multiplicación rusa.

# Contenido del módulo main.py
# import functions

# num1 = 5
# num2 = 6
# prod = functions.product(num1, num2)
# print(prod)

def product(num_1, num_2):

    if num_2 == 0:
        return 0
    elif num_2 == 1:
        return num_1
    elif num_2 % 2 == 0:
        result = product(num_1 * 2, num_2 // 2)
    else:
        result = num_1 + product(num_1 * 2, num_2 // 2)
    
    return result
print(product(5, 5))