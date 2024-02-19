from choice_file import choice_number_file


def data_file(nf = 0, access = 0):
    if nf == 0:
        nf = choice_number_file()
    if access == 0 or access in (2, 3):
        with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        if access == 0:
            return data, nf
        elif access == 2:
            return data
        else:
            return len(data), nf
    else:
        return nf
