from return_data_file import data_file
from choice_file import choice_number_file
from add_data import add_row
from two_button_choice import two_button
from delete_file import delete
import add_file

def copy():
    cnf = data_file(choice_number_file("который хотите скопировать"), 1)
    choice = two_button("Вы хотите скопировать в новый файл?", "Да", "Нет")
    if choice == 1:
        add_file.add_new_file(1, data_file(cnf, 2))
    else:
        t_len, nf = data_file(choice_number_file("в который хотите скопировать"), 3)
        add_row(data_file(cnf, 2), t_len, nf, 2)
    print('Файл скопирован')
    choice = two_button("Желаете удалить скопированный файл?", "Да", "Нет")
    if choice == 1:
        delete(cnf)