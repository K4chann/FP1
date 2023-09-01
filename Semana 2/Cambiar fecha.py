# Escriba un programa que lea del teclado una string que representa un fecha en el formato 'dd-mm-aaaa' y la muestre en formato 'mm-dd-aaaa'.

# Ejemplo:

# Si se introduce la string "01-06-1970"

# El programa muestra la string "06-01-1970"

date = input("Introduce una fecha con el formato dd-mm-aaaa: ")

month = date[3:5]
day = date[:2]
year = date[6:]

print(month, day, year, sep="-")

