# Desarrolle una función llamada mol_weigth que devuelva un resultado de tipo float. El método tendrá como parámetro una string.

# El parámetro pasado al método representará la fórmula molecular de un compuesto químico, y el método devolverá el peso molecular de dicho compuesto.

# El peso molecular de un compuesto químico se calcula sumando los pesos atómicos unitarios de cada elemento, multiplicados por el número de átomos
# de ese elemento presentes en cada molécula del compuesto.

# Para calcular los pesos atómicos de los elementos, se dispone de un módulo llamado chemistry que ofrece un función llamada atom_weight que acepta
# como parámetro una string que representa el símbolo de un elemento y devuelve su peso atómico unitario como valor float.

# Una fórmula molecular es una ristra formada por una secuencia de substrings que representan elementos químicos. Cada substring que representa un
# elemento está formada por dos partes, la primera obligatoria y la segunda opcional:

# La primera parte es el símbolo del elemento, formado por una letra mayúscula seguida o no de una letra minúscula.
# La segunda parte es un número entero (de una o dos cifras) que indica cuántos átomos de ese elemento entran en una molécula del compuesto.
# Si sólo entra un átomo, no se pone el número.

# Contenido del módulo main.py
# import chem_utils

# formula = "H2O"

# print(chem_utils.mol_weigth(formula))

import re
from chemistry import atom_weight

def mol_weigth(string):

    pattern = r"([A-Z][a-z]?)(\d{0,2})"

    return sum(
        [
            atom_weight(element) * (int(counter) if counter != "" else 1)
            for element, counter in re.findall(pattern, string)
        ]
    )
