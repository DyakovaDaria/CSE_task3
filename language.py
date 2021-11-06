# Класс-родитель Language содержит описание языка программирования как обобщенного артефакта

class Language:
    def __init__(self):
        self.creat_year = 0  # Год создания языка программирования
        self.popularity_perc = 0.0  # Процент популярности языка программирования
        self.name = ''  # Название языка программирования

    # Абстрактный метод инициализации языка программирования по входным данным
    def read_str_array(self, str_array, i):
        pass

    # Абстрактный метод инициализации языка программирования по рандомно генерируемым данным
    def random_generate(self):
        pass

    # Функция печати данных о языке программирования в консоль
    def print(self):
        print(f"It is procedural language: {self.name}: ")
        print(f"the year of creation = {self.creat_year}; ")
        print(f"popularity percentage = {self.popularity_perc:.{2}f}; ")
        print(f"quotient = {self.quotient():.{2}f}\n")
        pass

    # Функция вывода данных о языке программирования в файл
    def write(self, ostream):
        ostream.write(f"It is procedural language: {self.name}: ")
        ostream.write(f"the year of creation = {self.creat_year}; ")
        ostream.write(f"popularity percentage = {self.popularity_perc:.{2}f}; ")
        ostream.write(f"quotient = {self.quotient():.{2}f}\n")
        pass

    # Функция вычисления частного от деления года создания языка программирования на количество символов в его названии
    def quotient(self):
        name_length = float(len(self.name))
        return self.creat_year / name_length
