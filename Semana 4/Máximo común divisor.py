# Desarrolle una función, llamada mcd, que tome como parámetros dos números enteros positivos, el primero mayor o igual
# que el segundo, y devuelva su máximo común divisor (m.c.d.), esto es, el mayor entero del que ambos son múltiplos.

# El diagrama de flujo adjunto muestra el esquema iterativo a utilizar, denominado algoritmo de Euclides.
# Este se basa en que el m.c.d. de dos enteros es el mismo que el m.c.d. del menor de ellos y el resto de la división
# del mayor entre el menor, considerando finalmente que el m.c.d. de cualquier entero N y 0 es N.

# Por ejemplo:

# mcd(234, 62) = mcd(62, 48) = mcd(48, 14) = mcd(14, 6) = mcd(6, 2) = mcd(2, 0) = 2

# Aplicación al cálculo del m.c.d. de 135 y 40:

# Para la pareja (135, 40), dado que 40 es distinto de 0, se calcula el resto de 135 entre 40, que da 15.
# Para la pareja (40, 15), dado que 15 es distinto de 0, se calcula el resto de 40 entre 15, que da 10.
# Para la pareja (15, 10), dado que 10 es distinto de 0, se calcula el resto de 15 entre 10, que vale 5.
# Para la pareja (10, 5), dado que 5 es distinto de 0, se calcula el resto de 10 entre 5, que es 0.
# Dado que el menor de la pareja (5, 0) es 0, se concluye que 5 es el m.c.d. buscado.

def mcd(int_1, int_2):

    while int_2 != 0:
        resto = int_1 % int_2
        int_1, int_2 = int_2, resto
    
    return int_1