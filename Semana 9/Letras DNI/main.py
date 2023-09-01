# Se tiene un diccionario cuyas claves son strings que representan números de DNI (sin letra) y cuyos valores son nombres de personas.
# Se quiere modificarlo, manteniendo las claves, pero cambiando los valores de manera que sean tuplas de dos elementos, el primero de
# los cuales será una string con el número de DNI de la clave, al que se le habrá concatenado la letra, y el segundo, el nombre que era
# el valor original. Para ello:

# Desarrolle, en el módulo auxiliar, una función llamada add_letter que tome como parámetro una string representando un número de DNI,
# sin letra, y devuelva el mismo número de DNI al que se le habrá concatenado la letra correspondiente. Para calcular la letra de un DNI,
# hay que hallar el resto de dividir el número (como entero) entre 23 y usar el valor resultante como índice para seleccionar una letra de
# la string "TRWAGMYFPDXBNJZSQVHLCKE".
# Desarrolle, en el módulo string_utils, una función llamada change_dict que tome un diccionario como el descrito en el primer párrafo y
# lo modifique de la forma que allí se describe usando la función desarrollada para el apartado anterior.
# Por ejemplo:

# Entra 

# {
#     "11111111": "John Doe",
#     "12345678": "Périco de los Palotes",
#     "42123456": "Jaimito Chistes"
# }
# Se modifica como:

# {
#     '11111111': ('11111111H', 'John Doe'),
#     '12345678': ('12345678Z', 'Périco de los Palotes'), 
#     '42123456': ('42123456Z', 'Jaimito Chistes')
# }

import string_utils

persons = {
    "11111111": "John Doe",
    "12345678": "Périco de los Palotes",
    "42123456": "Jaimito Chistes"
}
string_utils.change_dict(persons)
print(persons)