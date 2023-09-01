# Desarrolle una función recursiva llamada caracteres_iguales que tome como parámetros dos strings y devuelva una lista de números enteros del
# mismo tamaño que la más corta de ambas strings.

# Cada posición de la lista almacenará un 1 o un 0 si el valor del carácter que ocupa la misma posición en la primera string es, respectivamente,
# igual o distinto del correspondiente de la segunda.

# Ejemplo:

# string1		= "agua que no has de beber"
# string2		= "déjala correr, además es lógico"

# resultado	= [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]

# Contenido del módulo main.py
# from functions import caracteres_iguales

# # Datos a procesar

# string1 = "agua que no has de beber"
# string2 = "déjala correr, además es lógico"

# # Proceso y resultados
# resultado = caracteres_iguales(string1, string2)
# print(resultado)

def caracteres_iguales(string_1, string_2):

    return (
        [] if (
            len(string_1) == 0 or len(string_2) == 0
        ) else (
            [1] + caracteres_iguales(string_1[1:], string_2[1:])
        ) if string_1[0] == string_2[0] else (
            [0] + caracteres_iguales(string_1[1:], string_2[1:])
        )
    )

