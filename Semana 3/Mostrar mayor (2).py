# Escriba un programa que lea dos números enteros y muestre en pantalla el mayor de los dos. Si son iguales mostrará el mensaje "Iguales".

# Ejemplo:

# Introduce un valor entero: 4
# Introduce otro valor entero: 7
# 7

# Introduce un valor entero: 5
# Introduce otro valor entero: 5
# Iguales

num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero: "))

print(
    "Iguales" if num1 == num2 else
    (num1 if num1 > num2 else num2)
)

#Alternativa
num1 = int(input("Introduce un valor entero: "))
num2 = int(input("Introduce otro valor entero: "))

if num1 == num2:
    print("Iguales")
elif num1 > num2:
    print("num1")
else:
    print(num2)