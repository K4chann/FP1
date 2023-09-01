# Desarrolle una función llamada save_initials, que tome dos strings como parámetros.

# El primer parámetro será el nombre de un fichero de texto formado por líneas compuestas de palabras en castellano separadas por espacios.

# El segundo parámetro se usará como nombre de un nuevo fichero, que tendrá tantas líneas como el primero, y que estarán formadas por las
# iniciales de las palabras del primer fichero, separadas entre sí por un espacio, sin espacios al principio ni al final, y terminadas todas
# en carácrter de fin de línea.

# Por ejemplo, si el fichero original contiene las líneas:

# esto es un
# fichero de prueba 
# que almacena palabras
# el resultante contendrá:

# e e u
# f d p
# q a p

# Contenido del módulo main.py
# import file_utils
# import string_utils

# string_utils.save_initials("input.txt", "output.txt")
# file_utils.show_file("output.txt")

def save_initials(file_name, output_name):

    with open(file_name, "r") as fr, open(output_name, "w") as fw:
        for line in fr:
            lista = []
            for word in line.split():
                lista.append(word[0])
            fw.write(" ".join(lista) + "\n")