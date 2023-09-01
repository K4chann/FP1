# Desarrolle una función llamada date, que tome como parámetros tres números enteros representando el día,
# mes y año de una fecha y devuelva una tupla de tres elementos que represente la misma fecha agrupando los tres valores pasados como parámetros.

# Contenido del módulo main.py
# import dates

# day = 1
# month = 6
# year = 1970
# result = dates.date(day, month, year)
# print(result)

def date(day: int, month: int, year: int) -> tuple:

    return (day, month, year)