#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Папа',183],
    ['Мама',169],
    ['Я',181],
    ['Дарья',120]
]
print('Рост отца -',my_family_height[0][1])
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print("Общий рост моей семьи -", my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] , "см")