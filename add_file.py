import add_data
import os

def add_new_file(access = 0):
    nf = len([name for name in os.listdir('db') if os.path.isfile(os.path.join('db', name))])+1
    with open(f'db/data_{nf}.txt','w', encoding='utf-8') as file:
        file.writelines('')
    print("Файл создан")
    if access == 0:
        choice = int(input("Вы хотите добавить первую запись?\n"
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
            add_data.add_row(nf, 1)
    else:
        return nf