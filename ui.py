from delete_or_copy_choice import choice
from change_data import change_row
from add_data import add_row
from print_data import print_file
from add_file import add_new_file


def check_number(n):
    while n < 1 or n > 7:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 5\n"
                      "Выберите функцию:\n"
                      "1. Создать\n"
                      "2. Добавить\n"
                      "3. Удалить\n"
                      "4. Изменить\n"
                      "5. Копировать\n"
                      "6. Вывод\n"
                      "7. Выход\n"
                      "Введите номер команды: "))
    return n


def start_menu():
    command = None
    while command != 7:
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Создать\n"
                            "2. Добавить\n"
                            "3. Удалить\n"
                            "4. Изменить\n"
                            "5. Копировать\n"
                            "6. Вывод\n"
                            "7. Выход\n"
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            add_new_file()
        elif command == 2:
            add_row()  
        elif command == 3:
            choice("удалить")
        elif command == 4:
            change_row()
        elif command == 5:
            choice("скопировать")
        elif command == 6:
            print_file()
    print("Спасибо, что воспользовались нашими услугами!\n"
          "Всего доброго! Приходите к нам ещё :)")