from delete_file import delete

def empty_delete_choice(nf):
    choice = int(input("Файл пустой\n"
                       "Желаете удалить файл?\n"
                       "1. Да\n"
                       "2. Нет\n"
                       "Введите номер ответа: "))
    while choice < 1 or choice > 2:
        choice = int(input("ОШИБКА!!\n"
                           "Введите 1 или 2\n"
                           "Желаете удалить файл?\n"
                           "1. Да\n"
                           "2. Нет\n"
                           "Введите номер ответа: "))
    if choice == 1:
        delete(nf)