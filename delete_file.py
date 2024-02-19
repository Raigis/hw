from return_data_file import data_file
import os

def delete(nf = 0):
    if nf == 0:
        nf = data_file(access = 1)
    os.remove(f'db/data_{nf}.txt')
    print("Файл удалён")