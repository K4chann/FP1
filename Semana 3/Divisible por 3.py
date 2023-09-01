# Escriba un programa que lea un número entero y muestre en pantalla el mensaje "Es divisible por 3" si el número leído es divisible por 3,
# o "No es divisible por 3" si no lo es.

# Recuerde que un número es divisible por otro si el resto de la división entera da cero. El cero es divisible por cualquier número.

# Ejemplos:

# Entra un número entero:45
# Es divisible por 3

# Entra un número entero:44
# No es divisible por 3

print(
    "Es divisible por 3" if int(
        input("Entra un número entero:")
    ) % 3 == 0 else
    "No es divisible por 3"
)

#Alternativa
num = int(input("Entra un número entero:"))

if num % 3 == 0:
    print("Es divisible por 3")
else:
    print("No es divisible por 3")