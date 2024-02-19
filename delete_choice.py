from delete_file import delete
from delete_data import delete_row

def choice():
    choice = int(input("Выберите, что нужно удалить:\n"
                       "1. Файл\n"
                       "2. Данные из файла\n"
                       "Введите номер ответа: "))
    while choice < 1 or choice > 2:
        choice = int(input("ОШИБКА!!\n"
                           "Введите 1 или 2\n"
                           "Выберите, что нужно удалить:\n"
                           "1. Файл\n"
                           "2. Данные из файла\n"
                           "Введите номер ответа: "))
    if choice == 1:
        delete()
    else:
        delete_row()