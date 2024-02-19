from two_button_choice import two_button
from delete_file import delete

def empty_delete_choice(nf):
    choice = two_button("Файл пустой\nЖелаете удалить файл?", "Да", "Нет")
    if choice == 1:
        delete(nf)