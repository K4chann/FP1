# Resaltar que no me encuentro cursando la asignatura de Fundamenntos de la Programación 1,
# por lo que algunos detalles sobre cómo debe realizarse el ejercicio o los parámetros que
# se toman así como la propia estructura del ejercicio no están en mis manos, dándose la
# posibilidad así de no ser los mismos que los dados durante el examen. 

# Ésta es una solución válida para aprobar el examen con la condición dada de "divide y vecerás".
# Perfectamente se puede realizar todo dentro de una misma función, aunque está el riesgo de
# obtener una menor puntuación debido a la "mala calidad del código".

from copy import deepcopy


def clarify_row(img_row: list, delta: int) -> list:
    """Clarifies an image's row.
    
    Parameters
        img_row: list
        A list containing ints which represents pixels
        delta: int
        255 - pmax (magnitude)
    Returns
        list
    """
    for column in range(len(img_row)):
        new_pixel = img_row[column] + delta
        img_row[column] = new_pixel if new_pixel <= 255 else 255
    
    return img_row

def clarify(img:list, delta: int) -> list:
    """Clarifies an image.
    
    Parameters
        img: list
        A list of lists containing ints which represents pixels
        delta: int
        255 - pmax (magnitude)
    Returns
        list
    """
    result = deepcopy(img)

    for row in range(len(result)):
        result[row] = clarify_row(img[row], delta)
    
    return result

def calc_max(img: list) -> int:
    """Calculates the max value of a matrix of pixels != 255.
    
    Parameters
        img: list
        A list of lists containing ints which represents pixels
    Returns
        int
    """
    elements = set(column for row in img for column in row) - {255}

    return max(elements)

def saturate(img: list) -> list:
    """Saturates a given image.
    
    Parameters
        img: list
        A list of lists containing ints which represents pixels
    Returns
        list
    """
    pmax = calc_max(img)
    return clarify(img, 255 - pmax)


##############################################################################
############ Z O N A - D E - P R U E B A S ###################################
if __name__ == "__main__":
    m = [
        [100, 100, 200, 100, 75, 100],
        [100, 100, 200, 100, 75, 100],
        [100, 100, 200, 100, 75, 100],
        [100, 100, 200, 100, 75, 100],
        [100, 100, 200, 100, 75, 100],
        [100, 100, 200, 100, 75, 255]
    ]

    rs = saturate(m)

    for row in rs:
        print(row)
