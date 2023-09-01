# Desarrolle una función llamada format_pows que tome como parámetro un número entre 0 y 9 y devuelva una string que contenga en secuencia:

# El propio número, ajustado a la derecha en un campo de ancho 2 relleno con ceros a la izquierda.
# El cuadrado del número, ajustado a la derecha en un campo de ancho 3 relleno con espacios (valor por omisión) a la izquierda.
# El cubo (tercera potencia) del número, ajustado a la derecha en un campo de ancho 4 relleno con caracteres '$' a la izquierda.
# Por ejemplo:

# Entra: 3
# Devuelve: "03  9$$27"
# Por ejemplo:

# Entra: 5
# Devuelve: "05 25$127"

# Contenido del módulo main.py
# import pows

# if __name__ == "__main__":
#     # Petición de datos
#     num = int(input("Dame un número entre 0 y 10: "))

#     # Cálculo y presentación del resultado
#     print(pows.format_pows(num))

def format_pows(num):

    return f"{num:02}{num**2:3}{num**3:$>4}"

print(format_pows(5))