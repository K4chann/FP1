def add_letter(number):

    letres = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni_letre = letres[int(number) % 23]

    return number + dni_letre