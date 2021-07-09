def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: ')
            file_obj.writelines(line)
            list = line.split()

            print(sum(map(int, list)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
summary()