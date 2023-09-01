# Desarrolle una función llamada suma que tome como parámetros tres números y devuelva su suma.

# Contenido del módulo main.py

# # Escriba su código aquí


# # No modifique el código por debajo de esta línea
# if __name__ == "__main__":
#     # Petición de datos
#     print("___Se van a sumar tres números___")
#     num1 = int(input("Primer número: "))
#     num2 = int(input("Segundo número: "))
#     num3 = int(input("Tercer número: "))

#     # Cálculo y presentación del resultado
#     result = suma(num1, num2, num3)
#     print("Resultado:", result)

def suma(num1, num2, num3):
    return num1 + num2 + num3

#Alternativa
def suma(num1, num2, num3):
    return sum(num1, num2, num3)
