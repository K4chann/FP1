# Desarrolle una función llamada capital que tome como parámetros tres números:
# un capital inicial, una tasa de interés (en tanto por uno) y un número de periodos,
# y devuelva el capital final tras ese número de periodos aplicando la fórmula del interés compuesto.

# Fórmula del interés compuesto:

# capital final = capital inicial * (1 + interés)**número de periodos

# Contenodo del módulo main.py

def capital(cap_i, tasa, periodos):

    return cap_i * (1 + tasa) ** periodos