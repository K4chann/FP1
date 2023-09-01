# Escriba un programa que lea un valor entero del teclado y muestre en pantalla los valores anterior y siguiente.
# Por ejemplo, si se introduce 5, se muestran en pantalla el 4 y el 6, en este orden.

# Ejemplo (cualquiera de las dos opciones es valida):

# Opción 1:
# Introduce un valor entero: 12
# 11
# 13

# Opción 2:
# Introduce un valor entero: 12
# 11 13

#Opción 1
input_int = int(input("Introduce un valor entero: "))
print(input_int - 1, input_int + 1, sep="\n")

#Opción 2
input_int = int(input("Introduce un valor entero: "))
print(input_int - 1, input_int + 1)