# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

user_min = int(input('Input your minimum: '))
user_max = int(input('Input your maximum: '))

def fill_list () -> list:
    list = []
    length = 6
    for i in range(length):
        list.append(random.randint(-100, 100))
    return list

def check_in_range (list_to_check, min, max) -> str:
    for i in range(len(list_to_check)):
        if list_to_check[i] < max and list_to_check[i] > min:
            if i == len(list_to_check)-1:
                print(i, end = ' ')
            else:
                print(i, end = ', ')
            

users_list_to_check = fill_list()
print('Your list is: ', users_list_to_check)
print('Check your result below: ')
print('[', end = ' ')
check_in_range(users_list_to_check, user_min, user_max)
print(']', end = ' ')


