from print_data import print_file
import os



def choice_number_file(text = "с которым Вы хотите работать"):
    print_file()
    number = int(input(f"Выберите файл, {text}\n"
                       f"Введите цифру от 1 до {len([name for name in os.listdir('db') if os.path.isfile(os.path.join('db', name))])}: "))
    while number < 1 or number > len([name for name in os.listdir('db') if os.path.isfile(os.path.join('db', name))]):
        number = int(input(f"Ошибка!!!\n"
                           f"Введите цифру от 1 до {len([name for name in os.listdir('db') if os.path.isfile(os.path.join('db', name))])}: "))
    return number
