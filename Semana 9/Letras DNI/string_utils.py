import auxiliar


def change_dict(dnis_dict: dict):

    for key, value in dnis_dict.items():
        dnis_dict[key] = (auxiliar.add_letter(key), value)