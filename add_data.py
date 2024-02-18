from return_data_file import data_file
from add_file import add_new_file


def add_row(nf = 0, access = 0):
    if access == 0:
        choice = int(input("Вы хотите создать новый файл?\n"
                           "1. Да\n"
                           "2. Нет\n"
                           "Введите номер ответа: "))
        while choice < 1 or choice > 2:
            choice = int(input("ОШИБКА!!\n"
                               "Введите 1 или 2\n"
                               "Вы хотите создать новый файл?\n"
                               "1. Да\n"
                               "2. Нет\n"
                               "Введите номер ответа: "))
        if choice == 1:
            data, nf = data_file(add_new_file(1))
        else:
            data, nf = data_file()
    else:
        data, nf = data_file(nf)
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    birthdate = input("Введите дату рождения: ")
    town = input("Введите город: ")
    now_number_row = len(data) + 1
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{birthdate};{town}\n')
    print("Данные успешно записаны!")