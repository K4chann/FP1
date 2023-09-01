# Una fórmula molecular es una string formada por una secuencia de substrings que representan elementos químicos.
# Cada substring que representa un elemento está formada por dos partes, la primera obligatoria y la segunda opcional:

# La primera parte es el símbolo del elemento, formado por una letra mayúscula, o una letra mayúscula seguida de una letra minúscula.
# La segunda parte es un número entero (de una o dos cifras) que indica cuántos átomos de ese elemento entran en una molécula del compuesto.
# Si sólo entra un átomo, no se pone el número.
# La siguiente imagen representa la estructura de una fórmula molecular, tal como se ha descrito en los párrafos anteriores.

# Ejemplos: "H2O", "NaCl", "H2SO4", "HCl", "CHPO3".

# Desarrolle una función llamada validate_formula que tome como parámetro una string. La función debe devolver True si la string pasada como
# parámetro tiene la estructura de una fórmula química y False si no la tiene.

# Contenido del módulo main.py
# import string_utils

# formula = "H2O"

# if string_utils.validate_formula(formula):
#     print("Estructura válida")
# else:
#     print("Estructura no válida")

import re

def validate_formula(formula):

    pattern = r"([a-z0-9][a-z0-9][a-z]\d{3,}?)"

    return not bool(re.search(pattern, formula))