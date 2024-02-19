def two_button(text, first_button, second_button):
    choice = int(input(f"{text}\n"
                       f"1. {first_button}\n"
                       f"2. {second_button}\n"
                       "Введите номер ответа: "))
    while choice < 1 or choice > 2:
        choice = int(input("ОШИБКА!!\n"
                           "Введите 1 или 2\n"
                           f"{text}\n"
                           f"1. {first_button}\n"
                           f"2. {second_button}\n"
                           "Введите номер ответа: "))
    return choice