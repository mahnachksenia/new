#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

str = ' '
f = my_favorite_movies + ','
list = []
for i in f:
    if i != ',':
        str += i
    else:
        list.append(str)
        str = ' '
print(list[0], list[-1], list[1], list[-2])