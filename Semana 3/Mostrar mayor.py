# Escriba un programa que lea dos números enteros y muestre en pantalla el mayor de los dos (si son iguales da igual el que se muestre).

# Ejemplo:

# Introduce un valor entero: 23
# Introduce otro valor entero: 43
# El mayor es: 43

#Opción 1:
num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero: "))

print("El mayor es:", num1 if num1 > num2 else num2)

#Opción 2:
num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero: "))

print("El mayor es:", max(num1, num2))

#Opción 3
num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

print("El mayor es:", greater)