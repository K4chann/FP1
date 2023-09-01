# En matemáticas, una progresión aritmética es una sucesión numérica en la que cada elemento, menos el primero,
# se obtiene sumándole al anterior una cantidad constante, que se conoce como diferencia.

# Por ejemplo, la sucesión 5, 7, 9, 11, 13, 15, ··· es una progresión aritmética cuyo elemento inicial es el entero
# 5 y en la que cada uno de los elementos restantes se obtiene añadiendo 2 al anterior.

# Desarrolle una función llamada progresion, que tome tres números enteros como parámetros.
# El primer parámetro representará el valor inicial de la progresión deseada y el segundo la
# mencionada diferencia de la progresión. La función debe devolver una lista conteniendo sus n
# primeros elementos (siendo n el tercer parámetro), en el orden de la progresión.

# Ejemplo:

# input: 5 2 6
# output: [5, 7, 9, 11, 13, 15] 
# input: -3 5 3
# output: [-3, 2, 7]

# Contenido del módulo main.py
# import functions

# print("Se va a generar una progresión aritmética")
# inicial = int(input("Valor inicial: "))
# incremento = int(input("Distancia: "))
# cuantos = int(input("Nº de valores a generar: "))
# frecs = functions.progresion(inicial, incremento, cuantos)
# print(frecs)

def progresion(int_1, int_2, int_3):

    return [
        int_1 + int_2 * num
        for num in range(int_3)
    ]

    # Alternativa

    to_return = []

    for num in range(int_3):
        to_return.append(int_1 + int_2 * num)
    
    return to_return