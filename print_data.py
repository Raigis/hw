import os

def print_file():
    for i in range(1, len([name for name in os.listdir('db') if os.path.isfile(os.path.join('db', name))])+1):
        with open(f'db/data_{i}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"Вывод данных из {i}-ого файла:\n"
              f"{''.join(data)}")
        print()
