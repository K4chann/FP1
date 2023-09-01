# Desarrolle una función llamada month que tome como parámetro una string que representa una fecha en formato dd-mm-aaaa
# y devuelva una string que represente el mes de la fecha pasada. Nótese que el mes ocupa las posiciones cuarta y quinta de la string pasada.

# Ejemplo:

# Entra: "01-06-1970"
# Sale: "06"

# Contenido del módulo main.py
# from string_utils import month

# if __name__ == "__main__":
#     # Datos iniciales
#     date = "01-06-1970"

#     # Cálculo y presentación del resultado
#     result = month(date)
#     print("El mes en", date, "es", result)


def month(date: str) -> str:
    return date[3:5]