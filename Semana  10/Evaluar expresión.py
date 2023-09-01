# Desarrolle una función llamada evaluate que tome como parámetro una expresión aritmética simple y devuelva el resultado (numérico) de su evaluación.

# A efectos de este ejercicio, se considera una expresión aritmética simple:

# Un número (int o float)
# Una tupla de 3 elementos, de los cuales el primero y el tercero son expresiones aritméticas simples, que serán los operandos "izquierdo" y "derecho",
# respectivamente, y el segundo es una string con uno de los valores '+', '-', '*' o '/', que representa el operador aritmético a aplicar sobre los
# resultados de dichos operandos.
# Ejemplos de expresiones aritméticas simples

# 35
# 3.14
# (3.5, '+', 12)
# (10, '-', (5, '*', 3))  --> 10-(5x3) = -5

# Contenido del módulo main.py
# import math_utils

# test_exp = ((56, '+', (5, '*', 2)), '/', (12, '-', 2))
# print(math_utils.evaluate(test_exp))

def evaluate(exp):

    if type(exp) == int or type(exp) == float:
        return exp
    elif type(exp) == tuple:
        if exp[1] == "+":
            result = evaluate(exp[0]) + evaluate(exp[2])
        elif exp[1] == "-":
            result = evaluate(exp[0]) - evaluate(exp[2])
        elif exp[1] == "*":
            result = evaluate(exp[0]) * evaluate(exp[2])
        elif exp[1] == "/":
            result = evaluate(exp[0]) / evaluate(exp[2])

    return result