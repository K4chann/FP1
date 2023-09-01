# Desarrolle una función llamada sub2upper que admita como parámetros dos strings y devuelva una nueva string.
# La nueva string será igual que la pasada como primer parámetro, pero sustituyendo todas las apariciones de
# la string pasada como segundo parámetro por su versión en mayúsculas.

# Ejemplo:
# sub2upper("El policia alto dio el alto al ladrón alto en el alto", "alto")

# RESULTADO: "El policia ALTO dio el ALTO al ladrón ALTO en el ALTO"

# Contenido del módulo main.py
# import string_utils

# print(
#     string_utils.sub2upper(
#         "El policia alto dio el alto al ladrón alto en el alto", "alto"
#     )
# )

def sub2upper(string_1: str, string_2: str):

    return string_1.replace(string_2, string_2.upper())