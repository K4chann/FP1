# Escriba un programa que lea un número entero y muestre lo siguiente, según sea divisible o no por 2, 3, 5 o/y 7:

# Si el número fuera divisible por más de uno de ellos, mostrará el menor.
# Si el número fuera divisible por solo uno de ellos, mostrará tal divisor.
# Si el número no fuera divisible por ninguno de ellos, mostrará 0.
# Lo indicado anteriormente es solo una forma de expresar los requisitos que ha de cumplir la ejecución del programa, cuyo código no tiene por qué realizar esas comprobaciones por separado ni en ese orden (los requisitos se podrían haber escrito de hecho en cualquier otro orden, o haber expresado de otras maneras distintas pero a los efectos equivalentes). A la hora de escribir el programa, será importante el orden en que se encadenen las condiciones, p.e. si resulta ser divisible por 2, ya no será necesaria ninguna comprobación más.

# Ejemplo:

# Dame un valor entero: 3456
# 2

num = int(input("Dame un valor entero: "))

if num % 2 == 0:
    print(2)
elif num % 3 == 0:
    print(3)
elif num % 5 == 0:
    print(5)
elif num % 7 == 0:
    print(7)
else:
    print(0)