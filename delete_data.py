from return_data_file import data_file
from choice_row import choice_number_row
from empty_delete import empty_delete_choice


def delete_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        empty_delete_choice(nf)
    else:
        number_row = choice_number_row(count_rows)
        del data[number_row - 1]
        data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        print("Строка успешно удалена!")
        if len(data) == 0:
            empty_delete_choice(nf)
