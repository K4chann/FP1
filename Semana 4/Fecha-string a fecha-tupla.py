# Desarrolle una función llamada datestr2datetuple que tome como parámetro una string que representa un fecha en
# el formato "dd-mm-aaaa"  y devuelva una tupla de tres strings que representa la misma fecha ("dd", "mm", "aaaa").

# Por ejemplo:

# Si se pasa "01-06-1970" se devuelve ("01", "06", "1970")

# Contenido del módulo main.py
# import dates

# date = "01-06-1970"
# result = dates.datestr2datetuple(date)
# print(result)

def datestr2datetuple(date: str) -> tuple:

    return tuple(date.split("-"))

    # Alternativa

    day = date[:2]
    month = date[3:5]
    year = date[6:]

    return (day, month, year)