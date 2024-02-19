from return_data_file import data_file
from two_button_choice import two_button
import add_file


def add_row(cd = None, t_len = None, nf = None, access = 0):
    if access == 0:
        choice = two_button("Вы хотите создать новый файл?", "Да", "Нет")
        if choice == 1:
            data, nf = data_file(add_file.add_new_file(1))
        else:
            data, nf = data_file()
    elif access == 2:
        with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
            for i in range(len(cd)):
                temp_data = cd[i].split(';')
                file.write(f'{i+t_len+1};{temp_data[1]};'
                           f'{temp_data[2]};{temp_data[3]};{temp_data[4]}')
        return
            
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