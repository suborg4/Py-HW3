# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def program_diff_max_min_fractional(list1):
    list1 = list(map(float, input("Введите числа через пробел:\n").split()))
    list2 = []
    for i in list1:
        num1 = i % 1
        list2.append(round(num1, 2))
    diff = max(list2) - min(list2)
    return diff

print('Программа считает разницу между максимальным') 
print('и минимальным значением дробной части элементов') 
list1 = []
print(program_diff_max_min_fractional(list1))