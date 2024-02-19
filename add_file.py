from two_button_choice import two_button
import add_data
import os

def add_new_file(access = 0, data = ''):
    nf = len([name for name in os.listdir('db') if os.path.isfile(os.path.join('db', name))])+1
    with open(f'db/data_{nf}.txt','w', encoding='utf-8') as file:
        file.writelines(data)
    print("Файл создан")
    if access == 0:
        choice = two_button("Вы хотите добавить первую запись?", "Да", "Нет")
        if choice == 1:
            add_data.add_row(nf = nf, access = 1)
    else:
        return nf