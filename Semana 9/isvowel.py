# Desarrolle una función llamada isvowel que admita como parámetro una string y devuelva un valor booleano indicando
# si dicha string está compuesta solo por vocales (True) o no (False).
# Considere las vocales tanto en mayúscula como en minúscula, acentuadas o no, y la u con diéresis
# ("aeiouüáéíóúAEIOUÜÁÉÍÓÚ").

# Ejemplo:
# result = isvowel("aeouieeÍo") # devuelve True
# result = isvowel("Hola mundo") # devuelve False

# Contenido del módulo main.py
# import string_utils

# print(string_utils.isvowel("aeouieeÍo"))
# print(string_utils.isvowel("Hola mundo"))

def isvowel(string):

    vowels = "aeiouüáéíóúAEIOUÜÁÉÍÓÚ"

    for character in string:
        if character not in vowels:
            return False
    
    return True