# Desarrolle una función llamada transform_date que tome como parámetro una string que representa una fecha en formato dd-mm-aaaa
# y devuelva una string que represente la misma fecha en el formato mm-dd-aaaa.

# # Contenido del módulo main.py
# from string_utils import transform_date

# if __name__ == "__main__":
#     # Datos iniciales
#     date = "01-06-1970"

#     # Cálculo y presentación del resultado
#     result = transform_date(date)
#     print("La fecha", date, "transformada es", result)

def trasnform_date(date: str) -> str:
    day = date[:2]
    month = date[3:5]
    year = date[6:]

    return ("-".join(month, day, year))