# Se tienen listas de números reales que contienen, cada una, las notas obtenidas por los estudiantes en un cierto examen.

# Desarrolle una función llamada avg_grade, que tome como parámetros una de tales listas de notas y devuelva la correspondiente nota media,
# redondeada a dos decimales (recuerde la función round()).

# Contenido del módulo main.py
# import functions

# grades = [8, 8, 9, 5, 6, 4, 7, 4, 10]
# avg = functions.avg_grade(grades)
# print("la nota media es", avg)

def avg_grade(grades_list):

    return sum(grades_list) / len(grades_list)

    # Alternativa

    acumulator = 0
    len = len(grades_list)

    for grade in grades_list:
        acumulator += grades

    return grades / len
