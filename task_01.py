import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str):

            if hasattr(var, 'keys'):
                for key, value in var.items():
                    print(f'\nКлюч: \'{key}\' значение {value}')
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory


# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

a = int(input('Введите целое трехзначное число:'))

hundred = a // 100
dozen = (a // 10) % 10
unit = a % 10

summa = hundred + dozen + unit
mult = hundred * dozen * unit

print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифр в числе: {mult}')
print(f'Затраты памяти на сумму: {sys.getsizeof(summa)}')
print(f'Затраты памяти на произведения: {sys.getsizeof(mult)}')

# Затраты памяти на сумму: 28
# Затраты памяти на произведения: 28



# ***************************************************************************************************
# a = int(input('Введите целое трехзначное число:'))
#
# summa = (a // 100) + ((a // 10) % 10) + (a % 10)
# mult = (a // 100) * ((a // 10) % 10) * (a % 10)
#
# print(f'Сумма цифр в числе: {summa}')
# print(f'Произведение цифр в числе: {mult}')

# Затраты памяти программы:  84
# Переменные:  [234, 24, 9]


# ***************************************************************************************************
# a = int(input('Введите целое трехзначное число:'))
#
# print(f'Сумма цифр в числе: {(a // 100) + ((a // 10) % 10) + (a % 10)}')
# print(f'Произведение цифр в числе: {(a // 100) * ((a // 10) % 10) * (a % 10)}')

# Затраты памяти программы:  28
# Переменные:  [234]

# ВЫВОД: Использование дополнительных переменных занимает в памяти больше места, но их наличие порой облегчает
# читабельность кода. Сччитаю, что хорошим компромиссом этих критериев будет вариант 2.



# *******************Для проверки написанной функции на других типах переменных**************************
#  Определить, какое число в массиве встречается чаще всего.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив:', array, sep='\n')

numbers = dict()

for item in array:

    if item not in numbers:
        numbers[item] = 1

    else:
        numbers[item] += 1

print(f'Повторения чисел в массиве:\n{numbers}')

max_count = 0
num_max_count = []

for num in numbers:

    if numbers[num] > max_count:
        max_count = numbers[num]
        num_max_count = [num]

    elif numbers[num] == max_count:
        num_max_count.append(num)

print('\nЧаще всего встречается:', end=' ')
print(*num_max_count)
print(f'Количество повторений: {max_count}')


# Массив:
# [5, 3, 2, 4, 1, 1, 2, 1, 0, 4]
# Повторения чисел в массиве:
# {5: 1, 3: 1, 2: 2, 4: 2, 1: 3, 0: 1}
#
# Чаще всего встречается: 1
# Количество повторений: 3


# *******************Для проверки написанной функции на других типах переменных**************************
a = 1
b = [1, [2, 2], 3]
c = {'a': 1, 'ab': [2, 3], 'abc': {4: 5, '66': 7, 8: 'de'}}
d = 'abcd'
e = {1, 'ab', 2}

# Переменные:  [1, [1, [2, 2], 3], {'a': 1, 'ab': [2, 3], 'abc': {4: 5, '66': 7}}, 'abcd']
# Затраты памяти программы:  1655

# ***************************************************************************************************
# собираем переменные для подсчета затрачиваемой памяти
_variable = []
for i in dir():
    if i[0] != '_' and not hasattr(locals()[i], '__name__'):
        _variable.append(locals()[i])

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))