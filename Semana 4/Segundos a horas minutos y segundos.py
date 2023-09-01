# Desarrolle una función llamada seconds2hms que tome como parámetro un número entero que representa una cantidad de segundos
# y devuelva una tupla de tres elementos con dicha cantidad convertida a horas, minutos y segundos
# (por supuesto, en el resultado tanto los minutos como los segundos deben ser inferiores a 60).

# Por ejemplo:

# seconds2hms(52038) -> (14, 27, 18), o sea: 52038 segundos equivalen a 14 horas, 27 minutos y 18 segundos

# Nota: recuerde que el operador de la división es //, no el operador /

# Contenido del módulo main.py
# import time_utils

# if __name__ == "__main__":
#     result = time_utils.seconds2hms(52038)
#     print(result)

def seconds2hms(seconds: int) -> tuple:

    # 1 hora = 3600 segundos
    # 1 minuto = 60 segundos

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    new_seconds = (seconds % 3600) % 60

    return (hours, minutes, new_seconds)

print(seconds2hms(52038))