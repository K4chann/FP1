# Desarrolle una función llamada seconds2hms, que tome como parámetro un número entero que representa una cantidad
# de segundos y devuelva un diccionario de tres elementos que representen esa cantidad convertida a horas, minutos y segundos.
# Las claves serán 'horas', 'minutos' y 'segundos'.

# Por ejemplo:

# secons2hms(52038) -> {'horas': 14, 'minutos': 27, 'segundos': 18}; es decir, 52038 segundos equivalen a 14 horas, 27 minutos y 18 segundos.

# Nota: recuerde que la división entera usa el operador //, no el operador /

# Contenido del módulo main.py
# import time_utils

# if __name__ == "__main__":
#     result = time_utils.seconds2hms(52038)
#     print(result)

def seconds2hms(seconds):

    cociente, resto = divmod(seconds, 3600)

    hours = cociente
    minutes = resto // 60
    seconds_left = resto % 60

    return {"horas": hours, "minutos": minutes, "segundos": seconds_left}