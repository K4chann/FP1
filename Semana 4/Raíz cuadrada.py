# La raíz cuadrada de un número real positivo number es otro real result tal que result * result es
# igual a number y, por tanto, number / result es igual a result; igualdad esta última en la que se
# inspira el denominado algoritmo babilónico para el cálculo de la raíz cuadrada, mediante el cual se
# obtienen aproximaciones sucesivas cada vez más precisas, y que se ilustra en el diagrama de flujo adjunto.

# En dicho algoritmo se toma el propio number como primera aproximación de result, cuyo valor que se irá
# refinando calculando sucesivamente como nuevo valor de result el promedio entre number / result y result,
# hasta que obtengamos una precisión suficientemente buena.

# Como utilizamos coma flotante para representar, aunque solo aproximadamente en general, los números reales,
# y además como consecuencia de ello los cálculos introducen errores de redondeo, estaremos limitados en cuanto
# a la precisión que podamos pretender. Más concretamente, daremos por "suficientemente bueno" el valor de result,
# y por tanto terminaremos las iteraciones, cuando la mitad de la distancia entre result y number / result llegue
# a ser igual o menor que un número muy pequeño, que hemos llamado accuracy en el diagrama de flujo, y que será
# la "precisión" con la que obtendremos la solución.

# Por ejemplo, si number es igual a 25 y accuracy es igual a 1E-10 (0,0000000001), result iría tomando los
# siguientes valores (en este caso, al ser number un cuadrado perfecto además de pequeño, con menor accuracy
# la solución podría incluso ser exacta):

# 25
# 13.0
# 7.461538461538462
# 5.406026962727994
# 5.015247601944898
# 5.000023178253949
# 5.000000000053722
# Desarrolle una función llamada square_root que tome como parámetros dos números reales positivos, y devuelva la raíz cuadrada del primero,
# calculada con la precisión especificada por el segundo empleando el mencionado algoritmo.

# Contenido del módulo main.py
# import functions

# num1 = 25.0
# num2 = 1E-10
# root = functions.square_root(num1, num2)
# print(root)

def square_root(num, accuracy):

    result = num

    while abs((num / result) - result) / 2 > accuracy:
        result = (num / result + result) / 2
    
    return result