import json
from iterator import CU_FILE
import hashlib

file = input('Пожалуйста, введите путь и имя файла для генерации md5 hash (при пустом вводе будет использованы значения по умолчанию): ')
file = file or CU_FILE

class MD5Generator:
    """
    MD5Generator is a class that gets the file and generates md5 hash line by line
    """

    def __init__(self, file):
        self.file = file

    def __iter__(self):
        pass
        return self

    def md5_gen(self):
        with open(self.file) as f:
            for line in f:
                yield line.upper(f.readline())
                md5_hash = hashlib.md5(line.encode())
                print('Хэшируемая строка:', line, 'md5 хэш: ', md5_hash.hexdigest())
                print()

        for item in self.file:
            print(item)
