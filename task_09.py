# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
myMatrix = []
for number in range(5):
    myMatrix.append([random.randint(1, 100) for i in range(5)])

print('Матрица: ')
for item in myMatrix:
    for x in item:  # Перебираем в строках все элементы (по значению)
        print("%4s" % x, end=' ')  # Выводим значение элемента, переход строки в консоли не ставим
    print()

print('Транспонированная матрица: ')
myMatrix = zip(*myMatrix)
minArr = []
for item in myMatrix:
    minArr.append(min(item))
    for x in item:  # Перебираем в строках все элементы (по значению)
        print("%4s" % x, end=' ')  # Выводим значение элемента, переход строки в консоли не ставим
    print()
print(f'Минимальные элементы колонок матрицы: {minArr}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max(minArr)}')
