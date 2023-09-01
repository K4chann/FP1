# Desarrolle una función llamada format_frecs que tome como parámetro una tupla. El primer valor de esa tupla será un diccionario cuyas
# claves son palabras de un texto y cuyos valores son la frecuencia de aparición absoluta de esas palabras en ese texto.
# El segundo valor de la tupla representará el número total de palabras en el texto.

# La función deberá devolver una lista de strings con tantos elementos como palabras recoja el diccionario. Cada elemento de esta lista
# será una string formada por una palabra separada por dos puntos de su frecuencia relativa (frecuencia absoluta multiplicada por 100 y
#                                                                                            dividida por el número total de palabras).
# Cada una de estas strings estará formateada de tal manera que la palabra ocupará un campo de 10 caracteres de ancho y estará seguida
# de dos puntos, a continuación aparecerá su frecuencia relativa, como valor float, ocupando un campo de 6 caracteres de ancho, con dos
# posiciones decimales, y se terminará con el símbolo de porcentaje (%).

# Ejemplo:

# input:  (
#     {"Esto": 2,"una": 4, "otro": 2, "el": 10, "esdrújula": 1, "pantufla": 2 }, 
#     21
# )

# output: [
#     "Esto      :  9.52%",
#     "una       : 19.05%",
#     "otro      :  9.52%",
#     "el        : 47.62%",
#     "esdrújula :  4.76%",
#     "pantufla  :  9.52%"
# ]

def format_frecs(tupla: tuple):

    return [
        f"{k:10}:{v * 100 / tupla[1]:6.2f}%" for k, v in tupla[0].items()
    ]