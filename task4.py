# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(x):
    n = bin(x)
    print("Вид введенного числа в двоичной системе счисления :", n[2:])
    return n

print('Программа преобразовывает десятичное число в двоичное') 
x = int(input("Введите число: "))
decimal_to_binary(x)
