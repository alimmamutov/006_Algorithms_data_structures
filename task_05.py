# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

r = [random.randint(-100, 100) for i in range(15)]

print(f'Массив {r}')
maxItem = - 101
maxInd = -1
for ind, i in enumerate(r):
    if i < 0:
        if i > maxItem:
            maxItem = i
            maxInd = ind

print(f'Максимальный отрицательный элемент = {maxItem} ({maxInd})')
