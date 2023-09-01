# Desarrolle una función recursiva llamada is_sym que tome como parámetro una lista y determine si es simétrica, devolviendo True
# si lo es, y False si no lo es. Una lista es simétrica si la secuencia de valores que se obtiene al recorrerla de izquierda a derecha
# es la misma que al recorrerla de derecha a izquierda (esta es una definición no recursiva, por lo que antes de escribir el código deberá
# encontrar la definición recursiva equivalente).

# Ejemplos:

# [12, 23, 34, 45, 67, 89]  --> False

# [10, 12, 35, 12, 10]  --> True

# Contenido del módulo main.py
# import math_utils

# l1 = [12, 23, 34, 45, 67, 89]
# l2 = [10, 12, 35, 12, 10]
# r1 = "SÍ ES" if math_utils.is_sym(l1) else "NO ES"
# print(l1, r1, "SIMÉTRICA")
# r2 = "SÍ ES" if math_utils.is_sym(l2) else "NO ES"
# print(l2, r2, "SIMÉTRICA")

def is_sym(lista):

    return True if len(lista) == 0 else (
        is_sym(lista[1:-2]) if lista[0] == lista[-1] else False
    )


