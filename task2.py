# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random as rand
from math import ceil

def task_info():
    print('Программа считает произведение пар чисел списка')

def random_list(list_size):
    list1 = [rand.randint(1,20) for i in range(list_size)]
    print(list1)
    return list1

def multiplication_pairs_numbers(list1):
    list2 = []
    for i in range(ceil(list_size/2)):
        list2.append(list1[i]*list1[-i-1])
    return list2

task_info()
list_size = int(input('Введите длину списка: '))
print(multiplication_pairs_numbers(random_list(list_size)))