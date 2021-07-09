class StoreMashines():
    def __init__(self):
        self.my_store = []

    def reception(self):
        try:
            unit = input('Введите наименование: ')
            unit_p = int(input('Введите цену за ед: '))
            unit_q = int(input('Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}

            for item in self.my_store:
                if unique["Модель устройства"] != item["Модель устройства"]:
                    continue

                item["Цена за ед"] = unique["Цена за ед"]
                item["Количество"] += unique["Количество"]
                break

            else:
                self.my_store.append(unique)

            print(f'Текущий список -\n {self.my_store}')

        except:
            return 'Ошибка ввода данных'

        print('Для выхода - Q, продолжение - Enter')
        if input('---> ').lower() == 'q':
            print(f'Весь склад -\n {self.my_store}')
            return 'Выход'
        else:
            return self.reception()


class Orgtech():
    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists


class Printer(Orgtech):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Orgtech):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Orgtech):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


def main():
    unit_1 = Printer('hp', 2000, 5, 10)
    unit_2 = Scanner('Canon', 1200, 5, 10)
    unit_3 = Copier('Xerox', 1500, 1, 15)
    print(unit_1.to_print())
    print(unit_3.to_copier())

    store = StoreMashines()
    print(store.reception())


if __name__ == "__main__":
    main()
