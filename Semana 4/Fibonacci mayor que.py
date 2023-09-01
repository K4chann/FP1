# La sucesión de Fibonacci se puede definir de la siguiente manera:
# f1 = 1
# f2 = 1
# fn = fn-1 + fn-2  (para n>2)

# Esto es, cada número es la suma de los dos anteriores. Por tanto, los 10 primeros números de la sucesión resultan ser:
# 1, 1, 2, 3, 5, 8, 13, 21, 34 y 55.

# Desarrolle una función llamada fibo_mayor_que que tome como parámetro un número entero positivo y devuelva el primer valor
# de la sucesión de fibonacci que sea mayor que ese número.

# Por ejemplo, fibo_mayor_que(10) devuelve 13; fibo_mayor_que(15) devuelve 21

# El diagrama de flujo adjunto muestra el algoritmo para solucionar el problema planteado

# Contenido del módulo main.py
# import functions

# num1 = 135
# result = functions.fibo_mayor_que(num1)
# print(result)

def fibo_mayor_que(num):

    objetivo = num
    before = 1
    current = 1

    while current <= objetivo:
        pivot = before
        before = current
        current += pivot
    
    return current