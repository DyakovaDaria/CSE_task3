from container import Container
import sys
import time


# main.py содержит главную функцию

# Сообщение о том, что входные данные неверны
def err_message1():
    print("incorrect command line!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -n number outfile01 outfile02\n")


# Сообщение о том, что введенное количество генерируемых параметров неверно
def err_message2(size):
    print(f"incorrect number of languages = {size}. Set 0 < number <= 10000\n")


# Сообщение о том, что введен неверный параметр-идентификатор
def err_message3():
    print("incorrect qualifier value!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -n number outfile01 outfile02\n")


if __name__ == '__main__':
    start_time = time.time()
    if len(sys.argv) != 5:
        err_message1()
        sys.exit(1)

    print('==> Start')

    # Создаем объект контейнера, в котором будут храниться данные
    cont = Container()

    output_file_name1 = "result.txt.out"
    output_file_name2 = "result2.txt.out"

    # Ввод данных из файла
    if sys.argv[1] == "-f":
        # Считывание названия файла с тестовыми данными
        in_file_name = sys.argv[2]
        ifile = open(in_file_name)
        # Считывание данных из файла в строку
        str = ifile.read()
        ifile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        str_array = str.replace('\n', ' ').split(' ')
        cont.fill_cont(str_array)
        output_file_name1 = sys.argv[3]
        output_file_name2 = sys.argv[4]

    # Рандомная генерация данных
    elif sys.argv[1] == "-n":
        # Считывание количества генерируемых элементов контейнера
        size = int(sys.argv[2])
        if size < 1 or size > 10000:
            err_message2(size)
            sys.exit(3)
        # Вызов функции заполнения контейнер арандомно генерируемыми данными
        cont.rand_fill_cont(size)

    else:
        err_message3()
        exit(2)

    # Вывод входных данных из командной строки и их длины
    print("Length: ", len(sys.argv), "\nIn: ", sys.argv)

    # Создание файла, в который запишется содержимое контейнера до сортировки
    # и запись содержимого контейнера в файл
    ofile1 = open(output_file_name1, 'w')
    cont.write(ofile1)
    ofile1.close()
    # Вывод времени записи неотсортированных данных в файл
    print(
        f"--- Unsorted container elements were saved to the file at: {round(time.time() - start_time, 5)} seconds ---")

    # Вызов метода сортировки содержимого контейнера
    cont.merge_sort(0, len(cont.store) - 1)

    # Создание файла, в который запишется содержимое контейнера после сортировки
    # и запись содержимого контейнера в файл
    ofile2 = open(output_file_name2, 'w')
    ofile2.write("Sorted container:\n")
    cont.write(ofile2)
    ofile2.close()
    # Вывод времени записи неотсортированных данных в файл
    print(
        f"--- Sorted container elements were saved to the file at: {round(time.time() - start_time, 5)} seconds ---")

    print("==> Stop")
    print(f"--- The program worked in: {round(time.time() - start_time, 5)} seconds ---")
