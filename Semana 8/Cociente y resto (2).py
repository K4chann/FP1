# Desarrolle una función llamada division, que tome como parámetros dos números enteros y devuelva un diccionario con el cociente
# y el resto de la división entera entre el primer y el segundo parámetro, asociados respectivamente a las claves 'Cociente' y 'Resto'.

# Por ejemplo:

# Entran: 7 y 2

# Sale: {'Cociente': 3,  'Resto': 1}

# Contenido del módulo main.py
# import functions

# if __name__ == "__main__":
#     print("Se va a realizar una división entera")
#     dividendo = int(input("Dame el dividendo: "))
#     divisor = int(input("Dame el divisor: "))
#     result = functions.division(dividendo, divisor)
#     print(result)

def division(num_1, num_2):

    return {"Cociente": num_1 // num_2, "Resto": num_1 % num_2}
