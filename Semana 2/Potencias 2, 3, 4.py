# Escriba un programa que lea del teclado un número entero y muestre en pantalla el resultado de elevarlo al cuadrado,
# el cubo y la cuarta potencia, en este orden.

# Ejemplo (ambas opciones son válidas):

# Opción 1:
# Introduce un valor entero: 5
# Potencias:
# 25
# 125
# 625

# Opción 2:
# Introduce un valor entero: 5
# Potencias: 25, 125, 625

#Opción 1
num = int(input("Introduce un valor entero: "))
print(num ** 2, num ** 3, num ** 4, sep="\n")

#Opción 2
num = int(input("Introduce un valor entero: "))
print(num ** 2, num ** 3, num ** 4)