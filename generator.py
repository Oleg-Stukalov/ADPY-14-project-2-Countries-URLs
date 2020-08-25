from iterator import CU_FILE
import hashlib

file = input('Пожалуйста, введите путь и имя файла для генерации md5 hash (при пустом вводе будет использованы значения по умолчанию - country_url.json): ')
file = file or CU_FILE
#file = CU_FILE


#Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
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
                #print('111', line)
                yield print('Хэшируемая строка:', line, 'md5 хэш: ', hashlib.md5(line.encode()).hexdigest())
                print()



    # for item in file:
    #     print(item)

