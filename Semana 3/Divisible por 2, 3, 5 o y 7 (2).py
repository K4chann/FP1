# Escriba un programa que lea un número entero y muestre lo siguiente, según sea divisible o no por 2, 3, 5 o/y 7:

# Si el número fuera divisible por más de uno de ellos, los mostrará de menor a mayor, p.e. si se entra el valor 56, se mostrarán el 2 y el 7.
# Si el número fuera divisible por solo uno de ellos, mostrará tal divisor.
# Si el número no fuera divisible por ninguno de ellos, no mostrará nada.
# Ejemplo:
# Dame un valor entero: 3456
# 2
# 3

num = int(input("Dame un valor entero: "))

if num % 2 == 0:
    print(2)
if num % 3 == 0:
    print(3)
if num % 5 == 0:
    print(5)
if num % 7 == 0:
    print(7)