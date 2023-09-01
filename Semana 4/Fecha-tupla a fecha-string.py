# Desarrolle una función llamada datetuple2datestr que tome como parámetro una tupla de tres strings
# que representa una fecha (dd, mm, aaaa) y devuelva una string que representa la misma fecha en el formato dd-mm-aaaa.
# Por ejemplo:

# Si se pasa ("01", "06", "1970") se devuelve "01-06-1970"

# Nota: recuerde el operador de concatenación de strings (+)

# Contenido del módulo main.py
# import dates

# day = "01"
# month = "06"
# year = "1970"
# date = (day, month, year)
# result = dates.datetuple2datestr(date)
# print(result)

def datetuple2datestr(date: tuple) -> str:

    return "-".join(date)

    # Alternativa
    date_str = ""
    for index in range(len(date)):

        if index != len(date) - 1:
            date_str += date[index] + "-"
        else:
            date_str += date[index]