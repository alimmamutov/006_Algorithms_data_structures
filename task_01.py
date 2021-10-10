# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random


def optimized_bubble_sort(arr):
    a, i, t = arr[:], 0, True
    while t:
        t = False
        for j in range(len(a) - i - 2):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                t = True
        i = i + 1
    return a, i


def default_bubble_sort(arr):
    r = list(arr)
    n = 1
    while n < len(r):
        for i in range(len(r) - n):
            if r[i] > r[i + 1]:
                r[i], r[i + 1] = r[i + 1], r[i]
        n += 1
    return r, n


array = [random.randint(-100, 100) for i in range(150)]
print('Список до сортировки:')
print(array)
sortedArr, n = default_bubble_sort(array)
print()
print('Список после стандартной сортировки пузырьком:')
print(sortedArr)
print(f'Количество итераций: {n}')
sortedArr, n = optimized_bubble_sort(array)
print()
print('Список после оптимизированной сортировки пузырьком:')
print(sortedArr)
print(f'Количество итераций: {n}')



# a = 0
# print(a)
# print(dif(a))
# print(a)
