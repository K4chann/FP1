# Escriba un programa que lea del teclado una string que representa un fecha en el formato 'dd-mm-aaaa' y muestre el mes.

# Ejemplo:

# Si se introduce la string "01-06-1970"

# El programa muestra la string "06"

# Nótese que los dígitos que forman el mes ocupan las posiciones cuarta y quinta de la string fecha.

print(input("Introduce una fecha con el formato dd-mm-aaaa: ")[3:5])