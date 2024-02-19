from return_data_file import data_file
from choice_file import choice_number_file
import os

def delete(nf = 0):
    if nf == 0:
        nf = data_file(choice_number_file('который хотите удалить'), 1)
    os.remove(f'db/data_{nf}.txt')
    print("Файл удалён")
    i = 1
    for name in os.listdir('db'):
        if os.path.isfile(os.path.join('db', name)):
            os.rename(f'db/{name}', f'db/data_{i}.txt')
            i += 1