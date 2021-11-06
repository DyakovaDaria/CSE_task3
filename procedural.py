from language import Language
import string
import random


# Класс Procedural содержит описание процедурного языка программирования как базовой альтернативы

class Procedural(Language):
    def __init__(self, creat_year, popularity_perc, name):
        super().__init__()
        self.creat_year = creat_year  # Год создания языка программирования
        self.popularity_perc = popularity_perc  # Процент популярности языка программирования
        self.name = name  # Название языка программирования
        self.abstract_data_types = False  # Наличие/отсутствие абстрактных типов данных в языке программирования

    # Функция инициализации процедурного языка программирования по входным данным,
    # возвращает измененный индекс массива данных (сколько элкментов взято для инициализации)
    def read_str_array(self, str_array, i):
        if i >= len(str_array) - 1:
            return 0
        self.creat_year = int(str_array[i])
        self.popularity_perc = float(str_array[i + 1])
        self.abstract_data_types = bool(str_array[i + 2])
        self.name = str_array[i + 3]
        i += 4
        return i

    # Функция генерации рандомного названия языка программирования
    def generate_random_name(self, length):
        letters = string.ascii_lowercase
        first_letter = random.choice(string.ascii_uppercase)
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return first_letter + rand_string

    # Функция генерации данных для инициализации процедурного языка программирования
    def random_generate(self):
        length = random.randint(2, 9)
        self.name = self.generate_random_name(length)
        self.creat_year = random.randint(1940, 2020)
        self.abstract_data_types = bool(random.randint(0, 1))
        self.popularity_perc = random.uniform(0.0, 99.9)
