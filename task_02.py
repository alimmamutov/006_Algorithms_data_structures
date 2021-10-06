# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile


def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


cProfile.run('eratosthenes_sieve(1000)')
# 4289 function calls in 0.043 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.043    0.043 <string>:1(<module>)
#         1    0.041    0.041    0.043    0.043 task_02.py:28(eratosthenes_sieve)
#         1    0.001    0.001    0.001    0.001 task_02.py:33(<listcomp>)
#         2    0.000    0.000    0.000    0.000 task_02.py:55(<listcomp>)
#         2    0.000    0.000    0.000    0.000 task_02.py:58(<listcomp>)
#         1    0.000    0.000    0.043    0.043 {built-in method builtins.exec}
#      4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


cProfile.run('eratosthenes_sieve(3000)')
#       13770 function calls in 0.474 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.474    0.474 <string>:1(<module>)
#      1    0.470    0.470    0.474    0.474 task_02.py:28(eratosthenes_sieve)
#      1    0.001    0.001    0.001    0.001 task_02.py:33(<listcomp>)
#      3    0.000    0.000    0.000    0.000 task_02.py:55(<listcomp>)
#      3    0.001    0.000    0.001    0.000 task_02.py:58(<listcomp>)
#      1    0.000    0.000    0.474    0.474 {built-in method builtins.exec}
#  13756    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


cProfile.run('eratosthenes_sieve(10000)')
#     48786 function calls in 6.182 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    6.182    6.182 <string>:1(<module>)
#      1    6.165    6.165    6.182    6.182 task_02.py:28(eratosthenes_sieve)
#      1    0.003    0.003    0.003    0.003 task_02.py:33(<listcomp>)
#      4    0.002    0.001    0.002    0.001 task_02.py:55(<listcomp>)
#      4    0.006    0.002    0.006    0.002 task_02.py:58(<listcomp>)
#      1    0.000    0.000    6.182    6.182 {built-in method builtins.exec}
#  48769    0.005    0.000    0.005    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

cProfile.run('search_prime(1000)')
# 1003 function calls in 0.036 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.036    0.036 <string>:1(<module>)
#     1    0.036    0.036    0.036    0.036 task_02.py:120(search_prime)
#     1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
#   999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#


n = 521

if eratosthenes_sieve(n) == test(n):
    print(f'{n}-ое простое число {eratosthenes_sieve(n)}')
    print('OK')
else:
    print('Ошибка')

if search_prime(n) == test(n):
    print(f'{n}-ое простое число {search_prime(n)}')
    print('OK')
else:
    print('Ошибка')

# Количество простых чисел в диапазоне до 10000: 1229
# 521-ое простое число 3733
# OK
# Количество простых чисел в диапазоне до 10000: 1229
# 521-ое простое число 3733
# OK
