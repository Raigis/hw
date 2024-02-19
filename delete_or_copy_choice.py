from delete_file import delete
from delete_data import delete_row
from copy_file import copy
from copy_data import copy_row
from two_button_choice import two_button

def choice(function):
    choice = two_button(f"Выберите, что нужно {function}", "Файл", "Данные из файла")
    if function == "удалить":
        if choice == 1:
            delete()
        else:
            delete_row()
    else:
        if choice == 1:
            copy()
        else:
            copy_row()