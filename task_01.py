# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
import cProfile, timeit, sys
time1, time2 = None, None


def first1(n):
    if n == 1:
        return n
    elif n > 0:
        return n + first1(n-1)


def first2(n):
    sumo = 0
    for sumI in range(1, n+1):
        sumo += sumI
    return sumo


def second(n):
    return n * (n + 1) // 2


def main1():
    time1 = timeit.timeit(main11(), setup='from __main__ import main11', number = 1)


def main11():
    for n in range(1, 1500):
        if first1(n) == second(n):
            # print(f'Для n={n} - True')
            continue
        else:
            # print(f'Для n={n} - False')
            break


def main2():
    time2 = timeit.timeit(main22(), setup='from __main__ import main22', number = 1)


def main22():
    for n in range(1, 1500):
        if first2(n) == second(n):
            # print(f'Для n={n} - True')
            continue
        else:
            # print(f'Для n={n} - False')
            break


sys.setrecursionlimit(1000000)
print('Через рекурсию: ')
cProfile.run('main1()')
print('Через массив: ')
cProfile.run('main2()')
print(f'Время работы Через рекурсию:    {time1}')
print(f'Время работы Через массив:      {time2}')

# ----------------------------------------------------------------------------------------------
#                                           Результаты:
# ----------------------------------------------------------------------------------------------
# Через рекурсию:
#          1125753 function calls (3002 primitive calls) in 0.599 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.598    0.598 <string>:1(<module>)
#      1499    0.001    0.000    0.001    0.000 task_01.py:22(second)
#         1    0.002    0.002    0.598    0.598 task_01.py:26(main1)
# 1124250/1499    0.596    0.000    0.596    0.000 task_01.py:8(first1)
#         1    0.000    0.000    0.599    0.599 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Через массив:
#          3002 function calls in 0.076 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.076    0.076 <string>:1(<module>)
#      1499    0.075    0.000    0.075    0.000 task_01.py:15(first2)
#      1499    0.000    0.000    0.000    0.000 task_01.py:22(second)
#         1    0.001    0.001    0.076    0.076 task_01.py:36(main2)
#         1    0.000    0.000    0.076    0.076 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}