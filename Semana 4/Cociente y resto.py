# # Desarrolle una función llamada division que tome como parámetros dos números enteros y devuelva una tupla de
# # dos valores que contenga, en este orden, el cociente y el resto de la división entera entre el primer y el segundo parámetro.

# # Por ejemplo:

# # Entran 7 y 2

# # Sale (3, 1)

# # Contenido del módulo main.py
# # import functions

# if __name__ == "__main__":
#     print("Se va arealizar una división entera")
#     dividendo = int(input("Dame el dividendo: "))
#     divisor = int(input("Dame el divisor: "))
#     result = functions.division(dividendo, divisor)
#     print(result)

def division(int_1, int_2) -> tuple:

    return (int_1 // int_2, int_1 % int_2)