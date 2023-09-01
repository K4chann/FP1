# Desarrolle una función llamada date, que tome como parámetros tres números enteros representando el día,
# mes y año de una fecha y devuelva un diccionario que represente dicha fecha. Las claves del diccionario
# serán 'Día', 'Mes' y 'Año' y los valores los correspondientes números pasados como parámetros
# (el primero es el día, el segundo el mes y el tercero en año).

# Contenido del módulo main.py
# import dates

# day = 1
# month = 6
# year = 1970
# result = dates.date(day, month, year)
# print(result)

def date(day: int, month: int, year: int):

    return {"Día": day, "Mes": month, "Año": year}