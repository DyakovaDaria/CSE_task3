from language import Language
from functional import Functional
from object_oriented import ObjectOriented
from procedural import Procedural
import random


# Класс Container представляет простейший контейнер

class Container:
    def __init__(self):
        self.store = []

    # Функция заполнения контейнерами данными из массива str_array
    def fill_cont(self, str_array):
        # Переменная-итератор, необходимая для проверки того,
        # что все элементы массива сохранены в контейнере
        i = 0
        language = Language()
        while i < len(str_array):
            # Ключ-идентификатор базовой альтернативы
            key = int(str_array[i])
            if key == 1:
                i += 1
                language = Procedural(language.creat_year, language.popularity_perc, language.name)
                i = language.read_str_array(str_array, i)
                self.store.append(language)
            elif key == 2:
                i += 1
                language = ObjectOriented(language.creat_year, language.popularity_perc, language.name)
                i = language.read_str_array(str_array, i)
                self.store.append(language)
            elif key == 3:
                i += 1
                language = Functional(language.creat_year, language.popularity_perc, language.name)
                i = language.read_str_array(str_array, i)
                self.store.append(language)
            else:
                pass
        if i == 0:
            pass

    # Заполнение контейнера рандомно сгенерированными данными
    def rand_fill_cont(self, length):
        language = Language()
        for i in range(length):
            key = random.randint(1, 3)
            if key == 1:
                language = Procedural(language.creat_year, language.popularity_perc, language.name)
                language.random_generate()
                self.store.append(language)
            elif key == 2:
                language = ObjectOriented(language.creat_year, language.popularity_perc, language.name)
                language.random_generate()
                self.store.append(language)
            elif key == 3:
                language = Functional(language.creat_year, language.popularity_perc, language.name)
                language.random_generate()
                self.store.append(language)

    # Функция печати содержимого контейнера в консоль
    def print(self):
        length = len(self.store)
        print(f"Container is store {length} languages:\n")
        for lang in self.store:
            lang.Print()
        pass

    # Функция вывода содержимого контейнера в файл
    def write(self, ostream):
        length = len(self.store)
        ostream.write(f"Container is store {length} languages:\n")
        for lang in self.store:
            lang.write(ostream)
            ostream.write('\n')
        pass

    # Сортировка по убыванию для частного от деления года создания
    # на количество символов в названии и "слияние" двух массивов
    def merge(self, first, last):
        mas = Container()
        for i in range(len(self.store)):
            mas.store.append(self.store[i])
        middle = (first + last) // 2  # Вычисление среднего элемента
        start = first  # Начало левой части
        final = middle + 1  # Начало правой части
        for j in range(first, last + 1):
            # Сравнение элементов по их частному от деления года создания на количество символов в названии
            if start <= middle and (final > last or self.store[start].quotient() > self.store[final].quotient()):
                mas.store[j] = self.store[start]
                start += 1
            else:
                mas.store[j] = self.store[final]
                final += 1
        # Записываем полученный отсортированный результат в список
        for i in range(first, last + 1):
            self.store[i] = mas.store[i]

    # Функция рекурсивной сортировки содержимого контейнера
    def merge_sort(self, first, last):
        if first < last:
            mid = first + (last - first) // 2
            self.merge_sort(first, mid)
            self.merge_sort(mid + 1, last)
            self.merge(first, last)
