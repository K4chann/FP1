# Escriba un programa que lea dos números enteros. Sea m el primer número y sea n el segundo;
# el programa debe mostrar el mensaje "m es divisible por n" (sustituyendo m y n por sus respectivos valores)
# si el primer número leído es divisible por el segundo, o "m no es divisible por n" si no lo es.

# Recuerde que un número es divisible por otro si el resto de la división entera da cero. El cero es divisible por cualquier número.

# Ejemplo:

# Introduce un valor entero: 42
# Introduce otro valor entero: 3
# 42 es divisible por 3

# Introduce un valor entero: 42
# Introduce otro valor entero: 4
# 42 no es divisible por 4

num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero:"))

to_print = str(num1) + " es divisible por " + str(num2) if num1 % num2 == 0\
    else str(num1) + " no es divisible por " + str(num2)


print(to_print)

#Alternativa
num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero:"))

if num1 % num2 == 0:
    print(num1, "es divisible por", num2, sep=" ")
else:
    print(num1, "no es divisible por", num2, sep=" ")