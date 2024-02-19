from return_data_file import data_file
from choice_row import choice_number_row
from choice_file import choice_number_file
from add_data import add_row
from two_button_choice import two_button
from delete_data import delete_row
import add_file

def copy_row():
    cdata, cnf = data_file()
    cnr = choice_number_row(len(cdata))
    choice = two_button("Вы хотите скопировать в новый файл?", "Да", "Нет")
    if choice == 1:
        add_file.add_new_file(1, cdata[cnr-1])
    else:
        t_len, nf = data_file(choice_number_file("в который хотите скопировать"), 3)
        add_row([cdata[cnr-1]], t_len, nf, 2)
    print('Данные скопированы')
    choice = two_button("Желаете удалить скопированные данные", "Да", "Нет")
    if choice == 1:
        delete_row(cnr, cnf, cdata)