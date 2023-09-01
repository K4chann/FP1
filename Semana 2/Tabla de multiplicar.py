# Escriba un programa que lea del teclado un número entero y muestre en pantalla la tabla de multiplicar correspondiente a ese número.

# Por ejemplo, si se introduce el 3 la ejecución del programa quedaría como:

# Introduce un valor entero: 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

num = int(input("Introduce un valor entero: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)