from ean_dictionary import *


class Product:
    """Class of store products"""
    def __init__(self, item):
        self.name = item['name']
        self.price = item['price']
        self.quantity = item['quantity']
        self.colour = item['colour']
        self.ean = item['ean']
        if self.ean[:3] in d.keys():
            self._country = d[self.ean[:3]]
        else:
            self._country = 'Страна изготовления неопределена'

    country = property()

    @country.setter
    def country(self, country):
        if self._country == 'Страна изготовления неопределена':
            self._country = country
        else:
            print('У данного товара страна изготовления уже задана!')

    @country.getter
    def country(self):
        return self._country

    def __str__(self):
        info = '|{:^10}|{:^10}|{:^10}|{:^15}|{:^20}|{:^15}'.format(self.name, self.price, self.quantity, self.colour,
                                                                   self.ean, self._country)
        return info

    def __repr__(self):
        return self.__str__()


class Basket:
    """Class of shopping basket"""
    total_sum = 0

    def __init__(self, item):
        self._client = item['_client']
        self.items = item['items']
        self.date = item['date']
        self.total_number_of_products = len(item['items'])

    def __str__(self):
        s = 'Корзина сформирована пользователем: ' + self._client + '\n'
        s += 'Дата формирования: ' + self.date + '\n'
        s += 'Количество товаров в корзине: ' + str(self.total_number_of_products) + '\n'
        Basket.total_sum = 0
        for item in self.items:
            Basket.total_sum += float(item['price']) * float(item['quantity'])
        s += 'Общая стоимость выбранных товаров: ' + str(Basket.total_sum) + '\n'
        s += 'Выбранные товары: ' + '\n'
        for i in self.items:
            s += Product(i).__str__() + '\n'
        return s

    def __repr__(self):
        return self.__str__()
