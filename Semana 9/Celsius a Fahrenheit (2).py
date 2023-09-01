# Desarrolle una función llamada celsius2fahrenheit que tome como parámetro un número, que representa una temperatura en 
# grados Celsius y devuelva una string con el mensaje "X grados Celsius equivalen a Y grados Fahrenheit", donde X es el
# número pasado como parámetro e Y es su equivalente en grados Fahrenheit, ambos como valores de tipo float formateados
# en un campo de 5 caracteres de ancho con una precisión de un dígito decimal.

# Nota: La conversión de grados Celsius (C) a Fahrentheit (F) se hace según la fórmula F = (C * 9/5) + 32

# Por ejemplo:

# Entra: 36
# Devuelve: " 36.0 grados Celsius equivalen a  96.8 grados Fahrenheit"

# Contenido del módulo main.py
# from measurements import celsius2fahrenheit

# if __name__ == "__main__":
#     # Petición de datos
#     print("___Se va aconvertir de grados Celsius a Fahrentheit___")
#     celsius = int(input("Temperatura en grados Celsius: "))

#     # Cálculo y presentación del resultado
#     fahrenheit = celsius2fahrenheit(celsius)
#     print(fahrenheit)

def celsius2fahrenheit(temp):

    fahrenheit = (temp * 9 / 5) + 32

    return f"{temp} grados Celsius equivalen a {fahrenheit} grados Fahrenheit"