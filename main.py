from store import *
import json


def add_product(data):
    item = {'name': input('Название товара: '), 'price': input('Цена товара: '),
            'quantity': input('Количество товара: '), 'colour': input('Цвет товара: '),
            'ean': input('13-значный штрих-код: ')}
    while len(str(item['ean'])) != 13 and type(item['ean']) != int:
        item['ean'] = input('Введите 13-значный штрих-код правильно: ')
    data['items'].append(item)
    return data


def remove_product(data, item):
    for i in data['items']:
        if i['name'] == item:
            data['items'].remove(i)
            print('Товар удален из корзины.')
    return data


def write_to_file(basket):
    with open('basket.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(basket.__dict__, ensure_ascii=False), file=f)


def read_from_file(basket):
    with open('basket.txt', 'r', encoding='utf-8') as f:
        for i in f:
            basket.append(Basket(json.loads(i)))


def main():
    data = {}
    lst_items = []
    data['_client'] = input('Введите имя пользователя: ')
    data['date'] = input('Введите дату создания: ')
    data['items'] = lst_items
    store_basket = Basket(data)
    while True:
        commands = ['1 - Добавить товар в корзину',
                    '2 - Выгрузить данные в файл',
                    '3 - Загрузить данные из файла',
                    '4 -  Вывести информацию на экран',
                    '5 - Удалить товар из корзины',
                    '6 - Выйти из программы']
        for i in commands:
            print(i)
        while True:
            try:
                choice = int(input('Введите номер команды от 1 до 6: '))
                if choice < 1 or choice > 6:
                    raise Exception
                break
            except:
                print('Неверный ввод, попробуйте еще раз.')

        if choice == 1:
            add_product(data)
            store_basket = Basket(data)
            print('Товар добавлен в корзину.')
        elif choice == 2:
            write_to_file(store_basket)
            print('Данные выгружены в файл.')
        elif choice == 3:
            info = []
            read_from_file(info)
            print('Данные выгружены с файла.')
        elif choice == 4:
            if isinstance(store_basket, list):
                for i in store_basket:
                    print(i)
            else:
                print(store_basket)
        elif choice == 5:
            name = input('Введите название товара, который нужно удалить: ')
            remove_product(data, name)
            store_basket = Basket(data)
        elif choice == 6:
            print('Работа программы завершена.Спасибо за уделенное время!:)')
            break


if __name__ == '__main__':
    main()
