# Desarrolle una función llamada no_empty_lines, que reciba como parámetros dos strings. La primera string es el nombre de un fichero de texto.
# La función debe copiar el contenido de ese fichero, exceptuando las líneas vacías en un nuevo fichero cuyo nombre sea la string pasada como
# segundo parámetro. Se considera vacía cualquier línea que solo contenga caracteres de whitespace (recuérdese que tanto espacio como tabulador
# como caracter de fin de línea son caracteres de whitespace).

# Nota: el método strip() puede resultar útil.

# Contenido del módulo main.py
# import file_utils
# import string_utils

# string_utils.no_empty_lines("input.txt", "output.txt")
# file_utils.show_file("output.txt")

# Contenido del fichero input.txt
# agua tiene diptongo y perro no lo tiene


# otras palabra con diptongo

# son aurora y europa

# también lo es también

def no_empty_lines(file_name, output_name):

    with open(file_name, "r") as fr, open(output_name, "w") as fw:

        for line in fr:
            if len(line.strip()) != 0:
                print(line.strip(), file=fw)