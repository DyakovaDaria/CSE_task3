from language import Language
import string
import random


# Класс ObjectOriented содержит описание объектно-ориентированного языка программирования как базовой альтернативы

class ObjectOriented(Language):
    def __init__(self, creat_year, popularity_perc, name):
        super().__init__()
        self.creat_year = creat_year  # Год создания языка программирования
        self.popularity_perc = popularity_perc  # Процент популярности языка программирования
        self.name = name  # Название языка программирования
        self.inheritance = ''  # Вид наследования в языке программирования

    # Функция инициализации объектно-ориентированного языка программирования по входным данным,
    # возвращает измененный индекс массива данных (сколько элкментов взято для инициализации)
    def read_str_array(self, str_array, i):
        if i >= len(str_array) - 1:
            return 0
        k = int(str_array[i])
        if k == 1:
            self.inheritance = 'single'
        elif k == 2:
            self.inheritance = 'multiple'
        elif k == 3:
            self.inheritance = 'interface'
        self.creat_year = int(str_array[i + 1])
        self.popularity_perc = float(str_array[i + 2])
        self.name = str_array[i + 3]
        i += 4
        return i

    # Функция генерации рандомного названия языка программирования
    def generate_random_name(self, length):
        letters = string.ascii_lowercase
        first_letter = random.choice(string.ascii_uppercase)
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return first_letter + rand_string

    # Функция генерации данных для инициализации объектно-ориентированного языка программирования
    def random_generate(self):
        k = random.randint(1, 3)
        if k == 1:
            self.inheritance = 'single'
        elif k == 2:
            self.inheritance = 'multiple'
        elif k == 3:
            self.inheritance = 'interface'
        self.creat_year = random.randint(1940, 2020)
        self.popularity_perc = random.uniform(0.0, 99.9)
        length = random.randint(2, 9)
        self.name = self.generate_random_name(length)
