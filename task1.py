# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random as rand

def task_info():
    print('Программа считает сумму элементов списка,')
    print('стоящих на нечётной позиции')

def random_list(list_size):
    list1 = [rand.randint(1,50) for i in range(list_size)]
    print(list1)
    return list1

def sum_odd_index(list1):
    sum = 0
    for i in range(len(list1)):
        if i % 2 != 0:
            sum += list1[i]
    print(f"Сумма равна: {sum}")

task_info()
list_size = int(input('Введите длину списка: '))
sum_odd_index(random_list(list_size))