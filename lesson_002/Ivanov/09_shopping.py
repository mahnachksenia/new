#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
}
# Указать надо только по 2 магазина с минимальными ценами

sweets = {
    'печеньки': [
          { 'shop': 'ашанчик', 'price': 10.99,},
          { 'shop': 'пятерочка', 'price': 9.99, },
          { 'shop': 'магнитик', 'price': 11.99, }
                  ],
    'к0нфет0чки': [
          { 'shop': 'ашанчик', 'price': 34.99,},
          { 'shop': 'пятерочка', 'price': 32.99, },
          { 'shop': 'магнитик', 'price': 30.99, }
                  ],
    'карамельки': [
          { 'shop': 'ашанчик', 'price': 45.99,},
          { 'shop': 'пятерочка', 'price': 46.99, },
          { 'shop': 'магнитик', 'price': 41.99, }
                  ],
    'пир0женки': [  # А че так дорого пироженки стоят? Вместо одной пироженки можно купить 6 печенек
          { 'shop': 'ашанчик', 'price': 67.99,},
          { 'shop': 'пятерочка', 'price': 59.99, },
          { 'shop': 'магнитик', 'price': 62.99, }
                  ],
}