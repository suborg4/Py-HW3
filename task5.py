# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def list_number_fibonachi(n):
    Fib = [0, 1]
    negaFib = [1]
    for n in range(2, n+1):
        f = Fib[n-2] + Fib[n-1]
        Fib.append(f)
        if n%2 == 0:
            negaFib.insert(0, -(f))
        else:
            negaFib.insert(0, f)
    FinFib = negaFib + Fib
    print(f'{FinFib}')
    return FinFib

print('Программа составляет список чисел Фибоначчи для заданного числа') 
n = int(input('Введите число Фибоначчи: '))
list_number_fibonachi(n)